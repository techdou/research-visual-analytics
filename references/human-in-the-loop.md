# Human intervention with observable consequences

Specify who intervenes, which analytical/model state can change, why the person has useful knowledge, what executes, and what evidence allows revision. Selecting or browsing alone is valid interaction; it is not automatically a model-steering contribution.

## Action record

Question → evidence inspected → human decision → operation → computation/version → result/difference → accept/reject/revise → provenance.

Classify operations explicitly:
- Representation change: sort, lens, projection display, highlight.
- Query on stored results: filter, threshold existing scores, retrieve precomputed condition.
- Annotation/constraint: record a label or constraint; distinguish proposed from applied.
- Simulation: run a defined surrogate/what-if model and disclose assumptions.
- Model execution: invoke actual inference/training with configuration, inputs and version recorded.

For proposed changes show preview versus committed status, affected scope, running/error/stale states, and reversible local state when feasible. Respect the user's existing action authorization; do not invent approval requirements. Separate undoing an interface state from reverting an external training/data mutation.

For a modality-removal example, cached full-modality outputs cannot demonstrate removal performance. Use a recorded matching ablation or an actual supported rerun; otherwise label the test unavailable and keep diagnostic exploration useful.

Evaluate whether intervention helps the specified task against an appropriate no-intervention or familiar-interaction baseline. Preserve failed interventions and contradictory evidence; do not narrate every edit as improvement.
