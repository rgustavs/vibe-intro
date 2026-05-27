@@
type: title
eyebrow: A working introduction · appendix B
title: Plain-English|*Glossary.*
@@
The words that come up while you build —|defined the way you'd explain them to a friend.

===

@@
type: default
eyebrow: 01 · How to read this
title: Just enough to *follow along.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">These are working definitions, not dictionary ones. The goal is for the words to stop feeling like a wall when the agent uses them — not to make you an expert.</p>
    <p class="body subtext">If a term here isn't enough, the best move is the one from appendix A: ask the agent to <em>explain it in plain English</em>, in the context of your own project.</p>
  </div>
  <div class="card">
    <div class="label">Grouped by</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Working with your code</li>
      <li>Running things on your machine</li>
      <li>The parts of a web app</li>
      <li>Shipping &amp; the AI itself</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Working with your code
title: Saving and *tracking* changes.
@@
:::anatomy
- Repository | The folder holding your whole project and its history | Often shortened to "repo".
- Commit | A saved checkpoint you can return to | Like a labelled save point in a game.
- Branch | A parallel copy where you try things safely | Mess it up and the main version is untouched.
- Merge | Folding a branch's changes back into the main one | How a finished experiment rejoins the project.
lede: All four come from chapter four — this is the quick reminder.
:::

===

@@
type: default
eyebrow: 03 · Running things
title: Making it *go* on your machine.
@@
:::anatomy
- Dependency | Code your app borrows from others | You install these so you don't rebuild everything.
- Environment | The set-up your app needs to run | Right versions, right tools, all in place.
- Server | A program that waits and responds to requests | Your app's "back room" while it runs.
- Localhost / port | Your own machine, at a numbered door | "localhost:5173" is a server running on your laptop.
lede: When something "won't start", it's almost always one of these — see appendix C.
:::

===

@@
type: default
eyebrow: 04 · The parts of a web app
title: Front, back, and the *link* between.
@@
:::anatomy
- Frontend | What you see and click — the screen | Built with React in our stack.
- Backend | The logic behind the screen | Built with FastAPI — it does the real work.
- API | The agreed way the two talk to each other | "When I click save, send the note to the backend."
- Endpoint | One specific door on the backend | Like "/notes" for everything about notes.
- Database | Where information is kept between visits | SQLite in our stack — a single file of data.
lede: The whole stack from chapter five, in five lines.
:::

===

@@
type: default
eyebrow: 05 · Shipping & the AI
title: Going live, and the *agent.*
@@
:::anatomy
- Deploy | Putting your app online for others to use | Moving it from your laptop to the internet.
- Hosting | The service that keeps it running online | Someone else's computer, always on.
- Agent | The AI that reads, writes, and runs code for you | Your pair — you describe, it builds.
- Prompt | The instruction you give the agent | The whole subject of appendix A.
- Token | The small chunks models read and write in | Roughly a word-piece — see the next slide.
- Context window | The most tokens a model can hold at once | Its short-term memory; fill it and it forgets.
lede: Deploy and hosting are chapter eight; the agent is chapter one.
:::

===

@@
type: default
eyebrow: 06 · Tokens & the context window
title: Why a chat can *run out.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">A model measures everything it reads and writes in <em>tokens</em> — roughly word-pieces (about four characters each). Every model has a <em>context window</em>: the most tokens it can hold at one time. That window has to fit your prompts, the agent's replies, <strong>and</strong> any code it's looking at.</p>
    <p class="body subtext">As a chat grows, the window fills up. When it's full, the oldest parts drop out of view and the model starts to "forget" what you said early on. That's what people mean by running out of tokens — you've run past the window, not out of money.</p>
  </div>
  <div class="stack-sm">
    <div class="card">
      <div class="label">Signs you're running out</div>
      <ul class="dotlist" style="margin-top: 8px;">
        <li>It contradicts a decision you made earlier</li>
        <li>It re-asks something you already answered</li>
        <li>It repeats a mistake you'd corrected</li>
      </ul>
    </div>
    <div class="card">
      <div class="label">What to do</div>
      <ul class="dotlist" style="margin-top: 8px;">
        <li>Start a fresh chat for each new task</li>
        <li>One job per chat — keep it focused (appendix A)</li>
        <li>Give a short recap when you start over</li>
        <li class="muted">Lean on commits, not the chat, to hold progress (chapter four)</li>
      </ul>
    </div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A long chat also costs more and replies slow down. A short, fresh chat is usually sharper — and cheaper.</p>
:::

===

@@
type: default
eyebrow: 07 · A note on jargon
title: You don't have to *memorise* this.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Recognise, don't recite</div>
    <p>You only need enough to follow a sentence and ask a good follow-up. Understanding deepens by building, not by studying lists.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">The agent is your dictionary</div>
    <p>Any time a word blocks you: "explain <em>{{the word}}</em> like I'm new to this, using my project as the example." It will.</p>
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
A repo holds your project; commits are save points; branches are safe places to try things.
Frontend is the screen, backend is the logic, and the API is how they talk.
A model's context window is finite — when a chat fills it up, start fresh with a short recap.
You don't need to memorise jargon — recognise it, and ask the agent to explain the rest.
lede: The words stop being a wall once you've met them once.
:::
