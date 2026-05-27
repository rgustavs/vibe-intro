@@
type: title
eyebrow: A working introduction · chapter six
title: Version Control|*Basics.*
@@
The safety net under every vibe coding session —|save points, history, and a way back, with Git and GitHub.

===

@@
type: default
eyebrow: 01 · Why this matters
title: Your *undo*, but for everything.
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">When an agent is changing your files quickly, things will sometimes break. Without save points, you can lose a working version and not know how to get it back.</p>
    <p class="body subtext">Version control records snapshots of your project over time. You can always return to a version that worked — which makes you brave enough to experiment.</p>
  </div>
  <div class="card">
    <div class="label">Without it</div>
    <div class="title">"It worked an hour ago"</div>
    <p>No way back. You retype, re-prompt, and hope.</p>
    <div class="label" style="margin-top: 20px;">With it</div>
    <div class="title">"Go back to the last good one"</div>
    <p>Every working version is saved. Returning takes seconds.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: Commits are *save points.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">A <em>commit</em> is a labelled snapshot of your whole project at a moment in time. You make one whenever things are in a good state. The list of commits is your history — and you can jump back to any of them.</p>
  <div class="prompt-block good">
<span class="tag">history</span>
<span class="c"># Newest at the top</span>
<span class="k">a1c9f2</span>  Add delete button to notes
<span class="k">7e44b0</span>  Make the list a card layout
<span class="k">3b2d18</span>  First working notes page

<span class="c"># Each line is a save point you</span>
<span class="c"># can return to.</span>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Commit early, commit often — especially right after something works.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Four words you'll *actually* use.
@@
:::anatomy
- Repository | Your project, tracked | "The folder Git is watching." Often shortened to "repo".
- Commit | A saved snapshot | "A version, with a short message describing it."
- Branch | A safe side-track | "Try a change without touching the main version."
- Remote | The online copy | "Your project on GitHub, as a backup and to share."
lede: That's most of the vocabulary. Everything else is detail you can learn later.
:::

===

@@
type: default
eyebrow: 04 · The everyday loop
title: The four-step *daily* rhythm.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">You don't need to master Git. You need one small habit, repeated. Most editors and agents can do these steps for you with a click or a sentence.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Change</span><span class="d">Vibe-code until something works.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Review</span><span class="d">Look at what changed (the diff).</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Commit</span><span class="d">Save a snapshot with a short message.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Push</span><span class="d">Send it to GitHub as a backup.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Commit when it works. Push when you pause.</p>
:::

===

@@
type: default
eyebrow: Principle 1
title: Branches make you *fearless.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">When to start a branch</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Trying a risky or big change</li>
      <li>Exploring an idea you might throw away</li>
      <li>Working on something while main stays stable</li>
      <li class="muted">If it works, merge it back. If not, delete it.</li>
    </ul>
  </div>
  <p class="lede">A branch is a parallel copy. Your main version stays safe while you experiment — so a failed idea costs you nothing.</p>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: Write a *good commit message.*
@@
:::example
lead:
### Future-you is the reader.
A commit message is a note to yourself. "stuff" tells you nothing in a week; a short, specific line tells you exactly what that save point was.
Describe what changed, in plain words.
tags: Clarity, History, Habit
---
kind: bad
tag: unhelpful
git commit -m "stuff"
git commit -m "fixes"
git commit -m "asdf"

# In a week, these tell
# you nothing.
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: The *daily flow*, in practice.
@@
:::example
lead:
### You can just ask the agent.
You rarely need to type these by hand — "commit this with a message about the delete button, then push" usually works. But here's what happens underneath.
Read it once; you'll recognise it forever.
tags: Commit, Push, Confidence
---
tag: terminal
[c]# See what changed[/c]
git status

[c]# Save a snapshot with a clear message[/c]
git commit -m [arg]"Add delete button to notes"[/arg]

[c]# Send it to GitHub (your backup)[/c]
git push

[c]# Made a mess? Go back to the last commit[/c]
git restore .
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: Easy *mistakes* to skip.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Never committing</div><p>One huge commit after a week. If anything breaks, there's no good point to return to. Commit small and often.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Committing secrets</div><p>Passwords or API keys saved into history are hard to remove. Keep them out of the project files.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Forgetting to push</div><p>A commit only on your laptop isn't a backup. Push to GitHub when you pause so your work is safe.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Fearing the jargon</div><p>Pull, merge, rebase — you can ignore most of it at first. Commit, push, and restore cover the early days.</p></div>
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
A commit is a save point; the history is your way back.
Build the habit: change, review, commit, push.
Use a branch to experiment safely while main stays stable.
Write short, specific commit messages for future-you.
lede: A safety net. So you can be brave.
:::
