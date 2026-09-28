# Evaluation Rubric for Research Visual Analytics

## Contents
- 1. Problem/task fit
- 2. Data abstraction & semantics
- 3. Visual encoding
- 4. Panel architecture
- 5. Multi-view coordination
- 6. Interaction quality
- 7. Comparison support
- 8. Evidence traceability
- 9. Uncertainty / limitations
- 10. Provenance / reproducibility
- 11. Visual restraint & readability
- 12. Performance & scalability
- 13. Accessibility
- 14. Scientific integrity
- Review format
- Critical gates precede scores


Score each dimension 0–3. Do not reduce the result to a single “beauty score”; use the rubric to locate design weaknesses.

## 1. Problem/task fit
- 0: no clear research question
- 1: generic dashboard goals
- 2: tasks mostly mapped to views
- 3: each key view/interaction has explicit task justification

## 2. Data abstraction & semantics
- 0: units/types/relations unclear
- 1: basic fields shown
- 2: transformations and data types documented
- 3: hierarchy/time/space/uncertainty/provenance explicitly modeled where relevant

## 3. Visual encoding
- 0: misleading or decorative
- 1: readable but weakly justified
- 2: appropriate encoding with consistent semantics
- 3: encoding clearly optimizes the intended analytical judgment

## 4. Panel architecture
- 0: unrelated card grid
- 1: weak grouping
- 2: clear roles and focal hierarchy
- 3: panel roles form a coherent analytical workflow

## 5. Multi-view coordination
- 0: views independent when they should link
- 1: superficial highlighting only
- 2: useful selection/filter coordination
- 3: shared state supports complementary evidence and complex analysis

## 6. Interaction quality
- 0: interaction cosmetic or confusing
- 1: basic zoom/hover/filter
- 2: task-oriented operations with clear feedback
- 3: fluent, reversible interaction exposes cause/effect and supports reasoning

## 7. Comparison support
- 0: user must remember prior state
- 1: limited side-by-side comparison
- 2: aligned scales/state comparison
- 3: comparison is a first-class workflow with differences made perceptually clear

## 8. Evidence traceability
- 0: aggregate patterns cannot be checked
- 1: limited details
- 2: drill-down to supporting records/attributes
- 3: clear path from pattern → explanation → source evidence

## 9. Uncertainty / limitations
- 0: uncertain outputs shown as certain
- 1: caveat in text only
- 2: important uncertainty visible
- 3: uncertainty is integrated into analysis and interaction

## 10. Provenance / reproducibility
- 0: analysis state is opaque
- 1: current state visible
- 2: key parameters/history recorded
- 3: important states can be compared/restored/reproduced

## 11. Visual restraint & readability
- 0: decoration competes with data
- 1: generic dashboard aesthetic
- 2: restrained, readable research UI
- 3: visual hierarchy strongly reinforces analytical hierarchy

## 12. Performance & scalability
- 0: unusable at target scale
- 1: works only on tiny examples
- 2: suitable for expected scale
- 3: architecture anticipates large data with aggregation/Canvas/WebGL/query coordination where needed

## 13. Accessibility
- 0: inaccessible color/controls
- 1: partial keyboard/contrast support
- 2: core tasks work without hover-only dependence and with sufficient contrast
- 3: semantic controls, focus behavior, labels, and non-color cues are consistently implemented

## 14. Scientific integrity
- 0: fabricated/misleading claims
- 1: unclear transformations/metrics
- 2: computations and units traceable
- 3: claims, transformations, provenance, and data limitations are explicit and reproducible

## Review format

When reviewing, return:

1. **Critical analytical issues**
2. **Major structural/interaction issues**
3. **Minor visual polish issues**
4. **What already works**
5. **Revised task-to-view plan**
6. **Highest-leverage next changes**

## Critical gates precede scores

A critical encoding, identity, statistical, version-consistency or evidence-integrity failure blocks a validated verdict regardless of other scores. Unknown needs a named test. Describe observed behavior separately from intended behavior. Do not penalize a sufficient conventional view for lacking novelty or simple interaction for lacking complexity.
