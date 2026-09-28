---
name: research-visual-analytics
description: Design and audit scientific visual-analysis workspaces (科研可视分析/研究Panel), coordinated views, model diagnostics, and evidence-bearing research figures. Use for task-to-view architecture, encoding correctness, multi-view semantics, uncertainty, reproducible interaction and analytical implementation review. Exclude ordinary KPI dashboards, simple one-chart requests, styling-only changes, and architecture diagrams without data analysis.
---

# Research Visual Analytics

Work from Research question → Task → Data abstraction → Encoding → View → Interaction → Evidence → Evaluation. Treat this as an engineering synthesis of visualization research, not a standardized named theory.

## Ownership and scope

Own analytical correctness, task-to-view architecture and evidence verification. Use `visualization-innovation` for unresolved invention; do not restart a fixed design unless correctness requires it. The artifact/domain or implementation skill owns its deliverable. Both skills work independently: audit a custom design even if the companion is unavailable.

Exchange one design record with stable question/view/link/state IDs, source facts, encoding/decoding rules, coordination contract, comparison population, novelty boundary, risks and validation status. Review critical issues first; return specific fixes. Stop the review loop when material issues are resolved or explicitly reported as blockers.

## Select resources by task

| Task | Read | Required result |
|---|---|---|
| Frame / design a workspace | `references/task-to-view-matrix.md`, `references/panel-pattern-library.md` | Question-to-evidence map and panel roles |
| Audit custom visual encodings | `references/encoding-audit.md` | Expressiveness, decoding and comparison checks |
| Design or debug linked views | `references/coordination-contract.md` | Explicit mappings, operators, invariants and state tests |
| Review statistics / uncertainty | `references/statistical-integrity.md` | Population, denominator and uncertainty audit |
| Human intervention / model steering | `references/human-in-the-loop.md` | Action authority, real computation and result provenance |
| Reproducible story / static export | `references/evidence-story.md` | State-linked claims and readable static evidence |
| Implement / refactor | `references/technology-decision-guide.md`, `references/open-source-code-patterns.md` | Shared state, derived views and tested code |
| Evaluate design or skill outputs | `references/evaluation-rubric.md`, `references/behavioral-evaluation.md` | Evidence-backed findings and limits |

## Workflow

1. **Inspect the requested artifact and sources.** Identify design, review, implement, refactor or teaching mode. Preserve the requested deliverable. Do not substitute conceptual advice when runnable code or edits were requested.
2. **Build the problem model.** Establish audience, question, entities, keys, relations, data types/units, transformations, uncertainty and expected scale. Resolve material unknown semantics; proceed with marked assumptions otherwise. Use `references/academic-foundations.md` for theory-backed rationale.
3. **Map tasks to evidence.** For each major view record question, data needed, encoding, operation and evidence produced. Remove redundant views. Choose role, size and placement by analytical importance, complexity and use frequency rather than a fixed A/B/C panel template.
4. **Audit encoding.** Check what marks and channels mean, what comparisons are valid, and how sorting, projection or lens distortion changes interpretation. Preserve meaningful scales and consistent semantic color. Compare custom representations to a competitive familiar baseline.
5. **Specify shared state.** Apply the coordination contract to important links: source, typed selection, mapping, target computation, reference population, feedback and undo. Distinguish highlight, filter, derive, parameter change and model execution. Prefer one state/query coordinator over pairwise event chains.
6. **Trace evidence.** Make material transformations and filters visible. Link aggregates to records when required. Expose missingness, uncertainty, approximation and group support. Save consequential states when the workflow needs comparison, replay or story export.
7. **Implement proportionally.** Separate source data, transformations, analytical state, queries, renderers and interactions. Use stable IDs; record seeds for stochastic processing. Keep credentials outside source. Check current APIs/version compatibility when selecting a stack; historical code notes are not current API guarantees.
8. **Verify real behavior.** Check semantic invariants and representative action traces before cosmetic polish. Test at the intended scale and export size when relevant. Require accessible alternatives to hover, color-only and drag-only core actions. A screenshot verifies appearance, not correct state propagation.
9. **Deliver with status.** State what works, which checks ran, and what remains unknown. Do not infer measured user benefit from a rubric score or successful structural validation.

## Visual defaults

Prefer white/light neutral backgrounds, fine separators, compact readable type, limited semantic color, a clear focal analysis view and supporting evidence. Use little decorative chrome. Keep density subordinate to legibility, accessibility and task demands. Scientific imagery or medium constraints may justify dark/3D presentation; explain the analytical reason. Avoid KPI grids, glow and large decorative cards when they displace evidence.

## Integrity gates

Block delivery as a validated analytical result if there is a misleading encoding, invalid cross-view identity mapping, changing undisclosed denominator, stale computation shown as current, fabricated evidence, or an unsupported causal claim. A coherent conventional view can pass; novelty is not a requirement.

When reviewing, distinguish **critical** semantic/statistical errors, **major** workflow/evidence failures and **minor** visual polish. Give concrete fixes and tests. Never average a critical failure away with strong aesthetics or usability scores.

## Completion by mode

- **Design:** question-to-view map, encoding/interaction model, important coordination contracts, implementation direction and risk-specific evaluation.
- **Review:** prioritized findings tied to the source, corrected semantics/design, retained strengths and acceptance checks.
- **Implement/refactor:** runnable artifact, data assumptions, operational instructions, tested action traces and remaining limitations.
- **Figure/story:** readable evidence at target size, matching source/state and caption, no essential hover-only content.
- **Explain:** concise domain-relevant reasoning, without running the whole workflow.

## Resources and tools

Use `assets/project-brief-template.md`, `assets/review-checklist.md`, and `assets/coordination-contract-template.json` only where useful.

- `references/anti-patterns.md`: failure modes.
- `references/routing-and-composition.md`: mixed-task ownership.
- `references/academic-foundations.md`, `references/source-manifest.md`: academic grounding; verify primary sources for citations.
- `references/code-inspection-notes.md`: inherited implementation notes; verify relevant code/version before relying on them.
- `references/case-study-prompted-pws.md`: domain-specific source example, never a layout template.
- `references/evals.md`: routing scenarios; `references/behavioral-evaluation.md`: output/task evaluation.
- `scripts/check_coordination.py`: structural contract lint; use `--help`. It does not execute the target application or prove its semantics.
- `scripts/audit_design_brief.py`: advisory keyword coverage only, not design quality.
- `scripts/scaffold_brief.py`: copy canonical template; use `--help`.
- `scripts/validate_skill.py`: structural validation, requiring Python 3 and PyYAML.
- `scripts/package_skill.py`: export on explicit request; use `--help`.
