@@
type: title
eyebrow: A working introduction · chapter eight
title: Trust &|*Evaluation.*
@@
An agent acts on its own.|So the question isn't just "was the answer good?" — it's "was that the right way to get there?"

===

@@
type: default
eyebrow: 01 · Where we are
title: From *what it is* to *can I trust it.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Chapter one showed what an agent is: a model in a loop, using tools to act toward a goal. Now that you've seen it build real things, the closing question is oversight.</p>
    <p class="body subtext">An agent takes actions with real consequences. Evaluating it isn't like grading a chatbot's reply — you have to judge the <em>sequence of actions</em> it chose, not just the final output.</p>
  </div>
  <div class="card">
    <div class="label">The shift in your job</div>
    <div class="title">From output to trajectory</div>
    <p>For a chatbot, the test is the answer. For an agent, the test is the path it took to get there.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · The surface
title: The tools *are* the product.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">If the prompt was the spec, the agent's <em>toolset</em> is now the surface area. It's the most reviewable part of the system — and the part with real-world consequences. If you can't list the tools, you can't review the agent.</p>
  <div class="prompt-block good">
<span class="c"># Vague (unreviewable):</span>
"Agent can access our API,
database, and email."

<span class="c"># Scoped (reviewable):</span>
<span class="k">search_orders</span>(from, to) &rarr; read-only,
   returns top 50
<span class="k">draft_reply</span>() &rarr; drafts only,
   never sends
  </div>
</div>
:::

===

@@
type: default
eyebrow: Principle 1
title: Bound the *autonomy.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Autonomy is a slider, not a switch. Before you let an agent run, decide how far it can go on its own — and answer these questions explicitly.</p>
    <p class="body subtext">Start low. Earn each notch with real evidence the agent behaved.</p>
  </div>
  <div class="card">
    <div class="label">Decide before you ship</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Maximum steps before it stops?</li>
      <li>Maximum budget before it pauses?</li>
      <li>Which actions need a human OK?</li>
      <li>Which actions are irreversible?</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Principle 2
title: If you can't *see* it, you can't trust it.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Every tool call, every argument, every result should be recorded. That record — the <em>trace</em> — is how your team debugs, how a customer complaint gets answered, and how you catch a silent failure.</p>
    <p class="body subtext">Build the flight recorder before the cleverness. You'll need it on day one, not month three.</p>
  </div>
  <div class="card">
    <div class="label">A usable trace shows</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Which tool was called</li>
      <li>With what arguments</li>
      <li>What it returned</li>
      <li class="muted">At every step of the loop</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 03 · New failure modes
title: Agents fail in *new ways.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Loops</div><p>Same tool, same arguments, three times over. Cap retries and detect repetition.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Wrong arguments</div><p>Hallucinated IDs, fabricated dates, made-up emails. Validate inputs before the tool runs.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Runaway cost</div><p>500 API calls before anyone notices. Set a step budget, a token budget, a hard alarm.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Silent success</div><p>It reports "done" but nothing changed. Verify side effects — don't trust the summary.</p></div>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 04 · The core idea
title: Evaluate the *trajectory.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Two agents can reach the same answer — one by luck, one by judgment. The only way to tell them apart is to look at the path.</p>
  </div>
  <div class="card">
    <div class="label">Ask of every run</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Did it pick the right tool?</li>
      <li>Were the arguments sensible?</li>
      <li>Did it stop at the right moment?</li>
      <li>Did it ask for help when it should?</li>
    </ul>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">For a chatbot, the test is the output. For an agent, the test is the path.</p>
:::

===

@@
type: default
eyebrow: 05 · Pitfalls
title: Where agents *quietly go wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">"Give it everything"</div><p>Massive, fuzzy toolsets fail. A few sharp tools beat many vague ones.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">No human in the loop</div><p>A day-one agent emailing real customers. Stage it: review, then assist, then act.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Chatbot-shaped evals</div><p>"Was the answer good?" is the wrong question. Ask: "Was that a defensible sequence of actions?"</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">No fallback path</div><p>When the agent fails, what does the user see? Decide that before you ship.</p></div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 01
title: A triage agent that *drafts, never sends.*
@@
:::example
lead:
### Bounded autonomy in practice.
This agent pulls messages, clusters them, and prepares replies — but the irreversible step, sending, always waits for a human.
Notice the explicit stop conditions and the draft-not-send default. That's what earns trust.
tags: Bounded, Escalation, Draft-not-send
---
tag: agent policy
[h]Goal[/h]Triage today's support inbox.

[h]Tools[/h][k]fetch_messages[/k]() → read-only
[k]classify[/k](msg) → tag + urgency
[k]draft_reply[/k]() → [ok]draft only[/ok]

[h]Policy[/h]- Cluster similar issues.
- Draft a reply for each cluster.
- [k]Never send[/k] without human review.
- Flag anything tagged "urgent".

[h]Stop when[/h]Inbox triaged, or 40 tool calls,
whichever comes first.
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
An agent is a model in a loop with tools — review it as a system, not a chat.
Tools are the product surface. Bound them, scope them, list them.
Inspect every step. Stage the autonomy. Earn each notch with evidence.
Evaluate the trajectory, not just the final answer.
lede: Calm autonomy. Inspectable judgment.
:::
