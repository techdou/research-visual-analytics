# Open-Source Visualization Code Patterns

## Contents
- D3 — https://github.com/d3/d3
- Vega / Vega-Lite — https://github.com/vega/vega and https://github.com/vega/vega-lite
- Observable Plot — https://github.com/observablehq/plot
- Mosaic — https://github.com/uwdata/mosaic
- Crossfilter — https://github.com/crossfilter/crossfilter
- deck.gl — https://github.com/visgl/deck.gl
- ECharts and other high-level chart libraries
- Architecture pattern for research workspaces
- Source-code inspection


The goal is not to imitate library aesthetics. Study architectural ideas that make analytical interfaces composable, linked, reproducible, and scalable.

## D3 — https://github.com/d3/d3

Why study it:
- low-level, web-standard-based approach;
- scales, shapes, selections, brushes, zoom, hierarchy, force layouts;
- works directly with SVG/Canvas/HTML;
- suitable for custom marks and layouts.

Patterns to borrow:
1. Separate scales from marks.
2. Use data joins/stable identity for updateable graphics.
3. Represent brush selection explicitly and invert screen coordinates through scales when needed.
4. Compose small modules rather than building one monolithic renderer.

When to use:
custom scientific/analytical views, bespoke interaction, publication-quality SVG.

## Vega / Vega-Lite — https://github.com/vega/vega and https://github.com/vega/vega-lite

Why study them:
- declarative visualization grammar;
- layered and multi-view composition;
- interaction as declarative selections/parameters;
- specifications are inspectable and reproducible.

Patterns to borrow:
1. Keep data transformations, encodings, and view composition explicit.
2. Treat selections as semantic state that can drive conditional encodings and filters.
3. Use layered/faceted/repeated views instead of duplicating imperative code.
4. Make the visualization specification serializable when reproducibility matters.

When to use:
standard statistical/analytical graphics, reproducible research specs, fast linked-view prototypes.

## Observable Plot — https://github.com/observablehq/plot

Why study it:
- concise layered grammar for exploratory tabular visualization;
- sensible statistical transformations and marks;
- good examples of minimal code expressing analytical intent.

Patterns to borrow:
1. Prefer declarative marks/channels over manual pixel calculations for conventional plots.
2. Layer annotations and reference marks as part of the analytical graphic.
3. Keep examples deterministic and snapshot-testable.

## Mosaic — https://github.com/uwdata/mosaic

Research basis: Heer & Moritz, IEEE TVCG 2024, DOI 10.1109/TVCG.2023.3327189.

Why study it:
- decouples interactive views from scalable data processing;
- clients publish declarative queries;
- central coordinator manages selections and cross-filtering;
- DuckDB-backed computation can support millions/billions of records.

Patterns to borrow:
1. Separate visual state from data-query execution.
2. Centralize selection/filter coordination across clients.
3. Push aggregation/filtering toward the data layer for large datasets.
4. Treat interoperability across views as an architectural concern.

## Crossfilter — https://github.com/crossfilter/crossfilter

Why study it:
- fast multidimensional filtering and grouping;
- incremental updates support coordinated views.

Patterns to borrow:
1. Recompute only what changed when filters move.
2. Keep dimensions/filter state explicit.
3. Multiple charts should read from one coordinated filter model.

Note: the project seeks maintainers; study the pattern, not necessarily the dependency choice for new production systems.

## deck.gl — https://github.com/visgl/deck.gl

Why study it:
- GPU-oriented rendering of large datasets;
- data mapped into composable layers;
- interaction includes picking, highlighting, filtering;
- supports multiple views/projections.

Patterns to borrow:
1. Separate data objects from layer accessors that map values to visuals.
2. Use layered rendering for complex spatial scenes.
3. Move to GPU/tiling/level-of-detail when mark count exceeds SVG/DOM practicality.
4. Keep rendering and view/camera configuration distinct.

## ECharts and other high-level chart libraries

Use them when the analytical task is well served by conventional charts and delivery speed matters.

Do not let the option list of a chart library determine the research design. Wrap library charts behind shared analytical state so they coordinate with custom D3/SVG/Canvas views.

## Architecture pattern for research workspaces

A robust implementation often looks like:

```text
Raw Data
  ↓
Typed / Validated Data
  ↓
Transform & Analysis Layer
  ↓
Shared Analytical State
  ├─ filters
  ├─ selection IDs
  ├─ parameters
  ├─ comparison groups
  └─ history
  ↓
Derived View Models
  ↓
Panel Renderers
  ├─ declarative charts
  ├─ D3/SVG custom view
  ├─ Canvas/WebGL view
  └─ detail table
```

Do not make views mutate raw data directly. User operations update analytical state or explicit annotations; derived data then updates dependent views.

## Source-code inspection

For concrete architecture observations from D3 Brush, Vega-Lite selection compilation, Mosaic Coordinator, Crossfilter dimensions/filters, and deck.gl Layer lifecycle, read `references/code-inspection-notes.md`.
