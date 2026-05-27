@@
type: title
eyebrow: A working introduction · appendix C
title: When It|*Won't Behave.*
@@
A calm field guide to the everyday snags —|what they mean, and the move that fixes them.

===

@@
type: default
eyebrow: 01 · First, don't panic
title: Most snags are *ordinary.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Nearly every problem a beginner hits is common and well-understood — the agent has seen it a thousand times. The fix is rarely dramatic; it's usually one small thing out of place.</p>
    <p class="body subtext">Before anything else, do the three things from chapter seven: read the error, change one thing, and remember you can always return to your last good commit.</p>
  </div>
  <div class="card">
    <div class="label">The opening move</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Read the error — it often names the cause</li>
      <li>Copy it exactly and hand it to the agent</li>
      <li>One change at a time, then check</li>
      <li class="muted">Worst case: restore the last commit and retry</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Common snags
title: Symptom, cause, *fix.*
@@
:::anatomy
- Won't start | A dependency isn't installed | Ask the agent to install what's missing, then start again.
- Page is blank | The frontend or backend isn't running | Check both are started; open the browser console for the error.
- "Address already in use" | An old run is still holding the port | Stop the previous one, or ask for a different port.
- "Module not found" | Code is calling something not installed | Paste the name; ask the agent to add it.
lede: Don't memorise these — recognise the shape, then paste the exact message.
:::

===

@@
type: default
eyebrow: 03 · The hardest one
title: When the agent goes in *circles.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">The sign</div>
    <p>It "fixes" the bug, the same error comes back, it tries again, and you're three changes deep with nothing better. The thread has lost the plot.</p>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Stop and reset</div><p>Restore your last good commit (chapter four). You lose the muddled attempts — and the mess with them.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Re-describe, smaller</div><p>Start fresh with a tighter goal and the exact error. A clean slate beats a confused one.</p></div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · stuck report
title: Turn "still broken" into a *fix.*
@@
:::example
lead:
### Give the agent the loop so far.
When a fix didn't take, say so plainly: what you tried, what still happens, and the exact message. That stops it repeating the same dead end.
tags: Tried, Still see, Exact error
---
tag: copy & adapt
[h]I tried[/h]Your last change to {{the save
button}}, but it didn't help.

[h]I still see[/h]The same crash when I
{{save an empty note}}.

[h]Exact error[/h]
[k]sqlite3.IntegrityError: NOT NULL
constraint failed: notes.title[/k]

[h]Let's[/h]Try a [k]different approach[/k] this
time, and explain the plan first.
:::

===

@@
type: default
eyebrow: 04 · The safety net
title: The undo that *always* works.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">Because you commit working versions as you go (chapter four), no session can truly break things. Returning to the last good commit throws away everything since — including whatever tangled it up.</p>
  <div class="prompt-block good">
<span class="tag">when in doubt, ask plainly</span>
<span class="h">Reset me</span>
Take the project [k]back to my last
working commit[/k] and throw away
the changes since then.

<span class="c"># Then re-describe the goal
# from a clean starting point.</span>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">You never have to "fix forward" out of a mess. You can always step back to solid ground.</p>
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: How snags turn into *spirals.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Hiding the error</div><p>Saying "it broke" instead of pasting the message throws away the one clue that names the cause.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Piling on changes</div><p>Asking for five fixes at once. When something improves, you can't tell which change did it.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Never committing</div><p>No save points means no safety net — and nowhere clean to retreat to when it tangles.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Pushing on tired</div><p>An hour deep and frustrated is when mistakes compound. Reset, step away, come back clear.</p></div>
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
Most snags are ordinary — read the error and paste it exactly before doing anything else.
Recognise the common shapes: not installed, not running, port in use, module missing.
If the agent loops, stop: restore your last good commit and re-describe with a tighter goal.
Frequent commits mean you can always retreat to solid ground — you never have to fix forward.
lede: Calm beats clever when things break.
:::
