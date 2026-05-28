@@
type: title
eyebrow: A working introduction · chapter six
title: Functional Modelling|*for builders.*
@@
AI builds exactly what you ask for.|How to write complete, consistent requirements so it builds the right thing.

===

@@
type: default
eyebrow: 01 · Why this matters
title: AI amplifies *vague requirements.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">In the past, if you wrote a vague request, a human engineer would wander over and ask, "What happens if the user has no data yet?"</p>
    <p class="body subtext">An AI won't ask. It quietly invents an answer — and if it guesses wrong, untangling it later can take hours. The hard part has shifted from <em>writing the code</em> to <em>describing exactly what you want</em>.</p>
  </div>
  <div class="card">
    <div class="label">A human developer</div>
    <div class="title">Fills in the gaps</div>
    <p>People use common sense and what they know about your team to guess what you meant.</p>
    <div class="label" style="margin-top: 20px;">An AI developer</div>
    <div class="title">Does exactly what you say</div>
    <p>It builds precisely what you describe. If your rules contradict each other, it picks one quietly.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: Breaking "ideas" into *functions.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">Functional analysis is the process of taking a high-level feature ("Export to CSV") and breaking it down into a system of discrete inputs, logic rules, edge cases, and outputs.</p>
  <div class="prompt-block good">
<span class="c"># "Export to CSV" is not a spec.</span>
<span class="c"># This is a functional breakdown:</span>

<span class="k">Input:</span> User clicks [Export], Date Range
<span class="k">State check:</span> Does user have 'Admin' role?
<span class="k">Logic:</span> Fetch data. Map columns.
<span class="k">Edge:</span> If &gt;10k rows -> email link instead.
<span class="k">Edge:</span> If 0 rows -> show toast error.
<span class="k">Output:</span> File download trigger.
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">If you don't define the edges, the AI will guess them.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Four parts of a functional spec.
@@
:::anatomy
- Actor & State | Who is doing this, and what is their current context? | "A free-tier user with zero existing projects."
- Trigger | The exact event that starts the flow. | "Clicks the 'Create New' button."
- Logic / Rules | The business constraints that must be checked. | "Limit is 3 projects. Check DB count."
- Outcome | The resulting state changes and UI updates. | "Project created, route to /editor, show success."
lede: When feeding an AI, structure beats prose. Map the state machine before you ask for the code.
:::

===

@@
type: default
eyebrow: Principle 1
title: *Completeness:* The happy path is only 20%.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">It's natural to describe only the "happy path" — when everything works perfectly. The AI needs you to spell out the unhappy paths too.</p>
    <ul class="dotlist" style="margin-top: 16px;">
      <li>What happens when the database is empty?</li>
      <li>What happens if the API times out?</li>
      <li>What happens if they input text instead of a number?</li>
    </ul>
  </div>
  <div class="card">
    <div class="label">The Completeness Checklist</div>
    <div class="title">The 4 States</div>
    <p>1. <strong>Blank state</strong> (First time user)</p>
    <p>2. <strong>Loading state</strong> (Waiting for network)</p>
    <p>3. <strong>Error state</strong> (Something broke)</p>
    <p>4. <strong>Ideal state</strong> (The happy path)</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Principle 2
title: *Consistency:* Resolving contradictions.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">Contradictory rules</div>
    <div class="title">Easy to miss</div>
    <p>Rule A: "Users can delete their own comments."</p>
    <p>Rule B: "Once a thread is locked, no changes can be made."</p>
    <p style="margin-top: 10px; color: #b07a52;">The AI will quietly pick one. You need to say which wins: <em>"A locked thread overrides the right to delete."</em></p>
  </div>
  <div class="stack">
    <p class="body">AI reads top to bottom. If conflicting rules are scattered across a long document, the AI can write buggy code without flagging it.</p>
    <p class="body subtext">Working through the behaviour first forces you to reconcile overlapping rules before the agent writes a single line of code.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 04 · Pitfalls
title: Where requirements *break* the AI.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card">
      <div class="title" style="font-size: 19px;">"Make it like Stripe"</div>
      <p>Assuming the AI shares your mental model of a third-party app. Be literal. Describe the exact behaviour, not the analogy.</p>
    </div>
    <div class="card">
      <div class="title" style="font-size: 19px;">Implicit Variables</div>
      <p>"Send a notification." To whom? In app or email? With what copy? Define the exact payload.</p>
    </div>
  </div>
  <div class="stack-sm">
    <div class="card">
      <div class="title" style="font-size: 19px;">Mixing "what" and "how"</div>
      <p>Telling the AI exactly how to build it in code, instead of describing the behaviour you want. Describe the behaviour; let the AI write the syntax.</p>
    </div>
    <div class="card">
      <div class="title" style="font-size: 19px;">The "etc." trap</div>
      <p>"Show fields for name, email, etc." The AI will invent random fields to fill in the "etc." List everything you actually want.</p>
    </div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 06
title: The *Vague* vs. The *Functional*.
@@
:::example
lead:
### Breaking down a feature request.
If you feed the "Vague" request to an AI coder, it will generate a generic UI, forget validation, and hallucinate a database schema.
The "Functional" version gives the agent explicit boundaries, ensuring the generated code matches the business logic.
tags: Deconstruction, Logic, Boundaries
---
kind: bad
tag: Vague Idea
"We need a promo code feature
on the checkout page. If they
enter 'SUMMER', take 10% off."

[c]AI guesses: Does it stack?
Is it case sensitive? When does
it expire? What if it's invalid?[/c]
:::

===

@@
type: example
eyebrow: Worked example · 02 of 06
title: The *Functional* version.
@@
:::example
lead:
### This is what you feed the AI.
By defining the exact inputs, validation rules, state changes, and unhappy paths, you leave no room for the AI to invent incorrect behaviour.
---
tag: Functional Spec
[h]Feature: Apply Promo Code[/h]
[k]Input:[/k] Text field, max 20 chars.
[k]Trigger:[/k] Click "Apply" or press Enter.

[h]Validation Logic:[/h]
1. Strip whitespace, uppercase input.
2. Check DB: Is code active?
3. Check DB: Is expiration > today?
4. Rule: Only ONE code per order.
   (Replace existing if applied again).

[h]Outcomes (Success):[/h]
- Calculate 10% off `cart_total`.
- Update `discount_amount` state.
- Show green text: "Code applied!"

[h]Outcomes (Negative):[/h]
- If invalid/expired: Show red text
  "Invalid code". Do not change total.
:::

===

@@
type: example
eyebrow: Worked example · 03 of 06
title: Formatting for AI: *Given / When / Then*.
@@
:::example
lead:
### The language of logic.
Behaviour-Driven Development (BDD) formatting is a quiet superpower when prompting AI — these models have seen a great deal of it.
It forces you to declare the initial state (Given), the trigger (When), and the exact expected result (Then).
tags: BDD, Gherkin, State mapping
---
tag: BDD Spec
[h]Scenario: Downgrading a subscription[/h]

[k]GIVEN[/k] the user is on the 'Pro' plan
  [k]AND[/k] their current billing cycle
      ends on day X
  [k]AND[/k] they have 5 active projects

[k]WHEN[/k] they click "Downgrade to Free"

[k]THEN[/k] schedule plan change for day X
  [k]AND[/k] show banner "Plan ends on X"
  [k]AND[/k] do NOT lock projects immediately
  [k]AND[/k] send webhook to billing system

[c]# The AI translates this directly into[/c]
[c]# if/else statements and API calls.[/c]
:::

===

@@
type: example
eyebrow: Worked example · 04 of 06
title: Mapping the *State Transitions*.
@@
:::example
lead:
### Preventing impossible actions.
If an invoice is "Paid", a user shouldn't be able to click "Edit". If you don't explicitly list allowed transitions, the AI might leave the Edit button active.
Provide a simple transition map in your prompt.
tags: State Machine, Enums, Transitions
---
tag: State Map Prompt
[h]Entity: Invoice[/h]
Status enum: [Draft, Sent, Paid, Void]

[h]Allowed Transitions:[/h]
- Draft -> Sent
- Draft -> Void
- Sent -> Paid
- Sent -> Void

[h]Rules for UI generation:[/h]
If status == Paid:
  - Disable 'Edit' and 'Send' buttons.
  - Show 'Download Receipt' button.

[c]# Giving this to an AI ensures the React[/c]
[c]# component maps exactly to reality.[/c]
:::

===

@@
type: default
eyebrow: 04 · Tools for analysis
title: Using *Agent Skills* for analysis.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Writing a complete spec from scratch is hard. You'll naturally miss edge cases and contradictory rules.</p>
    <p class="body subtext">An <em>Agent Skill</em> is a saved instruction you summon by name — think of it as handing the agent a specific job. Two of them help you <em>discover</em> and <em>stress-test</em> your requirements before you ever ask an agent to write code.</p>
  </div>
  <div class="card">
    <div class="label">Step 1: Discover</div>
    <div class="title">The Brainstorm skill</div>
    <p>Use it to open things up — let the AI surface edge cases, odd states, and unhappy paths you haven't considered.</p>
    <p class="subtext" style="margin-top: 6px;">Source: <a href="https://sickn33.github.io/antigravity-awesome-skills/skill/brainstorming">sickn33.github.io · brainstorming</a></p>
    <div class="label" style="margin-top: 20px;">Step 2: Validate</div>
    <div class="title">The Grill Me skill</div>
    <p>Use it to tighten things up — let the AI pick at your written logic and point out the contradictions.</p>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 05 of 06
title: Using the *Brainstorm* skill.
@@
:::example
lead:
### Finding the missing states.
When you have a rough idea, trigger the [Brainstorm skill](https://sickn33.github.io/antigravity-awesome-skills/skill/brainstorming). Because it's designed to be a divergent facilitator, it won't just say "great idea."
It will actively help you map out the negative paths you need for your functional spec.
tags: Discovery, Edge Cases, Brainstorm Skill
---
tag: workflow
[h]You:[/h]
"@brainstorm-partner I want to build
a 'transfer project ownership' feature.
Help me map the edge cases."

[h]Brainstorm Agent:[/h]
"Let's look at the edges:
1. What if the recipient doesn't have
   a paid account?
2. What if the recipient rejects the
   transfer? Where does the project go?
3. What happens to the original owner's
   billing during the pending state?

Which of these 3 paths should we map
out first?"
:::

===

@@
type: example
eyebrow: Worked example · 06 of 06
title: Using the *Grill Me* skill.
@@
:::example
lead:
### Stress-testing the logic.
Once you've written your functional spec (your Given/When/Thens), do not immediately hand it to a coding agent.
Feed it to the "Grill Me" skill first. It acts as an adversarial QA engineer, reading your logic strictly to find contradictions.
tags: Validation, QA Review, Grill Me Skill
---
tag: workflow
[h]You:[/h]
"@grill-me-stakeholder Review this
checkout spec for logical holes."

[h]Grill Me Agent:[/h]
"This spec is broken in two places:
1. You stated 'Promo codes apply to
the total', but later said 'Shipping
is calculated post-discount.' If shipping
is free over $50, does the promo code
drop them below the free shipping tier?

2. Your State Machine allows 'Draft -> Paid'.
You bypassed the 'Sent' state entirely.
How can a user pay an invoice they
haven't received?"
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
AI amplifies vagueness — the hard part is now describing exactly what you want.
Use BDD (Given/When/Then) to lay out the logic clearly for the agent.
Use the *Brainstorm* skill to discover the unhappy paths and edge cases.
Use the *Grill Me* skill to check your logic for holes before generating code.
lede: Clear thinking. Calm execution.
:::
