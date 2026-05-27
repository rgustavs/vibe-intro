#!/usr/bin/env python3
"""
Download the deck webfonts (Fraunces / Inter / JetBrains Mono) into
src/assets/fonts/ and write a fonts.css that references the local files.

Run once on a machine with internet:  python tools/fetch_fonts.py
After this, `python build.py` automatically base64-embeds the fonts so every
compiled deck works fully offline (no Google Fonts CDN needed).

Only the latin + latin-ext subsets are kept, to keep file sizes reasonable.
"""

import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "src", "assets", "fonts")

CSS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500"
    "&family=Inter:wght@400;500;600"
    "&family=JetBrains+Mono:wght@400;500&display=swap"
)
# A modern browser UA makes Google serve woff2 (not ttf).
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# keep only these subsets (named in the comment line before each @font-face)
KEEP = {"latin", "latin-ext"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    os.makedirs(FONTS, exist_ok=True)
    # clean any prior font files
    for fn in os.listdir(FONTS):
        if fn.endswith(".woff2") or fn == "fonts.css":
            os.remove(os.path.join(FONTS, fn))

    css = fetch(CSS_URL).decode("utf-8")
    blocks = re.split(r"(?=/\*\s)", css)

    # group by (family, subset): variable fonts share one file across weights,
    # so collapse the weight blocks into a single @font-face with a weight range.
    groups = {}  # (fam, subset) -> {url, weights:set, unicode}
    order = []
    for block in blocks:
        m_sub = re.match(r"/\*\s*([\w-]+)\s*\*/", block.strip())
        subset = m_sub.group(1) if m_sub else ""
        if subset and subset not in KEEP:
            continue
        m_fam = re.search(r"font-family:\s*'([^']+)'", block)
        m_url = re.search(r"url\((https://[^)]+\.woff2)\)", block)
        m_wt = re.search(r"font-weight:\s*([\d ]+)", block)
        m_ur = re.search(r"unicode-range:\s*([^;]+);", block)
        if not (m_fam and m_url):
            continue
        fam = m_fam.group(1)
        key = (fam, subset)
        if key not in groups:
            groups[key] = {"url": m_url.group(1), "weights": set(), "unicode": (m_ur.group(1).strip() if m_ur else "")}
            order.append(key)
        if m_wt:
            for w in m_wt.group(1).split():
                groups[key]["weights"].add(int(w))

    out_css = []
    for key in order:
        fam, subset = key
        g = groups[key]
        fname = "%s-%s.woff2" % (fam.replace(" ", ""), subset or "x")
        data = fetch(g["url"])
        with open(os.path.join(FONTS, fname), "wb") as f:
            f.write(data)
        weights = sorted(g["weights"]) or [400]
        wrange = "%d %d" % (weights[0], weights[-1]) if len(weights) > 1 else str(weights[0])
        out_css.append(
            "/* %s · %s */\n"
            "@font-face {\n"
            "  font-family: '%s';\n"
            "  font-style: normal;\n"
            "  font-weight: %s;\n"
            "  font-display: swap;\n"
            "  src: url(%s) format('woff2');\n"
            "  unicode-range: %s;\n"
            "}" % (fam, subset, fam, wrange, fname, g["unicode"])
        )
        print("  fetched %s (%d bytes, weights %s)" % (fname, len(data), wrange))

    with open(os.path.join(FONTS, "fonts.css"), "w", encoding="utf-8") as f:
        f.write("\n".join(out_css) + "\n")
    print("wrote %d @font-face rules to src/assets/fonts/fonts.css" % len(out_css))
    print("now run: python build.py  (fonts will be embedded for offline use)")


if __name__ == "__main__":
    main()
