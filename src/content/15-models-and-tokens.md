@@
type: title
eyebrow: A working introduction · appendix E
title: Models &|*tokens.*
@@
Which model to reach for, and what you're actually paying for.|A plain-English guide to Opus, Sonnet, Haiku — and the tokens they read and write.

===

@@
type: default
eyebrow: 01 · Why this matters
title: The model is a *lever you control.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Behind every agent sits a <em>model</em> — the AI that actually does the reading, thinking and writing. Most tools let you pick which one. It's one of the few dials you turn directly.</p>
    <p class="body subtext">Pick well and work feels fast, sharp and cheap. Pick badly and you either wait (and pay) for power you didn't need, or you fight a model that's out of its depth. This appendix shows how to match the model to the job — and what a <em>token</em> is, so the costs stop feeling mysterious.</p>
  </div>
  <div class="card">
    <div class="label">Two questions, every session</div>
    <div class="title">How hard is this job?</div>
    <p>A one-line tweak and a full redesign deserve different models.</p>
    <div class="label" style="margin-top: 20px;">How much will it read?</div>
    <div class="title">How many tokens?</div>
    <p>What you send and what it writes both cost — measured in tokens.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: A *token* is a chunk of text.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Models don't read letters or whole words — they read <em>tokens</em>: small word-pieces, roughly <strong>four characters</strong> each, or about <strong>¾ of a word</strong> on average.</p>
    <p class="body subtext">Common words are a single token. Rarer words split into several. Spaces, punctuation, line breaks and code symbols all count too. Everything the model touches is first chopped into tokens — that's the unit it thinks and bills in.</p>
  </div>
  <div class="prompt-block good">
<span class="c"># One word -> one or more tokens</span>

<span class="k">"task"</span>        [arr]->[/arr] 1 token
<span class="k">"tracker"</span>     [arr]->[/arr] 1 token
<span class="k">"tokeniser"</span>   [arr]->[/arr] token + iser  (2)
<span class="k">"unbelievable"</span> [arr]->[/arr] un + bel + iev + able

<span class="c"># Rule of thumb</span>
[ok]100 tokens  ~=  75 words[/ok]
[ok]1,000 words ~=  1,300 tokens[/ok]
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Roughly four characters a token. You'll never count by hand — you just need the feel.</p>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 07
title: Counting a *real prompt.*
@@
:::example
lead:
### Both sides of the conversation count.
You pay for *input* (everything you send — your words plus any files or code the agent is looking at) and for *output* (everything it writes back).
A short question with a huge file attached is a big input. A short question that triggers a 600-line file is a big output. Both add up.
tags: Input, Output, Counting
---
tag: Token tally
[h]You send (input):[/h]
"Build a task tracker." 
        [arr]->[/arr] ~5 tokens

A 40-line spec you pasted
        [arr]->[/arr] ~400 tokens

[h]Agent writes (output):[/h]
A React component, ~120 lines
        [arr]->[/arr] ~1,500 tokens

[c]# Total billed this turn:[/c]
[ok]~1,905 tokens (input + output)[/ok]
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: The *context window:* the model's desk.
@@
:::anatomy
- The window | The most tokens a model can hold at once | Very large today — a whole book's worth, hundreds of thousands of tokens.
- middle: What fills it | Your prompts + the agent's replies + every file it reads | All three share the same desk space.
- bottom: When it's full | The oldest parts slide out of view | The model starts to "forget" what you said early on.
lede: Running "out of tokens" means you've run past the window — not out of money. A fresh chat clears the desk.
:::

===

@@
type: default
eyebrow: 04 · The three Claude models
title: Opus, Sonnet, *Haiku.*
@@
:::html
<div class="grid-3 reveal" style="margin-top: var(--space-md);">
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">The heavyweight</div>
    <div class="title">Opus</div>
    <p>Deepest reasoning. Slowest and dearest. For the genuinely hard problems where getting it right matters more than speed.</p>
  </div>
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">The workhorse</div>
    <div class="title">Sonnet</div>
    <p>Balanced — fast and very capable. Handles the large majority of everyday building. The sensible default.</p>
  </div>
  <div class="card" style="border-top: 3px solid #C9BAA6;">
    <div class="label">The sprinter</div>
    <div class="title">Haiku</div>
    <p>Fastest and cheapest, lighter reasoning. For quick edits, simple questions and high-volume, low-difficulty jobs.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Same family, three sizes. They trade <em>capability</em> against <em>speed</em> and <em>cost</em> — you choose where to sit.</p>
:::

===

@@
type: default
eyebrow: 05 · The trade-off
title: Capability vs. *speed vs. cost.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">You can't have all three at once. A bigger model thinks harder but is slower and costs more per token; a smaller one is quick and cheap but shallower.</p>
    <p class="body subtext">The trick isn't "always pick the best one." It's matching the model to the difficulty of the task in front of you — and being willing to switch mid-project.</p>
  </div>
  <div class="card">
    <div class="label">As you go bigger</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Reasoning gets <strong>deeper</strong></li>
      <li>Replies get <strong>slower</strong></li>
      <li>Cost per token goes <strong>up</strong></li>
    </ul>
    <div class="label" style="margin-top: 20px;">As you go smaller</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Replies get <strong>faster</strong></li>
      <li>Cost drops <strong>sharply</strong></li>
      <li>It struggles with <strong>hard logic</strong></li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 06 · When to use which
title: A simple *decision guide.*
@@
:::anatomy
- Reach for Opus | Architecture, gnarly multi-file bugs, big refactors, tricky logic | When a wrong answer is expensive and you'd happily wait for a right one.
- middle: Stay on Sonnet | Building features, writing components, normal debugging, explaining code | Your default for ~80% of vibe coding. Start here.
- bottom: Drop to Haiku | Rename things, tweak copy, format data, quick yes/no questions | When the job is easy and you want the answer now.
lede: Start on the workhorse. Escalate to Opus when you're stuck; drop to Haiku when it's trivial.
:::

===

@@
type: example
eyebrow: Worked example · 02 of 07
title: *Trivial* job, small model.
@@
:::example
lead:
### Don't send a heavyweight to do a sprint.
"Rename a button" needs no deep reasoning. Using a big model here just means waiting longer and paying more for an identical result.
Haiku does it instantly. Save the big model's thinking for problems that actually need it.
tags: Haiku, Quick edits, Cost
---
tag: Good fit · Haiku
[h]The job:[/h]
"Change the 'Submit' button label
to 'Save changes' across the app."

[h]Why Haiku:[/h]
- Pure find-and-replace, no logic.
- You want it done in a second.
- It might run dozens of times today.

[ok]Fast, cheap, exactly right.[/ok]
:::

===

@@
type: example
eyebrow: Worked example · 03 of 07
title: *Hard* job, big model.
@@
:::example
lead:
### When getting it right is worth the wait.
A subtle bug that spans the frontend, the API and the database is exactly where deeper reasoning earns its keep.
A small model may patch the symptom and miss the cause — and you'll pay more in rework than you saved on tokens.
tags: Opus, Debugging, Architecture
---
tag: Good fit · Opus
[h]The job:[/h]
"Payments succeed but orders show
'pending'. It only happens for
returning customers. Find the cause."

[h]Why Opus:[/h]
- Cross-cutting: React, FastAPI, SQLite.
- Needs a theory, not a guess.
- A wrong fix here costs real money.

[ok]Slower, dearer — and worth it.[/ok]
:::

===

@@
type: default
eyebrow: 07 · Other suppliers
title: Everyone ships the *same shape.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Anthropic isn't alone. The other big labs offer the very same three-tier line-up under different names — a deep flagship, a balanced middle, and a small fast one.</p>
    <p class="body subtext">OpenAI's GPT family and Google's Gemini family both follow this large / medium / small pattern. The names and benchmarks shuffle every few months; the <em>shape</em> doesn't.</p>
  </div>
  <div class="card">
    <div class="label">Think in tiers, not brands</div>
    <div class="title">Flagship</div>
    <p>Opus · GPT flagship · Gemini Pro — deepest reasoning.</p>
    <div class="title" style="margin-top: 14px;">Balanced</div>
    <p>Sonnet · GPT mid · Gemini Flash — the daily workhorse.</p>
    <div class="title" style="margin-top: 14px;">Small &amp; fast</div>
    <p>Haiku · GPT mini · Gemini Flash-Lite — quick and cheap.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Learn the three tiers once and you can read any provider's menu.</p>
:::

===

@@
type: example
eyebrow: Worked example · 04 of 07
title: Judging a model on *your* work.
@@
:::example
lead:
### Benchmarks are a starting point, not a verdict.
Leaderboard scores are measured on generic tests, not on your task. The model that tops a chart may not be the one that best understands *your* codebase and style.
Keep a small, repeatable task and run it on a couple of models before you commit.
tags: Testing, Benchmarks, Fit
---
tag: A fair test
[h]Your pocket benchmark:[/h]
"Add a 'mark all done' button to the
task list. Match the existing style.
Write a test for the empty list."

[h]Run it on two models. Compare:[/h]
- Did it match your conventions?
- Did the test actually pass?
- Was the speed worth the cost?

[c]# The winner on YOUR task wins.[/c]
:::

===

@@
type: default
eyebrow: 08 · Pitfalls
title: Where model choice *goes wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card">
      <div class="title" style="font-size: 19px;">Always the biggest</div>
      <p>Using the heavyweight for every tweak. You wait longer and pay more for results a smaller model nails instantly.</p>
    </div>
    <div class="card">
      <div class="title" style="font-size: 19px;">Always the cheapest</div>
      <p>Forcing hard problems onto a small model. It guesses, you re-prompt five times — and spend more than the big model would have cost.</p>
    </div>
  </div>
  <div class="stack-sm">
    <div class="card">
      <div class="title" style="font-size: 19px;">Forgetting output counts</div>
      <p>"It's a short question!" — but it asked for a 500-line file. Output is often the bigger half of the bill.</p>
    </div>
    <div class="card">
      <div class="title" style="font-size: 19px;">Pasting the whole repo</div>
      <p>Dumping every file when a snippet would do. You fill the window with noise and pay for tokens the model didn't need.</p>
    </div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 05 of 07
title: The *same task*, two bills.
@@
:::example
lead:
### Why tokens — not turns — are the cost.
Two people ask for the same feature. One pastes their entire project "for context"; the other pastes the one file that matters.
The work is identical. The bill is not — because cost follows tokens read and written, not the number of messages.
tags: Cost, Context, Tokens
---
tag: Two approaches
[h]Person A — "here's everything":[/h]
pastes 30 files
        [arr]->[/arr] ~60,000 input tokens

[h]Person B — "here's the file":[/h]
pastes 1 relevant file
        [arr]->[/arr] ~2,000 input tokens

[c]# Same feature. Same answer.[/c]
[ok]B pays a fraction — and gets a
sharper reply from a clearer desk.[/ok]
:::

===

@@
type: example
eyebrow: Worked example · 06 of 07
title: *Escalating* mid-task.
@@
:::example
lead:
### Start cheap, climb only when stuck.
You don't pick one model for the whole day. Begin on the workhorse; if it spins on a genuinely hard step, lift that one step to the heavyweight, then drop back down.
This keeps most of your work fast and cheap, and spends the expensive thinking only where it's needed.
tags: Sonnet, Opus, Workflow
---
tag: A real session
[k]Sonnet:[/k] builds the task form  [ok]ok[/ok]
[k]Sonnet:[/k] adds the list view    [ok]ok[/ok]
[k]Sonnet:[/k] stuck on a race bug   [arr]x[/arr]

  [c]# escalate this one step[/c]
[k]Opus:[/k] diagnoses the root cause [ok]ok[/ok]

  [c]# drop back down[/c]
[k]Sonnet:[/k] writes the regression test
:::

===

@@
type: default
eyebrow: 09 · In practice
title: Choosing inside *your tools.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">In VS Code with Antigravity, the model is a dropdown in the chat panel. Switching is instant and you can change it between turns.</p>
    <p class="body subtext">Pair this with the habit from the glossary: one job per chat, and start fresh when the window fills. A short, focused chat on the right-sized model is faster, cheaper and sharper than a long one on the biggest.</p>
  </div>
  <div class="card">
    <div class="label">A workable default</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Live on <strong>Sonnet</strong> for building</li>
      <li>Jump to <strong>Opus</strong> when you're genuinely stuck</li>
      <li>Drop to <strong>Haiku</strong> for quick, simple edits</li>
      <li class="muted">Start a fresh chat per task to keep tokens low</li>
    </ul>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 07 of 07
title: Asking the agent to *advise.*
@@
:::example
lead:
### You can just ask.
Not sure which model fits? Describe the task and let the agent tell you. It knows its own trade-offs and will usually steer you sensibly.
This is the same move as the glossary's "the agent is your dictionary" — let it teach you as you go.
tags: Self-service, Habit
---
tag: prompt
[h]You:[/h]
"I need to reformat a CSV and rename
its columns. Nothing clever. Which
model is overkill here, and which is
the cheap, fast choice?"

[h]Agent:[/h]
"That's pure data wrangling, no tricky
logic — a small, fast model like Haiku
is the right call. Save Opus for the
parts that need real reasoning."
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
A token is a chunk of text (~4 characters); both what you send and what the model writes are counted.
The context window is a shared desk — prompts, replies and files all sit on it; a fresh chat clears it.
Opus, Sonnet, Haiku trade capability against speed and cost — start on Sonnet, escalate or drop as needed.
Every supplier ships the same three tiers; think flagship / balanced / small, and test on your own task.
lede: Right-size the model. Right-size the context. Calm, cheap, sharp.
:::
