# Stage 4.9A Evidence Report — Chapter 2: Background and Related Work

## 25.1 Git state

- Verified `HEAD` as `4fa3f4f` (`step 4.8`) on branch `main`; `git show -s` confirmed its parent is `12acb9a` (`step 4.7`).
- The initial worktree was dirty. Pre-existing changes were present in root documentation and requirements, the router and tests, a submodule, run output, literature metadata, checked result CSVs, and temporary scripts. None was reset, staged, committed, or discarded.
- Initial `git status --short` paths were: `README.md`, `SCRIPTS.md`, `causal-irregular-time-series`, `fix_preprocessor.py`, `prompt.txt`, `requirements-full.txt`, `requirements-router.txt`, `requirements.txt`, `router.py`, `runs/validate_demo/config/physionet_resolved_config.csv`, `tests/test_router.py`, `thesis-writing/important-md-copies/clinicause_root_project_overview.md`, `thesis-writing/important-md-copies/clinicause_root_router_usage.md`, `thesis-writing/important-md-copies/strats_project_overview.md`, `thesis-writing/literature/metadata/catalog.csv`, the pre-existing `thesis-writing/results/checked_*.csv` and `results_manifest.csv` changes, and `tmp_verify_router.py`.
- Stage-owned changes are limited to `thesis-writing/thesis/chapters/02_background_related_work.tex`, `thesis-writing/logs/unresolved_placeholders.md`, `thesis-writing/logs/deferred_fixes.md`, this report, and the regenerated `thesis-writing/thesis/main.pdf`.
- No earlier or later chapter, bibliography, literature corpus file, result, figure, code, configuration, planning file, or audit file was edited by Stage 4.9A. A before/after SHA-256 snapshot of all 43 literature-directory files was identical. The pre-existing catalog worktree modification remained byte-identical during this stage.
- No commit or push was performed.

## 25.2 Baseline build

From `thesis-writing/thesis`, ran `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf`. The baseline returned status 0 and produced a 107-page PDF. Biber completed and citations/references resolved. The baseline retained 99 overfull and 1,108 underfull box warnings documented by Stage 4.8; these were non-fatal and concentrated in existing tables and long entries.

## 25.3 Corpus validation

| Measure | Validated value | README comparison |
| --- | ---: | --- |
| Core catalog entries | 35 | matches |
| Optional catalog entries | 5 | matches |
| Usable local PDFs | 38 | matches |
| Literal PDF statuses | 29 `present`, 9 `downloaded` | both statuses resolve to valid local PDFs |
| Missing PDFs | 2 | matches |
| Core PDFs materially inspected | 32 | excludes the one historical, out-of-scope model PDF and the two missing PDFs |
| Optional PDFs inspected | 0 | optional material was unnecessary |

`sha256sum -c metadata/checksums.sha256` returned `OK` for all 38 local PDFs. The filesystem contains 33 core PDFs and 5 optional PDFs. No difference from the corpus README was found after normalizing `present` and `downloaded` as locally available.

## 25.4 Literature inspected

The table records every source cited in Chapter 2. “A/I/M/D” abbreviates abstract, introduction/background, methods or defining formulation, and discussion/limitations. PDF paths are relative to `thesis-writing/literature/`.

| Citation key | Tier | PDF path/status | Sections inspected | Claim supported | Usage limitation | Chapter 2 location |
| --- | --- | --- | --- | --- | --- | --- |
| `silva2012physionet` | core | `papers/dataset_physionet_challenge_silva_et_al_2012.pdf`; present | A/I, challenge design, data/task description | PhysioNet 2012 challenge role, early-ICU irregular records, mortality task | No claim that the local pipeline reproduces the challenge exactly | Critical-care EHR time series; PhysioNet 2012 |
| `johnson2016mimiciii` | core | `papers/dataset_mimiciii_johnson_et_al_2016.pdf`; present | A/I, database description, access/limitations | MIMIC-III as a broad relational critical-care database | No local cohort count or exact extraction claim | Critical-care EHR time series; MIMIC-III |
| `harutyunyan_2019_mimiciii_benchmark` | core | `papers/dataset_mimiciii_benchmark_harutyunyan_et_al_2019.pdf`; present | A/I/M, benchmark tasks and preprocessing, discussion | A reproducible benchmark view of MIMIC-III and task-specific extraction | Benchmark is one view, not the database or this thesis's exact pipeline | MIMIC-III and benchmark research |
| `sun_2026_review_irregular_medical_timeseries` | core | `papers/review_irregular_medical_timeseries_sun_et_al_2026.pdf`; present | A/I, taxonomy, missingness/irregularity sections, limitations | Irregular-series representation choices and observation-process concerns | Review used for taxonomy, not local performance or universal ranking | Critical-care EHR time series; representation challenges |
| `lipton_kale_wetzel_2016_missingness_rnns` | core | `papers/model_missingness_rnn_lipton_et_al_2016.pdf`; present | A/I/M, missingness experiments, discussion | Missingness patterns can be predictive and require explicit handling | Does not show that a local model handles missingness correctly | Critical-care EHR time series |
| `cho2014gru` | core | `papers/model_gru_cho_et_al_2014.pdf`; present | I/M, encoder--decoder and gated-unit formulation | Reset/update gates and recurrent hidden-state role | General sequence paper, not an ICU irregularity solution | Recurrent baselines; four-model table |
| `che2018grud` | core | `papers/model_grud_che_et_al_2018.pdf`; present | A/I/M, decay equations, clinical experiments, discussion | Masks, elapsed time, and learned input/hidden-state decay | Predictive missingness handling does not remove causal measurement bias | Recurrent baselines; four-model synthesis/table |
| `bai2018tcn` | core | `papers/model_tcn_bai_et_al_2018.pdf`; present | A/I/M, dilation/residual architecture, evaluation discussion | Causal dilated convolution, residual blocks, receptive field | General sequence comparison; local ICU input contract remains separate | TCN; four-model table |
| `tipirneni2022strats` | core | `papers/model_strats_tipirneni_reddy_2022.pdf`; present | A/I/M, triplet embeddings, pretraining, experiments/limitations | Sparse time--variable--value triplets, attention, self-supervised forecasting | Published method is distinguished from the local supervised multi-label adaptation | STraTS; four-model table |
| `banda_2018_electronic_phenotyping` | core | `papers/phenotyping_ehr_banda_et_al_2018.pdf`; present | A/I, rule/model taxonomy, validation discussion | Electronic-phenotyping sources and evolution from rules to learned methods | Does not validate the project's rule-derived proxy states | Electronic phenotyping |
| `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping` | core | `papers/phenotyping_respiratory_failure_essay_et_al_2020.pdf`; present | A/I/M, rule definition, validation/discussion | Example of transparent rule-based respiratory-failure cohort phenotyping | Example only; not imported as the local proxy definition | Electronic phenotyping; clinical definitions |
| `ratner_et_al_2020_snorkel` | core | `papers/phenotyping_weak_supervision_snorkel_ratner_et_al_2020.pdf`; downloaded | A/I/M, label model, applications, limitations | Programmatic labeling functions and learned source-dependency/accuracy aggregation | Project majority voting is explicitly not claimed to implement Snorkel | Weak supervision and label aggregation |
| `singer_2016_sepsis3` | core | `papers/clinical_sepsis3_singer_et_al_2016.pdf`; present | definition, operational criteria, limitations | Clinical consensus as conceptual grounding for sepsis-related constructs | Not evidence that project proxies are diagnoses or validated phenotypes | Clinical-definition sources |
| `kdigo_2012_acute_kidney_injury` | core | `papers/clinical_kdigo_acute_kidney_injury_2012.pdf`; downloaded | AKI definition/staging and relevant guideline context | Conceptual grounding for kidney-injury criteria | No claim of complete temporal/baseline-data implementation | Clinical-definition sources |
| `taylor_et_al_2001_isth_dic` | core | `papers/clinical_dic_isth_taylor_et_al_2001.pdf`; downloaded | definition/scoring proposal and discussion | Conceptual grounding for DIC scoring constructs | No claim that local variables reproduce formal scoring | Clinical-definition sources |
| `ranieri_et_al_2012_berlin_ards` | core | `papers/clinical_ards_berlin_definition_ranieri_et_al_2012.pdf`; missing | PDF unavailable; metadata only | Names the Berlin definition as a clinical reference point | No component, threshold, validation, or detailed method claim drawn from it | Clinical-definition sources |
| `vincent_et_al_1996_sofa` | core | `papers/clinical_sofa_vincent_et_al_1996.pdf`; missing | PDF unavailable; metadata only | Names SOFA as a clinical reference point | No score construction, threshold, or validation detail drawn from it | Clinical-definition sources |
| `hernan_robins_2016_target_trial` | core | `papers/causal_target_trial_emulation_hernan_robins_2016.pdf`; present | I, target-trial components, worked guidance, discussion | Eligibility, strategies, assignment, time zero, follow-up, outcome, contrast, analysis | Thesis does not claim complete target-trial emulation | Target-trial thinking |
| `hernan_taubman_2008_well_defined_interventions` | core | `papers/causal_well_defined_interventions_hernan_taubman_2008.pdf`; downloaded | I, consistency/intervention argument, examples/discussion | Need for sufficiently defined interventions and versions of treatment | Does not establish that proxy-state exposure is well defined | Target-trial thinking |
| `smit_2023_causal_inference_icu_scoping_review` | core | `papers/review_causal_inference_icu_smit_et_al_2023.pdf`; present | A/I, workflow/recommendations, ICU limitations | ICU-specific confounding, time-varying processes, reporting discipline | Review motivates boundaries; it does not validate this analysis | Observational causal questions |
| `pearl_1995_causal_diagrams` | core | `papers/causal_causal_diagrams_pearl_1995.pdf`; present | I, graphical criteria/backdoor material, examples | DAG paths, colliders, and adjustment-set reasoning | Does not validate project-specified arrows or exchangeability | DAGs and adjustment |
| `chernozhukov2018dml` | core | `papers/causal_double_machine_learning_chernozhukov_et_al_2018.pdf`; present | A/I, orthogonal scores, cross-fitting, theory/discussion | Orthogonality, nuisance estimation, cross-fitting, residualization | Does not prove local execution, identification, or lack of confounding | Double machine learning |
| `oprescu_et_al_2019_econml` | core | `papers/software_econml_oprescu_et_al_2019.pdf`; downloaded | A/I, library scope/API examples, discussion | Software context for heterogeneous-effect estimators | Library availability is not method execution or estimate validation | Double machine learning |
| `wager2018causalforest` | core | `papers/causal_causal_forest_wager_athey_2018.pdf`; present | A/I/M, assumptions, consistency/inference, discussion | Forest-based conditional-effect estimation and inference conditions | Does not validate local CATEs, subgroups, or clinical actionability | Causal forests and HTE |
| `athey2019grf` | core | `papers/causal_generalized_random_forests_athey_et_al_2019.pdf`; present | A/I/M, local moment framework, theory/applications | Adaptive neighborhoods and generalized random-forest framework | No local estimator-equivalence or performance claim | Causal forests and HTE |
| `bica_2021_individualized_treatment_effects_ehr_ml` | core | `papers/review_ite_ehr_ml_bica_et_al_2021.pdf`; present | A/I, challenge taxonomy, evaluation/validation discussion | Confounding, missingness, selection, shift, and counterfactual validation problems in EHR HTE | Review motivates caution, not local individual-effect validation | HTE in EHR and critical care |
| `lipkovich_2024_modern_hte_methods` | core | `papers/causal_hte_methods_lipkovich_et_al_2024.pdf`; present | A/I, method taxonomy, subgroup/validation discussion | HTE method landscape and exploratory-versus-confirmatory discipline | No claim that project subgroups are confirmed | HTE in EHR and critical care |
| `curth_2024_ml_individualized_treatment_effects` | core | `papers/review_ml_individualized_treatment_curth_et_al_2024.pdf`; present | A/I, evaluation challenges, opportunities/limitations | Individualized-effect estimation and validation difficulties | No clinical personalization claim for thesis outputs | HTE in EHR and critical care |
| `iwashyna_2015_hte_critical_care` | core | `papers/review_hte_critical_care_iwashyna_et_al_2015.pdf`; present | I, critical-care HTE examples, reporting implications | Difference between average effects, genuine effect heterogeneity, and spurious subgroups | Trial-oriented discussion used as caution, not evidence for local effects | HTE in EHR and critical care |
| `crump_et_al_2009_limited_overlap` | core | `papers/causal_limited_overlap_crump_et_al_2009.pdf`; downloaded | A/I/M, trimming/target population, discussion | Limited overlap, variance, extrapolation, and target-population consequences | Does not establish local positivity or prescribe an unreported trim | Overlap and empirical support |
| `cinelli_hazlett_2020_sensitivity` | core | `papers/sensitivity_omitted_variable_bias_cinelli_hazlett_2020.pdf`; downloaded | A/I/M, robustness values, benchmarking, discussion | Omitted-variable sensitivity and observed-covariate benchmarking | Robustness values do not prove absence of hidden confounding | Sensitivity workflows |
| `chernozhukov_et_al_2026_ovb_causal_ml` | core | `papers/sensitivity_ovb_causal_ml_chernozhukov_et_al_2026.pdf`; downloaded | A/I, bias bounds/inference, examples/limitations | Omitted-variable-bias sensitivity for causal ML targets | Recent method is used conceptually, not as proof of local robustness | Sensitivity workflows |
| `sharma_kiciman_2020_dowhy` | core | `papers/software_dowhy_sharma_kiciman_2020.pdf`; downloaded | A/I, model--identify--estimate--refute workflow, refuter examples | Diagnostic/refutation workflow and software context | Does not imply that every refuter was implemented or is a formal randomization test | Sensitivity and diagnostic workflows |

No web source was used. Detailed claims were based on the 32 inspected core PDFs; the two missing-PDF citations were restricted to naming clinical reference points.

## 25.5 Chapter structure

| Top-level section | Subsections | Approximate words |
| --- | ---: | ---: |
| ICU EHR Datasets and Irregular Sampling | 4 | 1,010 |
| Irregular Time-Series Representation Models | 6 | 1,040 |
| Proxy Phenotyping and Weak Supervision | 4 | 816 |
| Causal Diagrams, Identification, HTE, Overlap, and Sensitivity | 8 | 1,765 |

Chapter 2 has exactly four top-level sections and 22 subsections. `detex | wc -w` reports approximately 4,759 words overall; section-only counts differ slightly because the total also includes the chapter heading and cross-section material. The two tables are `tab:background-datasets` and `tab:background-model-families`. Figure count: 0. Transitions connect dataset properties to representations, representations to proxies, proxies to causal use, and the final synthesis to Chapter 3.

## 25.6 Dataset background

- PhysioNet sources: `silva2012physionet`, supported by `sun_2026_review_irregular_medical_timeseries` and `lipton_kale_wetzel_2016_missingness_rnns` for general irregularity/missingness context.
- MIMIC sources: `johnson2016mimiciii` for the database and `harutyunyan_2019_mimiciii_benchmark` for one benchmark extraction.
- Distinctions: bounded shared-task records versus a broad relational database; different source structure, era, variables, identifiers, measurement processes, preprocessing burden, and construct definitions; methodological portability rather than pooled populations.
- No cohort size, event count, variable count, prevalence, or thesis-specific dataset statistic was asserted. The text explicitly avoids claiming exact reproduction of an original benchmark or equivalence of similarly named variables/proxies.

## 25.7 Model background

| Family | Primary source | Core concept | Irregularity handling | Local-thesis relationship | Stated limitation |
| --- | --- | --- | --- | --- | --- |
| STraTS | `tipirneni2022strats` | triplet embeddings and transformer attention, with forecasting pretraining | directly represents observed time--variable--value events | sparse-event focal family; local multi-label heads/training/export are deferred to Chapter 5 | event selection, normalization, truncation, vocabulary, and local adaptation remain consequential |
| GRU | `cho2014gru` | reset/update-gated recurrent state | depends on the supplied prepared sequence | general recurrent baseline | ordinary GRU does not inherently resolve elapsed time or absence |
| GRU-D | `che2018grud` | recurrent state with learned decay | masks and elapsed-time features make missingness explicit | missingness-aware recurrent baseline | decay is structured, may be site-specific, and is not a causal correction |
| TCN | `bai2018tcn` | causal dilated convolution and residual blocks | operates on a defined regular sequence representation | convolutional baseline | canonical paper is not ICU-specific; binning/masks/aggregation remain local choices |


## 25.8 Proxy and weak-supervision background

- Phenotyping sources: `banda_2018_electronic_phenotyping` and `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping`.
- Clinical-definition sources: `singer_2016_sepsis3`, `kdigo_2012_acute_kidney_injury`, `taylor_et_al_2001_isth_dic`, plus the deliberately limited missing-PDF reference points `ranieri_et_al_2012_berlin_ards` and `vincent_et_al_1996_sofa`.
- Weak-supervision source: `ratner_et_al_2020_snorkel`.
- Learned weak supervision estimates source quality/dependency and aggregates probabilistically; the thesis uses deterministic majority voting over model-generated proxy labels. Chapter 2 expressly says the latter is not a learned Snorkel label model.
- Diagnosis-language boundary: project constructs are analytical proxy states, not chart-adjudicated diagnoses, validated phenotypes, clinical consensus, or ground truth. External definitions are conceptual anchors and do not validate the project rules.

## 25.9 Causal background

| Topic | Citations | Thesis boundary |
| --- | --- | --- |
| Target trial/intervention definition | `hernan_robins_2016_target_trial`, `hernan_taubman_2008_well_defined_interventions`, `smit_2023_causal_inference_icu_scoping_review` | No complete target-trial emulation or proof that a proxy exposure is a well-defined intervention |
| DAGs and adjustment | `pearl_1995_causal_diagrams` | Project-specified DAGs guide observed-variable adjustment; arrows, completeness, temporal order, and exchangeability are not validated |
| DML | `chernozhukov2018dml`, `oprescu_et_al_2019_econml` | Orthogonality/cross-fitting do not prove local execution, repair missing confounders, define exposure, or create support |
| Causal forests/GRF | `wager2018causalforest`, `athey2019grf` | Flexibility and inference theory do not validate local CATEs, subgroups, importance, transport, or clinical actionability |
| HTE in EHR/ICU | `bica_2021_individualized_treatment_effects_ehr_ml`, `lipkovich_2024_modern_hte_methods`, `curth_2024_ml_individualized_treatment_effects`, `iwashyna_2015_hte_critical_care` | Prognosis is separated from effect modification; the thesis remains exploratory and non-clinical |
| Overlap | `crump_et_al_2009_limited_overlap` | Global exposure mixture and matching summaries do not establish local common support or positivity |
| Sensitivity | `cinelli_hazlett_2020_sensitivity`, `chernozhukov_et_al_2026_ovb_causal_ml` | Sensitivity is model/scale dependent and cannot prove absence of unmeasured confounding |
| Diagnostic/refutation workflows | `sharma_kiciman_2020_dowhy` | Procedural context only; no claim that all DoWhy refuters were used or that every perturbation is a formal randomization test |

Identification is presented before estimation. No cited method is used to validate a project graph, local execution, estimate, or clinical recommendation.

## 25.10 CausalPFN

Chapter 2 mentions CausalPFN once, exactly as follows:

> The empirical study additionally evaluates CausalPFN in an exploratory role; its detailed theoretical positioning remains limited pending a verified primary method reference. No architecture or method-family claim is made here on the basis of its name or local output.

No technical description, superiority claim, or invented citation was added. Its exploratory role remains consistent with later chapters. The primary-source gap remains tracked in `unresolved_placeholders.md` and `DF-4.9A-001`.

## 25.11 InterpNet

`grep -Rni "InterpNet\|interpnet" thesis-writing/thesis --include='*.tex'` returned no matches. Chapter 2 contains no mention, and its five-row model table excludes the historical family. Historical corpus/catalog metadata was left unchanged.

## 25.12 Citation inventory

| Key | Uses | Role | Claim families supported | PDF status |
| --- | ---: | --- | --- | --- |
| `athey2019grf` | 1 | primary method | GRF/local-moment framework | present |
| `bai2018tcn` | 2 | primary method | TCN convolution/dilation/residual blocks | present |
| `banda_2018_electronic_phenotyping` | 1 | review | electronic-phenotyping taxonomy/validation | present |
| `bica_2021_individualized_treatment_effects_ehr_ml` | 1 | review | EHR individualized-effect challenges | present |
| `che2018grud` | 3 | primary method | GRU-D masks, gaps, decay | present |
| `chernozhukov2018dml` | 1 | primary method | DML orthogonality/cross-fitting | present |
| `chernozhukov_et_al_2026_ovb_causal_ml` | 1 | primary method | OVB sensitivity for causal ML | downloaded |
| `cho2014gru` | 2 | primary method | GRU gating | present |
| `cinelli_hazlett_2020_sensitivity` | 1 | primary method | robustness values/benchmarking | downloaded |
| `crump_et_al_2009_limited_overlap` | 1 | primary method | limited overlap and target population | downloaded |
| `curth_2024_ml_individualized_treatment_effects` | 1 | review | individualized-effect evaluation | present |
| `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping` | 1 | primary application | rule-based EHR phenotyping example | present |
| `harutyunyan_2019_mimiciii_benchmark` | 1 | primary dataset/benchmark | MIMIC-III benchmark extraction/tasks | present |
| `hernan_robins_2016_target_trial` | 1 | primary methodological | target-trial specification | present |
| `hernan_taubman_2008_well_defined_interventions` | 1 | primary methodological | intervention versions/consistency | downloaded |
| `iwashyna_2015_hte_critical_care` | 1 | review/perspective | critical-care HTE interpretation | present |
| `johnson2016mimiciii` | 1 | primary dataset | MIMIC-III structure and scope | present |
| `kdigo_2012_acute_kidney_injury` | 1 | clinical guideline | AKI conceptual definition | downloaded |
| `lipkovich_2024_modern_hte_methods` | 1 | review | HTE methods and exploratory discipline | present |
| `lipton_kale_wetzel_2016_missingness_rnns` | 1 | primary method | informative missingness in clinical RNNs | present |
| `oprescu_et_al_2019_econml` | 1 | primary software | EconML implementation context | downloaded |
| `pearl_1995_causal_diagrams` | 1 | primary method | DAG/backdoor/collider reasoning | present |
| `ranieri_et_al_2012_berlin_ards` | 1 | clinical definition | ARDS reference point only | missing |
| `ratner_et_al_2020_snorkel` | 1 | primary system/method | learned weak-supervision aggregation | downloaded |
| `sharma_kiciman_2020_dowhy` | 1 | primary software/method | model--identify--estimate--refute workflow | downloaded |
| `silva2012physionet` | 1 | primary dataset | PhysioNet 2012 challenge/data role | present |
| `singer_2016_sepsis3` | 1 | clinical consensus | sepsis conceptual definition | present |
| `smit_2023_causal_inference_icu_scoping_review` | 1 | review | ICU observational-causal workflow/limitations | present |
| `sun_2026_review_irregular_medical_timeseries` | 2 | review | irregular-series taxonomy and limitations | present |
| `taylor_et_al_2001_isth_dic` | 1 | clinical definition | DIC score reference point | downloaded |
| `tipirneni2022strats` | 2 | primary method | STraTS triplets/attention/pretraining | present |
| `vincent_et_al_1996_sofa` | 1 | primary clinical score | SOFA reference point only | missing |
| `wager2018causalforest` | 1 | primary method | causal forests/conditional effects | present |

Totals: 34 unique keys, 36 citation commands, and 41 key uses. Every key exists exactly once in `references.bib` and has exactly one catalog row. Citations remain adjacent to the claims they support.

## 25.13 Results-boundary validation

The thesis-specific design statements in Chapter 2 are:

1. The study uses PhysioNet 2012 and MIMIC-III as separate methodological settings, not as a pooled population.
3. Published model forms are precedents; local preprocessing, targets, heads, training, and exports are defined later.
4. Project rules produce analytical proxy states; model outputs are predicted proxy labels; deterministic voting aggregates them.
5. Project-specified, dataset-specific DAGs guide observed-variable adjustment.
6. CausalPFN is exploratory and lacks a verified primary method citation.
7. The thesis integrates irregular-series prediction, proxy-state construction, DAG-guided estimation, and diagnostics through an evidence-tracked interface.
8. LLM prompts contributed candidate proxy-state and DAG design provenance only; they were not an executed estimator, discovery method, expert, or source of validation.
9. Chapters 3--9 contain the actual study objects, implementation, assumptions, and diagnostic hierarchy.

The result-term scan (`AUROC`, `AUPRC`, `minRP`, agreement counts, cohort counts, effect values, matching pairs, and downsampled result) returned no Chapter 2 matches. No thesis-specific numerical result, local model ranking, effect estimate, direction, significance claim, or clinical recommendation appears.

## 25.14 Placeholders and deferred fixes

- Removed six generic Chapter 2 placeholders: four `[STAGE 4 DRAFT REQUIRED]`, one `[VALIDATION REQUIRED]`, and one `[CITATION REQUIRED]`.
- Retained precise gates for a primary CausalPFN source; clinical review of proxy definitions; literature-rule family coverage; the LLM-literature decision; and supervisor ratification of related-work framing.
- Added `DF-4.9A-001` through `DF-4.9A-010`: CausalPFN primary source, clinical proxy source coverage, LLM literature decision, Chapter 1/2 overlap, Chapter 2/6 overlap, Chapter 2/7 overlap, historical excluded-model metadata, core-versus-optional classification, two missing PDFs, and the Stage 4.9B whole-thesis citation/bibliography audit.
- Chapter 2 now contains zero generic placeholder markers.

## 25.15 Final build

Ran exactly from `thesis-writing/thesis`:

```bash
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

Return status: 0. Output: `thesis-writing/thesis/main.pdf`, 119 A4 pages, 2,821,468 bytes at validation time, SHA-256 `7dc5a07b9b624f2ba7d8cc76110f75c44265e97b71b5e4ac74d247db3e154263`.

Final validation: 0 unresolved citations, 0 unresolved references, 0 duplicate labels (112 labels/112 unique), 0 Biber errors or warnings, and 0 fatal LaTeX errors. Bibliography generation succeeded with all 34 Chapter 2 keys.

Layout warnings: 99 overfull and 1,149 underfull boxes thesis-wide. Chapter 2 contributes 0 overfull and 41 underfull boxes; its underfull warnings arise from intentionally narrow `p{}` cells in the two synthesis tables. The baseline already had 99 overfull and 1,108 underfull boxes, so Chapter 2 did not increase the overfull count. The PDF was generated successfully and the warnings are non-blocking.

## 25.16 Readiness

**READY WITH NON-BLOCKING WARNINGS**

Stage 4.9A satisfies the structural, source, method-boundary, placeholder, citation, scope, and build requirements. Remaining gates are explicit in the tracking logs. No experiment, web research, literature download, corpus/bibliography edit, commit, push, or Stage 4.9B work occurred.
