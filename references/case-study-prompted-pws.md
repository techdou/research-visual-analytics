# Case Study: EuroVis 2025 Prompted-PWS Visual Analytics System

Reference:
Y. Lin, S. Wei, H. Zhang, D. Qu, J. Bai. “An Interactive Visual Enhancement for Prompted Programmatic Weak Supervision in Text Classification.” Computer Graphics Forum, 44(3), EuroVis 2025. DOI: 10.1111/cgf.70131.

Use this only as a design-study example. Do not copy the project domain, layout, or figures by default.

## What is worth learning

### 1. Requirements drive views
The system requirements include guidance for developing prompted label functions, actionable ways to inject user knowledge, support for evaluation of individual iterations, and analysis of LF↔LF and LF↔data relationships.

### 2. Interrelated views, not chart collage
The UI combines dataset overview, sample/data list, LF development, LF status/history, pairwise LF relation analysis, and LF-data relation analysis.

Each view corresponds to a different analytical question.

### 3. Two-stage iteration
Stage 1: refine an individual LF using development-space exploration and evaluation.
Stage 2: evaluate the set of LFs globally, including conflict/redundancy and relationships to data, then merge/modify/create LFs.

General lesson: complex research workflows may need both local-object iteration and global-system iteration.

### 4. Matrix chosen for pairwise relations
The authors considered a chord diagram but selected a matrix for better scalability/accessibility as LF count increases.

General lesson: choose representation after considering relation type and scale, not visual novelty.

### 5. RadViz chosen for relation semantics
RadViz anchors correspond to LFs and positions data according to LF influence; it was selected over generic dimensionality reduction because the analytical question is LF-data relationship, not only sample similarity.

General lesson: layout coordinates should have meaning aligned to the research question.

### 6. Detail evidence remains available
Sample lists expose errors/missed cases so users can inspect why rules fail.

General lesson: aggregate relations should be traceable to underlying evidence when interpretation requires it.

## What not to generalize

- RadViz is not a default research visualization.
- A/B/C/D/E panel composition is not a universal layout.
- Label functions and weak supervision are domain-specific.
- Small cards are not inherently “scientific”; their value depends on the analytical task.
