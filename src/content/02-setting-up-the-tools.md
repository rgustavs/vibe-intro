@@
type: title
eyebrow: A working introduction · chapter two
title: Setting Up|*the Tools.*
@@
Where vibe coding actually happens —|VS Code and Antigravity, and the agent loop inside them.

===

@@
type: default
eyebrow: 01 · Why this matters
title: Two great homes for *vibe coding.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">To vibe-code, you need one place to talk to an AI agent and see the files it creates. Two tools do this really well, and they feel similar once you're inside.</p>
    <p class="body subtext">You don't need both. Pick one, learn the loop, and the skills carry straight over to the other.</p>
  </div>
  <div class="card">
    <div class="label">VS Code</div>
    <div class="title">Popular editor + AI</div>
    <p>The most widely used code editor, with AI agents added through extensions. Familiar, flexible, everywhere.</p>
    <div class="label" style="margin-top: 20px;">Antigravity</div>
    <div class="title">Agent-first by design</div>
    <p>An editor built around an AI agent from the start. The agent is the main way you work, not an add-on.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Tool 1
title: *VS Code:* the familiar editor.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">VS Code is a free editor from Microsoft. On its own it just opens and edits files — the vibe coding comes from an AI extension you add, like GitHub Copilot or Claude.</p>
    <p class="body subtext">Because it's so common, almost any guide or colleague's setup will match what you see on screen.</p>
  </div>
  <div class="card">
    <div class="label">Getting started</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Install VS Code (free)</li>
      <li>Add an AI agent extension</li>
      <li>Sign in to the agent</li>
      <li>Open a folder to work in</li>
      <li class="muted">Open the chat / agent panel</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Tool 2
title: *Antigravity:* agent-first.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Antigravity is an editor designed around an AI agent. Instead of bolting AI on, the agent is front and centre — you mostly describe what you want and watch it work across your files.</p>
    <p class="body subtext">It's a great fit if you're new and want the conversation, not the configuration. The agent can plan, edit several files, and run things for you.</p>
  </div>
  <div class="card">
    <div class="label">Getting started</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Install Antigravity</li>
      <li>Sign in</li>
      <li>Create or open a project</li>
      <li>Describe your first task in the agent panel</li>
      <li class="muted">Review what it proposes before accepting</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · The loop, in the editor
title: The same four steps, on screen.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">The describe-run-review-refine loop from chapter one happens right inside the editor. Knowing where each step lives is most of the battle.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Type in the agent panel</span><span class="d">Describe the change you want.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Watch the files change</span><span class="d">The agent edits; the diff shows what moved.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Run it in the terminal</span><span class="d">Start the app or open the file.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Reply with the next step</span><span class="d">Or report what went wrong.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Different tools, same rhythm.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Five parts of your *workspace.*
@@
:::anatomy
- Project folder | Everything for one app lives here | Files, code, and settings in one place.
- Editor | Where the code is shown | You can read changes even if you don't write them.
- Agent panel | Where you talk to the AI | Describe tasks; see what it proposes.
- Terminal | Where you run things | Start the app, install tools, see output.
- Source control | Where you save versions | Commits and history — chapter 03.
lede: You'll spend most of your time in just two: the agent panel and the terminal.
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: Your *first project* prompt.
@@
:::example
lead:
### Ask the agent to set the stage.
A good opening prompt tells the agent what to build, where to put it, and to keep it runnable. Then it asks how to run it.
You're not just getting code — you're getting the instructions to see it work.
tags: Scaffold, Run, Clarity
---
tag: agent panel
[h]Task[/h]Create a tiny web page in this
folder that says "Hello, Cambio" and
shows today's date.

[h]Constraints[/h]- One file: index.html
- Plain HTML and JavaScript, no
  frameworks.

[h]Finish by[/h]Telling me exactly how to open it
in my browser.
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: Read the *diff*, then run.
@@
:::example
lead:
### Accept nothing you haven't looked at.
When the agent changes files, the editor shows a diff — green for added lines, red for removed. You don't need to understand every line; you need to see the shape of the change.
Then run it, and tell the agent what you saw.
tags: Review, Diff, Feedback
---
tag: what to check
[c]# The diff shows what changed:[/c]
[k]+[/k] added these lines
[k]-[/k] removed these lines

[h]Ask yourself[/h]- Does this touch only what I asked for?
- Did it create a new file I expected?

[h]Then run it[/h]Open index.html (or run the command
the agent gave you) and look.

[c]# If it's wrong, say what you saw — not[/c]
[c]# just "it's broken".[/c]
:::

===

@@
type: default
eyebrow: 04 · Pitfalls
title: Early *snags* — and fixes.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Not signed in</div><p>The agent panel sits silent. Most setup problems are just a missing sign-in. Check that first.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">No folder open</div><p>The agent has nowhere to put files. Open (or create) a project folder before you start.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Fear of the terminal</div><p>It's just a place to type commands the agent gives you. Copy, paste, press Enter. That's it.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Tweaking settings first</div><p>You don't need a perfect setup to start. Install, sign in, and run the loop. Customise later.</p></div>
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
Pick one tool — VS Code or Antigravity — and learn its loop.
The agent panel is where you describe; the terminal is where you run.
Always read the diff before you accept a change.
The terminal is friendly: it just runs the commands you're given.
lede: One workspace. One rhythm.
:::
