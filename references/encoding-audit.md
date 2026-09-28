# Encoding correctness audit

Audit intended judgments, not chart names. Ask a user to decode one mark and compare two values against the data.

| Check | Failure signal | Repair |
|---|---|---|
| Expressiveness | Order/metric geometry implies a relation absent from data | Use nominal channels or explain nonmetric layout |
| Effectiveness | Exact comparison depends on hue/area/occluded depth | Add aligned position/length or numeric evidence |
| Scale | Unannounced normalization or changing axes reverses impression | Fix scale or disclose transformation and context |
| Layout | Sorting/force rearrangement looks like data change | Preserve order/anchors or label layout-only change |
| Aggregation | One mark silently represents unequal support | Show count/support, distribution or weighted definition |
| Missingness | Missing represented as zero or omitted without indication | Explicit missing state and denominator |
| Projection/lens | Screen distance treated as physical/causal distance | Show distortion/uncertainty and link original attributes |
| Cross-view color | Same color changes meaning between panels | Shared semantic mapping and distinct selection cue |
| Interaction | Important evidence only in hover/drag/color | Keyboard/tap/explicit selection and non-color alternative |
| Export | Screenshot requires prior interaction to decode | Annotate state, legend and comparison reference |

Use invariance checks when relevant: reorder records with unchanged IDs; add duplicate memberships; test ties, negative values, outliers and nulls; change viewport without changing selection semantics. Synthetic examples test the renderer, not a scientific conclusion.

For a custom glyph or family, request mapping, worked decode, comparison validity and failure envelope. Require a simpler baseline and identify the additional evidence or workflow benefit. Reject misleading candidates regardless of aesthetic novelty.
