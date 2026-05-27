# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static slide-deck compiler for a teaching series ("Vibe Coding — A Working Introduction"). Editable Markdown in `src/content/` is compiled by a single zero-dependency Python script into self-contained HTML decks under `dist/`. There is no application runtime, no package manager, and no test suite — the deliverable is static HTML.

## Commands

```bash
python build.py              # compile all decks -> dist/ (also writes index.html + decks.zip)
python tools/fetch_fonts.py  # one-time, needs internet: download webfonts into src/assets/fonts/
```

- Requires only Python 3 standard library. No dependencies to install.
- `build.py` prints one line per deck and ends with either `No warnings.` or a warning count. **A clean build means zero warnings** — warnings flag malformed front-matter or directives and should be fixed, not ignored.
- After any content edit, run `python build.py` and confirm it reports no warnings. This is the closest thing to a test.
- Preview locally by opening a file in `dist/` (e.g. `dist/index.html`) in a browser, or serve the folder: `python -m http.server -d dist`.
- `dist/` is gitignored; never commit it. CI rebuilds it.

## CI / deploy

`.github/workflows/build.yml` runs `python build.py` and deploys `dist/` to GitHub Pages on push to `main`. The source of truth is `src/` + `build.py`, never the generated HTML.

## Architecture

The build is a one-pass compiler in `build.py`. To understand it, read these together:

- **`src/series.json`** — the manifest. Lists decks in order; each entry carries metadata (`source`, `output`, `title`, `title_html`, `aria`, `blurb`, `audience`, `reading`) and inline `brandmark_svg` / `title_mark_svg` artwork. **Deck order and the landing-page list come entirely from this array.**
- **`src/content/NN-name.md`** — one Markdown file per chapter, in a custom dialect (below).
- **`src/layout/`** — `deck.html` and `index.html` are templates with `{{PLACEHOLDER}}` tokens substituted by `build.py`; `nav.js` is the inlined keyboard/swipe navigation.
- **`src/styles/`** — `deck.css` (decks) and `index.css` (landing page), inlined into every output.
- **`src/assets/fonts/`** — if `fonts.css` exists, `build.py` base64-embeds the woff2 files so decks work fully offline; otherwise it falls back to the Google Fonts CDN.

Each deck compiles to a single self-contained `.html` (CSS, JS, fonts all inlined). `build.py` also emits `index.html` and a `decks.zip` of everything.

**Chapter chaining is automatic.** The "Next chapter" slide and the end-of-series slide are generated from the position of a deck in `series.json` — do not hand-author them. Reordering or adding a chapter is purely a `series.json` + content-file change.

## Authoring format (the Markdown dialect)

Defined and documented at the top of `build.py` (docstring) — read it before editing content. Summary:

- `===` on its own line separates slides.
- Each slide opens with an `@@ ... @@` front-matter block: `type:` (`title` | `default` | `example` | `takeaways`), `eyebrow:`, `title:`. In `title:`, `*emphasis*` → `<em>` and `|` → line break.
- Block directives, fenced `:::name ... :::`: `compare`, `anatomy`, `example`, `takeaways`, and `html` (raw passthrough / escape hatch).
- Prompt-block highlight tokens inside fenced/example bodies: `[h]header[/h]`, `[k]keyword[/k]`, `[c]comment[/c]`, `[arr]arrow[/arr]`, `[arg]arg[/arg]`, `[ok]ok[/ok]`, and `{{..}}` (shorthand for `[k]..[/k]`).
- Inline prose: `**bold**`, `*italic*`, `` `code` ``, `[text](url)`.
- `anatomy` rows may be prefixed `middle:` / `bottom:` for row styling; `~` before a list item marks it `muted`.

### Adding a chapter

1. Create `src/content/NN-name.md` following the established slide arc (title → Why this matters → Definition → Anatomy → loop/principles → worked examples → Pitfalls → Takeaways).
2. Add a deck entry to `series.json` (including both SVGs, using the brand palette below).
3. Run `python build.py`; confirm no warnings and that the new chapter appears on the index and chains correctly.

## Content conventions

These are deliberate and consistent across chapters — match them, don't drift:

- **British spelling** and a calm, beginner-friendly voice. The audience is non-coders ("no deep coding background required").
- The recurring spine is the **describe → run → review → refine** loop; most chapters reuse it.
- Tools are standardised as **VS Code + Antigravity**; the reference stack is **React / FastAPI / SQLite**. Avoid introducing other tools (e.g. Cursor) or naming drift (e.g. "Node.js" for the frontend).
- Brand palette used in SVGs and accents: `#6F7F6A` (green), `#8FA9B8` (blue), `#C9BAA6` (tan), `#A8BDB6` (sage).
