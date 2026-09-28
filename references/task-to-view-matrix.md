# Task-to-View Matrix

Use this as a starting point, not a lookup table that overrides domain reasoning.

| Analytical task | Useful starting views | Important interactions | Common failure |
|---|---|---|---|
| Compare magnitudes | aligned bars, dot plot, slope graph, table | sort, highlight, group | decorative area/pie makes close comparison hard |
| Explore correlation | scatter, hexbin/density, SPLOM | brush, filter, regression toggle | overplotting hidden |
| Inspect multivariate profiles | parallel coordinates, heatmap, glyph/small multiples | reorder axes, brush, normalize | too many channels/axes without task focus |
| Find clusters | scatter/projection, density, similarity matrix | select, adjust parameters, compare solutions | treating embedding distance as ground truth |
| Inspect pairwise relations | matrix, adjacency matrix, graph | sort/reorder, pair selection, filter | node-link hairball for dense relations |
| Follow temporal change | line, horizon, small multiples, event timeline | zoom, brush, align, compare intervals | dual axes and inconsistent scales |
| Compare experimental conditions | aligned small multiples, interval plots, distribution plots | linked highlight, facet, baseline toggle | only showing averages |
| Inspect uncertainty | interval/band, distribution, ensemble/small multiples | threshold, confidence level, sample drilldown | collapsing probability into deterministic label |
| Inspect spatial structure | map, spatial density, linked attribute view | pan/zoom, spatial brush, region filter | geography dominates non-spatial question |
| Trace individual evidence | table/sample view + linked main view | search, select, details-on-demand | aggregate cannot be traced to source records |
| Compare models | aligned metrics, residual/error views, calibration, confusion matrix | model switch, pair compare, slice filter | leaderboard-only KPI design |
| Understand hierarchy | tree, treemap, icicle, sunburst, indented list | drill, collapse, focus+context | area encoding used for precise comparisons |
| Understand flow | Sankey/alluvial, state transition matrix, path view | filter source/target, trace path | visual crossings overwhelm flow structure |
| Explore text/topics | document list, embedding/map, term/topic matrix | search, semantic filter, linked documents | projection shown without original text evidence |
| Review iterative analysis | history timeline, snapshots, parameter traces | undo/redo, compare, bookmark | only current state remains visible |

## Panel role heuristic

A Panel should generally have one dominant role:

- **Orientation:** what data/state am I looking at?
- **Detection:** where is the pattern/anomaly?
- **Explanation:** what attributes/relations explain it?
- **Comparison:** how does it differ from another state/group?
- **Control:** what analytical parameter/query can I change?
- **Evidence:** which records support the pattern?
- **History:** how did the analysis arrive here?

A single view may support multiple tasks, but avoid giving every panel every role.
