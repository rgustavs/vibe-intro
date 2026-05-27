@@
type: title
eyebrow: A working introduction · chapter seven
title: Debugging &|*Verifying.*
@@
What to do when it breaks —|and how to be sure it actually works before you move on.

===

@@
type: default
eyebrow: 01 · Why this matters
title: It *will* break. That's normal.
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Earlier chapters warned against saying "it's broken." This is the chapter that teaches the fix: how to report a problem so the agent can solve it, and how to confirm a fix really worked.</p>
    <p class="body subtext">Things breaking isn't failure — it's the normal middle of building. The skill is turning a vague "it's not working" into something the agent can act on.</p>
  </div>
  <div class="card">
    <div class="label">"It's broken"</div>
    <div class="title">The agent guesses</div>
    <p>With nothing to go on, it changes something at random and hopes.</p>
    <div class="label" style="margin-top: 20px;">A clear report</div>
    <div class="title">The agent fixes</div>
    <p>Given the steps, the error, and the gap, it can find the actual cause.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: A good report has *three parts.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">A useful bug report says what you <em>did</em>, what you <em>expected</em>, and what you <em>saw</em> — plus the exact error text, copied not paraphrased. That's enough for the agent to reproduce and reason about the problem.</p>
  <div class="prompt-block good">
<span class="tag">a clear bug report</span>
<span class="h">I did</span>
Clicked "Save" on a new note.

<span class="h">I expected</span>
The note to appear in the list.

<span class="h">I saw</span>
Nothing happened. The console shows:
<span class="k">TypeError: notes.map is not a function</span>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Paste the real error. It's the single most useful thing you can give the agent.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Four parts of a *bug report.*
@@
:::anatomy
- Steps | Exactly what you did | "Open the app, type a title, press Save."
- Expected | What should have happened | "A new row appears at the top of the list."
- Actual | What happened instead | "The page went blank and nothing saved."
- Error text | The message, copied exactly | From the screen, the terminal, or the browser console.
lede: The agent can't see your screen. These four parts are how you hand it your eyes.
:::

===

@@
type: default
eyebrow: 04 · The debugging loop
title: Reproduce, report, fix, *verify.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">Debugging is the same describe-run-review-refine loop, pointed at a problem. The one step beginners skip is the last one: actually confirming the fix worked.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Reproduce</span><span class="d">Make the bug happen again on purpose.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Report</span><span class="d">Did / expected / saw, with the error text.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Fix</span><span class="d">Let the agent change one thing.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Verify</span><span class="d">Run the same steps. Confirm it's gone.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">"It should work now" is not the same as "I checked, and it works."</p>
:::

===

@@
type: default
eyebrow: Principle 1
title: Change *one thing* at a time.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">Why one change</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>If you change five things, you can't tell which one fixed it</li>
      <li>A single change is easy to check and easy to undo</li>
      <li>Commit when it works, so you have a clean point to return to — chapter four</li>
      <li class="muted">Stuck for ages? Restore the last good commit and try again</li>
    </ul>
  </div>
  <p class="lede">Version control is your debugging safety net. A bad fix costs you nothing when you can always go back.</p>
</div>
:::

===

@@
type: default
eyebrow: Principle 2
title: Verify like a *stranger.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Don't trust "should"</div>
    <p>The agent often says a change "should fix it." Believe nothing until you've run the exact steps that failed and watched them pass.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">Check the edges too</div>
    <p>It works with a normal note — but what about an empty one, a very long one, or none at all? Try the cases that broke it before.</p>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: "It's broken" vs. a *real* report.
@@
:::example
lead:
### The difference is what the agent can do next.
The vague message gives the agent nothing — it can only guess and poke. The clear report lets it reproduce the problem and find the actual cause.
The error text alone often points straight at the fix.
tags: Steps, Error text, Specifics
---
kind: bad
tag: useless
"the save thing is broken
again, please fix"

[c]# Broken how? On which page?
What did you see? Was there
an error message?[/c]
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: The *report*, then the *check.*
@@
:::example
lead:
### Report clearly, fix once, then verify.
Give the agent the three parts and the error. When it proposes a fix, don't just accept it — run the exact steps that failed.
The bug is only fixed once you've watched it not happen.
tags: Report, Fix, Verify
---
tag: agent panel
[h]I did[/h]Added a note with an empty title
and pressed Save.

[h]I expected[/h]A message telling me the title
is required.

[h]I saw[/h]The app crashed. Terminal shows:
[k]sqlite3.IntegrityError: NOT NULL
constraint failed: notes.title[/k]

[h]Then I check[/h]Try saving an empty title again —
do I now see the message, not a crash?
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: Where debugging *goes wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">"It's broken"</div><p>The classic. No steps, no error, no detail. The agent can only guess. Always say did / expected / saw.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Not reading the error</div><p>The message often names the problem outright. Read it, paste it — don't scroll past it.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Assuming it's fixed</div><p>Accepting "this should work" without running it. Half the time it doesn't. Always check the steps that failed.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Fixing in the dark</div><p>Changing many things at once. When it works, you won't know why — and you'll break it again. One change, then check.</p></div>
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
Breaking is normal — the skill is reporting it clearly, not avoiding it.
Say what you did, expected, and saw, and paste the exact error.
Change one thing at a time; commit working versions as you go.
A fix isn't done until you've re-run the steps and watched it work.
lede: Calm under errors. Sure of the fix.
:::
