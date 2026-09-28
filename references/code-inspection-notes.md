# Code Inspection Notes from Open-Source Visualization Systems

These notes are based on source-code inspection, not only README summaries. They capture transferable architecture ideas; do not copy internal implementations blindly.

## D3 Brush — `d3/d3-brush/src/brush.js`

Observed patterns:
- brush behavior is parameterized by dimensional mode (X, Y, XY);
- interaction state is explicit and attached to the bound element (`__brush`);
- the behavior dispatches semantic lifecycle events (`start`, `brush`, `end`);
- the brush extent, filters, touch behavior, handles, and cursor semantics are configurable;
- the brush returns a selection that can be translated back through scales by the application.

Transferable lesson:
**Make selection a first-class state with a semantic lifecycle.** Do not bury brush logic inside one chart's mouse handlers. This makes linked-view coordination and undo/history easier.

## Vega-Lite Selection Compiler — `vega/vega-lite/src/compile/selection/assemble.ts`

Observed patterns:
- selections are compiled into explicit signals and selection data stores;
- selection resolution supports global/union/intersection-like semantics across multi-view contexts;
- selection state can modify stores, drive scales, filters, and conditional encodings;
- view composition and selection compilation are separate concerns.

Transferable lesson:
**Represent interaction semantically, then compile/render it.** A research workspace benefits from a small analytical state model (selection, filter, focus, parameter) that multiple views consume.

## Mosaic Coordinator — `uwdata/mosaic/packages/mosaic/core/src/Coordinator.ts`

Observed patterns:
- a central Coordinator manages clients and selection/filter groups;
- data queries are submitted through a QueryManager;
- caching, consolidation, prefetching, and pre-aggregation are centralized;
- client views request data rather than directly owning database communication;
- selection changes are coordinated at architecture level.

Transferable lesson:
**For large linked-view systems, centralize query and coordination.** Do not let every Panel independently fetch, aggregate, and filter the same dataset.

## Crossfilter — `crossfilter/crossfilter/src/index.js`

Observed patterns:
- dimensions expose filter/filterRange/filterFunction/filterAll operations;
- filter state is tracked compactly with bit arrays;
- listeners propagate incremental data/filter changes;
- groups update from shared dimensions instead of recomputing every view from raw data;
- dimensions have stable IDs and can be disposed/reused.

Transferable lesson:
**Incremental shared filtering beats per-chart recomputation for dense coordinated dashboards/workspaces.** Model dimensions and filters explicitly.

## deck.gl Layer Core — `visgl/deck.gl/modules/core/src/lib/layer.ts`

Observed patterns:
- rendering is layer-oriented with declarative props;
- data loading/transform, event/picking behavior, coordinate systems, transitions, and rendering state are separated;
- `updateTriggers` supports controlled change detection;
- picking/highlighting are first-class layer concerns;
- layers share context but keep their own lifecycle/state.

Transferable lesson:
**At large scale, use a lifecycle-aware rendering abstraction.** Separate data/accessors/state/picking/rendering instead of rebuilding GPU scenes on every interaction.

## Cross-project synthesis

A research visual analytics architecture should usually separate:

1. **Data source / storage**
2. **Transformation & analysis**
3. **Shared analytical state**
4. **Query/coordination layer** (when data is large or many views link)
5. **View models**
6. **Renderers** (SVG / Canvas / WebGL / chart library)
7. **Interaction semantics**
8. **History/provenance**

This separation is more reusable than copying the exact framework architecture of any one project.
