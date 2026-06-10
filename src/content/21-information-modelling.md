@@
type: title
eyebrow: A working introduction · appendix K
title: Information Modelling|*as a story.*
@@
Start with a tiny people-and-skills story.|Then evolve it into relationships, history, levels, and questions the system can answer.

===

@@
type: default
eyebrow: 01 · The story
title: Start with *four simple facts.*
@@
:::html
<div class="grid-2 reveal model-story-intro">
  <div class="stack">
    <p class="body">Information modelling is how we turn a real-world story into a structure a system can store, validate, and ask questions about.</p>
    <p class="body subtext">Our story starts small: workers, teams, skills, and skill areas. We add only one idea at a time so the model evolves visibly.</p>
  </div>
  <div class="model-fact-card">
    <div class="model-fact"><span>Worker</span><strong>Johan</strong><em>belongs to People Success</em></div>
    <div class="model-fact"><span>Worker</span><strong>Martin</strong><em>belongs to People Success</em></div>
    <div class="model-fact"><span>Skill</span><strong>Antigravity</strong><em>belongs to AI Tools</em></div>
    <div class="model-fact"><span>Skill</span><strong>Lovable</strong><em>belongs to AI Tools</em></div>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Objects
title: Name the *things* first.
@@
:::html
<div class="model-step reveal"><span>Step 1</span><strong>Find the objects</strong><em>Worker and Skill become the first reusable concepts.</em></div>
<div class="model-canvas reveal">
  <div class="model-node worker"><span>Worker</span><strong>Johan</strong><small>a person who can hold skills</small></div>
  <div class="model-node worker"><span>Worker</span><strong>Martin</strong><small>a person who can hold skills</small></div>
  <div class="model-node skill"><span>Skill</span><strong>Antigravity</strong><small>a capability people can learn</small></div>
  <div class="model-node skill"><span>Skill</span><strong>Lovable</strong><small>a capability people can learn</small></div>
</div>
<p class="lede reveal" style="margin-top: var(--space-xl);">A model begins by separating nouns from prose: Worker and Skill are the first entity types.</p>
:::

===

@@
type: default
eyebrow: 03 · Classification
title: Add the *containers* around them.
@@
:::html
<div class="model-step reveal"><span>Step 2</span><strong>Add ownership</strong><em>Workers belong to teams; skills belong to areas.</em></div>
<div class="model-canvas model-canvas-groups reveal">
  <div class="model-group team">
    <span class="group-label">Team</span>
    <strong>People Success</strong>
    <div class="model-node worker compact">Johan</div>
    <div class="model-node worker compact">Martin</div>
  </div>
  <div class="model-group area">
    <span class="group-label">Skill Area</span>
    <strong>AI Tools</strong>
    <div class="model-node skill compact">Antigravity</div>
    <div class="model-node skill compact">Lovable</div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Teams classify workers. Areas classify skills. These are two simple one-to-many relationships.</p>
:::

===

@@
type: default
eyebrow: 04 · First diagram
title: Draw the *relationship rules.*
@@
:::html
<div class="model-er reveal">
  <div class="model-entity"><span>Team</span><strong>People Success</strong></div>
  <div class="model-link"><b>has many</b><i>1 → many</i></div>
  <div class="model-entity"><span>Worker</span><strong>Johan, Martin</strong></div>
  <div class="model-entity"><span>Skill Area</span><strong>AI Tools</strong></div>
  <div class="model-link"><b>has many</b><i>1 → many</i></div>
  <div class="model-entity"><span>Skill</span><strong>Antigravity, Lovable</strong></div>
</div>
<div class="grid-2 reveal" style="margin-top: var(--space-lg);">
  <div class="card"><div class="label">Rule</div><div class="title">A worker belongs to one team</div><p>Johan and Martin both point back to People Success.</p></div>
  <div class="card"><div class="label">Rule</div><div class="title">A skill belongs to one area</div><p>Antigravity and Lovable both point back to AI Tools.</p></div>
</div>
:::

===

@@
type: default
eyebrow: 05 · The twist
title: Workers and skills are *many-to-many.*
@@
:::html
<div class="model-step reveal"><span>Step 3</span><strong>Notice the many-to-many</strong><em>The cross-links are where the model starts to carry business meaning.</em></div>
<div class="model-many reveal">
  <div class="model-column">
    <div class="model-node worker">Johan</div>
    <div class="model-node worker">Martin</div>
  </div>
  <div class="model-web">
    <svg viewBox="0 0 380 180" role="img" aria-label="Many-to-many lines between workers and skills">
      <path d="M20 45 C130 15 250 15 360 45" />
      <path d="M20 135 C130 165 250 165 360 135" />
      <path class="ghost" d="M20 45 C130 90 250 90 360 135" />
      <path class="ghost" d="M20 135 C130 90 250 90 360 45" />
    </svg>
    <div class="model-badge">many ↔ many</div>
  </div>
  <div class="model-column">
    <div class="model-node skill">Antigravity</div>
    <div class="model-node skill">Lovable</div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A worker can have many skills. A skill can have many workers. That relationship needs its own place in the model.</p>
:::

===

@@
type: default
eyebrow: 06 · Join object
title: Turn the line into *Skill Assignment.*
@@
:::html
<div class="model-step reveal"><span>Step 4</span><strong>Name the relationship</strong><em>Once a relationship has data of its own, promote it into a box.</em></div>
<div class="model-join reveal">
  <div class="model-node worker"><span>Worker</span><strong>Johan</strong></div>
  <div class="model-arrow">→</div>
  <div class="model-node assignment"><span>Skill Assignment</span><strong>Johan has Antigravity</strong><small>the relationship as data</small></div>
  <div class="model-arrow">→</div>
  <div class="model-node skill"><span>Skill</span><strong>Antigravity</strong></div>
</div>
<div class="model-table reveal">
  <div class="model-table-head"><span>Worker</span><span>Skill</span><span>Meaning</span></div>
  <div><span>Johan</span><span>Antigravity</span><span>Johan has Antigravity skill</span></div>
  <div><span>Martin</span><span>Lovable</span><span>Martin has Lovable skill</span></div>
</div>
:::

===

@@
type: default
eyebrow: 07 · Full picture
title: The model now has *five boxes.*
@@
:::html
<div class="model-schema reveal">
  <div class="model-entity team"><span>Team</span><strong>People Success</strong></div>
  <div class="model-entity worker"><span>Worker</span><strong>Johan<br>Martin</strong></div>
  <div class="model-entity assignment"><span>Skill Assignment</span><strong>who has what</strong></div>
  <div class="model-entity skill"><span>Skill</span><strong>Antigravity<br>Lovable</strong></div>
  <div class="model-entity area"><span>Skill Area</span><strong>AI Tools</strong></div>
  <svg viewBox="0 0 900 260" aria-hidden="true">
    <path d="M165 75 L285 75" /><text x="190" y="58">has workers</text>
    <path d="M445 75 L565 75" /><text x="468" y="58">has skill</text>
    <path d="M735 75 L735 175" /><text x="746" y="130">belongs to</text>
    <path d="M365 142 L365 175 L445 175 L445 142" /><text x="370" y="203">worker has many skills</text>
  </svg>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">The join box is what makes the model explainable: it names the relationship instead of hiding it in a line.</p>
:::

===

@@
type: default
eyebrow: 08 · Advanced topic
title: Add *level* to the relationship.
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Skill level does not belong on Worker, because Johan can be level 2 in Antigravity and level 1 in Lovable.</p>
    <p class="body subtext">It does not belong on Skill either, because Antigravity is not always level 2. The level belongs to the assignment between a worker and a skill.</p>
  </div>
  <div class="model-node assignment large"><span>Skill Assignment</span><strong>Worker + Skill + Level</strong><small>Johan · Antigravity · Level 2</small></div>
</div>
<div class="model-table reveal" style="margin-top: var(--space-lg);">
  <div class="model-table-head"><span>Worker</span><span>Skill</span><span>Level</span></div>
  <div><span>Johan</span><span>Antigravity</span><span>1</span></div>
  <div><span>Martin</span><span>Lovable</span><span>1</span></div>
</div>
:::

===

@@
type: default
eyebrow: 09 · Time enters
title: After *Aug 30*, facts can change.
@@
:::html
<div class="model-step reveal"><span>Step 5</span><strong>Make change explicit</strong><em>After Aug 30 is not a note — it is part of the information.</em></div>
<div class="model-timeline reveal">
  <div class="model-time-card now"><span>Before Aug 30</span><strong>Current known skills</strong><p>Johan has Antigravity level 1.<br>Martin has Lovable level 1.</p></div>
  <div class="model-time-arrow">→</div>
  <div class="model-time-card future"><span>After Aug 30</span><strong>New skill events</strong><p>Johan gets level 2 in Antigravity.<br>Martin gets level 2 in Antigravity.</p></div>
</div>
<div class="model-table model-table-4 reveal" style="margin-top: var(--space-lg);">
  <div class="model-table-head"><span>Date</span><span>Worker</span><span>Skill</span><span>Level</span></div>
  <div><span>before Aug 30</span><span>Johan</span><span>Antigravity</span><span>1</span></div>
  <div><span>after Aug 30</span><span>Johan</span><span>Antigravity</span><span>2</span></div>
  <div><span>after Aug 30</span><span>Martin</span><span>Antigravity</span><span>2</span></div>
</div>
:::

===

@@
type: default
eyebrow: 10 · Design choice
title: Store today, or store the *history?*
@@
:::html
<div class="grid-2 reveal">
  <div class="card" style="border-top: 3px solid #8FA9B8;">
    <div class="label">Snapshot model</div>
    <div class="title">Only current level</div>
    <p>Good when you only need to know the answer today: "Who is level 2 in Antigravity now?"</p>
    <div class="model-mini">Johan · Antigravity · Level 2</div>
  </div>
  <div class="card" style="border-top: 3px solid #C9BAA6;">
    <div class="label">Event model</div>
    <div class="title">Every change over time</div>
    <p>Good when you need auditability: "When did Martin become level 2? What changed after Aug 30?"</p>
    <div class="model-mini">After Aug 30 · Martin · Antigravity · Level 2</div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-xl);">Information modelling is not drawing boxes. It is choosing what questions the business must be able to answer.</p>
:::

===

@@
type: default
eyebrow: 11 · Final model
title: The evolved *information model.*
@@
:::html
<div class="model-final reveal">
  <div class="model-final-row top">
    <div class="model-entity team"><span>Team</span><strong>People Success</strong></div>
    <div class="model-entity area"><span>Skill Area</span><strong>AI Tools</strong></div>
  </div>
  <div class="model-final-row middle">
    <div class="model-entity worker"><span>Worker</span><strong>Johan<br>Martin</strong><small>belongs to Team</small></div>
    <div class="model-entity skill"><span>Skill</span><strong>Antigravity<br>Lovable</strong><small>belongs to Area</small></div>
  </div>
  <div class="model-entity assignment wide"><span>Skill Assignment / Skill Event</span><strong>Worker + Skill + Level + Effective date</strong><small>Johan · Antigravity · Level 2 · after Aug 30</small></div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">The journey: objects → containers → many-to-many relationship → level → time.</p>
:::

===

@@
type: default
eyebrow: 12 · Takeaway
title: A good model makes *questions easy.*
@@
:::takeaways
Which workers belong to People Success?
Which skills belong to AI Tools?
Who has Antigravity skill?
Who reached level 2 after Aug 30?
What changed over time, not just what is true now?
lede: If the model can answer the questions cleanly, the system has the right shape.
:::
