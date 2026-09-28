# Routing and Skill Composition

This file helps an agent decide whether Research Visual Analytics (RVA) should be primary, secondary, or not used.

## Primary use

RVA should be primary when the requested deliverable is mainly an analytical visualization or visualization system, for example:

- research / scientific visualization UI;
- paper-style research panel or visual analytics workspace;
- coordinated multi-view exploration;
- custom D3/SVG/Canvas/WebGL analytical visualization;
- experiment/model comparison and error-analysis interface;
- uncertainty, provenance, relation, parameter-space, or evidence-traceability visualization;
- refactoring a generic dashboard into a research analysis workspace;
- reviewing visualization design for a VIS/EuroVis/CHI-style research system.

## Secondary use

Use RVA as supporting guidance when another artifact or domain owns the final deliverable:

- **Presentation / slides:** presentation skill owns the deck; RVA guides analytical figures and visual evidence.
- **Document / paper / report:** document or writing workflow owns the document; RVA guides figures and visual-analysis sections.
- **Spreadsheet:** spreadsheet skill owns workbook logic; RVA contributes only if advanced analytical visualization is requested.
- **Web application:** web/app implementation workflow owns the product; RVA owns the analytical workspace, view coordination, and visual encodings.
- **Paper review:** paper-reading workflow owns factual interpretation; RVA joins when the user asks to critique the paper's visualization/interaction design.
- **Domain analysis (remote sensing, education, biology, networks, etc.):** domain workflow owns domain correctness; RVA maps domain tasks to visual analysis.

## Do not use as primary

- ordinary KPI / operations dashboard where conventional charts are sufficient;
- one simple chart request (bar, line, pie, scatter) with no research/analysis-system intent;
- decorative infographic, poster, marketing image, landing page, or brand design;
- slide beautification where the chart is incidental;
- generic frontend styling with no analytical visualization component;
- pure statistical analysis with no visualization deliverable.

## Ambiguous cases

### “做一个 dashboard”
- If it is for research exploration, experiments, scientific data, model diagnostics, or evidence tracing → RVA primary.
- If it is for revenue/KPIs/operations reporting → use business/dashboard tooling; RVA only if user explicitly wants research-style analysis.

### “做模型结果可视化”
- If the user needs model comparison, error analysis, uncertainty, embeddings, attribution, diagnostics, or interactive exploration → RVA primary.
- If the user only wants one accuracy bar chart → RVA usually unnecessary.

### “做论文 Figure”
- If the figure communicates analytical relationships or combines coordinated evidence → RVA useful/primary.
- If it is a simple schematic/architecture diagram → diagram or image workflow may be more appropriate.

## Composition rule

When multiple skills apply, preserve ownership:

**Artifact/domain skill owns the deliverable; RVA owns analytical visualization decisions.**

Do not let RVA override explicit user format, domain facts, data integrity, or artifact-specific constraints.

## Shared handoff and stopping rule

Innovation owns invention; RVA owns analytical correctness. Transfer one record containing question/view/link/state IDs, mapping/decoding rules, coordination contract, known facts, baseline and validation status. If the companion is absent, apply the core integrity checks locally. For fixed implementation, do not rerun ideation. Reopen a design only for a concrete unresolved risk; no automatic infinite review loop.
