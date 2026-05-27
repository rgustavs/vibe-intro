@@
type: title
eyebrow: A working introduction · chapter four
title: High-Resolution|*Prompting.*
@@
The prompt is the spec now.|Whatever you don't say, the model has to guess — so learn to say it well.

===

@@
type: default
eyebrow: 01 · Why this matters
title: The prompt *is* the spec.
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Chapter two showed the loop: describe, generate, run, refine — and that vague in means vague out. This chapter is the craft of the <em>describe</em> step.</p>
    <p class="body subtext">When a feature runs on a model, the prompt defines the behaviour: what it does, how it sounds, what it returns. The old flow was Spec → Engineer → Code → Behaviour. The new flow is <strong>Spec → Prompt → Behaviour</strong>. The prompt is product surface area — and it's yours to own.</p>
  </div>
  <div class="card">
    <div class="label">The core rule</div>
    <div class="title">No hidden intent</div>
    <p>The model has no source of intent other than the words you give it.</p>
    <p style="margin-top: 12px;"><em>Whatever isn't in the prompt, the model has to guess.</em></p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: What a prompt *really* is.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">A prompt isn't just your question. It's <em>everything the model reads before it answers</em>: the system instructions, the role you gave it, the conversation so far, any documents you pasted, and the task itself.</p>
  <div class="card">
    <div class="label">Everything the model sees</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>System instructions &amp; role</li>
      <li>Background docs and data</li>
      <li>The conversation history</li>
      <li>Your actual question</li>
    </ul>
    <p style="margin-top: 12px;">All of it competes for the same context window — so every word should earn its place.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Five parts of a *useful prompt.*
@@
:::anatomy
- Role | Who the model should be | "You are a research synthesizer for a B2B PM team."
- Context | What it needs to know | Background, definitions, and constraints it can't infer.
- Task | The one thing to do | A single clear instruction, not five stacked together.
- Examples | What good looks like | One or two worked cases it can pattern-match against.
- Format | The shape of the answer | Markdown or JSON, length, the exact fields you want.
lede: You won't need all five every time — only the parts the model can't safely guess.
:::

===

@@
type: default
eyebrow: Principle 1
title: *Specificity* beats cleverness.
@@
The same task, two ways. The second isn't longer because it's wordy — it's longer because it actually says what you want.

:::compare
[bad] vague
Summarize this user feedback.
---
[good] specific
Summarize these 12 user interviews
into the 5 most frequent themes.
For each: a one-line headline, two
supporting quotes, and how many
interviews mentioned it.
:::

> If you can picture three different answers that would all satisfy your prompt, it's too vague.

===

@@
type: default
eyebrow: Principle 2
title: Give the model *what you know.*
@@
The model can't read your team's mind. Hand it the context you're carrying in your head.

:::compare
[bad] no context
Write a launch email for our new
bulk-export feature.
---
[good] full context
Write a launch email for bulk export.
{{Audience}}: ops managers, Growth plan.
{{Why}}: built after 14 interviews.
{{Tone}}: practical, no superlatives.
{{Length}}: under 150 words, one CTA.
:::

> Same task. The second one will sound like your team actually wrote it.

===

@@
type: default
eyebrow: Principle 3
title: *Show* what good looks like.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Models are pattern matchers. The fastest way to get your voice is to give them a pattern to match — one worked example beats a paragraph of adjectives.</p>
    <p class="body subtext">Don't describe your release-note style. Paste one, then ask for the next.</p>
  </div>
  <div class="prompt-block good">
<span class="c"># Show, then ask:</span>

<span class="k">Here's how we write release notes:</span>
"Bulk export is here. Pick a date
range, hit export, get a CSV.
Large exports arrive by email."

<span class="k">Now write one for:</span> saved filters.
  </div>
</div>
:::

===

@@
type: default
eyebrow: Principle 4
title: Decide the *shape* of the answer.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Output format is the single cheapest lever to make an AI feature feel less random. Decide the shape <em>before</em> you ask.</p>
  </div>
  <div class="card">
    <div class="label">Pick the shape for the reader</div>
    <p><strong>For code:</strong> JSON — strict fields, parseable.</p>
    <p style="margin-top: 8px;"><strong>For people:</strong> Markdown — headers, bullets, a length cap.</p>
    <p style="margin-top: 8px;"><strong>For decisions:</strong> recommendation, confidence, reasoning, alternatives — same order, every time.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 04 · Iteration
title: A prompt is a *feature,* not a wish.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">A prompt that works on the one example in your head is a demo. A prompt that works across a set of real inputs is a feature.</p>
    <p class="body subtext">Treat prompts like code: version them, diff them in reviews, and when one regresses, fix it like a bug.</p>
  </div>
  <div class="card">
    <div class="label">Build a tiny eval set</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Collect 5–10 real inputs</li>
      <li>Include the boring and the weird</li>
      <li>Run changes against the set</li>
      <li class="muted">Not just the example top of mind</li>
    </ul>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A prompt that works once is a demo. A prompt that works on the eval set is a feature.</p>
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: Where prompts *quietly fail.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">"Don't do X"</div><p>Negative instructions are unreliable. Tell the model what to do instead, not just what to avoid.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Buried instruction</div><p>The ask arrives after a long context dump. Put it near the top, and repeat it near the bottom.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Cherry-picked testing</div><p>It worked once. It also needs to work on the boring, the weird, and the adversarial input.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Mood, not format</div><p>"Make it short and nice" is a vibe. Specify the length and the structure literally.</p></div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: Synthesizing *user research.*
@@
:::example
lead:
### Role, context, task, format — together.
This prompt names who the model is, what it's working from, the single task, and the exact shape of the output. Nothing is left to guess.
The result reads like a teammate's memo, not a generic summary.
tags: Role, Task, Format
---
tag: high-res prompt
[h]Role[/h]You are a research synthesizer for
a B2B product team.

[h]Context[/h]18 user interviews are pasted below.
We sell to operations managers.

[h]Task[/h]Find the 3 most common themes.

[h]Format[/h]For each theme:
- A one-line headline
- 2 supporting quotes
- Count of interviews mentioning it
- One hypothesised root cause
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: The weekly *stakeholder update.*
@@
:::example
lead:
### Audience and shape do the heavy lifting.
By naming who reads it, what they care about, the voice, and the exact structure, you turn raw notes into a polished update on the first try.
This is a prompt you save and reuse every week.
tags: Audience, Voice, Structure
---
tag: high-res prompt
[h]Task[/h]Turn my raw notes (below) into our
weekly exec update.

[h]Audience[/h]CEO, CTO, Head of Sales.
They have 90 seconds to read it.

[h]Voice[/h]Factual, calm, concise. No hype.

[h]Format[/h]- Subject line
- 3 bullets: what shipped
- 2 bullets: risks
- 1 bullet: what we learned
- 0–1 ask
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
Prompts are product surface area — own them like a feature.
Be specific, give the context you hold, show an example, name the format.
Iterate against a small set of real inputs, not a single lucky case.
When in doubt, the prompt isn't too long — it's too vague.
lede: Clarity for thinking. Calm for focus.
:::
