@@
type: title
eyebrow: A working introduction · appendix G
title: Lovable|*vs. our approach.*
@@
Two routes to the same idea: describe it, get working software.|One hands you a finished app in the browser; the other hands you the keys.

===

@@
type: default
eyebrow: 01 · Why this matters
title: Same *philosophy*, different vehicle.
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Lovable is vibe coding too — you describe behaviour in plain language and an AI builds it. The difference isn't the idea; it's how much the platform does <em>for</em> you versus how much you keep in your own hands.</p>
    <p class="body subtext">This isn't "one is better". They sit at two ends of a spectrum, and knowing where each shines lets you pick the right tool for the job in front of you.</p>
  </div>
  <div class="card">
    <div class="label">Lovable</div>
    <div class="title">Hands you the app</div>
    <p>Chat in the browser; it builds and hosts a working web app for you.</p>
    <div class="label" style="margin-top: 20px;">Our approach</div>
    <div class="title">Hands you the keys</div>
    <p>An agent in your own editor; you own the code, the stack and where it runs.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: What each one *actually is.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">Lovable</div>
    <div class="title">A hosted app builder</div>
    <p>You describe what you want in a chat box on their website. It generates a full web app on a stack it chooses, shows a live preview, and deploys it — all in the browser, nothing to install.</p>
  </div>
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">Our approach</div>
    <div class="title">An agent in your editor</div>
    <p>VS Code + Antigravity (chapter three). The agent writes code in <em>your</em> project, on your stack (chapter five), tracked in Git (chapter four), deployed where you choose (chapter eight).</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">One is a managed product. The other is your workshop.</p>
:::

===

@@
type: default
eyebrow: 03 · The spectrum
title: From *managed* to *owned.*
@@
:::anatomy
- Managed | The platform picks the stack, hides the plumbing, hosts it | Lovable — fastest start, least to learn.
- middle: In between | Export the code and take it elsewhere when you outgrow it | The bridge most teams cross eventually.
- bottom: Owned | You hold the code, the stack and the hosting | Our approach — most control, most responsibility.
lede: The further right you go, the more power and the more responsibility you take on.
:::

===

@@
type: default
eyebrow: 04 · Head to head
title: The *trade-offs*, side by side.
@@
:::html
<div class="grid-2 reveal">
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">Lovable</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li><strong>Setup:</strong> none — open a browser</li>
      <li><strong>First version:</strong> seconds</li>
      <li><strong>Control:</strong> guided, within the platform</li>
      <li><strong>The code:</strong> on their platform (export possible)</li>
      <li><strong>Deploy:</strong> one click, their hosting</li>
      <li class="muted"><strong>Ceiling:</strong> can hit walls on deep custom logic</li>
    </ul>
  </div>
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">Our approach</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li><strong>Setup:</strong> once (chapter three)</li>
      <li><strong>First version:</strong> minutes</li>
      <li><strong>Control:</strong> total — every file is yours</li>
      <li><strong>The code:</strong> fully yours, in Git</li>
      <li><strong>Deploy:</strong> anywhere you choose (chapter eight)</li>
      <li class="muted"><strong>Ceiling:</strong> as high as you can describe</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 05 · Horses for courses
title: What each is *best* at.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Reach for Lovable when…</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>You want a prototype or demo today</li>
      <li>It's a landing page or simple web app</li>
      <li>You're validating an idea before investing</li>
      <li>Nobody on hand wants to touch an editor</li>
    </ul>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">Reach for our approach when…</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>It's a tool you'll own and govern (chapter ten)</li>
      <li>It needs custom logic or odd integrations</li>
      <li>It must run on your own infrastructure</li>
      <li>You want skills that transfer and no lock-in</li>
    </ul>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: A demo by *lunchtime.*
@@
:::example
lead:
### Speed beats control here.
You need something clickable for a 2pm meeting to test whether an idea lands. Nobody will run it next week if the idea flops.
This is Lovable's sweet spot: from sentence to a live link in minutes, with zero setup.
tags: Prototype, Validation, Speed
---
tag: good fit · Lovable
[h]The job:[/h]
"A sign-up page for a workshop, with
a form and a confirmation screen, live
on a link I can share this afternoon."

[h]Why Lovable:[/h]
- Throwaway-friendly; speed is everything.
- No custom logic, no integrations.
- A live URL with nothing to install.

[ok]Idea tested before the day is out.[/ok]
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: A tool the team will *keep.*
@@
:::example
lead:
### Ownership beats speed here.
The rota tool from chapter ten isn't a demo — a department will lean on it, it touches your own data, and it must be owned and supported for years.
This is our approach's sweet spot: full control, your stack, your hosting, no platform holding the keys.
tags: Owned tool, Control, Longevity
---
kind: good
tag: good fit · our approach
[h]The job:[/h]
"An internal rota tool that reads our
staff list, runs on our server, and
we can hand over and maintain."

[h]Why our approach:[/h]
- Lives in Git; any owner can pick it up.
- Custom logic and a private data source.
- Deploys on infrastructure we control.

[ok]A real asset, not a rented demo.[/ok]
:::

===

@@
type: default
eyebrow: 06 · The hybrid path
title: You can *start* on one, *finish* on the other.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">It's not a one-time choice. A common, sensible path is to prototype fast on Lovable to prove the idea, then — if it earns a place — export the code and bring it into your own editor to own and grow.</p>
    <p class="body subtext">That graduation is exactly chapter ten's story: the moment a useful experiment becomes a tool someone depends on, give it real ownership rather than leaving it on a platform nobody on your team controls.</p>
  </div>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Prototype</span><span class="d">Prove the idea fast on Lovable.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Decide</span><span class="d">Worth keeping? Then it needs an owner.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Export</span><span class="d">Take the code into your own project.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Own it</span><span class="d">Grow and maintain it on your stack.</span></div></div>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 07 · Pitfalls
title: Traps on *either* road.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Mistaking a demo for a product</div><p>A Lovable prototype that quietly becomes load-bearing — with no owner and no plan. Graduate it (chapter ten) or retire it.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Lock-in by drift</div><p>Building so much on one platform that leaving means a rewrite. Export early if you know you'll outgrow it.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Over-engineering a throwaway</div><p>Reaching for the full workshop to test a five-minute idea. If it's disposable, take the fast road.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Tool tribalism</div><p>Insisting one tool fits every job. Match the road to the destination, not to habit.</p></div>
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
Lovable and our approach are both vibe coding — the difference is managed versus owned.
Lovable wins on speed and zero setup; our approach wins on control, ownership and no lock-in.
Prototype fast on Lovable; bring it home to your own stack when it becomes a tool to keep.
Match the road to the destination — a throwaway demo and an owned tool deserve different tools.
lede: Right tool, right job. The philosophy is the same either way.
:::
