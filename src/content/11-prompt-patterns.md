@@
type: title
eyebrow: A working introduction · appendix A
title: Prompt|*Patterns.*
@@
A pocket set of reusable prompts —|fill in the blanks and adapt them to your project.

===

@@
type: default
eyebrow: 01 · How to use this
title: Starting points, not *scripts.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Every pattern here is a template with <code>{{blanks}}</code> to fill in. They're starting points — read them, swap in your details, and adjust the wording to fit what you're building.</p>
    <p class="body subtext">They all lean on the same describe → run → review → refine loop from chapter one. Nothing here is new; it's the same skills, written down so you don't start from a blank page.</p>
  </div>
  <div class="card">
    <div class="label">Three habits</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>One job per prompt — don't bundle five requests</li>
      <li>Fill every <code>{{blank}}</code> with a concrete detail</li>
      <li>Run and check the result before the next prompt</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · The shape
title: Most prompts share *four parts.*
@@
:::anatomy
- Goal | What you want, in one line | "Add a way to mark a note as done."
- Context | Where it fits, what exists | "We already have the notes list from chapter five."
- Constraints | Limits and must-haves | "Keep the existing style. Don't change the database."
- Done when | How you'll know it worked | "I can tick a note and it stays ticked after refresh."
lede: You won't always need all four — but when a prompt goes wrong, a missing part is usually why.
:::

===

@@
type: example
eyebrow: Pattern · 01 · Start something new
title: Scaffold a *first version.*
@@
:::example
lead:
### When you're staring at an empty project.
Describe the whole thing at a high level and ask for the simplest version that runs. Resist adding features here — you just want something on screen to react to.
tags: Goal, Stack, Smallest version
---
tag: copy & adapt
[h]Goal[/h]Build a small {{app}} that lets me
{{do the one main thing}}.

[h]Stack[/h]Use our usual setup:
{{React}}, {{FastAPI}}, {{SQLite}}.

[h]Start small[/h]Give me the simplest version
that runs, with [k]nothing extra[/k] yet.
Tell me how to start it.
:::

===

@@
type: example
eyebrow: Pattern · 02 · Add a feature
title: Build on what *already works.*
@@
:::example
lead:
### Add one capability to a working app.
Name what exists so the agent builds on it instead of replacing it. End with how you'll check it — that keeps the change small and testable.
tags: Context, One feature, Done when
---
tag: copy & adapt
[h]Context[/h]The {{notes app}} already
{{lists and saves notes}}.

[h]Add[/h]Let me {{mark a note as done}}.
Keep everything else as it is.

[h]Done when[/h]I can {{tick a note}} and it
[k]stays that way after a refresh[/k].
:::

===

@@
type: example
eyebrow: Pattern · 03 · Change behaviour
title: Adjust *one* existing thing.
@@
:::example
lead:
### Reshape something that already exists.
Point at the exact thing, say what's wrong with it now, and say what you want instead. Specific in, specific out.
tags: This thing, Now, Instead
---
tag: copy & adapt
[h]Change[/h]On the {{notes list}}, the
{{newest note shows at the bottom}}.

[h]I want[/h]Newest at the [k]top[/k] instead.

[h]Leave alone[/h]Don't touch how notes are
{{saved or styled}} — only the order.
:::

===

@@
type: example
eyebrow: Pattern · 04 · Understand the code
title: Ask it to *explain.*
@@
:::example
lead:
### You don't have to read code to understand it.
When you're unsure what a file or change does, ask for a plain-English tour. This is also how you sanity-check a change before you accept it.
tags: Plain English, No jargon, What if
---
tag: copy & adapt
[h]Explain[/h]In [k]plain English[/k], what does
{{this file / this change}} do?

[h]Keep it simple[/h]No jargon. Assume I'm
{{new to coding}}.

[h]Then[/h]What could [k]go wrong[/k] with it,
and what should I test?
:::

===

@@
type: default
eyebrow: 03 · The difference it makes
title: Vague in, *vague* out.
@@
:::compare
[bad] missing the parts
"make the notes better
and add some features"

[c]# Better how? Which features?
# The agent can only guess —
# and it will guess wrong.[/c]
---
[good] goal + context + done-when
[h]Goal[/h]Let me search my notes by title.

[h]Context[/h]The list from chapter five.

[h]Done when[/h]Typing filters the list live.
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
Patterns are starting points — fill the blanks with your own concrete details.
One job per prompt; run and check before you ask for the next thing.
Goal, context, constraints, done-when — a missing part is usually why a prompt fails.
When unsure, ask the agent to explain in plain English before you accept a change.
lede: A page of prompts beats a blank one.
:::
