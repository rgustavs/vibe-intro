@@
type: title
eyebrow: A working introduction · appendix I
title: Designing with|*Google Stitch.*
@@
Before the agent writes a line of code, you can hand it a picture of what "good" looks like.|Stitch turns a sentence into a designed screen — and a designed screen is a far clearer brief than a sentence alone.

===

@@
type: default
eyebrow: 01 · Why this matters
title: A *picture* is a better brief.
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Describing behaviour in words is the core skill (chapter two). But for anything you can <em>see</em> — a screen, a layout, a flow — a design is worth a thousand prompts. It pins down spacing, hierarchy and tone in a way prose struggles to.</p>
    <p class="body subtext">Google Stitch lets a non-designer produce that picture in minutes. You then carry it into your vibe coding project as the visual target the agent builds towards.</p>
  </div>
  <div class="card">
    <div class="label">Without a design</div>
    <div class="title">"Make it look nice"</div>
    <p>The agent guesses. You get something generic and spend the afternoon nudging it.</p>
    <div class="label" style="margin-top: 20px;">With a design</div>
    <div class="title">"Build this screen"</div>
    <p>The agent has a concrete target — layout, colours, type — and gets close on the first try.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: What Stitch *actually is.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">In one line</div>
    <div class="title">A prompt-to-UI design tool</div>
    <p>An experimental tool from Google Labs, powered by Gemini. You describe a screen — or paste a screenshot — in plain language, and it generates a designed interface for web or mobile, which you refine by chatting.</p>
  </div>
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">What it is not</div>
    <div class="title">Not your finished app</div>
    <p>It produces <em>designs</em> and rough front-end markup — a starting point, not production code wired to your data. Think of it as a fast way to draw, not a replacement for building (chapter five).</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A sketchpad with a brain — it draws the screen so you can react to something real.</p>
:::

===

@@
type: default
eyebrow: 03 · Anatomy
title: The Stitch *workspace.*
@@
:::anatomy
- Prompt box | Where you describe the screen in plain language, or paste a reference image | Your intent, the same skill as chapter two.
- middle: Canvas | The live preview of the generated design, for web or mobile | What you react to and refine.
- middle: Theme controls | Palette, fonts, corner roundness, light or dark | Where corporate branding gets dialled in.
- middle: Variants | Several takes on the same screen, side by side | Pick a direction without re-prompting from scratch.
- bottom: Export | Copy the front-end code, or send the design to Figma | The bridge into your vibe coding project.
lede: Five parts: describe, see, brand, choose, export.
:::

===

@@
type: default
eyebrow: 04 · How to use it
title: Describe, generate, *refine.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">It's the same loop you already know — <strong>describe → run → review → refine</strong> — applied to a design instead of code. You stay in the chat, reacting to a picture, until the screen looks right.</p>
    <p class="body subtext">Start broad ("a dashboard for a rota tool"), then refine in small steps ("move the filters to a left sidebar", "make the primary button green"). Small, specific asks beat one giant prompt.</p>
  </div>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Describe</span><span class="d">One screen, plain language. Add a reference image if you have one.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Generate</span><span class="d">Stitch draws it — often a few variants to choose from.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Review</span><span class="d">Does the layout, hierarchy and tone fit? Pick the closest variant.</span></div></div>
    <div class="loop-step"><span class="n">4</span><div><span class="t">Refine</span><span class="d">Adjust in small steps until it's right, then export.</span></div></div>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 05 · Corporate branding
title: Make it follow the *house style.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Put the brand into words</div><p>Name the exact colours (hex), the typeface, the tone (calm, professional), and how rounded or square things should feel. Stitch can only match what you spell out.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Use the theme controls</div><p>Don't fight the prompt — set the palette and fonts directly in the theme panel so every screen stays consistent.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Show a reference</div><p>Paste a screenshot of an existing branded page or your design system. Matching a picture beats describing one.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Keep a brand brief</div><p>Write the palette, type and tone once, save it, and paste it at the top of every prompt so nothing drifts between screens.</p></div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 02
title: A reusable *brand brief.*
@@
:::example
lead:
### Spell the brand out once.
A vague "make it on-brand" gives Stitch nothing to match. Hand it the actual tokens — colours, type, tone, shape — and save the block to reuse on every screen.
This keeps a whole set of designs consistent, the way a real design system would.
tags: Branding, Consistency, Reuse
---
tag: paste at the top of every prompt
[h]Brand brief — Cambio[/h]
[c]# Reuse this on every screen[/c]

Palette:
  [arg]primary[/arg]   [k]#6F7F6A[/k] (green)
  [arg]accent[/arg]    [k]#8FA9B8[/k] (blue)
  [arg]neutral[/arg]   [k]#C9BAA6[/k] (tan)

Type:    [k]Inter[/k], generous spacing
Tone:    calm, professional, uncluttered
Shape:   softly rounded corners, light theme

[ok]Every screen now matches the house style.[/ok]
:::

===

@@
type: default
eyebrow: 06 · From design to code
title: Two ways *out.*
@@
:::html
<div class="grid-2 reveal">
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">Copy the code</div>
    <div class="title">Front-end markup</div>
    <p>Stitch can hand you the generated HTML/CSS for the screen. Useful as a <em>reference</em> the agent can read — not something to paste into your app wholesale.</p>
  </div>
  <div class="card" style="border-top: 3px solid #6F7F6A;">
    <div class="label">Send to Figma</div>
    <div class="title">An editable design</div>
    <p>Push the design into Figma to tidy it up, share it with the team, or hand it to whoever owns the brand before it becomes code.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Either way, what leaves Stitch is a <em>target</em>, not the final build.</p>
:::

===

@@
type: example
eyebrow: Worked example · 02 of 02
title: Into *Antigravity.*
@@
:::example
lead:
### Rebuild it on your own stack.
Don't paste Stitch's raw export into your app. Instead, give the agent the design as a visual target and ask it to recreate the screen properly — in React, wired to your FastAPI and SQLite back end (chapter five).
Then it's the usual loop: describe → run → review → refine (chapter seven).
tags: Antigravity, React, Handoff
---
kind: good
tag: prompt to the Antigravity agent
[h]The job:[/h]
"Here is a Stitch design for the rota
dashboard ([k]screenshot + markup attached[/k]).

Rebuild this screen as a [k]React[/k] component
in our project, matching the layout and
the brand colours. Use our existing
components where they fit, and wire the
data to the [k]/api/rota[/k] endpoint."

[h]Why this way:[/h]
- The design is the target; the agent owns the code.
- It fits your stack, not Stitch's throwaway markup.
- Every file lives in Git (chapter four).

[ok]A branded screen, built to keep.[/ok]
:::

===

@@
type: default
eyebrow: 07 · Pitfalls
title: Where it goes *wrong.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Shipping the export</div><p>Pasting Stitch's raw markup straight into your app. It doesn't know your components, data or stack — treat it as a reference, then rebuild (chapter five).</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Branding by vibes</div><p>"Make it on-brand" with no hex codes or fonts. Spell the brand out; better still, paste a reference and use the theme controls.</p></div>
  </div>
  <div class="stack-sm">
    <div class="card"><div class="title" style="font-size: 19px;">Designing the whole app at once</div><p>Asking for ten screens in one prompt. Do one screen at a time, refine it, then move on — same as small, specific asks everywhere else.</p></div>
    <div class="card"><div class="title" style="font-size: 19px;">Forgetting accessibility</div><p>A pretty palette can fail on contrast. Check that text is readable and tap targets are large enough before you build.</p></div>
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
Stitch turns a sentence into a designed screen — a far clearer brief for the agent than words alone.
It's the same loop you know: describe → generate → review → refine, applied to a design.
Make it follow the brand by spelling out colours, type and tone, using the theme controls, and pasting a reference.
Carry the design — not the raw export — into Antigravity, and rebuild it properly on your own stack.
lede: Design fast in Stitch; build it to keep in your own project.
:::
