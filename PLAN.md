# Syllabus — remaining work

Tracks the outstanding items from the syllabus review. The series now has
eight chapters, all building cleanly:

1. What is vibe coding
2. Describing what you want *(new — beginner)*
3. Setting up the tools
4. Version control basics
5. The vibe-coded stack
6. Functional modelling *(moved later — advanced deep dive)*
7. Debugging & verifying *(new)*
8. Shipping it

## 1. Browser QA of the new/edited chapters
- **Why:** chapter 06 and the chapter 04–05 edits were verified to *build* with no
  warnings, but the rendered decks have not been viewed in a browser.
- **Do:** `python build.py`, then open `dist/06-shipping-it.html` and `dist/index.html`.
  Check the title-slide brandmark, slide spacing, worked-example prompt blocks, and
  the 05→06 "Next chapter" link.
- **Done when:** chapter 06 looks visually consistent with chapters 01–03.

## 2. Add a "Debugging & verifying" chapter — DONE
- Added `src/content/07-debugging-and-verifying.md` (chapter 07, near shipping) plus
  its `series.json` entry. Teaches the fix for "it's broken": report what you did /
  expected / saw with the exact error, change one thing at a time, then verify.
- Builds clean and chains 06 → 07 → 08.

## 3. Reconsider chapter order — DONE
- Split per owner decision: new beginner "Describing what you want" chapter added
  early as chapter 02; the advanced functional-modelling deck moved later to
  chapter 06 as a deep dive. File renames + `series.json` reorder; chaining is automatic.

## 4. Fold "Prompting" back into the path — DEFERRED
- **Decision:** skipped for now (owner's call). Prompting content remains in git
  history (and `Functional analysis .txt` / `Vibe coded stack .txt` as source notes).
- The new beginner chapter 02 already covers the core "describe clearly" skill, so a
  separate prompting chapter is lower priority. Revisit if a PM-pitched angle is wanted.

## 5. Open a PR
- Branch `claude/syllabus-outline-review-6lex4` is pushed but no PR exists yet.
- Open one once the owner is happy with the chapter set and order.

> Remaining: item 1 (browser QA of the new/edited chapters) and item 5 (open a PR).
