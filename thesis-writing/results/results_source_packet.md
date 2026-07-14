# Stage 4.6A Results Source Packet

This packet points to checked CSVs; it deliberately does not reproduce full numerical tables.

## C10.1 Data and cohort summary
- Checked file: `checked_cohort_candidates.csv`
- Canonical source artifacts: Export, majority-vote, and run-summary counts
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Pipeline-contract-specific counts
- Blocked fields: Raw cohort totals
- Required wording boundary: Do not merge pipeline counts
- Remaining human decision: Cohort-count source
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix/supporting.

## C10.2 Proxy prevalence and co-occurrence
- Checked file: `checked_proxy_prevalence.csv; checked_proxy_cooccurrence.csv`
- Canonical source artifacts: MIMIC rule-based tables
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Existing values only
- Blocked fields: PhysioNet counterpart tables
- Required wording boundary: Proxy states, not diagnoses
- Remaining human decision: Proxy exposure selection
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix/supporting.

## C10.3 Predictive performance
- Checked file: `checked_predictive_metrics.csv`
- Canonical source artifacts: Ten training summaries and paired logs
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Validation/test metrics
- Blocked fields: InterpNet numerical results
- Required wording boundary: Do not overstate split provenance
- Remaining human decision: Model comparison hierarchy
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Main text candidate.

## C10.4 Learning-curve diagnostics
- Checked file: `checked_figure_candidates.csv`
- Canonical source artifacts: Archived learning-curve PNGs
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Diagnostic figures
- Blocked fields: Selected figure
- Required wording boundary: Diagnostic only, not test-metric substitute
- Remaining human decision: Learning-curve selection
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix.

## C10.5 Mortality prediction from proxy states
- Checked file: `checked_mortality_prediction.csv`
- Canonical source artifacts: Canonical mortality text outputs
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Existing source metrics
- Blocked fields: Formal causal interpretation
- Required wording boundary: Proxy-state mortality-prediction association
- Remaining human decision: Presentation role
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix/supporting.

## C10.6 Matching results
- Checked file: `checked_matching_results.csv; checked_matching_failures.csv`
- Canonical source artifacts: Cross-run table and per-run summaries
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Matched-pair fields
- Blocked fields: Approved estimand wording
- Required wording boundary: Do not call mean_pair_effect ATE or ATT
- Remaining human decision: Matching wording
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Main text candidate.

## C10.7 CATE estimates
- Checked file: `checked_cate_candidates.csv`
- Canonical source artifacts: Full per-run global summaries
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Mean CATE and distribution fields
- Blocked fields: Primary estimator/sampling/exposures
- Required wording boundary: Do not call mean_cate ATE
- Remaining human decision: Primary hierarchy
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Main text candidate.

## C10.8 Heterogeneity diagnostics
- Checked file: `checked_heterogeneity_candidates.csv`
- Canonical source artifacts: Patient-level CATE and feature artifacts
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Artifact availability
- Blocked fields: New subgroup effects
- Required wording boundary: Feature importance is not mechanism
- Remaining human decision: Figure choice
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix.

## C10.9 Overlap and support
- Checked file: `checked_matching_results.csv; checked_matching_failures.csv`
- Canonical source artifacts: Matching support fields
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Match rate and failures
- Blocked fields: Dedicated overlap figure
- Required wording boundary: No positivity claim
- Remaining human decision: Omit/generate figure later
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix.

## C10.10 Sensitivity
- Checked file: `checked_sensitivity_candidates.csv`
- Canonical source artifacts: Non-PFN benchmark artifacts
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Existing diagnostics
- Blocked fields: Primary contour
- Required wording boundary: Keep source classification
- Remaining human decision: Contour selection
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix/main-text decision.

## C10.11 Permutation checks
- Checked file: `checked_permutation_candidates.csv`
- Canonical source artifacts: Archived aggregate files
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Existing trial summaries
- Blocked fields: New p-values
- Required wording boundary: Do not label formal test without source support
- Remaining human decision: Role decision
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix.

## C10.12 Cross-dataset comparison
- Checked file: `checked_cate_candidates.csv`
- Canonical source artifacts: Separate dataset rows
- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence
- Available numerical fields: Dataset-specific estimates
- Blocked fields: Combined average
- Required wording boundary: No cross-dataset pooling
- Remaining human decision: Comparison scope
- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.
- Recommended role: Appendix/supporting.
