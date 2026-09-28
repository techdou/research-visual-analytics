# Technology Decision Guide

Use this after the analytical design is clear.

## D3 + SVG
Choose when:
- marks are in the hundreds to low tens of thousands;
- custom layout/interaction is central;
- vector export/publication quality matters;
- DOM inspectability/accessibility is useful.

## D3 + Canvas
Choose when:
- custom 2D rendering is needed;
- mark count is too high for DOM/SVG;
- interaction can be implemented with spatial indexing/picking.

## Vega-Lite / Vega
Choose when:
- the view is expressible as grammar-of-graphics encodings;
- reproducible specs matter;
- layered, faceted, repeated, or linked selections are central;
- rapid iteration beats bespoke rendering.

## Observable Plot
Choose when:
- concise exploratory/statistical graphics are sufficient;
- layered marks and transformations cover the need;
- custom interaction is not the primary innovation.

## ECharts
Choose when:
- conventional charts and standard interactions dominate;
- development speed matters;
- the system can wrap charts in shared analytical state.

Do not choose ECharts solely because an example visually resembles the desired result.

## Canvas/WebGL/deck.gl
Choose when:
- very large point/line/polygon sets;
- geospatial/scientific rendering;
- GPU filtering/picking/layers are useful;
- SVG would become a performance bottleneck.

## Crossfilter / Mosaic / DuckDB
Choose when:
- many linked views operate on a large table;
- filters/aggregations change interactively;
- query/state coordination is more important than a specific rendering library.

## Three.js
Choose when:
- true 3D geometry, volume, spatial simulation, or physically meaningful 3D interaction is required.

Avoid using 3D as a stylistic substitute for a 2D analytical chart.

## Hybrid architecture
It is often appropriate to mix:
- Vega-Lite/ECharts for standard views;
- D3/SVG for a custom relation panel;
- Canvas/WebGL for dense points;
- one shared state/query layer across all views.

The interface should feel coherent even when renderers differ.
