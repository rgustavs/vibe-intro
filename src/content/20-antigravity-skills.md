@@
type: title
eyebrow: A working introduction · appendix J
title: Antigravity's|*Built-in Skills.*
@@
Four native commands do the heavy lifting.|Type a slash, pick a command, and the agent interrogates your idea, runs a whole job to completion, schedules itself, or drives a browser — no setup required.

===

@@
type: default
eyebrow: 01 · Why this matters
title: Four commands, four *hard moments.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Antigravity is agent-first (chapter three), and four built-in commands handle the moments that trip beginners up: a vague brief, a job too big to babysit, a chore you keep forgetting, and checking the app actually works.</p>
    <p class="body subtext">You don't configure them or install anything. You type a slash, and the agent runs a workflow it already knows.</p>
  </div>
  <div class="card">
    <div class="label">The four</div>
    <div class="title">A slash and a word</div>
    <p><code>/grill-me</code> — interrogates your idea.<br><code>/goal</code> — runs to completion.<br><code>/schedule</code> — repeats on a timer.<br><code>/browser</code> — drives the web.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: What a *native command* is.
@@
:::html
<div class="grid-2 reveal">
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">In one line</div>
    <div class="title">A shortcut to a built-in workflow</div>
    <p>You type <code>/</code> and a keyword in the agent panel. Each one triggers a specific way of working the agent already knows — no prompt-crafting required.</p>
  </div>
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">"Native" means</div>
    <div class="title">Built in, nothing to add</div>
    <p>These four ship with Antigravity. You don't install or set them up — they're there from the first project, ready to use.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A keyword that swaps a long prompt for a known routine.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: The four *at a glance.*
@@
:::anatomy
- /grill-me | Cross-examines you before any code is written | Pins down what you actually want to build.
- middle: /goal | Runs a big objective to completion on autopilot | Milestones and subagents, no babysitting.
- middle: /schedule | Turns a prompt into a recurring background job | Cron for the agent.
- bottom: /browser | Drives a real browser to read docs and check the app | Live verification, not guesswork.
lede: Four commands, four moments they save you.
:::

===

@@
type: example
eyebrow: Command · /grill-me
title: Be *interrogated* first.
@@
:::example
lead:
### The alignment interrogator.
Type /grill-me and the agent halts, refuses to write anything yet, and cross-examines you — sequential questions that map the edge cases and extract what you actually want to build.
It's the describing skill from chapter two, but the agent drives it. Answering ten sharp questions now saves a rebuild — and a lot of token spend — later.
tags: Clarify, Edge cases, Alignment
---
tag: agent panel
[h]You type[/h][k]/grill-me[/k] I want a tool that lets
the team book meeting rooms.

[h]It fires back[/h][c]# No code yet — questions first[/c]
- Who can book: anyone, or named staff?
- Can two people hold the same slot?
- What happens to a no-show booking?
- Recurring bookings, or one-offs only?

[ok]It builds the right thing, not the first thing.[/ok]
:::

===

@@
type: default
eyebrow: Command · /goal
title: Hand it the *whole job.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body"><code>/goal</code> points the agent at a big, complex objective and lets it run to completion on its own. It breaks the work into <strong>milestones</strong>, spins up subagents to build, test and debug in parallel, and keeps going without stopping for intermediate sign-off.</p>
    <p class="body subtext">This is high-autonomy working (appendix F). Use it when the target is clear and you're happy to review the finished result rather than every step.</p>
  </div>
  <div class="card">
    <div class="label">Good fit</div>
    <div class="title">"Build the whole reports page"</div>
    <p>A clear objective with many small steps — let it run.</p>
    <div class="label" style="margin-top: 20px;">Poor fit</div>
    <div class="title">"Rethink our pricing"</div>
    <p>Fuzzy or high-stakes? Stay in the loop instead.</p>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Command · /schedule
title: Put chores on a *timer.*
@@
:::example
lead:
### Cron for the agent.
/schedule turns a prompt into a recurring background job. Back it with a cron-like time and the agent runs the task on its own — the routine maintenance you'd otherwise forget.
Good for baseline upkeep: audits, checks, summaries. You read the result when it lands.
tags: Recurring, Background, Upkeep
---
tag: agent panel
[h]You type[/h][k]/schedule[/k] "Run a dependency and
vulnerability audit every Friday
at midnight."

[h]It sets up[/h][c]# Recurring, no babysitting[/c]
when:  [k]0 0 * * 5[/k]  (Fri, 00:00)
task:  audit dependencies, flag risks
then:  post a short summary

[ok]Routine upkeep happens without you.[/ok]
:::

===

@@
type: default
eyebrow: Command · /browser
title: Let it *drive the app.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body"><code>/browser</code> tells the agent to spin up its own headless Chromium and actually use the web. It browses live documentation, or hooks into your running app through the Chrome DevTools Protocol to click through screens, profile performance and catch layout regressions.</p>
    <p class="body subtext">This is the verify habit from chapter seven, done by the agent: it doesn't just claim the page works — it opens it and checks.</p>
  </div>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Browse docs</span><span class="d">Reads the current page, not a stale memory.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Click through</span><span class="d">Drives your local app like a user would.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Profile</span><span class="d">Measures performance via DevTools.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Catch regressions</span><span class="d">Spots layout that's shifted or broken.</span></div></div>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Pitfalls
title: Where it goes *wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">/goal on a fuzzy brief</div><p>Autopilot only helps when the target is clear. Run /grill-me first, then let /goal loose.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Rushing past /grill-me</div><p>Skipping the questions to "just build it" is how you get the wrong thing twice. Answer them.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Set-and-forget /schedule</div><p>A scheduled job still produces output someone must read. Make sure its summaries actually reach a person.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Trusting "it works" without /browser</div><p>If it matters that the screen looks right, have the agent open it and show you.</p></div>
  </div>
</div>
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four commands to *remember.*
@@
:::takeaways
/grill-me makes the agent interrogate you first, pinning down what to build before any code.
/goal hands it a whole objective to run to completion, with subagents working in parallel.
/schedule turns a prompt into a recurring background job on a cron-like timer.
/browser lets it drive a real browser — to read live docs and verify your app.
lede: A slash and a word: interrogate, run, schedule, verify.
:::
