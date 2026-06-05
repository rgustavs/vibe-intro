@@
type: title
eyebrow: A working introduction · appendix J
title: Antigravity's|*Built-in Skills.*
@@
The agent doesn't start from nothing.|Antigravity ships with a set of skills it already knows how to use — and a way to teach it new ones. Knowing what's there saves you asking for what you already have.

===

@@
type: default
eyebrow: 01 · Why this matters
title: Know what's *already there.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Antigravity is agent-first (chapter three): the agent can plan, edit across files, run commands and check its own work. Much of what you might think you need to set up is already built in.</p>
    <p class="body subtext">Learn the handful of built-in skills and you'll write shorter prompts, hand the agent bigger steps, and stop reaching for tools you already have.</p>
  </div>
  <div class="card">
    <div class="label">The instinct</div>
    <div class="title">"How do I get it to test the page?"</div>
    <p>You start hunting for an extension or a workaround.</p>
    <div class="label" style="margin-top: 20px;">The reality</div>
    <div class="title">"It can already open the browser"</div>
    <p>Browser checks, plans and memory are built in. Just ask.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: What "built-in *skills*" means.
@@
:::html
<div class="grid-2 reveal">
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">In one line</div>
    <div class="title">What the agent can do out of the box</div>
    <p>The things Antigravity can already do — plan, edit, run, browse and remember — without you installing or configuring anything.</p>
  </div>
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">And one named feature</div>
    <div class="title">"Skills" with a capital S</div>
    <p>Antigravity also calls reusable packs of know-how <em>Skills</em> — small Markdown files that teach the agent your project's conventions. More on those near the end.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Two senses of the word: what it can already do, and what you can teach it.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: The skills it *ships with.*
@@
:::anatomy
- Plan first | The agent breaks a task into steps before touching code | You see the plan and can correct it early.
- middle: Edit across files | It changes several files at once, not one at a time | The diff shows every move (chapter three).
- middle: Run commands | It uses the terminal to install, build and start the app | No copying commands by hand.
- middle: Check in the browser | It opens the running app and looks at the screen | "Browser-in-the-loop" — it verifies the UI itself (chapter seven).
- middle: Remember | It saves useful context to a knowledge base | Conventions carry over to the next task.
- bottom: Work in parallel | The Agent Manager runs several agents at once | Mission control for bigger jobs.
lede: Six things the agent can do before you add anything.
:::

===

@@
type: default
eyebrow: 04 · Artifacts
title: How it *shows its work.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">As it works, the agent produces <strong>Artifacts</strong> — a plan, a task list, screenshots, a short recording of the app running. They turn "trust me" into "see for yourself".</p>
    <p class="body subtext">This is the review step of describe → run → review → refine (chapter one). You read the Artifact, leave a comment on it, and the agent adjusts — often without stopping.</p>
  </div>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Plan</span><span class="d">A checklist of what it intends to do.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Diff</span><span class="d">Exactly which lines changed, and where.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Screenshot</span><span class="d">The running screen, captured for you.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Recording</span><span class="d">A short clip of the feature actually working.</span></div></div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: Let it *verify itself.*
@@
:::example
lead:
### Ask for the check, not just the change.
The agent can open your app in a browser and confirm the result. So don't stop at "add the button" — ask it to prove the button works and show you.
This is the verify habit from chapter seven, using a skill that's already built in.
tags: Browser, Verify, Artifacts
---
kind: good
tag: agent panel
[h]Task[/h]Add a "Download CSV" button to the
reports page.

[h]Then verify[/h]Open the app in the browser, click
the button, and confirm a file
downloads.

[h]Show me[/h]A [k]screenshot[/k] of the page and a short
[k]recording[/k] of the download working.

[ok]You review the result, not just the code.[/ok]
:::

===

@@
type: default
eyebrow: 05 · Teaching new skills
title: Add your own *Skills.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">A <strong>Skill</strong> is a small Markdown file describing a job the agent should do your way — a coding convention, a review checklist, a deployment routine. It stays dormant until a request matches it, then loads into the agent's context on its own.</p>
    <p class="body subtext">It's the same idea as a reusable prompt (appendix A), but saved where the agent finds it automatically — no copy-paste each time.</p>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Workspace Skills</div><p>Live in the project, under <code>.agent/skills/</code>. Shared with the team through Git (chapter four), so everyone's agent follows the same rules.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Global Skills</div><p>Live on your machine and apply to every project. Good for personal habits that aren't project-specific.</p></div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: A Skill the team *shares.*
@@
:::example
lead:
### Write the convention down once.
Instead of reminding the agent of your house rules in every prompt, save them as a Skill. Antigravity loads it whenever the work matches — and because it lives in Git, the whole task force gets it.
A few plain sentences are enough; you don't write code.
tags: Skill, Convention, Reuse
---
tag: .agent/skills/our-stack/SKILL.md
[h]name:[/h] our-stack
[h]description:[/h] How we build and test
features in this project.

[c]# When building a feature[/c]
- Use [k]React[/k] on the front end, [k]FastAPI[/k]
  and [k]SQLite[/k] on the back (chapter five).
- Put new endpoints under [k]/api[/k].
- After any change, open the browser
  and verify it before finishing.

[ok]Every agent on the team now works your way.[/ok]
:::

===

@@
type: default
eyebrow: 06 · Pitfalls
title: Where it goes *wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Rebuilding what's built in</div><p>Hunting for a testing extension when the agent can already open the browser. Ask for the built-in skill first.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Skipping the Artifacts</div><p>Accepting the work without reading the plan, diff or screenshot. They exist so you can review — use them (chapter seven).</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Skills that say too much</div><p>One Skill stuffed with every rule you can think of. Keep each one short and about a single job, so it loads when it should.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Too many agents at once</div><p>Spawning a crowd in the Agent Manager and losing track. Start with one; add parallel agents only when the work is truly separate.</p></div>
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
Antigravity's agent can already plan, edit, run, browse and remember — learn the built-in skills before adding anything.
Artifacts — plans, diffs, screenshots, recordings — are how it shows its work; read them to review (chapter seven).
Ask the agent to verify in the browser, not just make the change.
Save your house rules as Skills in Git so the whole team's agent works the same way.
lede: Know what's built in; teach it the rest.
:::
