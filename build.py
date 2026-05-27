#!/usr/bin/env python3
"""
Vibe Coding Intro — static deck compiler (zero dependencies, stdlib only).

Reads editable Markdown content (src/content/*.md) + a shared layout/CSS/JS
and emits self-contained static HTML decks into dist/, plus a landing page
and a decks.zip. Run:  python build.py

Authoring format (per .md file):
  - Slides are separated by a line containing only ===
  - Each slide opens with an @@ ... @@ front-matter block:
        @@
        type: default | title | example | takeaways
        eyebrow: small label text
        title: Heading with *emphasis*   (| inserts a line break on title slides)
        @@
  - Body supports a small Markdown subset + block directives:
        > line              -> .lede callout (consecutive > lines join; | -> <br>)
        - line              -> .dotlist item
        ```                 -> fenced code -> .prompt-block (tokens applied)
        plain paragraph     -> .body paragraph
    Inline: **bold** *italic* `code` [text](url)
  - Directives (fenced by :::name ... :::):
        :::compare   two prompt panels (bad/good)
        :::anatomy   pill | main | sub rows + optional lede:
        :::example   lead column + a prompt-block (for worked examples)
        :::takeaways auto-numbered lines + optional lede:
        :::html      raw HTML passthrough (escape hatch)
  - Prompt-block highlight tokens (inside fences/compare/example bodies):
        [h]..[/h] section header   [k]..[/k] keyword   [c]..[/c] comment
        [arr]..[/arr] arrow        [arg]..[/arg] arg    [ok]..[/ok] ok
        {{..}}  shorthand for [k]..[/k]
  Deck metadata (title, brandmark, order, audience) lives in src/series.json.
"""

import html
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
CONTENT = os.path.join(SRC, "content")
LAYOUT = os.path.join(SRC, "layout")
STYLES = os.path.join(SRC, "styles")
FONTS = os.path.join(SRC, "assets", "fonts")
DIST = os.path.join(ROOT, "dist")

CDN_FONT_HEAD = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
)

warnings = []


def warn(msg):
    warnings.append(msg)
    print("WARN: " + msg, file=sys.stderr)


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# --------------------------------------------------------------------------
# inline rendering
# --------------------------------------------------------------------------

def render_inline(text):
    """Escape, then apply a tiny inline Markdown subset. For prose."""
    out = html.escape(text, quote=False)
    # code spans first (protect contents)
    out = re.sub(r"`([^`]+)`", lambda m: "<code>" + m.group(1) + "</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    return out


def render_title(text):
    """Title front-matter: *em* -> <em>, | -> <br/>. Escaped."""
    out = html.escape(text, quote=False)
    out = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", out)
    out = out.replace("|", "<br/>")
    return out


TOKEN_SPANS = {
    "h": "h", "k": "k", "c": "c", "arr": "arr", "arg": "arg", "ok": "ok",
}


def render_tokens(text):
    """Prompt-block body: escape &<>, then apply [x]..[/x] and {{..}} tokens."""
    out = html.escape(text, quote=False)
    for name, cls in TOKEN_SPANS.items():
        out = re.sub(
            r"\[" + name + r"\](.*?)\[/" + name + r"\]",
            lambda m: '<span class="' + cls + '">' + m.group(1) + "</span>",
            out,
            flags=re.DOTALL,
        )
    out = re.sub(r"\{\{(.*?)\}\}", r'<span class="k">\1</span>', out, flags=re.DOTALL)
    return out


# --------------------------------------------------------------------------
# front-matter
# --------------------------------------------------------------------------

def parse_front_matter(slide_text, where):
    meta = {}
    lines = slide_text.split("\n")
    # drop leading blank lines
    idx = 0
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx < len(lines) and lines[idx].strip() == "@@":
        idx += 1
        while idx < len(lines) and lines[idx].strip() != "@@":
            line = lines[idx]
            if ":" in line:
                key, _, val = line.partition(":")
                meta[key.strip()] = val.strip()
            elif line.strip():
                warn("malformed front-matter line in %s: %r" % (where, line))
            idx += 1
        if idx >= len(lines):
            warn("unclosed @@ front-matter in %s" % where)
        else:
            idx += 1  # skip closing @@
    body = "\n".join(lines[idx:])
    return meta, body


# --------------------------------------------------------------------------
# directive renderers
# --------------------------------------------------------------------------

def render_prompt_block(body, cls, tag):
    inner = render_tokens(body.strip("\n"))
    tag_html = ('<span class="tag">%s</span>\n' % html.escape(tag, quote=False)) if tag else ""
    return '<div class="prompt-block %s">\n%s%s</div>' % (cls, tag_html, inner)


def directive_compare(raw, where):
    parts = raw.split("\n---\n")
    panels = []
    for part in parts:
        lines = part.split("\n")
        # find the marker line [bad]/[good]
        cls, tag, start = "good", "", 0
        for j, ln in enumerate(lines):
            s = ln.strip()
            m = re.match(r"\[(bad|good)\]\s*(.*)$", s)
            if m:
                cls = m.group(1)
                tag = m.group(2).strip()
                start = j + 1
                break
        body = "\n".join(lines[start:])
        panels.append(render_prompt_block(body, cls, tag))
    return '<div class="grid-2 reveal">\n%s\n</div>' % "\n".join(panels)


def directive_anatomy(raw, where):
    rows = []
    lede = ""
    for ln in raw.split("\n"):
        s = ln.strip()
        if not s:
            continue
        if s.startswith("lede:"):
            lede = s[len("lede:"):].strip()
            continue
        if not s.startswith("-"):
            warn("anatomy: ignored line in %s: %r" % (where, ln))
            continue
        s = s[1:].strip()
        rowcls = ""
        m = re.match(r"(middle|bottom)\s*:\s*(.*)$", s)
        if m:
            rowcls = " " + m.group(1)
            s = m.group(2)
        cells = [c.strip() for c in s.split("|")]
        pill = render_inline(cells[0]) if cells else ""
        main = render_inline(cells[1]) if len(cells) > 1 else ""
        sub = render_inline(cells[2]) if len(cells) > 2 else ""
        p = "<p>%s%s</p>" % (main, ("<span>%s</span>" % sub) if sub else "")
        rows.append('<div class="anatomy-row%s"><span class="pill">%s</span>%s</div>' % (rowcls, pill, p))
    lede_html = ('<p class="lede">%s</p>' % render_inline(lede)) if lede else ""
    return '<div class="anatomy reveal">\n<div class="anatomy-stack">\n%s\n</div>\n%s</div>' % (
        "\n".join(rows), lede_html)


def directive_example(raw, where):
    if "\n---\n" not in raw:
        warn("example missing '---' separator in %s" % where)
        lead_raw, right_raw = raw, ""
    else:
        lead_raw, right_raw = raw.split("\n---\n", 1)

    # lead column — one element per line
    lead_parts = []
    tags = []
    for line in lead_raw.split("\n"):
        s = line.strip()
        if not s:
            continue
        if s == "lead:":
            continue
        if s.startswith("lead:"):
            s = s[len("lead:"):].strip()
            if not s:
                continue
        if s.startswith("tags:"):
            tags = [t.strip() for t in s[len("tags:"):].split(",") if t.strip()]
            continue
        if s.startswith("### "):
            lead_parts.append("<h3>%s</h3>" % render_inline(s[4:].strip()))
        else:
            lead_parts.append("<p>%s</p>" % render_inline(s))
    if tags:
        lead_parts.append('<ul class="tags">%s</ul>' % "".join(
            "<li>%s</li>" % html.escape(t, quote=False) for t in tags))
    lead_html = "<div class=\"lead\">\n%s\n</div>" % "\n".join(lead_parts)

    # right column (prompt-block)
    cls, tag = "good", ""
    rlines = right_raw.split("\n")
    start = 0
    while start < len(rlines):
        s = rlines[start].strip()
        m = re.match(r"(kind|tag)\s*:\s*(.*)$", s)
        if m:
            if m.group(1) == "kind":
                cls = m.group(2).strip() or "good"
            else:
                tag = m.group(2).strip()
            start += 1
        else:
            break
    body = "\n".join(rlines[start:])
    right_html = render_prompt_block(body, cls, tag)
    return '<div class="example-grid reveal">\n%s\n%s\n</div>' % (lead_html, right_html)


def directive_takeaways(raw, where):
    items = []
    lede = ""
    for ln in raw.split("\n"):
        s = ln.strip()
        if not s:
            continue
        if s.startswith("lede:"):
            lede = s[len("lede:"):].strip()
            continue
        items.append(s)
    rows = []
    for n, item in enumerate(items, 1):
        rows.append('<div class="num">%02d</div><div class="t">%s</div>' % (n, render_inline(item)))
    block = '<div class="takeaways reveal">\n%s\n</div>' % "\n".join(rows)
    if lede:
        block += '\n<p class="lede reveal" style="margin-top: var(--space-2xl);">%s</p>' % render_inline(lede)
    return block


DIRECTIVES = {
    "compare": directive_compare,
    "anatomy": directive_anatomy,
    "example": directive_example,
    "takeaways": directive_takeaways,
}


# --------------------------------------------------------------------------
# loose markdown (between directives) -> reveal blocks
# --------------------------------------------------------------------------

def render_loose(text, where):
    blocks = []
    lines = text.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.strip() == "":
            i += 1
            continue
        # fenced code -> prompt-block
        if line.strip().startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # closing fence
            blocks.append('<div class="prompt-block reveal">\n%s</div>' % render_tokens("\n".join(buf)))
            continue
        # lede (blockquote)
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(lines[i].lstrip()[1:].strip())
                i += 1
            txt = render_inline(" ".join(buf)).replace("|", "<br/>")
            blocks.append('<p class="lede reveal">%s</p>' % txt)
            continue
        # list
        if re.match(r"\s*-\s+", line):
            items = []
            while i < n and re.match(r"\s*-\s+", lines[i]):
                item = re.sub(r"^\s*-\s+", "", lines[i])
                cls = ""
                if item.startswith("~"):
                    cls = ' class="muted"'
                    item = item[1:].strip()
                items.append("<li%s>%s</li>" % (cls, render_inline(item)))
                i += 1
            blocks.append('<ul class="dotlist reveal">%s</ul>' % "".join(items))
            continue
        # paragraph (until blank line)
        buf = []
        while i < n and lines[i].strip() != "" and not lines[i].strip().startswith("```") \
                and not lines[i].lstrip().startswith(">") and not re.match(r"\s*-\s+", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        blocks.append('<p class="body reveal">%s</p>' % render_inline(" ".join(buf)))
    return blocks


def render_body(body, where):
    """Split body into directives + loose markdown, return list of reveal blocks."""
    blocks = []
    lines = body.split("\n")
    i = 0
    n = len(lines)
    loose_buf = []

    def flush_loose():
        if loose_buf:
            text = "\n".join(loose_buf)
            if text.strip():
                blocks.extend(render_loose(text, where))
            loose_buf.clear()

    while i < n:
        m = re.match(r"^:::(\w+)\s*$", lines[i].strip())
        if m:
            flush_loose()
            name = m.group(1)
            i += 1
            buf = []
            while i < n and lines[i].strip() != ":::":
                buf.append(lines[i])
                i += 1
            if i >= n:
                warn("unclosed :::%s directive in %s" % (name, where))
            i += 1  # closing :::
            raw = "\n".join(buf)
            if name == "html":
                blocks.append(raw)
            elif name in DIRECTIVES:
                blocks.append(DIRECTIVES[name](raw, where))
            else:
                warn("unknown directive ':::%s' in %s" % (name, where))
            continue
        loose_buf.append(lines[i])
        i += 1
    flush_loose()
    return blocks


# --------------------------------------------------------------------------
# slide assembly
# --------------------------------------------------------------------------

def render_slide(meta, body, index, deck, total_hint, where):
    typ = meta.get("type", "default")
    eyebrow = meta.get("eyebrow", "")
    title = meta.get("title", "")
    parts = []

    if typ == "title":
        if deck.get("title_mark_svg"):
            parts.append('<div class="title-mark reveal" aria-hidden="true">%s</div>' % deck["title_mark_svg"])
        if eyebrow:
            parts.append('<div class="eyebrow reveal">%s</div>' % render_inline(eyebrow))
        if title:
            parts.append('<h1 class="display reveal">%s</h1>' % render_title(title))
        # body -> lede paragraph(s)
        lede_text = " ".join(l.strip() for l in body.strip().split("\n") if l.strip())
        if lede_text:
            parts.append('<p class="lede reveal" style="margin-top: var(--space-lg);">%s</p>'
                         % render_title(lede_text))
        meta_bits = []
        if deck.get("audience"):
            meta_bits.append("<span>Audience <strong>%s</strong></span>" % html.escape(deck["audience"], quote=False))
        meta_bits.append("<span>Length <strong>%d slides</strong></span>" % total_hint)
        if deck.get("reading"):
            meta_bits.append("<span>Reading <strong>%s</strong></span>" % html.escape(deck["reading"], quote=False))
        parts.append('<div class="title-meta reveal">%s</div>' % "".join(meta_bits))
        return '  <section class="slide title-slide" data-slide="%d">\n%s\n  </section>' % (
            index, "\n".join("    " + p for p in parts))

    # default / example / takeaways
    slide_class = "slide example" if typ == "example" else "slide"
    if eyebrow:
        parts.append('<div class="eyebrow reveal">%s</div>' % render_inline(eyebrow))
    if title:
        if typ == "example":
            parts.append('<h2 class="heading reveal" style="font-size: clamp(24px, 3.4vw, 40px); margin-bottom: var(--space-md);">%s</h2>' % render_title(title))
        else:
            parts.append('<h2 class="heading reveal">%s</h2>' % render_title(title))
    parts.extend(render_body(body, where))
    return '  <section class="%s" data-slide="%d">\n%s\n  </section>' % (
        slide_class, index, "\n".join("    " + p for p in parts))


def next_chapter_slide(index, total, current, decks):
    pos = decks.index(current)
    if pos < len(decks) - 1:
        nxt = decks[pos + 1]
        eyebrow = "Next chapter"
        title = nxt["title"]
        href = nxt["output"]
        label = "Open chapter %02d" % (pos + 2)
    else:
        eyebrow = "End of series"
        title = "Back to the start."
        href = "index.html"
        label = "Series index"
    inner = (
        '<div class="eyebrow reveal">%s</div>\n'
        '<h2 class="heading reveal">%s</h2>\n'
        '<a class="next-chapter reveal" href="%s">%s <span class="arrow">&rarr;</span></a>'
    ) % (eyebrow, render_title(title), href, html.escape(label, quote=False))
    return '  <section class="slide" data-slide="%d">\n%s\n  </section>' % (
        index, "\n".join("    " + l for l in inner.split("\n")))


# --------------------------------------------------------------------------
# fonts
# --------------------------------------------------------------------------

def font_head_and_css():
    """Return (font_head_html, font_face_css). Embeds woff2 if a fonts.css exists."""
    fonts_css_path = os.path.join(FONTS, "fonts.css")
    if not os.path.isfile(fonts_css_path):
        return CDN_FONT_HEAD, ""
    import base64
    css = read(fonts_css_path)

    def repl(m):
        rel = m.group(1).strip("'\"")
        fpath = os.path.join(FONTS, rel)
        if not os.path.isfile(fpath):
            warn("font file missing: %s" % rel)
            return m.group(0)
        with open(fpath, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        return "url(data:font/woff2;base64,%s)" % b64

    css = re.sub(r"url\(([^)]+)\)", repl, css)
    return "", css


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------

def build():
    series = json.loads(read(os.path.join(SRC, "series.json")))
    decks = series["decks"]

    deck_shell = read(os.path.join(LAYOUT, "deck.html"))
    index_shell = read(os.path.join(LAYOUT, "index.html"))
    deck_css = read(os.path.join(STYLES, "deck.css"))
    index_css = read(os.path.join(STYLES, "index.css"))
    nav_js = read(os.path.join(LAYOUT, "nav.js"))
    font_head, font_face = font_head_and_css()

    os.makedirs(DIST, exist_ok=True)
    # clean prior html/zip
    for fn in os.listdir(DIST):
        if fn.endswith(".html") or fn == "decks.zip":
            os.remove(os.path.join(DIST, fn))

    def sub(template, mapping):
        return re.sub(r"\{\{(\w+)\}\}", lambda m: mapping.get(m.group(1), m.group(0)), template)

    outputs = []
    for deck in decks:
        where = deck["source"]
        raw = read(os.path.join(CONTENT, deck["source"]))
        slide_texts = [s for s in re.split(r"(?m)^===\s*$", raw)]
        # count content slides + 1 next-chapter slide
        content_slides = [s for s in slide_texts if s.strip()]
        total = len(content_slides) + 1

        rendered = []
        for n, stext in enumerate(content_slides, 1):
            meta, body = parse_front_matter(stext, "%s slide %d" % (where, n))
            rendered.append(render_slide(meta, body, n, deck, total, "%s slide %d" % (where, n)))
        rendered.append(next_chapter_slide(total, total, deck, decks))

        # mark first slide active
        rendered[0] = rendered[0].replace('class="slide title-slide"', 'class="slide title-slide is-active"', 1)
        if "is-active" not in rendered[0]:
            rendered[0] = rendered[0].replace('class="slide"', 'class="slide is-active"', 1)

        page = sub(deck_shell, {
            "TITLE": deck["title_html"],
            "FONT_HEAD": font_head,
            "CSS": (font_face + "\n" if font_face else "") + deck_css,
            "ARIA_LABEL": deck["aria"],
            "BRANDMARK_SVG": deck["brandmark_svg"],
            "BRANDMARK_LABEL": deck["brandmark_label"],
            "NAV_JS": nav_js,
            "SLIDES": "\n\n".join(rendered),
        })
        out_path = os.path.join(DIST, deck["output"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        outputs.append(deck["output"])
        print("built %s (%d slides)" % (deck["output"], total))

    # landing page
    cards = []
    for n, deck in enumerate(decks, 1):
        cards.append(
            '    <a class="chapter" href="%s">\n'
            '      <span class="num">%02d</span>\n'
            '      <span class="body-col"><span class="title">%s</span>'
            '<span class="blurb">%s</span></span>\n'
            '      <span class="meta">%s</span>\n'
            '    </a>' % (
                deck["output"], n,
                html.escape(deck["title"], quote=False),
                html.escape(deck.get("blurb", ""), quote=False),
                html.escape(deck.get("reading", ""), quote=False),
            )
        )
    index_page = sub(index_shell, {
        "TITLE": series["series_title"],
        "FONT_HEAD": font_head,
        "CSS": (font_face + "\n" if font_face else "") + deck_css + "\n" + index_css,
        "BRANDMARK_SVG": series.get("brandmark_svg", ""),
        "BRANDMARK_LABEL": series.get("brandmark_label", ""),
        "HEADING": render_title(series.get("heading", series["series_title"])),
        "LEDE": render_inline(series.get("lede", "")),
        "CHAPTERS": "\n".join(cards),
        "FOOTER": html.escape(series.get("footer", ""), quote=False),
    })
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page)
    print("built index.html")

    # zip of self-contained decks
    zip_path = os.path.join(DIST, "decks.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(DIST, "index.html"), "index.html")
        for out in outputs:
            z.write(os.path.join(DIST, out), out)
    print("built decks.zip")

    if warnings:
        print("\n%d warning(s)." % len(warnings), file=sys.stderr)
    else:
        print("\nNo warnings. Fonts: %s." % ("embedded/offline" if font_face else "Google Fonts CDN"))


if __name__ == "__main__":
    build()
