@@
type: title
eyebrow: A working introduction · appendix H
title: Vibe Coding|*Exercises.*
@@
Six projects to build end to end —|each one a real brief, with the business conditions spelled out.

===

@@
type: default
eyebrow: 01 · How to use these
title: Pick one and *build it.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">Each of the next six slides is a self-contained project — one per page. Read the brief, then run the same <code>describe → run → review → refine</code> loop from chapter one until it works.</p>
    <p class="body subtext">Use our usual setup: <strong>VS Code + Antigravity</strong>, and the <strong>React / FastAPI / SQLite</strong> stack. Start with the smallest version that runs, then add one condition at a time.</p>
  </div>
  <div class="card">
    <div class="label">For each project</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Scaffold the smallest version that runs</li>
      <li>Feed in the business conditions one at a time</li>
      <li>Check each against the "done when" before moving on</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · What makes a good brief
title: Good *business conditions.*
@@
:::anatomy
- Who & how many | The real scale you're planning for | "A division: 5 teams of 20 — 100 people."
- The rules | Constraints the answer must respect | "Never drop below 60% cover in any week."
- The inputs | What the user types or uploads | "Preferred weeks, headcount, a fill rate."
- Done when | The result that proves it works | "A coverage calendar with no red weeks."
lede: A vague brief gets a vague app. Pin down the numbers and the rules before you prompt — that is the real work.
:::

===

@@
type: example
eyebrow: Project · 01 · Planning
title: Summer *vacation planner.*
@@
:::example
lead:
### Plan summer leave for a division — 5 teams of 20.
Build a tool that allocates summer holidays across 100 people without leaving any team short-staffed. Business conditions: each team stays at least 60% staffed in every week from June to August; everyone submits three preferred weeks and gets at least two consecutive weeks off; public holidays count automatically; managers see a coverage heatmap per team, per week.
tags: 5 teams × 20, ≥60% cover, 3 preferred weeks
**Done when:** a week-by-week calendar shows green / amber / red cover per team and flags every clash.
---
tag: copy & adapt
[h]Goal[/h]Build a {{summer leave planner}} for a
division of {{5 teams of 20 people}}.

[h]Conditions[/h]Keep each team [k]≥60% staffed[/k]
every week, Jun–Aug. Everyone gets {{3 preferred
weeks}} and at least {{2 in a row}}.

[h]Done when[/h]A [k]coverage heatmap[/k] per team
per week flags any [k]under-staffed[/k] week.
:::

===

@@
type: example
eyebrow: Project · 02 · Estimating
title: AI tools *cost estimator.*
@@
:::example
lead:
### Estimate the cost of rolling AI tools out across Cambio.
Build an estimator that scales cost by organisation size. Business conditions: inputs are headcount, adoption rate, seats by tier and a model mix (Opus / Sonnet / Haiku); cost is seats × licence plus usage (tokens × per-model price); compare three scenarios — cautious, planned, full roll-out; show cost per employee and how the total moves as adoption rises.
tags: scales by headcount, 3 scenarios, model mix
**Done when:** enter headcount and an adoption %, see monthly and annual cost with a per-scenario breakdown.
---
tag: copy & adapt
[h]Goal[/h]Build an {{AI tools cost estimator}}
that scales by {{Cambio's headcount}}.

[h]Inputs[/h]{{Headcount}}, {{adoption %}}, seats per
tier, and a {{model mix}} (Opus/Sonnet/Haiku).

[h]Compare[/h]Three scenarios — [k]cautious,
planned, full[/k]. Show [k]cost per employee[/k]
and the [k]annual total[/k].
:::

===

@@
type: example
eyebrow: Project · 03 · Simulating
title: Meeting *availability simulator.*
@@
:::example
lead:
### How likely is it that everyone is free at once?
Build a Monte Carlo simulator that estimates the chance of finding a shared free slot, given how full people's calendars are. Business conditions: inputs are the number of attendees, working hours per day, slot length and a schedule fill rate (0–100%); generate thousands of random calendars at that fill rate and count how often a common free slot exists; show how the probability collapses as the group or the fill rate grows.
tags: Monte Carlo, fill rate 0–100%, 3–12 people
**Done when:** enter attendees and a fill rate, get a probability plus a curve as fill rate rises.
---
tag: copy & adapt
[h]Goal[/h]Build a {{meeting availability simulator}}
using a [k]Monte Carlo[/k] method.

[h]Inputs[/h]{{Attendees}} (3–12), {{slot length}},
working hours, and a {{schedule fill rate}} (0–100%).

[h]Method[/h]Run [k]thousands of trials[/k]; report the
[k]probability[/k] of a shared free slot and a curve.
:::

===

@@
type: example
eyebrow: Project · 04 · Detecting
title: KPI *anomaly detector.*
@@
:::example
lead:
### Spot when an operations metric drifts out of its normal range.
Build a detector for operations teams that flags unusual days in a KPI feed. Business conditions: the input is a CSV of daily values per metric (ticket volume, response time, uptime); compute a rolling baseline — mean ± a configurable number of standard deviations over a trailing window; flag any point outside it; group results by team and metric; weekends and known holidays shouldn't trigger false alarms.
tags: rolling baseline, per team/metric, configurable
**Done when:** upload a CSV of daily KPIs and anomalies are highlighted on a chart with a list.
---
tag: copy & adapt
[h]Goal[/h]Build a {{KPI anomaly detector}} for an
{{operations team}} from a daily CSV.

[h]Method[/h]Flag points outside a [k]rolling mean ±
N×stdev[/k] over a {{trailing window}}.

[h]Done when[/h]Anomalies show on a [k]chart[/k],
grouped by {{team and metric}}, weekends excluded.
:::

===

@@
type: example
eyebrow: Project · 05 · Documenting
title: Incident *postmortem generator.*
@@
:::example
lead:
### Turn a messy incident timeline into a clean, blameless postmortem.
Build a tool that drafts a structured postmortem from a timeline. Business conditions: inputs are an incident title, severity, impact and a list of timestamped events; output a blameless template — summary, impact, timeline, root cause and action items with owners; severity decides which sections are required; the result exports to Markdown.
tags: blameless template, severity-driven, exports MD
**Done when:** paste a timeline and get a filled-in postmortem you can export to Markdown.
---
tag: copy & adapt
[h]Goal[/h]Build an {{incident postmortem
generator}} from a {{timestamped timeline}}.

[h]Output[/h]A [k]blameless[/k] doc: summary, impact,
timeline, {{root cause}}, action items with [k]owners[/k].

[h]Done when[/h]{{Severity}} sets the required
sections and it [k]exports to Markdown[/k].
:::

===

@@
type: example
eyebrow: Project · 06 · Checking
title: License *usage validator.*
@@
:::example
lead:
### Check what you pay for against what you actually use.
Build a tool that validates software licence usage against entitlements. Business conditions: inputs are entitlements (product, seats purchased, expiry date) and actual usage (active users per product); flag over-allocation where usage exceeds seats, unused seats going to waste, and licences expiring within 30 / 60 / 90 days; show the cost of the waste, per product.
tags: seats vs usage, expiry windows, cost of waste
**Done when:** upload entitlements and usage, see over- and under-allocation with expiry warnings.
---
tag: copy & adapt
[h]Goal[/h]Build a {{licence usage validator}}:
{{entitlements}} vs {{actual usage}}.

[h]Flag[/h][k]Over-allocation[/k] (usage > seats),
[k]unused seats[/k], and {{expiries in 30/60/90 days}}.

[h]Done when[/h]A per-product view shows the
[k]cost of waste[/k] and every [k]expiry warning[/k].
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *carry over.*
@@
:::takeaways
A sharp brief beats a clever prompt — pin down the scale, the rules, and the "done when" first.
Build the smallest version that runs, then add one business condition at a time.
Real numbers (100 people, a fill rate, an adoption %) make the agent build the right thing.
Run and check each condition before the next — the same describe → run → review → refine loop.
lede: Six projects, one habit: describe the real conditions, and let the agent do the building.
:::
