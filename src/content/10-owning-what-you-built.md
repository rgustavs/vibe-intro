@@
type: title
eyebrow: A working introduction · chapter ten
title: Owning|*what you built.*
@@
Shipping is the start line, not the finish.|How a vibe-coded tool grows up into something owned — and how to stop experiments becoming orphaned debt.

===

@@
type: default
eyebrow: 01 · Why this matters
title: A live tool is a *commitment.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">In chapter eight you put your app online; in chapter nine you measured whether it helps. The moment real people rely on it, you've made a quiet promise: when it breaks, someone will care.</p>
    <p class="body subtext">Most task-force experiments never plan for that. The viber moves on, the tool keeps running, and one day it fails with nobody responsible. This chapter is about the unglamorous part — deciding who owns what, before you need to know.</p>
  </div>
  <div class="card">
    <div class="label">The trap</div>
    <div class="title">"It just sort of… stayed"</div>
    <p>A weekend experiment becomes a tool a department depends on — with no owner, no support, no plan.</p>
    <div class="label" style="margin-top: 20px;">The goal</div>
    <div class="title">A tool that's owned</div>
    <p>Someone owns the value, someone owns the upkeep, and everyone knows who.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: "Working" is not the same as *"owned."*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">A tool <em>works</em> when it does the job today. A tool is <em>owned</em> when it has named people responsible for two different things — and a plan for the day it stops working.</p>
    <p class="body subtext">These two kinds of ownership are easy to confuse, and a healthy tool needs both. A tool with neither is just debt that happens to be running.</p>
  </div>
  <div class="card">
    <div class="label">Business ownership</div>
    <div class="title">Owns the value</div>
    <p>Decides what it's for, whether it's still worth running, and what changes next. Usually the person who wanted it.</p>
    <div class="label" style="margin-top: 20px;">Technical ownership</div>
    <div class="title">Owns the upkeep</div>
    <p>Keeps it running, patched and secure; responds when it breaks. Often not the same person who built it.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 03 · The model
title: The four-quadrant *ownership model.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Plot any tool on two axes — is the <strong>business</strong> ownership clear, and is the <strong>technical</strong> upkeep supported? You get four quadrants. Only one is a healthy resting place.</p>
    <p class="body subtext">A vibe-coded tool is usually born in the top-left: loved by the business, supported by no one. The whole job of governance is to move it <em>up and right</em> — or retire it on purpose — before it slides down into the bottom-left.</p>
  </div>
  <div class="stack-sm">
    <div class="card" style="border-left: 3px solid #8FA9B8;">
      <div class="title" style="font-size: 18px;">Shadow tool</div>
      <p>Business cares · no upkeep. Where most experiments start. Useful but fragile.</p>
    </div>
    <div class="card" style="border-left: 3px solid #6F7F6A;">
      <div class="title" style="font-size: 18px;">Owned tool <span style="color:#6F7F6A;">— the goal</span></div>
      <p>Business cares · upkeep assigned. A real part of the portfolio.</p>
    </div>
    <div class="card" style="border-left: 3px solid #C9BAA6;">
      <div class="title" style="font-size: 18px;">Zombie service</div>
      <p>Nobody needs it · still maintained. Quietly costing money. Retire it.</p>
    </div>
    <div class="card" style="border-left: 3px solid #b07a52;">
      <div class="title" style="font-size: 18px;">Orphaned debt</div>
      <p>Nobody owns it · nobody maintains it. The failure mode this chapter exists to prevent.</p>
    </div>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 04 · The transition
title: From *experiment* to *owned tool.*
@@
:::anatomy
- Prove it | A viber builds it; the business confirms it helps | Chapter nine's evidence — is anyone actually using it?
- middle: Name the owners | Assign a business owner and a technical owner | Two names on a page. This single step prevents most orphaning.
- middle: Hand it over | Write down what it does, how it runs, and its secrets' home | A short handover note, not a manual. Reference appendix D for secrets.
- bottom: Review or retire | Revisit on a set date: keep, improve, or decommission | A tool with no end date lives forever, unowned.
lede: Graduation isn't a big project. It's four small, deliberate decisions made on purpose.
:::

===

@@
type: default
eyebrow: Principle 1 · borrowed from ITIL
title: When it breaks, have an *answer ready.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">ITIL is the standard playbook large IT teams use to run services. You don't need to learn it — just borrow one habit: <em>incident management</em>.</p>
    <p class="body subtext">An incident is simply "something that's meant to work, isn't." The point isn't paperwork; it's that the answer to "who do I tell, and who fixes it?" exists <strong>before</strong> the tool goes down — not improvised in a panic.</p>
  </div>
  <div class="card">
    <div class="label">Three things, agreed up front</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li><strong>Report</strong> — where do users say "it's broken"?</li>
      <li><strong>Respond</strong> — who looks, and how soon?</li>
      <li><strong>Recover</strong> — roll back to the last good version (chapter four) while it's fixed.</li>
    </ul>
    <p class="body subtext" style="margin-top: 12px;">For a small tool this can be three lines in a shared doc. The size of the answer should match the size of the tool.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Principle 2 · borrowed from ITIL
title: Every tool has a *lifecycle.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">ITIL's second borrowed idea: a service has a <em>life</em> — it's built, it runs, it's improved, and one day it's retired. Naming the stage you're in keeps a tool from drifting into limbo, half-supported and half-forgotten.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Build</span><span class="d">The vibe-coded experiment.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Run</span><span class="d">Owned, supported, in real use.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Improve</span><span class="d">Changes go through the same loop and review.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Retire</span><span class="d">Switched off on purpose, data handled.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Retiring a tool cleanly is a success, not a failure. An app nobody dares switch off is the real debt.</p>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 03
title: How a tool becomes *orphaned.*
@@
:::example
lead:
### The slide nobody notices.
No single decision orphans a tool. It's the absence of decisions — each reasonable in the moment — that lets a useful experiment rot into a liability.
Read it as a checklist of moments where naming an owner would have changed the ending.
tags: Anti-pattern, Drift, Debt
---
kind: bad
tag: The drift
[c]# A familiar story[/c]
A viber builds a rota tool.   [ok]works[/ok]
The team starts relying on it.
The viber changes role.
        [arr]->[/arr] no technical owner

An API key quietly expires.
        [arr]->[/arr] nobody is told
It breaks on a Monday.
        [arr]->[/arr] nobody knows who to ask

[c]# Now it's "owned" by everyone[/c]
[c]# and no one. Orphaned debt.[/c]
:::

===

@@
type: example
eyebrow: Worked example · 02 of 03
title: A clean *handover.*
@@
:::example
lead:
### A handover note, not a manual.
When a tool graduates, you don't write documentation — you answer the few questions the next person will actually ask.
Have the agent draft it for you: it knows what it built. You just confirm the owners and the dates.
tags: Handover, Ownership, ITIL
---
tag: prompt
[h]You:[/h]
"Draft a one-page ownership record
for this rota tool. Include:"

[k]- What it does[/k] (one paragraph)
[k]- Business owner:[/k] {{name}}
[k]- Technical owner:[/k] {{name}}
[k]- Where it runs[/k] + where secrets live
[k]- If it breaks:[/k] who to tell, how to
  roll back (chapter four)
[k]- Review date:[/k] {{date}} — keep or retire?

[c]# Pin it where the team will find it.[/c]
:::

===

@@
type: example
eyebrow: Worked example · 03 of 03
title: The five-minute *ownership check.*
@@
:::example
lead:
### Run this on anything still live.
Once a quarter, walk your task force's tools through five questions. Anything that fails two or more is sliding toward orphaned debt — fix the gap or plan the retirement.
It's a calm review, not an audit.
tags: Review, Governance, Lifecycle
---
tag: checklist
[h]For each live tool, ask:[/h]
1. Does it still earn its place?
   [c](chapter nine — is it used?)[/c]
2. Who is the business owner?
3. Who is the technical owner?
4. If it broke today, who'd know?
5. When did we last review it?

[ok]All five answered -> it's owned.[/ok]
[arr]Two or more blank -> act now.[/arr]
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: How experiments turn into *debt.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">"The builder owns it"</div><p>Assuming whoever vibe-coded it will support it forever. Roles change. Name a technical owner who stays.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">No off switch</div><p>Tools that can never be retired pile up. Decide a review date when you ship, not years later.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Governance theatre</div><p>A 40-page process for a 200-line app. Match the weight of the plan to the weight of the tool.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Silent dependence</div><p>Not noticing how many people now rely on the "experiment". Check usage before you assume it's disposable.</p></div>
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
Shipping is the start of ownership, not the end of the work.
Every live tool needs two owners — one for the value, one for the upkeep.
Use the four quadrants: move a tool toward *owned*, or retire it on purpose.
Borrow two ITIL habits: a plan for when it breaks, and a date to review or retire.
lede: Own it, or end it. Never let it drift.
:::
