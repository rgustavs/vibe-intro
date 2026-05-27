@@
type: title
eyebrow: A working introduction · chapter two
title: Describing|*What You Want.*
@@
The one skill the whole series rests on —|saying what you want clearly enough for an agent to build it.

===

@@
type: default
eyebrow: 01 · Why this matters
title: The skill is *describing*, not coding.
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Chapter one made the case: you describe, the agent builds. This chapter slows down on the describing — because it's the part that decides whether you get what you wanted.</p>
    <p class="body subtext">A clear description does the agent's guessing for it. A vague one leaves the agent to invent the details — and it will, quietly, often wrongly.</p>
  </div>
  <div class="card">
    <div class="label">A vague request</div>
    <div class="title">The agent guesses</div>
    <p>It fills the gaps with whatever seems likely, and you find out later it guessed wrong.</p>
    <div class="label" style="margin-top: 20px;">A clear request</div>
    <div class="title">The agent follows</div>
    <p>You've made the decisions. The agent does the typing, not the deciding.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: Intent, context, *constraints.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">A good description has three parts: the <em>intent</em> (what you want to happen), the <em>context</em> (what the agent should know), and the <em>constraints</em> (the lines it shouldn't cross). Miss one, and the agent fills it in for you.</p>
  <div class="prompt-block good">
<span class="tag">the shape of a request</span>
<span class="h">Intent</span>Let visitors leave a comment on
an article.

<span class="h">Context</span>It's the knowledgebase app.
Comments belong to one article.

<span class="h">Constraints</span>No login. Max 500 characters.
Newest comment first.
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Say the parts out loud, or the agent decides them for you.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: Five parts of a clear *request.*
@@
:::anatomy
- Intent | The outcome you want | "Visitors can search articles by keyword."
- Context | What the agent should know | "It's the knowledgebase from chapter five."
- Constraints | The boundaries to respect | "No new database. Match the existing style."
- Done-when | What success looks like | "Typing 'invoice' shows only matching articles."
- One thing | Keep the request small | One change you can run and check at a time.
lede: You don't need all five every time — but naming them is how vague becomes buildable.
:::

===

@@
type: default
eyebrow: Principle 1
title: *Specific* beats clever.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">The habit that makes it work</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Name the exact thing, not a category ("a Save button", not "some controls")</li>
      <li>Give numbers where they matter (how many, how long, how big)</li>
      <li>Show an example of the input and the output you expect</li>
      <li class="muted">Replace every "etc." with the actual list</li>
    </ul>
  </div>
  <p class="lede">You don't need the right words for it. Plain, specific language beats vague, technical-sounding language every time.</p>
</div>
:::

===

@@
type: default
eyebrow: Principle 2
title: Describe the *behaviour*, not the code.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Say what, not how</div>
    <p>"When the list is empty, show 'No notes yet'." You're describing what the user should see — the agent picks how to build it.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">Leave room for the expert</div>
    <p>Telling the agent which exact code to write throws away its strength. Describe the result and let it choose the tools.</p>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: From *vague* to *buildable.*
@@
:::example
lead:
### The same idea, made specific.
The vague version sounds reasonable but leaves a dozen decisions unmade. The agent has to guess every one of them.
The clear version answers those questions before they're asked — so the agent builds your idea, not its own.
tags: Intent, Specifics, Boundaries
---
kind: bad
tag: too vague
"Add a way for people to
get in touch."

[c]# Get in touch how? Email?
A form? Where does it send?
What if they leave it blank?[/c]
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: The *clear* version.
@@
:::example
lead:
### Intent, context, constraints — and a way to check it.
Notice it never mentions code. It describes what the visitor does, what should happen, and where the edges are.
End with "done-when" so you both know what success looks like.
tags: Clarity, Context, Done-when
---
tag: clear request
[h]Intent[/h]A contact form on the About page.

[h]Context[/h]Same notes app. It should match
the page's existing style.

[h]Constraints[/h]- Fields: name, email, message.
- All three are required.
- On send, show "Thanks, we'll be
  in touch" and clear the form.

[h]Done when[/h]I fill it in, press Send, and see
the thank-you message.
:::

===

@@
type: default
eyebrow: 04 · Pitfalls
title: Where descriptions *go wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Assuming it knows</div><p>"Make it like the other page." The agent can't see what's in your head. Spell out what "like" means.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">The "etc." trap</div><p>"Name, email, etc." The agent invents the rest. List everything you actually want, and nothing you don't.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Only the happy path</div><p>You describe it working perfectly and forget the empty, broken, or blank cases. Say what should happen when things go wrong too.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Asking for too much</div><p>A whole app in one paragraph. Describe one small piece, run it, then describe the next — chapter one's loop.</p></div>
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
A clear description is intent, context, and constraints — name all three.
Be specific: exact things, real numbers, examples, no "etc."
Describe the behaviour you want; let the agent choose the code.
Say what "done" looks like, so you both know when you're there.
lede: For bigger, logic-heavy features, chapter six goes deeper.
:::
