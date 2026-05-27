@@
type: title
eyebrow: A working introduction · appendix F
title: Agentic|*AI.*
@@
The shift from an AI that *answers* to one that *acts.*|What makes an AI "agentic", how the loop works, and how much rope to give it.

===

@@
type: default
eyebrow: 01 · Why this matters
title: From *answering* to *doing.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">A plain chatbot replies and stops. An <em>agentic</em> AI keeps going — it plans a task, takes actions to carry it out, checks the result, and tries again until the goal is met.</p>
    <p class="body subtext">The coding agent you've used all series is exactly this. Understanding how it works turns it from a black box into a tool you can steer — and know when to rein in.</p>
  </div>
  <div class="card">
    <div class="label">A chatbot</div>
    <div class="title">Gives you an answer</div>
    <p>"Here's the code you'd write." You then do the work.</p>
    <div class="label" style="margin-top: 20px;">An agent</div>
    <div class="title">Gets the job done</div>
    <p>Writes the file, runs it, reads the error, fixes it — then reports back.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: Three things make an AI *agentic.*
@@
:::html
<div class="grid-3 reveal" style="margin-top: var(--space-md);">
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">1 · Goals</div>
    <div class="title">It plans</div>
    <p>Given an outcome, it breaks the work into steps instead of needing each one spelled out.</p>
  </div>
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">2 · Tools</div>
    <div class="title">It acts</div>
    <p>It can read and write files, run commands, search the web — actually change things, not just talk.</p>
  </div>
  <div class="card" style="border-top: 3px solid #C9BAA6;">
    <div class="label">3 · Feedback</div>
    <div class="title">It adapts</div>
    <p>It reads the result of each action and decides the next move — looping until the goal is met.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Take away any one of these and you're back to a chatbot.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: The agent loop, *up close.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">This is describe → run → review → refine from chapter one — but the agent runs it <em>itself</em>, many times over, before handing back to you. You set the goal; it turns the handle.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Goal</span><span class="d">You describe the outcome you want.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Plan</span><span class="d">It works out the steps.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Act</span><span class="d">It uses a tool — edits a file, runs a test.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Observe</span><span class="d">It reads what happened, then loops back to act.</span></div></div>
    <div class="loop-step"><span class="n">5</span><div><span class="t">Report</span><span class="d">Goal met — it stops and shows you.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">One instruction from you can be dozens of act-and-observe turns underneath.</p>
:::

===

@@
type: default
eyebrow: 04 · Tools
title: Tools are the agent's *hands.*
@@
:::anatomy
- Read | Look at your files and project | "Open the notes page and the styles."
- middle: Write | Create and edit files | "Add a delete button to the list."
- middle: Run | Execute commands and tests | "Start the app; run the test suite."
- bottom: Reach out | Search the web, call an API | "Check the library's current syntax."
lede: An agent is only as capable — and as risky — as the tools you let it hold.
:::

===

@@
type: default
eyebrow: 05 · Autonomy
title: How much *rope* to give it.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Autonomy is a dial, not a switch. The same agent can ask permission for every action, or run unattended for minutes — you decide based on how reversible the work is.</p>
    <p class="body subtext">Turn it up for safe, checkable jobs; turn it down when actions are hard to undo. Commits (chapter four) are your safety net either way.</p>
  </div>
  <div class="card">
    <div class="label">From short to long leash</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li><strong>Suggest</strong> — it proposes; you approve each step</li>
      <li><strong>Auto within a task</strong> — it runs, pausing on risky moves</li>
      <li><strong>Background</strong> — it works alone, reports when done</li>
      <li class="muted">Match the leash to the cost of a mistake.</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 06 · When to lean in
title: Let it run — or *step in.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Let it run</div>
    <p>Well-scoped, verifiable work: scaffold a page, rename across files, write tests, fix a failing build. Effort and reasoning — where AI shines (chapter one).</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">Step in</div>
    <p>Anything turning on judgement, taste, or an irreversible action: deleting data, sending email, spending money, a product call. You decide; the agent assists.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">The more a task needs judgement or courage, the shorter the leash.</p>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 03
title: One goal, *many* steps.
@@
:::example
lead:
### You ask once; it loops many times.
A single, clear goal can unfold into a dozen tool calls. You don't drive each one — you set the destination and check the arrival.
Notice every step ends in a check, so a wrong turn is caught early.
tags: Goal, Loop, Tools
---
tag: under the hood
[h]You:[/h]
"Add a 'mark all done' button to the
task list, and a test for it."

[h]Agent (acting):[/h]
[k]reads[/k]  TaskList component
[k]edits[/k]  adds the button + handler
[k]writes[/k] a test for the new button
[k]runs[/k]   the test suite  [arr]->[/arr] [ok]passes[/ok]

[c]# Reports back: done, tests green.[/c]
:::

===

@@
type: example
eyebrow: Worked example · 02 of 03
title: Approving a *risky* action.
@@
:::example
lead:
### The pause that saves you.
A well-built agent stops before doing something hard to undo and asks first. Read these prompts — don't reflexively click "yes".
This is autonomy working as intended: speed on the safe steps, a checkpoint on the dangerous one.
tags: Permission, Safety, Reversibility
---
tag: the agent asks
[k]Agent:[/k] "Run the tests?"
        [arr]->[/arr] [ok]safe · allow[/ok]

[k]Agent:[/k] "Edit TaskList.jsx?"
        [arr]->[/arr] [ok]reversible · allow[/ok]

[k]Agent:[/k] "Delete the database file
        and rebuild it?"
        [arr]->[/arr] [arr]hard to undo · read first[/arr]

[c]# Commit before you say yes (chapter four).[/c]
:::

===

@@
type: example
eyebrow: Worked example · 03 of 03
title: Giving a goal it can *check itself.*
@@
:::example
lead:
### Make "done" testable.
Agents work best when success is something they can verify without you. A goal with a built-in check lets the loop run safely to a real finish.
Compare a vague goal with one the agent can prove it has met.
tags: Verifiable, Definition of done, Tests
---
kind: good
tag: a checkable goal
[h]Weak goal:[/h]
"Make the login better."
[c]# No way to know when it's done.[/c]

[h]Checkable goal:[/h]
"Login must reject a wrong password
with a visible error, and a test
must prove it. Stop when it's green."

[ok]The agent can run to a real finish.[/ok]
:::

===

@@
type: default
eyebrow: 07 · Pitfalls
title: Where agents *go wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Trusting autonomy blindly</div><p>Letting it run unattended on irreversible work. Speed is not the same as being right — keep a checkpoint.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Vague goals</div><p>"Improve the app." With no clear "done", the agent wanders. Give it a target it can check.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Runaway loops</div><p>Stuck agents can retry forever — burning time and tokens (appendix E). Stop it and re-scope.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Too many tools, too soon</div><p>Handing over web, files and the terminal at once. Grant access as trust is earned.</p></div>
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
Agentic AI doesn't just answer — it plans, uses tools, and loops until the goal is met.
Underneath, it runs describe → run → review → refine by itself, many times over.
Autonomy is a dial: short leash for risky, irreversible work; long leash for safe, checkable jobs.
Give it goals it can verify, and keep commits as your checkpoint before it acts.
lede: Set the goal. Hold the leash. Let it do the turning.
:::
