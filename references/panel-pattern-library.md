# Research Visual Analytics Panel Pattern Library

## Contents
- Pattern A — Overview + Evidence
- Pattern B — Overview + Relation + Detail
- Pattern C — Compare + Small Multiples
- Pattern D — Parameter Space + Result Space
- Pattern E — Spatial + Attribute
- Pattern F — Model Output + Error Analysis
- Pattern G — History / Provenance Workspace
- Pattern H — Progressive Research Panel
- Pattern I — Publication Figure Panel


These are reusable compositions, not fixed templates.

## Pattern A — Overview + Evidence

Use when analysts discover patterns in aggregate data but must verify individual records.

Structure:
- Overview / main pattern view
- Detail / sample table
- optional distribution or metadata view

Coordination:
selection in overview → evidence rows and attributes update.

Avoid when raw records have little analytical value.

## Pattern B — Overview + Relation + Detail

Use for networks, interactions, model relationships, rule relations, or entity ecosystems.

Structure:
- Main overview
- Relation view (matrix/graph/custom layout)
- details-on-demand

Coordination:
select relation pair → highlight shared objects → inspect details.

## Pattern C — Compare + Small Multiples

Use for experimental conditions, models, cohorts, parameter settings, time slices.

Structure:
- shared control/filter panel
- aligned repeated views
- difference or summary view

Rules:
- keep axes/scales comparable unless independence is explicitly justified;
- show baseline/normalization clearly.

## Pattern D — Parameter Space + Result Space

Use for simulations, model tuning, scientific parameter exploration.

Structure:
- parameter/condition view
- main result view
- response/metric view
- optional history

Coordination:
parameter change → recompute/preview → update result and metrics.

Prefer direct manipulation when it reduces mental mapping.

## Pattern E — Spatial + Attribute

Use when location matters but non-spatial attributes explain the pattern.

Structure:
- map/spatial view
- attribute/distribution view
- detail view

Coordination:
spatial brush ↔ attribute filters.

Do not let the map become decorative when geography is not an analytical variable.

## Pattern F — Model Output + Error Analysis

Use for ML/AI experiments and model evaluation.

Structure:
- global performance/behavior
- slice/group comparison
- error/residual/uncertainty view
- raw cases

Avoid leaderboard-only design.

## Pattern G — History / Provenance Workspace

Use for iterative analytical workflows.

Structure:
- current analysis state
- compact history/timeline/snapshots
- comparison of selected states

Record only consequential changes; avoid logging every mouse movement unless research requires it.

## Pattern H — Progressive Research Panel

Use when information density would otherwise overwhelm users.

Structure:
- compact overview
- focused analytical panel
- optional expandable details

Interaction:
progressive disclosure, details-on-demand, contextual controls.

## Pattern I — Publication Figure Panel

Use when a system screenshot or composite figure must communicate a workflow in a paper.

Principles:
- each subpanel has one story role;
- labels A/B/C... follow reading order;
- related encodings remain consistent;
- annotation highlights the analytical mechanism, not decorative UI;
- the figure should remain understandable when printed at column/page size.
