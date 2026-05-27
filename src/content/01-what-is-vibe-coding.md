@@
type: title
eyebrow: A working introduction · chapter one
title: What is|*Vibe Coding?*
@@
A practical way to build software by describing what you want —|and letting an AI agent write the code.

===

@@
type: default
eyebrow: 01 · Why this matters
title: You describe. *It builds.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">For decades, building software meant typing exact syntax in a programming language. The computer did only what the syntax said — and only if it was perfect.</p>
    <p class="body subtext">AI coding agents change the starting point. You describe what you want in plain language, and the agent writes the code. Your skill becomes <em>describing behaviour clearly</em>, not memorising syntax.</p>
  </div>
  <div class="card">
    <div class="label">Before</div>
    <div class="title">You wrote the code</div>
    <p>Every line, by hand, in a language the computer understands.</p>
    <div class="label" style="margin-top: 20px;">Now</div>
    <div class="title">You direct the code</div>
    <p>You describe the outcome and review the result. The agent does the typing.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: It's a *conversation*, not a command.
@@
The same idea, written two ways. The agent can act on the one on the right; it has to guess at the one on the left.

:::compare
[bad] vague
make me an app that
tracks stuff
---
[good] specific
Build a task tracker.
{{One SQLite table}}: id, title, done.
A list view and an add form.
No login.
:::

> The clearer your words, the better the software. Vague in, vague out.

===

@@
type: default
eyebrow: 03 · The loop
title: Describe, run, review, *refine.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">Vibe coding is a loop, not a single prompt. You describe a small piece of behaviour, the agent writes the code, you run it and look at the result, then you describe the next change.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Describe</span><span class="d">Say what you want, in plain language.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Generate</span><span class="d">The agent writes or edits the code.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Run &amp; review</span><span class="d">Try it. Read what changed.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Refine</span><span class="d">Describe the next change. Repeat.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Small loops beat one giant prompt.</p>
:::

===

@@
type: default
eyebrow: 04 · What good looks like
title: Five ingredients of a good session.
@@
:::anatomy
- Intent | What you want to happen | "Users can save a note and see it later."
- Context | What the agent should know | The files, the goal, and any constraints.
- Small steps | One change at a time | Easier to review, easier to undo.
- Review | You read the result | You stay the author and the editor.
- Save points | Commit working versions | Your safety net — see chapter 03.
lede: Give the agent intent and context — then keep it on a short leash.
:::

===

@@
type: default
eyebrow: Principle 1
title: Keep the steps *small.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">The habit that makes it work</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Ask for one change at a time</li>
      <li>Run it and look before moving on</li>
      <li>Keep each request small enough to check</li>
      <li class="muted">Save a working version before the next change</li>
    </ul>
  </div>
  <p class="lede">A big vague prompt gives you a big vague mess. Small, clear steps give you something you can trust.</p>
</div>
:::

===

@@
type: default
eyebrow: Principle 2
title: You stay the *author.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">The agent is fast, not wise</div>
    <p>It will happily write confident code that does the wrong thing. Speed is its gift; judgement is yours.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">You own the result</div>
    <p>Read what changed. Run it. If you can't roughly explain what it does, ask the agent to explain — then decide.</p>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: From one sentence to a *running page.*
@@
:::example
lead:
### A first prompt that actually works.
Notice it gives intent, a few constraints, and asks for next steps. That's enough for an agent to build something real and small.
You are not asking for a finished product — you are starting the loop.
tags: Intent, Constraints, Output
---
tag: vibe prompt
[h]Goal[/h]A page where I can add a note and
see all my notes in a list.

[h]Constraints[/h]- Keep it to one HTML file.
- Save notes in the browser so they
  survive a refresh.
- No login, no server.

[h]Then[/h]Show me how to open it, and tell me
what to type next if I want to delete
a note.
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: Refining is just *more describing.*
@@
:::example
lead:
### You don't restart. You nudge.
Each follow-up is a small, reviewable step. You run it, check it, then ask for the next change.
This is the whole craft: a series of small, clear requests.
tags: Iterate, Feedback, Small steps
---
tag: follow-ups
[c]# After the first version runs:[/c]

[k]You:[/k] The list is ugly. Make it a
clean card layout, newest first.

[k]You:[/k] Add a delete button to each
note. Ask me to confirm first.

[k]You:[/k] Right now I can save a blank
note. Don't allow that.

[c]# Each line is a small step you can check.[/c]
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: Where beginners *get stuck.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">One giant prompt</div><p>"Build me a CRM." You'll get something, but you won't understand it or be able to fix it. Start tiny.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Accepting blindly</div><p>Clicking "accept" without running or reading. Bugs pile up silently. Always check the result.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">No save points</div><p>Hours of changes with no way back. Commit working versions so you can always undo — chapter 03.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Vague feedback</div><p>"It's broken." Instead: what you did, what you expected, and what actually happened.</p></div>
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
You describe behaviour; the agent writes the code.
Work in small loops: describe, run, review, refine.
Give clear intent and context — vague in, vague out.
You stay the author: read it, run it, save working versions.
lede: Clear intent. Calm building.
:::
