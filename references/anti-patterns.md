# Anti-Patterns

## 1. Chart Gallery Dashboard
Symptom: one pie + one bar + one line + one scatter because they were available.
Fix: rewrite analytical questions and map each to evidence.

## 2. KPI-First Research UI
Symptom: giant cards dominate screen but users need relationships/distributions.
Fix: keep summary values compact; give space to analytical views.

## 3. Unlinked Multi-Panel Collage
Symptom: many panels, no shared selection/filter state.
Fix: define stable IDs and shared analytical state; link only when analytically meaningful.

## 4. Color as Decoration
Symptom: gradients/brand colors imply nonexistent categories or priorities.
Fix: reserve salient color for semantic state; document the mapping.

## 5. Custom-for-Custom's-Sake
Symptom: novel radial/glyph layout but users cannot judge the needed quantity.
Fix: compare against a standard baseline and retain custom design only if it reveals a relation more clearly.

## 6. Embedding = Truth
Symptom: t-SNE/UMAP distance interpreted as definitive similarity/clusters.
Fix: explain projection limits; link to original attributes/samples; allow parameter/slice checks.

## 7. Leaderboard-Only Model Analysis
Symptom: model comparison reduced to accuracy/F1 KPI cards.
Fix: add error slices, distributions, residuals, calibration/uncertainty, and example evidence appropriate to the model.

## 8. Hidden Transformation
Symptom: normalization, filtering, aggregation, smoothing, or imputation not visible.
Fix: disclose transformations and allow inspection/reversal when material.

## 9. Hover Prison
Symptom: essential information only appears on mouse hover.
Fix: use persistent selection/details for core tasks and keyboard/tap-accessible controls.

## 10. False Precision
Symptom: excessive decimals, exact-looking boundaries, deterministic labels for probabilistic outputs.
Fix: match precision to data quality and expose uncertainty.

## 11. Animation as Analysis
Symptom: motion draws attention but makes comparison harder.
Fix: use animation only for continuity/state transition; provide stable comparison states.

## 12. Panel Naming as Marketing
Symptom: “AI Insight Brain”, “Smart Cockpit”, “Intelligence Center”.
Fix: name panels by analytical function: Relation Analysis, Error Cases, Parameter Space, Sample Detail.

## 13. Backend-Driven UI
Symptom: UI mirrors API endpoints/database tables rather than analyst tasks.
Fix: organize around task sequences; keep implementation structure separate from information architecture.

## 14. Unjustified 3D
Symptom: perspective/occlusion added for novelty.
Fix: use 3D only when spatial structure or domain geometry is genuinely three-dimensional and interaction supports depth understanding.

## 15. Research Screenshot Without Story
Symptom: paper figure is a full UI screenshot with illegible text.
Fix: crop/compose panels around a clear analytical narrative, label subfigures, and add focused annotations.
