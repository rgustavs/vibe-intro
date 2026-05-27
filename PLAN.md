# Syllabus — remaining work

Tracks the outstanding items from the syllabus review. The series currently has
six chapters (01 What is Vibe Coding → 06 Shipping It), all building cleanly.

## 1. Browser QA of the new/edited chapters
- **Why:** chapter 06 and the chapter 04–05 edits were verified to *build* with no
  warnings, but the rendered decks have not been viewed in a browser.
- **Do:** `python build.py`, then open `dist/06-shipping-it.html` and `dist/index.html`.
  Check the title-slide brandmark, slide spacing, worked-example prompt blocks, and
  the 05→06 "Next chapter" link.
- **Done when:** chapter 06 looks visually consistent with chapters 01–03.

## 2. Add a "Debugging & verifying" chapter
- **Why:** the one gap still open from the review — "paste the error, say what you
  expected, say what you saw" and confirming the thing actually works. Chapter 01
  raises "it's broken" as a pitfall but nothing teaches the fix.
- **Do:** new `src/content/NN-debugging.md` + `series.json` entry, same slide arc and
  calm/British tone as chapters 01–03. Likely sits after 03 (version control) or
  alongside 06. Decide placement as part of item 3.
- **Done when:** builds clean, chains in order, reads like a chapter-1–3 sibling.

## 3. Reconsider chapter order
- **Why:** "describing behaviour clearly" (ch 04) is the core skill, introduced
  conceptually in ch 01. A beginner-level slice of it could come earlier (before
  tools), leaving the advanced BDD/state-machine material as a later deep dive.
- **Do:** decide whether to split ch 04 into a beginner "describing what you want"
  chapter (early) + an advanced "functional modelling" chapter (later). Reordering is
  a `series.json` array change plus possible file renames; chaining is automatic.
- **Open question:** confirm the intended learning order with the owner before moving
  chapters, since it changes the whole arc.

## 4. Fold "Prompting" back into the path
- **Context:** the standalone `prompting-for-pms` deck was removed from the repo; its
  content lives in git history (and `Functional analysis .txt` / `Vibe coded stack .txt`
  remain as source notes).
- **Why:** prompting overlaps the series' core skill and arguably deserves a proper
  beginner chapter rather than a separate PM-pitched deck.
- **Do:** if wanted, rewrite it as a new `src/content/` chapter in the unified
  audience/tone, recovering useful material from history (`git show <rev>:prompting-for-pms.html`).

## 5. Open a PR
- Branch `claude/syllabus-outline-review-6lex4` is pushed but no PR exists yet.
- Open one once the owner is happy with the chapter set and order.

> Sequencing note: settle item 3 (order) before investing in items 2 and 4, since
> placement of new chapters depends on the final arc.
