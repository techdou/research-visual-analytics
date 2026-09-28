# Statistical and population integrity

Record grain, eligible population, inclusion/exclusion, aggregation, weights, numerator/denominator, missing-data handling and reference group for every derived metric.

- Multi-label counts may count memberships rather than samples; proportions may sum above 100%. Label the chosen denominator and deduplicate at the correct grain.
- Filtering can change the denominator, the reference distribution or both. Display support and reference; do not compare conditional rates as if their populations stayed fixed.
- Pinned groups need snapshot/predicate semantics and overlap handling. For paired observations, compare matched units; disclose dropped matches. Repeated observations are not independent subjects.
- Changing composition can reverse aggregate trends. Inspect stratification before attributing a change to model quality or intervention.
- Distinguish missing values, unavailable modalities, zero, uncertainty and prediction disagreement. Confidence scores are not automatically calibrated probabilities.
- Label uncertainty source: sampling, model, measurement or approximation. Show method/coverage when available; never invent confidence intervals without requisite data or assumptions.
- Exploratory repeated slicing generates hypotheses; do not silently convert a discovered subgroup into confirmatory evidence. Disclose selection and use held-out or other appropriate validation for confirmatory claims.
- A correlation view, sensitivity display or model what-if does not establish a real-world causal effect. Identify the computation and assumptions.

Review all rates with an inspectable small example. Check empty denominators as undefined/no support, not 0%; specify ratio behavior at zero and units for differences. Separate accuracy of the data computation from effectiveness of the visualization.
