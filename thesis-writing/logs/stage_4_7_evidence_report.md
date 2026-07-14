# Stage 4.7 Evidence Report: Discussion

Date: 2026-07-14  
Scope: Chapter 11 only, plus the two tracking logs and this report  
Status: final build details completed after the clean validation build

## 36.1 Git State

- Required repair commit verified: `94d91e8` (`step 4.6B repair`).
- Branch: `main`.
- Initial worktree: dirty before Stage 4.7.  Pre-existing changes included root documentation, dependency/router/test files, a modified nested causal repository, prompt and literature metadata, checked result CSVs and `results_manifest.csv`, plus `tmp_verify_router.py`.  These user changes were preserved.
- Stage 4.7 files changed:
  - `thesis-writing/thesis/chapters/11_discussion.tex`
  - `thesis-writing/logs/unresolved_placeholders.md`
  - `thesis-writing/logs/deferred_fixes.md`
  - `thesis-writing/logs/stage_4_7_evidence_report.md` (created)
  - `thesis-writing/thesis/main.pdf` (clean-build output)
- No narrow correction to `main.tex` or `latexmkrc` was needed.
- Final worktree: remains dirty because all initial user changes are preserved and the five Stage 4.7 paths above are added/updated.  Build auxiliaries were cleaned after validation while retaining `main.pdf`.
- Results and figures: no Stage 4.7 write was made to a checked CSV, result manifest, decision register, source packet, figure register, figure, result artifact, bibliography, research-code file, or config.  Several of those paths were already dirty at entry; this statement concerns changes performed during Stage 4.7.
- No commit, push, figure creation/copy, experiment execution, or Stage 4.8 work occurred.

## 36.2 Baseline Build

Command run before drafting:

```bash
cd thesis-writing/thesis
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

- Result: success, return status 0.
- Baseline PDF: `thesis-writing/thesis/main.pdf`.
- Page size/count: A4, 90 pages.
- Baseline layout warnings: 95 overfull and 988 underfull boxes, as independently recorded by the immediately preceding Stage 4.6B-R repair report; `xdvipdfmx` also emitted the existing two duplicate internal page-object warnings (`Object @page.i already defined`).
- No fatal error or final unresolved citation/reference was present.

## 36.3 Files Inspected

### Thesis chapters

- Full current text of Chapters 3--12, with Chapter 10 treated as the numerical authority and Chapter 12 inspected only for continuity.
- `main.tex`, `latexmkrc`, figure README, front-matter/appendix inclusion context, and final build logs as needed for compilation and placement validation.

### Planning

- `thesis_story.md`
- `thesis_outline.md`
- `chapter_evidence_map.md`
- `citation_plan.md`
- `table_plan.md`
- `terminology_and_notation.md`
- `writing_order.md`
- `stage4_prompt_queue.md`

### Audit

- `unresolved_questions.md`
- claim ledger
- evidence inventory
- experiment inventory
- terminology map
- existing unresolved-placeholder and deferred-fix logs

### Result packet

- results manifest, source packet, decision register, and figure register
- checked cohort, predictive, matching, matching-failure, CATE, heterogeneity, sensitivity, and permutation tables needed to interpret Chapter 10
- no source value was recomputed or changed

### Stage 4 evidence reports

- Stage 4.2, 4.3, 4.3R, 4.4, 4.5, 4.6A, 4.6A-R, 4.6B, and 4.6B-R evidence/repair reports

### Literature metadata

- `thesis-writing/literature/metadata/references.bib`
- `thesis-writing/literature/metadata/catalog.csv`
- all 18 inserted keys were checked for exact existence in the bibliography and catalog; no bibliography edit was made

## 36.4 Main-RQ Answer

**Exact question:** “How can irregular ICU time-series data be converted into clinically interpretable proxy-state representations and used, under explicit causal assumptions, to support DAG-guided adjusted effect estimation for in-hospital mortality?”

**One-paragraph answer:** This thesis demonstrates an evidence-tracked framework in which dataset-specific irregular measurements are normalized into explicit data contracts; deterministic clinical rules define proxy-state prediction targets; irregular-time-series models predict those rule labels; normalized binary exports may be aggregated algorithmically; source-coded, project-specified DAGs define exposure-specific adjustment logic; and matching plus heterogeneous-effect estimators analyze the constructed proxy-state exposures.  The complete interface sequence was implemented and exercised in MIMIC-III and PhysioNet 2012.  The contribution is methodological feasibility and integration, not a clinically validated phenotype system or conclusive causal answer: interpretation remains conditional on construct measurement, intervention definition, temporal ordering, exchangeability, overlap, model adequacy, and provenance.

**Support:** Chapters 3--9 establish design, data contracts, proxy construction, prediction/aggregation, DAG methodology, diagnostics, and experiment governance; Chapter 10 supplies the checked empirical results.

**Boundaries:** no chart-adjudicated diagnoses, no empirically validated DAG, no guaranteed well-defined intervention, no proof of positivity or no unmeasured confounding, no bedside recommendation, and incomplete producing-run provenance.

## 36.5 Secondary-Question Matrix

| Question | Answer | Support | Answer strength | Principal limitation |
| --- | --- | --- | --- | --- |
| SRQ-1 | The pipeline uses separate causal and split-aware predictive contracts, linked through normalized identifiers, routing, export schemas, and voter inputs. | Chapters 4 and 6; router/source inspection; checked export schemas. | Implementation supported. | Exact processed hashes, producing commands, and final split lineage are incomplete. |
| SRQ-2 | Deterministic proxy states function consistently as prediction labels, aggregation inputs, and downstream exposures. | Chapter 5; active rule code; checked schemas. | Unresolved clinically. | No chart adjudication, complete clinical review, or cross-dataset construct equivalence. |
| SRQ-3 | All included predictive families completed the rule-label task; STraTS led the four archived MIMIC metrics and GRU-D led the four PhysioNet metrics. | Chapter 10 predictive table and Stage 4.6B report. | Empirically supported with qualifications. | No paired superiority tests/intervals; target validity and checkpoint lineage remain incomplete. |
| SRQ-4 | Paired probability/binary outputs are normalized and binary voter files are combined by deterministic identifier-aligned majority voting. | Chapter 6; active aggregation source; checked exports. | Implementation supported. | Algorithmic voting is not clinical consensus and can preserve shared error. |
| SRQ-5 | Source-coded project DAGs produce exposure-specific observed adjustment sets from available columns. | Chapter 7; graph and estimator source; checked adjustment records. | Conditional on assumptions. | Graph correctness, timing, identifiability, and unmeasured confounding are unresolved. |
| SRQ-6 | The frozen hierarchy shows broad directional triangulation across forest, linear, exploratory PFN, descriptive matching, and robustness diagnostics, with explicit exceptions. | Chapter 10 and checked CATE/matching/diagnostic packet. | Empirically supported with qualifications. | Agreement is not estimator equivalence, identification, or clinical actionability. |
| SRQ-7 | Construct, causal-identification, support, modeling, transport, provenance, fairness, and deployment limitations materially bound every result. | Chapters 5--10, audit logs, and the 17-row Chapter 11 matrix. | Partially supported. | Several limitations require new review, recovered provenance, or new validation evidence. |

## 36.6 Result Interpretation

| Result family | Evidence used | Interpretation in Chapter 11 | Prohibited overinterpretation avoided |
| --- | --- | --- | --- |
| Predictive findings | Checked predictive metrics and Chapter 10. | The leading architecture differed by dataset; representation choice is context dependent. | No universal superiority, clinical accuracy, or exact reproduction of published benchmark tasks. |
| Primary CausalForestDML | All 19 original-cohort primary rows. | Positive means for all nine MIMIC proxies and nine of ten PhysioNet proxies show systematic adjusted mortality-related variation under the implemented procedure. | No claim that proxy states caused mortality, that rankings are intervention priorities, or that estimates are population ATEs. |
| Matching | Fifteen successful original-cohort summaries, failures, warnings, pair/distance fields. | A transparent descriptive baseline and indirect support warning system; 14/15 signs aligned with the forest. | Not independent causal validation, automatic ATT, balance proof, or positivity proof; failures are not zero effects. |
| LinearDML | Nineteen original-cohort Forest--Linear comparisons. | Complete 19/19 directional agreement is useful model-form triangulation. | No equal magnitude/ranking/uncertainty, no unbiasedness claim, and no DAG validation. |
| CausalPFN | Nineteen original-cohort PFN comparisons and diagnostic status records. | Positive bounded conclusion: a complementary exploratory estimator that joined 18/19 all-three directional agreements. | Not called failed or superior; magnitude differences, absent PFN diagnostics, and missing primary citation remain explicit. |
| Cross-dataset comparison | Original analysis counts, proxy definitions, DAGs, and primary sign patterns. | The shared workflow is portable, while dataset context and construct differences matter. | No effect pooling, construct-equivalence assumption, biological inconsistency claim, or inference that larger MIMIC is more valid. |
| Downsampling | Fifty-seven matched original/downsampled comparisons. | A robustness-only population perturbation with broad 55/57 sign preservation. | Not causal validation, transport, or magnitude evidence; changed empirical population and both sign changes are explicit; no pooling. |
| Sensitivity | Per-treatment source/status fields and Chapter 10 summary. | Layered evidence with direct, reconstructed, partial, failed, and intentionally absent statuses. | No assertion that reconstructed is estimator-native or that benchmarks eliminate omitted-variable bias. |
| Permutation | Archived aggregate status/trial family and implementation record. | Disruption-based DML sanity checks. | Not automatically a formal randomization test, identification proof, or evidence for PFN. |
| Overlap | Matching availability, failures, distances, pair warnings; absence register. | Indirect empirical-support information only. | No claim that positivity is established; dedicated propensity/common-support and balance diagnostics remain missing. |

PhysioNet shock is preserved as the central exception: Forest and Linear means were negative, PFN was slightly positive, and matching was positive.  Chapter 11 treats this as estimator/representation/support sensitivity, not something resolved by voting and not a clinically protective effect.

## 36.7 Literature Comparison

| Citation key | Discussion claim | Usage boundary |
| --- | --- | --- |
| `banda_2018_electronic_phenotyping` | Electronic-phenotyping context for transparent proxy constructs. | Does not validate local rules or labels. |
| `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping` | Rule-based clinical phenotype context. | Does not establish local chart validity or dataset equivalence. |
| `ratner_et_al_2020_snorkel` | Broad weak-supervision motivation for combining noisy labels. | The local majority vote is explicitly not a learned Snorkel label model. |
| `sun_2026_review_irregular_medical_timeseries` | Context for irregular medical time-series representation. | Not local execution evidence or a superiority claim. |
| `lipton_kale_wetzel_2016_missingness_rnns` | Missingness can carry predictive information. | Does not prove why either local leader won. |
| `tipirneni2022strats` | Sparse/tokenized irregular-time-series modeling context for STraTS. | Local task is not claimed to reproduce the paper benchmark. |
| `che2018grud` | Missingness-aware recurrent modeling context for GRU-D. | Does not establish universal GRU-D superiority. |
| `pearl_1995_causal_diagrams` | DAG-based adjustment has explicit graphical assumptions. | Does not validate the project DAG or prove exchangeability. |
| `crump_et_al_2009_limited_overlap` | Limited overlap is a material identification/support issue. | No claim that local overlap was established. |
| `cinelli_hazlett_2020_sensitivity` | Sensitivity analysis can benchmark omitted-confounding robustness. | Does not show local unmeasured bias is absent. |
| `chernozhukov_et_al_2026_ovb_causal_ml` | Modern omitted-variable-bias context for causal ML. | Not proof of correctness for the archived diagnostics. |
| `hernan_robins_2016_target_trial` | Target-trial thinking clarifies observational causal questions. | No local target-trial emulation is claimed. |
| `hernan_taubman_2008_well_defined_interventions` | Intervention definition bounds causal interpretability. | Proxy illness states are not upgraded to treatments. |
| `smit_2023_causal_inference_icu_scoping_review` | ICU observational causal-analysis challenges. | Does not validate local assumptions or results. |
| `bica_2021_individualized_treatment_effects_ehr_ml` | EHR individualized-effect modeling context. | Predictive variation is not automatically actionable HTE. |
| `lipkovich_2024_modern_hte_methods` | Modern HTE validation and interpretation issues. | No method equivalence or local validation claim. |
| `curth_2024_ml_individualized_treatment_effects` | ML treatment-effect heterogeneity challenges. | Not evidence that local proxy contrasts are treatments. |
| `iwashyna_2015_hte_critical_care` | Critical-care heterogeneity and clinical interpretation context. | Does not supply local clinical validation. |

Every key exists exactly once in `references.bib`.  No literature citation is used to establish local execution, validate a project DAG, or fill the CausalPFN primary-source gap.

## 36.8 Limitations Matrix

| Chapter 11 row | Supporting repository evidence |
| --- | --- |
| Proxy construct validity | Active deterministic rules and schemas exist; no chart-adjudicated reference labels or sensitivity/specificity packet. |
| Prediction-label validity | Models and voters target rule-derived labels; common training targets create correlated-error risk. |
| Exposure definition | Binary illness-state proxies are used as exposures without a well-defined intervention/target-trial specification. |
| Temporal ordering | DAG code supplies topology, but record-level proxy/covariate/outcome timing is not fully validated. |
| DAG validity | Graphs are source-coded project assumptions derived partly from LLM-assisted design; no empirical/complete clinical validation. |
| Unmeasured confounding | Treatment-specific observed sets are limited to available columns; identifiability remains unresolved in the checked packet. |
| Overlap and support | Matching failures/warnings/distances exist; dedicated propensity, common-support, and balance artifacts do not. |
| Estimator/model dependence | Forest, Linear, and PFN agree broadly in sign but differ in magnitude, ordering, structure, and diagnostics. |
| Uncertainty and comparisons | Many main means lack intervals; no multiplicity strategy or new significance test is documented. |
| Outcome downsampling | Implementation retains positive outcomes and samples negatives, changing prevalence and the empirical population. |
| Cross-dataset transport | Different sizes, eras, variables, proxy ontologies, DAGs, measurement practices, and populations; no pooling or transport analysis. |
| Missing result configurations | Run summaries point to unavailable numbered producing configs. |
| Predictive provenance | Checked exports lack complete split, checkpoint-to-export, command, and copy lineage. |
| Ignored result archive | `final-results/` is ignored/untracked in the main repository; checksums exist but clean-checkout recovery is not assured. |
| LLM-assisted design | Prompt artifacts exist; exact settings and full accepted/rejected human decisions are incomplete. |
| Clinical validation | No prospective, independent clinical, or chart-review validation was performed. |
| Fairness and deployment | No subgroup fairness, safety, impact, or human-factors evaluation was performed. |

The table contains 17 body rows and is labeled `tab:discussion-limitations`.

## 36.9 Ethical Analysis

- **Misclassification:** rule and prediction errors can misstate clinical condition and bias downstream exposure contrasts, especially under differential measurement.
- **Automation bias:** users might mistake probabilities for diagnoses, rankings for clinical priorities, adjusted means for recommendations, or agreement for certainty.
- **Fairness:** no subgroup performance, calibration, support, effect-stability, or harm audit was performed; inclusion of demographics in adjustment is not fairness validation.
- **Data governance:** no institutional approval number, consent/waiver statement, ethics-board decision, data-use agreement, or retention wording was invented.
- **Deployment boundary:** the system is explicitly a retrospective research workflow and is not suitable for patient-level clinical deployment or treatment recommendation in its current form.
- **Open documentation gates:** institutional/data-governance wording; subgroup fairness and external clinical validation; clinical review of proxy definitions.

## 36.10 Numerical Claims

Result numerals were extracted manually and with `rg`; chapter, section, citation-key years, dataset-name years, and formatting constants were excluded.

| Value repeated in Chapter 11 | Population/denominator | Chapter 10 source | Verification |
| --- | --- | --- | --- |
| 9 positive MIMIC forest means | 9 original-cohort prespecified MIMIC exposures | Chapter 10 line 67 and primary table | exact |
| 9 positive and 1 negative PhysioNet forest means | 10 original-cohort prespecified PhysioNet exposures; shock negative | Chapter 10 line 105 and primary table | exact |
| 19/19 Forest--Linear directional agreement | all original-cohort dataset--exposure pairs | Chapter 10 line 194 | exact |
| 18/19 all-three directional agreement | all original-cohort Forest/Linear/PFN pairs | Chapter 10 line 237 and Figure 10 caption line 244 | exact |
| 14/15 matching--forest directional agreement | successful original-cohort matching rows | Chapter 10 line 189 | exact |
| 26,845 MIMIC records | original causal-analysis population | Chapter 10 lines 9 and 20 | exact |
| 7,993 PhysioNet records | original causal-analysis population | Chapter 10 lines 9 and 21 | exact |
| approximately 3.36 times larger | ratio of the preceding original causal-analysis populations | Chapter 10 lines 9 and 289 | exact as displayed |
| 55/57 preserved directions | matched original/downsampled estimator--dataset--exposure comparisons | Chapter 10 line 300 | exact |

The two PhysioNet sign changes are also stated in words in Chapter 11 and verified against Chapter 10 line 300.  No effect magnitude, p-value, interval, new aggregate, or result absent from Chapter 10 was introduced.

## 36.11 Placeholders and Deferred Fixes

Resolved generic Chapter 11 placeholder classes:

- two generic Stage 4 drafting placeholders
- two generic result placeholders
- two generic validation placeholders

Eight precise open gates retained/added in Chapter 11 and the placeholder log:

1. `[SUPERVISOR RATIFICATION REQUIRED: final causal-language and results hierarchy]`
2. `[CLINICAL REVIEW REQUIRED: proxy-state definitions and clinical interpretation]`
3. `[CITATION REQUIRED: primary CausalPFN method source]`
4. `[PROVENANCE REQUIRED: exact numbered causal configurations]`
5. `[PROVENANCE REQUIRED: predictive split and checkpoint-to-export lineage]`
6. `[PROVENANCE REQUIRED: exact producing commits and archive-copy history]`
7. `[ETHICS DOCUMENTATION REQUIRED: institutional approval and data-governance wording]`
8. `[VALIDATION REQUIRED: subgroup fairness and external clinical validation]`

Twelve Chapter-11 consolidation issues were added with the required fields:

- `DF-4.7-001` supervisor ratification
- `DF-4.7-002` clinical construct review
- `DF-4.7-003` CausalPFN literature
- `DF-4.7-004` exact causal configurations
- `DF-4.7-005` predictive lineage
- `DF-4.7-006` raw/processed, producer, and archive lineage
- `DF-4.7-007` overlap and balance
- `DF-4.7-008` intervention and target-trial definition
- `DF-4.7-009` subgroup fairness
- `DF-4.7-010` external/prospective validation
- `DF-4.7-011` LLM run/review manifest
- `DF-4.7-012` ethics and governance

## 36.12 Final Build

Final validation command:

```bash
cd thesis-writing/thesis
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

- Return status: 0.
- PDF path: `thesis-writing/thesis/main.pdf`.
- PDF: A4, 101 pages.
- Unresolved citations: 0.
- Unresolved references: 0.
- Duplicate labels: 0.
- Biber errors: 0.
- Fatal errors/emergency stops: 0.
- Layout warnings: 99 overfull and 1,087 underfull boxes thesis-wide.  Relative to the recorded baseline, Chapter 11 adds four small overfull boxes (maximum 8.91649 pt) and expected underfull wrapping in its long tables.  Spot checks of physical PDF pages 78, 83, and 88 confirmed the chapter opening and both tables remain within page bounds and readable.
- PDF conversion warnings: the existing two duplicate internal page-object warnings from front-matter page-label structure remain non-fatal.
- Post-validation `latexmk -c` removed auxiliary build files and retained the validated PDF.

Validation summary:

- exactly two Chapter 11 `section` commands
- all seven SRQs plus the main RQ answered explicitly
- `tab:discussion-rq-answers`: 8 body rows
- `tab:discussion-limitations`: 17 body rows
- all required hierarchy and agreement values match Chapter 10
- all causal/proxy-language matches reviewed and bounded
- unsupported LLM-claim scan: no occurrence
- `InterpNet|interpnet` scan over thesis TeX: no occurrence
- scope audit: no Stage 4.7 write outside allowed paths

## 36.13 Readiness

**READY WITH NON-BLOCKING WARNINGS**

Chapter 11 is drafted, evidence-bounded, structurally complete, and successfully built.  The remaining items are explicitly visible review, provenance, citation, validation, and ethics-documentation gates; they do not block beginning the separately authorized Stage 4.8, but they do block stronger clinical/causal language and final submission without review.
