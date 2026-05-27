@@
type: title
eyebrow: A working introduction · chapter one
title: The Agentic Shift|*from chat to action.*
@@
A chatbot answers a question.|An agent takes actions until the job is done — and that changes how you work with it.

===

@@
type: default
eyebrow: 01 · Why this matters
title: An agent doesn't answer. *It acts.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">You've used chat models: you ask, they reply, you decide what to do next. Vibe coding runs on something more capable — an <em>agent</em>.</p>
    <p class="body subtext">An agent doesn't just produce text. It works in steps: it reads files, writes code, runs commands, and checks its own work — looping until your goal is met. Understanding that shift is the foundation for everything in this series.</p>
  </div>
  <div class="card">
    <div class="label">Chatbot</div>
    <div class="title">One question, one answer</div>
    <p>You hold all the initiative. Nothing happens in the world unless you act on the reply.</p>
    <div class="label" style="margin-top: 20px;">Agent</div>
    <div class="title">A goal, then many steps</div>
    <p>It plans, takes actions, observes results, and keeps going. The work happens while you watch.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: A model *plus* a loop.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">An agent is a language model wrapped in scaffolding that lets it act: <strong>a model + instructions + tools + a loop</strong>. The model decides; the tools do; the loop keeps it going until the goal is reached.</p>
  <div class="prompt-block good">
<span class="c"># A chatbot is just the model.</span>
<span class="c"># An agent adds three things around it:</span>

<span class="k">Instructions:</span> who it is, what to do
<span class="k">Tools:</span> search, edit files, run code
<span class="k">Loop:</span> act, observe, decide, repeat
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">The model is the brain. The scaffolding is what gives it hands.</p>
:::

===

@@
type: default
eyebrow: 03 · The brain
title: The model: *reads text, writes text.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">At the centre is a large language model. It's the reasoning engine: it plans, summarises, chooses which tool to use, and decides when the job is done.</p>
    <p class="body subtext">But on its own it has hard limits — and knowing them tells you why the scaffolding exists.</p>
  </div>
  <div class="card">
    <div class="label">What the model can't do alone</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Reach live data on its own</li>
      <li>Remember past sessions</li>
      <li>Act in the world unaided</li>
    </ul>
    <p style="margin-top: 12px;">Everything beyond reading and writing text has to be wired around it.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 04 · The unit of work
title: Everything is *tokens.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Before the model reads anything, text is broken into <em>tokens</em> — small chunks, roughly four characters each. The model reads tokens, thinks in tokens, and writes tokens.</p>
    <p class="body subtext">That sounds technical, but it has two practical consequences you'll feel every day.</p>
  </div>
  <div class="card">
    <div class="label">Context window</div>
    <div class="title">Finite working memory</div>
    <p>Instructions, conversation, and files all share one space. Once it's full, the oldest content falls out.</p>
    <div class="label" style="margin-top: 20px;">Cost &amp; speed</div>
    <div class="title">Every token is metered</div>
    <p>Longer prompts cost more and run slower. <em>Concise wins.</em></p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 05 · Anatomy
title: Five parts *around the model.*
@@
:::anatomy
- System prompt | The standing instructions | Role, purpose, and the rules it follows every time.
- Tools | What it can actually do | Search, read a file, run code, call an API, send a message.
- Memory | What it carries forward | Notes from earlier loaded back in when relevant.
- Orchestration | The control logic | Decides when to call the model, use a tool, stop, or ask a human.
- Guardrails | The limits | Permissions, filters, and human checkpoints that keep it in bounds.
lede: Most of the work of building an agent lives in this scaffolding — not in the model itself.
:::

===

@@
type: default
eyebrow: 06 · The loop
title: Think, act, *observe,* repeat.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">What makes it an agent is the loop. It doesn't answer once — it takes a step, looks at the result, and decides the next step, over and over until the goal is met. This is the agent's <em>internal</em> loop — distinct from your own describe-run-review-refine loop in chapter two.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Think</span><span class="d">Plan the next step toward the goal.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Act</span><span class="d">Call a tool: edit a file, run a command.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Observe</span><span class="d">Read the result. Did it work?</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Repeat</span><span class="d">Until the job is done — or it should stop.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A good agent knows when to stop. A bad one loops forever.</p>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 01
title: What a loop *actually looks like.*
@@
:::example
lead:
### One goal, several steps.
Given a single instruction, the agent doesn't reply once — it runs a sequence of tool calls, checking the result each time before moving on.
Each step consumes tokens and carries forward what it learned. You watch this trace unfold in the editor.
tags: Loop, Tools, Observe
---
tag: agent trace
[h]Goal:[/h] "Add a delete button to the
notes app and make sure it works."

[k]Think:[/k] I need to find the notes UI.
[k]Act:[/k]   search files for "note list"
[k]Observe:[/k] found app.js, line 40

[k]Think:[/k] Add a button + handler.
[k]Act:[/k]   edit app.js
[k]Observe:[/k] file saved

[k]Think:[/k] Does it run?
[k]Act:[/k]   run the app
[k]Observe:[/k] [ok]page loads, delete works[/ok]

[c]# Goal met -> the agent stops.[/c]
:::

===

@@
type: default
eyebrow: 07 · What comes next
title: Capability raises a *new question.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">The power</div>
    <p>Because it acts in a loop, an agent can do real work end to end — not just suggest, but build, run, and fix.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">The responsibility</div>
    <p>If it takes actions on its own, how do you know they were the right ones? Trusting and evaluating an agent's work is its own skill — chapter eight.</p>
  </div>
</div>
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
An agent isn't a chatbot — it's a system that takes action toward a goal.
The model is the reasoning brain; it only reads and writes text.
Everything is tokens — a finite, metered context window that shapes cost and design.
Agents work in a loop: think, act, observe, repeat — until the job is done.
lede: It doesn't answer. It acts.
:::
