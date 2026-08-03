# Stage 4.10A Conclusion Evidence Brief

## 6.1 Research problem

This thesis addresses the integration problem of turning irregular ICU measurement histories into transparent analytical objects that can be used consistently across prediction and retrospective observational analysis.  It connects irregular-time-series representation, project-specific proxy-state construction and prediction, and DAG-guided adjusted mortality analysis across PhysioNet 2012 and MIMIC-III.  The central challenge is not simply selecting a model: each handoff must preserve the distinction between source measurements, rule-derived proxy states, predicted/aggregated labels, and assumption-dependent effect estimates, while retaining evidence and provenance boundaries.

## 6.2 Supported workflow summary

- Dataset-specific preprocessing produces causal and split-aware predictive data contracts; raw-data, processed-artifact, and split provenance are incomplete.
- Deterministic source-code rules construct project-specific clinically inspired proxy states; these are not verified diagnoses or complete clinical definitions.
- Prediction exports are normalized into probability/binary forms and may be aggregated by deterministic majority vote; voting is not clinical consensus.
- Dataset-specific, project-authored DAGs are encoded in source code and used to select observed adjustment variables; prompts are design provenance only.
- Matching produces descriptive empirical-support summaries; CausalForestDML is the primary model-estimated CATE estimator; LinearDML is secondary; CausalPFN is exploratory.
- Matching, sensitivity, and permutation diagnostics are available with coverage and provenance qualifications for DML estimators.  CausalPFN sensitivity and permutation stages were intentionally skipped.

## 6.3 Supported contribution set

| Contribution | Evidence source | Permitted wording | Forbidden stronger wording | Confidence |
| --- | --- | --- | --- | --- |
| Integrated pipeline design | Chapters 1, 3--9, 11 | An evidence-tracked retrospective workflow links preprocessing, proxy states, prediction, aggregation, graph-guided adjustment, estimation, and diagnostics. | A clinically validated end-to-end system. | supported |
| Common proxy-state interface | Chapters 3--7, 11 | Shared rule-derived proxy-state identifiers connect prediction and downstream analysis. | The interface establishes biological latent states or diagnoses. | supported with qualification |
| Cross-dataset application | Chapters 1, 9--11 | The workflow was applied separately to PhysioNet 2012 and MIMIC-III. | The results are pooled, transportable, or construct-equivalent across datasets. | supported with qualification |
| Predictive comparison | Chapter 10, Section 2; Chapter 11 SRQ-3 | Four learned models completed the archived proxy-label task, with dataset-specific leaders. | A universally superior architecture or clinical prediction validation. | supported with qualification |
| Transparent proxy construction | Chapters 5 and 11 | Deterministic rules make proxy construction inspectable and traceable to source code. | Exact thresholds form validated phenotypes or formal diagnoses. | supported with qualification |
| DAG-guided multi-estimator analysis | Chapters 7, 9--11 | Project graphs operationalize exposure-specific observed adjustment and support comparative estimator analysis under stated assumptions. | The DAG is validated or estimator use proves identification. | supported with qualification |
| Estimator agreement/disagreement analysis | Chapter 10, Sections 5--6; Chapter 11 SRQ-6 | Directional comparisons expose both broad agreement and substantive disagreement. | Agreement proves estimator correctness or causal effects. | supported with qualification |
| Evidence/provenance tracking | Chapters 1, 9, 11; Stage 4.6A/4.9B reports | Checked tables, manifests, hashes, source packets, and explicit deferred issues improve numerical traceability. | The repository alone supports complete clean-checkout reproduction. | supported with qualification |
| CausalPFN comparison | Chapter 10, Section 6; Chapter 11 SRQ-6 | CausalPFN contributes an exploratory empirical comparison with incomplete diagnostic and literature support. | Equivalent, validated, superior, or theoretically established treatment. | exploratory |

## 6.4 Supported findings

| Finding | Exact source location | Number may be repeated | Required qualification |
| --- | --- | --- | --- |
| The leading predictive family differed by dataset: STraTS in MIMIC-III and GRU-D in PhysioNet. | Chapter 10, Section 2, paragraphs 1--2 and Table `tab:results-predictive-performance`; Chapter 11 SRQ-3. | No metric value needed. | Archived proxy-label test summaries; no universal superiority, intervals, paired tests, or complete lineage. |
| Primary CausalForestDML summaries were positive for all nine MIMIC exposures and nine of ten PhysioNet exposures; PhysioNet shock was negative. | Chapter 10, Section 3, paragraphs 2 and 5; Tables `tab:results-forest-mimic` and `tab:results-forest-physionet`; Chapter 11 SRQ-6. | Yes: 9/9 and 9/10. | Mean model-estimated CATEs over the analyzed sample, conditional on assumptions; not clinical effects. |
| CausalForestDML and LinearDML had the same mean-effect direction in all 19 original-cohort dataset--exposure pairs. | Chapter 10, Section 5, paragraph 1 and Table `tab:results-linear-comparison`; Chapter 11 SRQ-6. | Yes: 19/19. | Directional triangulation only; magnitudes, rankings, uncertainty, and validity differ. |
| CausalPFN had the same direction as both DML estimators in 18 of 19 comparisons, with PhysioNet shock the exception. | Chapter 10, Section 6, paragraphs 1--2 and Figure `fig:results-three-estimator-direction`; Chapter 11 SRQ-6. | Yes: 18/19. | Exploratory only; no primary method citation and no comparable sensitivity/permutation diagnostics. |
| Outcome downsampling preserved direction in 55 of 57 matched comparisons, while changing the empirical population and two PhysioNet signs. | Chapter 10, Section 7, paragraph 2; Chapter 11 Cross-Dataset Interpretation and Robustness. | Omit from concise Chapter 12 prose unless needed. | Robustness perspective only; no pooling, transport, or stronger causal interpretation. |

## 6.5 Exploratory or bounded findings

- CausalPFN results remain exploratory because the canonical corpus lacks its verified primary source and the pipeline lacks the DML-equivalent diagnostic family.
- Matching is a descriptive/support baseline, not independent causal confirmation; failures, larger Hamming distances, and insufficient-pair flags are substantive limits.
- Causal estimates are conditional on proxy measurement, intervention definition, graph validity, temporal ordering, exchangeability, overlap, and model adequacy.
- Directional agreement is informative but does not establish equal magnitudes, uncertainty, estimator equivalence, or correctness; the PhysioNet shock disagreement must remain visible.
- Downsampled analyses use a different empirical population and remain robustness-only.
- Prediction findings concern rule-derived proxy labels and remain constrained by target validity and export provenance.

## 6.6 Required limitations

Chapter 12 must retain: project-specific proxy-state construct validity; rule/prediction/vote error propagation; observational identification assumptions and possible unmeasured confounding; uncertain DAG and temporal ordering; incomplete overlap and balance evidence; estimator/model dependence and incomplete uncertainty; CausalPFN literature/diagnostic gaps; clinical review absence; external validity, fairness, and deployment limits; raw/processed-data, configuration, split/checkpoint, commit, and archive-copy provenance gaps; and incomplete LLM prompt-run/human-review documentation.

## 6.7 Permitted future work

| Future-work item | Limitation addressed | Concrete next action | Requirement |
| --- | --- | --- | --- |
| Clinical construct validation | Project-specific proxy states and missing review | Conduct documented clinician review and, where feasible, blinded chart adjudication against frozen rules. | expert review; new data/annotation |
| Provenance completion | Missing configurations, artifact hashes, split/checkpoint, copy history | Create signed per-run manifests linking inputs, commands, configurations, commits, environments, and outputs. | implementation/documentation |
| Target-trial-aligned design | Ill-defined illness-state exposures and temporal ambiguity | Specify eligibility, time zero, intervention strategies, follow-up, estimand, and confounding plan before rerunning. | design; new experimentation |
| Support and uncertainty assessment | Missing propensity/balance evidence and incomplete intervals | Add prespecified overlap/balance diagnostics, support-aware estimands, uncertainty, multiplicity, and sensitivity procedures. | implementation; experimentation |
| External, temporal, subgroup, and prospective validation | Dataset-specificity, fairness, and no deployment evidence | Evaluate frozen definitions on additional cohorts and clinically justified subgroups before prospective safety/impact studies. | new data; expert review; experimentation |
| Error-propagation and handoff ablations | Measurement, rule, prediction, and aggregation error | Compare rule-derived, predicted, and voted states and ablate individual pipeline handoffs. | implementation; experimentation |
| CausalPFN verification | Missing primary source and diagnostic support | Verify its primary source/version and add an approved uncertainty/diagnostic plan before elevating its role. | literature authorization; implementation |
| Human-governed LLM provenance | Incomplete prompt and review record | Archive prompt settings plus rule/edge-level accepted/rejected human and clinical decisions. | documentation; expert review |

## 6.8 Forbidden conclusion claims

Chapter 12 must not claim that proxy states are verified diagnoses, validated phenotypes, or ground truth; that project DAGs are clinically validated; that matching, association, or estimator direction proves a treatment effect or causality; that CausalPFN has DML-equivalent theory or diagnostics; that the models are clinically ready or yield treatment recommendations; that an LLM was a medical expert or causal-discovery method; that overlap/positivity was globally proven; that tracked materials alone permit a clean-checkout rerun; or that this thesis invented the cited models, weak supervision, DAG, matching, DML, causal-forest, or sensitivity methods.
