@@
type: title
eyebrow: A working introduction · chapter six
title: Shipping|*It.*
@@
Getting your app off your laptop and onto the internet —|so anyone can open it with a link.

===

@@
type: default
eyebrow: 01 · Why this matters
title: "Works on my *machine*" isn't shared.
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Everything so far has run on your own computer. That's perfect for building — but nobody else can see it, and it stops the moment you close the laptop.</p>
    <p class="body subtext">Shipping means putting your app somewhere online, so it has a web address you can send to anyone. The agent can do most of the setup for you.</p>
  </div>
  <div class="card">
    <div class="label">On your laptop</div>
    <div class="title">Only you can see it</div>
    <p>It runs while your terminal is open, and stops when you close it.</p>
    <div class="label" style="margin-top: 20px;">Shipped</div>
    <div class="title">Anyone with the link</div>
    <p>It lives online, stays up, and you share a single address.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: Shipping is just *hosting* your app.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">To <em>host</em> an app is to put it on a computer that is always on, connected to the internet, with a public address. A <em>hosting service</em> rents you that computer and handles the hard parts.</p>
  <div class="prompt-block good">
<span class="tag">the idea</span>
<span class="c"># Your app, online, at an address</span>
<span class="c"># like:</span>
<span class="k">https://</span>cambio-notes.example.app

<span class="c"># Same app you built — now anyone</span>
<span class="c"># can open it in a browser.</span>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">You describe what to put online; the hosting service and the agent handle the wiring.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Four parts of *going live.*
@@
:::anatomy
- Host | Where the app runs online | A service that keeps a computer on for you, so the app stays up.
- Build | The packaged version | The agent bundles your code into the form the host runs.
- Secrets | Keys kept off the page | Passwords and API keys live on the host, never in the browser — see chapter 05.
- Address | The link you share | A web address anyone can open. You can use a custom name later.
lede: A hosting service usually handles the build and the address for you. You bring the code and the secrets.
:::

===

@@
type: default
eyebrow: 04 · The shipping loop
title: Push, deploy, check, *share.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">Shipping is its own small loop, and it reuses habits you already have. Most hosting services can rebuild your app automatically every time you push to GitHub.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Push</span><span class="d">Send your latest commit to GitHub — chapter 03.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Deploy</span><span class="d">The host builds and publishes it.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Check the live link</span><span class="d">Open the address and try it, as a stranger would.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Share</span><span class="d">Send the link. Gather feedback. Repeat.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Ship small and early — a rough live version beats a perfect local one.</p>
:::

===

@@
type: default
eyebrow: Principle 1
title: Let the agent *set it up.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">What to ask for</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Pick a simple, free host to start</li>
      <li>Have the agent write the deploy steps</li>
      <li>Ask for the exact commands to run</li>
      <li class="muted">Have it explain anything you don't recognise</li>
    </ul>
  </div>
  <p class="lede">You don't need to learn servers. Describe where you want it live, let the agent produce the steps — then run them and read the result.</p>
</div>
:::

===

@@
type: default
eyebrow: Principle 2
title: Always check the *live* version.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Live is not the same as local</div>
    <p>Things that worked on your laptop can break online — a missing secret, a wrong address, a file that never got pushed.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">Open it like a stranger</div>
    <p>Visit the real link in a fresh browser tab. Click through the main path. If it's broken, tell the agent exactly what you saw.</p>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: Ask the agent to *ship it.*
@@
:::example
lead:
### Describe the destination, not the plumbing.
You don't need to know how hosting works. Tell the agent what you built and that you want it online, and ask it to walk you through it step by step.
You're getting a plan you can follow, not a finished mystery.
tags: Deploy, Steps, Clarity
---
tag: agent panel
[h]Goal[/h]Put my notes app online so I can
send a colleague a link.

[h]Constraints[/h]- Use a free hosting service that's
  simple for a beginner.
- Keep my API keys off the public page.

[h]Finish by[/h]Giving me the exact steps and
commands, and the link to check
once it's live.
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: Check it, then *report back.*
@@
:::example
lead:
### The first deploy is rarely the last.
Open the live link and try the main thing your app does. If something is off, the fix is the same loop as always: say what you did, what you expected, and what you saw.
Then push again and let it redeploy.
tags: Verify, Feedback, Iterate
---
tag: what to check
[h]Open the live link[/h]- Does the page load for a stranger?
- Does the main action work end to end?
- Did anything work locally but not here?

[h]If it's broken[/h][k]You:[/k] On the live site, saving a note
does nothing, but it works locally.
The page shows a "failed to fetch" error.

[c]# Specific beats "it's broken" — every time.[/c]
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: Where shipping *trips* people.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Forgetting to push first</div><p>The host deploys what's on GitHub, not what's on your laptop. Commit and push before you deploy.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Secrets on the page</div><p>Keys pasted into the frontend are visible to anyone. They belong on the host, kept hidden — chapter 05.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Only testing locally</div><p>"It works on my machine" isn't shipped. Always open the real link and try it.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Waiting for perfect</div><p>Ship a small, rough version early. A live link you can share teaches you more than another day of polish.</p></div>
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
Shipping means hosting your app online, behind a link anyone can open.
Let the agent set it up: describe the destination, run the steps it gives you.
Push to GitHub first — the host deploys what's there. Then check the live link.
Keep secrets on the host, never on the page. Ship small, ship early.
lede: Off your laptop. Into the world.
:::
