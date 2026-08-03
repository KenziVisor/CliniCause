# Stage 4.10A Evidence Report — Conclusions and Future Work

## 1. Commit and branch validation

Verified `5739832 step 4.9B` on branch `main`; its immediate predecessor is `7ef3d97 step 4.9A`.  The Stage 4.9B report exists and concludes **READY WITH NON-BLOCKING WARNINGS**.  It records a 119-page validated thesis, no Chapter 10 numerical change, and readiness to draft Chapter 12.  Chapter 12 initially contained only the approved two-placeholder structure.

## 2. Initial worktree state

The worktree was already dirty before Stage 4.10A.  Existing unrelated changes include root documentation/code/requirements/tests, the nested causal repository, literature metadata, important-document copies, and checked result artifacts.  They were not overwritten, staged, or absorbed.  The prior Stage 4.9B changes were already committed.

## 3. Baseline build result

From `thesis-writing/thesis`, ran `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf`.  The baseline completed successfully at 119 pages with 0 unresolved citations, 0 unresolved references, 0 duplicate labels, 0 Biber warnings, and 0 fatal errors.  It had 99 overfull and 1,149 underfull box warnings.

## 4. Files inspected

Read Chapters 1 and 3--12; Chapter 8 is stored as `08_robustness_sensitivity_validation.tex`, rather than the stale name in the task declaration.  Chapter 2 was also checked for terminology.  Chapter 10 was treated as numerical authority, Chapter 11 as interpretation/limitation authority, and Chapter 1 as objective/RQ/contribution authority.

Inspected the required claim ledger, evidence inventory, experiment inventory, unresolved questions, terminology map, thesis-story/outline/evidence-map/notation/writing-order plans, Stage 4.8/4.9A/4.9B reports, and the current unresolved-placeholder and deferred-fix logs.  Later approved thesis text and Stage 4.9B findings took precedence where planning material differed.

## 5. Evidence brief summary

Created `stage_4_10A_conclusion_evidence_brief.md` before drafting.  It bounds the conclusion to an evidence-tracked workflow linking irregular-time-series representation, project-specific proxy states, prediction/aggregation, project-authored DAGs, and retrospective adjusted analysis across PhysioNet 2012 and MIMIC-III.  It distinguishes implementation-supported workflow contributions from qualified empirical findings and exploratory CausalPFN evidence, and it explicitly lists prohibited stronger claims.

## 6. Supported contribution set

The chapter includes only these supported contributions: transparent integration of the processing-to-analysis workflow; a shared proxy-state interface; separate causal and split-aware predictive contracts; cross-dataset application without pooling; a four-model predictive comparison; project-authored graph-guided multi-estimator analysis; descriptive matching and available diagnostic qualification; and evidence/provenance tracking.  It does not claim invention of the underlying models, weak supervision, DAGs, matching, DML, causal forests, or sensitivity methods.

## 7. Supported findings used

The chapter states that STraTS led the archived proxy-label metrics in MIMIC-III and GRU-D in PhysioNet; this is directly supported by Chapter 10, Section 2 and Chapter 11 SRQ-3.  It states that primary CausalForestDML mean summaries were positive for 9/9 MIMIC-III and 9/10 PhysioNet exposures, with PhysioNet shock negative; this comes from Chapter 10, Section 3 and Chapter 11 SRQ-6.  It states that CausalForestDML and LinearDML directions agreed in 19/19 original-cohort comparisons, and that CausalPFN agreed with both in 18/19, from Chapter 10, Sections 5--6 and Chapter 11 SRQ-6.

Each numerical statement is copied from Chapter 10 with its cohort, estimator role, and qualification preserved.  No new aggregate, metric, count, or figure is introduced.

## 8. Exploratory findings retained as exploratory

CausalPFN remains exploratory throughout Chapter 12: the approved corpus lacks a verified primary method source, and its sensitivity/permutation stages were intentionally absent from the archived diagnostic workflow.  Matching remains descriptive empirical-support evidence, not independent causal confirmation.  Outcome-downsampled analyses are retained only as a future-work/robustness limitation, not a primary conclusion.  The PhysioNet shock disagreement remains an example of estimator and support fragility.

## 9. Limitations carried into the chapter

The conclusion retains project-specific proxy validity, rule/prediction/vote error propagation, uncertain DAG and temporal ordering, non-manipulable exposure concerns, unmeasured confounding, incomplete overlap/balance evidence, estimator disagreement and incomplete uncertainty, missing CausalPFN support, incomplete clinical review, external/fairness/deployment limits, and incomplete raw-data/configuration/split/checkpoint/commit/archive provenance.  It also retains the bounded LLM role: prompts supplied design provenance only, while prompt-run settings and human-review decisions remain incomplete.

## 10. Future-work derivation

All future work follows a documented limitation: clinical review and chart-adjudicated validation for proxy states; target-trial-aligned observational design; support/balance/uncertainty/sensitivity procedures; provenance manifests; external, temporal, subgroup, and prospective validation; pipeline-handoff ablations; verified CausalPFN theory/version/diagnostics; and human-governed LLM decision records.  No future work is represented as completed.

## 11. Forbidden claims checked

The chapter does not call a proxy state a diagnosis, ground truth, or validated phenotype; does not describe the graph as validated; does not represent matching or estimator agreement as proof of a treatment effect; does not equate CausalPFN with DML estimators; does not claim clinical deployment readiness or treatment recommendations; does not describe an LLM as a medical expert or causal-discovery method; does not claim global positivity; and does not claim clean-checkout reproducibility.

The required risky-language scan produced one lexical match: `proved` occurs inside the non-claim word `approved` in “approved corpus.”  Manual review confirmed that it is not a prohibited conclusion claim.  The Chapter 12 InterpNet scan returned zero matches.

## 12. Citations used or intentionally omitted

Chapter 12 adds no external citations and no bibliography entry.  It refers to Chapter 10 and its sections for internal method/result provenance.  This avoids turning the conclusion into related work and avoids adding an unauthorized CausalPFN or LLM-methodology citation.

## 13. Numerical values repeated and Chapter 10 sources

| Repeated value | Chapter 10 source | Required boundary retained |
| --- | --- | --- |
| 9/9 MIMIC-III primary CausalForestDML summaries positive | Section 3, paragraph 2; Table `tab:results-forest-mimic` | Mean model-estimated CATE summaries over the analyzed sample, not clinical effects. |
| 9/10 PhysioNet primary CausalForestDML summaries positive; shock negative | Section 3, paragraph 5; Table `tab:results-forest-physionet` | Same conditional interpretation. |
| 19/19 CausalForestDML/LinearDML directional agreement | Section 5, paragraph 1; Table `tab:results-linear-comparison` | No equivalence, correctness, or uncertainty claim. |
| 18/19 all-three-estimator directional agreement | Section 6, paragraph 1; Figure `fig:results-three-estimator-direction` | CausalPFN remains exploratory and diagnostic-incomplete. |

## 14. Cross-check against Chapters 1, 10, and 11

| Conclusion claim | Introduction alignment | Results support | Discussion support | Evidence-brief status | Action |
| --- | --- | --- | --- | --- | --- |
| Evidence-tracked integrated workflow | Matches objective and primary contribution hierarchy. | Workflow/result handoffs are represented across the result packet. | Main RQ answer calls integration implementation-supported. | supported | Retained. |
| Dataset-specific predictive leaders | Matches SRQ-3. | Chapter 10 Section 2/Table predictive performance. | SRQ-3 retains qualified dataset-dependence. | supported with qualification | Retained without metrics. |
| Primary forest sign pattern | Matches SRQ-6 hierarchy. | Chapter 10 Section 3/tables. | SRQ-6 rejects causal and intervention-priority interpretation. | supported with qualification | Retained with explicit assumptions. |
| DML directional triangulation | Matches multi-estimator contribution. | Chapter 10 Section 5/table. | SRQ-6 states no equivalence/correctness conclusion. | supported with qualification | Retained with disagreement boundary. |
| CausalPFN complement | Introduction assigns exploratory role. | Chapter 10 Section 6/figure. | SRQ-6 retains literature and diagnostic gap. | exploratory | Retained as exploratory only. |
| Clinical/deployment boundary | Matches objective exclusions. | No clinical/deployment result exists. | Chapter 11 explicitly rejects bedside/deployment inference. | required limitation | Retained. |
| Future research priorities | Follows contribution boundaries. | No future work presented as a result. | Chapter 11 limitations and deferred fixes supply each need. | permitted | Retained as future work. |

No new method, result, citation, contribution, or hierarchy change was found.  Original cohorts remain primary; CausalForestDML remains primary; LinearDML remains secondary; CausalPFN remains exploratory; and outcome-downsampled analyses remain robustness-only.

## 15. Files changed

- `thesis-writing/thesis/chapters/12_conclusions_future_work.tex`
- `thesis-writing/logs/stage_4_10A_conclusion_evidence_brief.md`
- `thesis-writing/logs/stage_4_10A_evidence_report.md`
- `thesis-writing/thesis/main.pdf` from the permitted clean build

No tracking-log update was needed because Stage 4.10A identified no genuinely new unresolved issue and did not change an existing issue's status.

## 16. Final worktree state

The Stage 4.10A changes are limited to the files above.  Pre-existing unrelated modifications remain outside this scope and were not staged.  Auxiliary LaTeX build products were cleaned after validation; `main.pdf` is retained as the authorized build output.

## 17. Final build result

After drafting, ran `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf`.  The build succeeded and produced a 122-page PDF at `thesis-writing/thesis/main.pdf`, SHA-256 `0c9f01f824a0f58e6842262dd5fc6e1cca8cdf292c5c71f1421825099337a6a5`.  There are 0 unresolved citations, 0 unresolved references, 0 duplicate labels, 0 Biber warnings, and 0 fatal errors.  Layout warnings are 99 overfull and 1,149 underfull boxes, unchanged from the 119-page baseline; Chapter 12 introduced none.

## 18. Unresolved issues

The existing non-blocking external gates remain: supervisor ratification of related-work/results hierarchy; clinical review and validation of proxy states; verified primary CausalPFN source; missing SOFA and Berlin ARDS PDFs; exact causal configurations and predictive lineage; raw/processed/producers/archive provenance; overlap/balance, fairness, external/prospective validation; LLM prompt-run/human-review manifest; and institutional ethics/governance wording.  These issues were carried forward, not resolved or duplicated.

## 19. Readiness decision for Stage 4.10B

**READY FOR STAGE 4.10B WITH NON-BLOCKING WARNINGS**

Chapter 12, the prior evidence brief, and this report are complete; the build passes; conclusion claims are supported and bounded; and no unrelated file was modified by this stage.  The listed external validation, clinical-review, provenance, and supervisor gates remain non-blocking for the independent conclusion-consistency audit.
