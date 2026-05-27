@@
type: title
eyebrow: A working introduction · chapter nine
title: Measuring Value &|*Feedback.*
@@
Shipping is the start of learning, not the end —|here's how to find out if what you built actually helps.

===

@@
type: default
eyebrow: 01 · Why this matters
title: A live link is the *start.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">A live link isn't the finish line — it's the first time you can find out whether the thing you built actually helps anyone. Until real people use it, every belief about its value is a guess.</p>
    <p class="body subtext">Measuring closes the loop. It turns "I think this is useful" into "here's who used it, what they did, and what they told me" — which is exactly what tells you where to point the agent next.</p>
  </div>
  <div class="card">
    <div class="label">Shipped, not finished</div>
    <div class="title">Guessing</div>
    <p>No data, no feedback — you build what you assume people want.</p>
    <div class="label" style="margin-top: 20px;">Measuring</div>
    <div class="title">Knowing</div>
    <p>Usage and honest feedback show you what to improve next.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: Value has *two* halves.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">Measuring value asks one question: <em>is this actually helping the people it's for?</em> The answer comes from two sources — what people <em>do</em> with it (behaviour you can count) and what people <em>say</em> about it (feedback you collect).</p>
  <div class="prompt-block good">
<span class="tag">two halves of value</span>
<span class="h">What they do</span>
Did anyone use it? Did they
complete the one core action?

<span class="h">What they say</span>
Was it useful? What got in the
way? What's missing?
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Behaviour tells you <em>whether</em> it works. Feedback tells you <em>why</em>.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Four things worth *knowing.*
@@
:::anatomy
- Usage | Is anyone using it at all? | Visits, returns, sign-ins — the basic pulse.
- Core action | The one thing that means value | "A note saved", "a report made", "a booking taken".
- Feedback | What people tell you | A short form, a chat, or watching them use it.
- Outcome | The real-world goal it serves | Time saved, fewer emails, a job done quicker.
lede: Start with the core action. If people aren't doing the one thing that matters, nothing else does.
:::

===

@@
type: default
eyebrow: 04 · The learning loop
title: Ship, measure, listen, *improve.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">This is the describe-run-review-refine loop, zoomed out to the whole product. Once it's live, the "review" step is no longer just you — it's the people using it.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Ship</span><span class="d">Get a small version in front of real people.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Measure</span><span class="d">Count the core action; watch what happens.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Listen</span><span class="d">Ask a few users what helped and what didn't.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Improve</span><span class="d">Turn what you learned into the next prompt.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A shipped app you never measure is a guess you never checked.</p>
:::

===

@@
type: default
eyebrow: Principle 1
title: Measure the *one* thing that matters.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">Pick one signal of value</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Choose the single action that means someone got value</li>
      <li>Count that, before anything else</li>
      <li>Watch it over time, not just on launch day</li>
      <li class="muted">Page views and sign-ups feel good but rarely mean value</li>
    </ul>
  </div>
  <p class="lede">"Vanity" numbers go up and to the right and tell you nothing. One honest signal beats ten flattering ones.</p>
</div>
:::

===

@@
type: default
eyebrow: Principle 2
title: Watch real people, don't just *ask.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Watch, don't just ask</div>
    <p>Sit with a handful of people while they use it. Where they hesitate or get stuck tells you more than any survey — people are polite, but behaviour is honest.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">Ask open questions</div>
    <p>"What were you trying to do?" and "What got in the way?" beat "Do you like it?" — which only ever earns a kind yes.</p>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: Let the agent *add* the measuring.
@@
:::example
lead:
### You don't need a separate tool to start.
Ask the agent to record the core action and add a simple way for people to send a comment — both saved to the app you already have.
The smallest measuring is better than none.
tags: Core action, Feedback box, Keep it simple
---
tag: copy & adapt
[h]Goal[/h]Help me see if the {{notes app}}
is useful.

[h]Measure[/h]Count each time a note is
{{saved}} — that's our core action.

[h]Feedback[/h]Add a small "[k]Send feedback[/k]"
box that saves a comment to the
backend.

[h]Done when[/h]I can see the count and read
the comments.
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: Turn feedback into a *change.*
@@
:::example
lead:
### Feedback is only valuable once you act on it.
A single comment isn't a to-do — read across several, find the pattern, then describe the change clearly. That closes the loop back to the agent.
tags: Pattern, One change, Verify
---
tag: agent panel
[h]The pattern[/h]Three people said they couldn't
find their old notes.

[h]The change[/h]Add a search box that filters
the list by title as I type.

[h]Leave alone[/h]Don't change how notes are
saved — only finding them.

[h]Then[/h]I'll ask those three to try it
and tell me if it's [k]better[/k].
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: Where measuring *misleads.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Chasing vanity metrics</div><p>Watching page views climb while no one does the core action. Measure value, not applause.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Leading questions</div><p>"You like it, right?" only collects polite yeses. Ask what got in the way instead.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Collecting, never acting</div><p>Feedback you never turn into a change is just noise. Read for the pattern, then refine.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Hoovering up personal data</div><p>Only collect what you'll actually use, and keep it safe — appendix D. More data is more risk, not more insight.</p></div>
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
Shipping is the start of learning, not the end — a live link lets you finally measure value.
Value has two halves: what people do (the core action) and what they say (feedback).
Pick one honest signal and watch it; ignore vanity metrics that only flatter.
Watch real users, ask open questions, and turn the pattern you hear into the next prompt.
lede: Build, ship, learn — then build again.
:::
