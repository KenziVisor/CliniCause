# CliniCause AAAI-27 paper evidence map

Status: P0/P0A/P2 baseline plus P3--P6 manuscript claim activation, 2026-07-19

Scope: evidence control for the AAAI-27 manuscript; this file is not manuscript prose.
Canonical plan: `clinicause_aaai27_paper_operational_plan_v1.1.md`, Version 1.1.

## 1. Frozen repository baseline

| Item | Frozen value |
|---|---|
| Parent branch | `main` |
| Parent HEAD | `c335d327b3ca63045d362f180518a2bfa7005e6e` (`fix update router behavior`) |
| Full-run pointer commit | `d3195458` (`Complete run pipeline`); it advances both nested repository pointers but does not archive a root run manifest |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060`, clean detached worktree |
| Causal repository revision | `379ed9b75107b52007957ba5908e507b719c9247`, clean detached worktree |
| Thesis-source baseline | `8e33390a03076282214b0120191cfdd3fcfbcfbd` |
| Checked-results baseline | `9e6ada4616b8696139e6309b04672539768a2578` (format-only latest touch; scientific provenance remains that recorded by the results packet) |
| Reproducibility-package baseline | `d77fada7b63c2b0b37746302fcda1c6351fa3e9b` |
| Author-kit baseline | `26b639cf3da6551e0e2aee388c8b2bfd7368d238` |
| Working-tree exceptions present before this task | modified `prompt.txt`; untracked `clinicause_debug_operational_plan.md`; untracked canonical operational plan |
| Runtime check | `pytest -q` could not start because `pytest` is not installed; no runtime pass is inferred |

The baseline is intentionally descriptive. The current root and nested revisions must not be attributed retroactively as the revisions that produced the archived results.

### P3 stage baseline

| Item | P3 value |
|---|---|
| Task baseline / current HEAD before work | `884ff8e4d112ff732e43a6aea33ab9bddcf8ed5e` (`AAAI skeleton`) |
| Branch | `main` |
| Pre-existing dirty path | modified `prompt.txt` only; preserved and excluded from P3 edits/staging |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal repository revision | `379ed9b75107b52007957ba5908e507b719c9247` |
| Runtime-validation attempt | `python` unavailable; `python3 -m pytest` unavailable because the `pytest` module is not installed. No current test-pass claim is made. |

### P4 stage baseline

| Item | P4 value |
|---|---|
| Current HEAD before work | `14337a293eee03a24216c299c312ad5c7d61b3a7` (`AAAI P3`) |
| Branch | `main` |
| Last two commits inspected | `14337a2` (`AAAI P3`): prompt plus tracked LaTeX auxiliaries; `a851e38` (`docs: record P3 commit evidence`): P3 report only |
| Accepted P3 content commit | `60504040c86721782e6fdf8a29971c8b1e0ab9e4` (`paper: draft dataset construction and validation`) |
| Worktree before P4 | Modified `prompt.txt` only; pre-existing user work, protected and non-overlapping |
| Manuscript changes after P3 content commit | None. Later commits changed the P3 report, `prompt.txt`, and tracked build auxiliaries, but not `paper.tex`, `paper_evidence_map.md`, or `paper_build_report.md` |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal repository revision | `379ed9b75107b52007957ba5908e507b719c9247` |
| Repository policy | User explicitly deferred cleanup; tracked auxiliaries are preserved and may be regenerated, never deleted |

### P5 stage baseline

| Item | P5 value |
|---|---|
| Current HEAD before work | `b604d68fdf85aa278d80c3f8916c9fd1ef837bcc` (`AAAI p4`) |
| Branch | `main` |
| Last two commits inspected | `b604d68` (`AAAI p4`) and `14337a2` (`AAAI P3`) |
| Accepted P4 commit | `b604d68fdf85aa278d80c3f8916c9fd1ef837bcc` |
| Worktree before P5 | Modified `prompt.txt` only; protected user work with no overlap with permitted P5 paths |
| STraTS revision | `c37cf381b971af4a4a29ef09b93884a4afe61060` |
| Causal repository revision | `379ed9b75107b52007957ba5908e507b719c9247` |
| P5 numerical authority | Checked result CSVs under `thesis-writing/results/`; prompt values were not used as evidence |
| Figure 2 selection | Original sampling only; estimator-specific main-text selection statuses; exactly 19 combinations and three estimators required |

### P6 stage baseline

| Item | P6 value |
|---|---|
| Current HEAD before work | `47f487c84a92f0a0b6a8271b370ff9d7afcace23` (`AAAI P5`) |
| Branch | `main` |
| Last commits inspected | `47f487c` (`AAAI P5`), `b604d68` (`AAAI p4`), `14337a2` (`AAAI P3`), `a851e38` (`docs: record P3 commit evidence`), `6050404` (`paper: draft dataset construction and validation`), and `884ff8e` (`AAAI skeleton`) |
| Accepted P5 commit | `47f487c84a92f0a0b6a8271b370ff9d7afcace23` |
| Worktree before P6 | Modified `prompt.txt` and untracked Version 1.1 operational plan; both pre-existing, protected, and non-overlapping with permitted P6 edits |
| Canonical plan | `thesis-writing/paper-aaai/clinicause_aaai27_paper_operational_plan_v1.1.md`; Version 1.1; SHA-256 `8df13e88892da8cd0d78df33e0b7a997983d95f99222de0eb9605426e905b1c1` |
| Workflow followed | Revised consolidated P6--P10 sequence; P6 combines Discussion, Limitations, future-work priorities, and Conclusion |

### Evidence-packet hashes

| File | SHA-256 |
|---|---|
| `results/results_source_packet.md` | `1209cd85c04dae9a562f8db710a0f6bbb19db82db29e85aafeecb82298eb36e8` |
| `results/results_manifest.csv` | `b91815f835a0a16773db067fc6747fe590435e4ded32ab54fe9dace2255536dc` |
| `results/results_checksums.sha256` | `40696a1aa3492721fa1e311b3c6dce843a5de637efd7cf72d32bff28c302a7c1` |
| `results/checked_predictive_metrics.csv` | `506f9367f7af0946a9adb77970ae78a8a0e8578fce64a5c4a5cd3ec519ad601c` |
| `results/checked_cate_candidates.csv` | `2f550cf95e2acb9c1c7febf74735f0b36dfc2bd8592baf8e3d6dab5459252bff` |
| `results/checked_cohort_candidates.csv` | `872c0516ad7fbd8c2ef7e1e7d88fdeb6bb362f1b57c8796cc68d7742df4277cb` |
| `reproducibility/provenance_gaps.csv` | `4924691293d5a7c80a5c856b0dde19cd7edc90305ee15f76fcd5058a581b0f4e` |
| `literature/metadata/references.bib` | `8ffcee89e8d3ff617d88725ca4625c55d84d53bc6aa5cffdda5525fe26b3fb0e` |
| Canonical Version 1.1 operational plan | `8df13e88892da8cd0d78df33e0b7a997983d95f99222de0eb9605426e905b1c1` |

### Author-kit hashes

| File | SHA-256 |
|---|---|
| `AnonymousSubmission2027.tex` | `035ebdb17e57885a1fd43a188fd17777bdbf90f1fda1a1e000c49c7f52ce1f9d` |
| `AnonymousSubmission2027.pdf` | `ad424e5a94ce98da7cb10ed07b12ef20571e72f649b7c2b30e6af0f234a0c96a` |
| `CameraReady2027.tex` | `db509cb393dae5c113bf29633e17d31a5fefa610aad09056569034f9bcff5b46` |
| `CameraReady2027.pdf` | `cfa0a7e59c31fcb39c2bbd492673eb969afc269fb0e568b5c692ac3a53f1fef5` |
| `ReproducibilityChecklist.tex` | `06a3459158089bf1c64b738986118f1d1566e816da4b710c6397561e33c3d5e6` |
| `ReproducibilityChecklist.pdf` | `7fcc703769036e3566daccd59560aaca9b187f49da79fc9d1e13155b61e7dd9e` |
| `aaai2027.sty` | `391bce82815bf698b8e382dd3ae7e30c75d7ab46df140cb295b1266016bc8623` |
| `aaai2027.bst` | `5db7765ba99de5c1e4686f9b3940a0add9c5e702f2164514462bec130ccb6e3c` |
| `aaai2027.bib` | `ff8a860f20602b2645723856b80f0a0ad28ee7ec270158254400fdb80b429e45` |

## 2. Evidence authority and inspected sources

Use sources in this order when facts differ:

1. Checked CSVs plus their manifests/checksums for numerical claims.
2. `results_source_packet.md` and `results_decision_register.md` for selection and interpretation rules.
3. Reproducibility tables for recorded lineage and explicit provenance gaps.
4. Thesis chapters for definitions, motivation, method descriptions, and already-bounded interpretation.
5. Current implementation/tests only for statements about the current validation contract, never historical production provenance.
6. `final-results` only as the historical archive described by its local guidance.
7. The canonical operational plan for paper strategy and scope, not as numerical evidence.

### Primary repository sources

| Topic | Authoritative source(s) | Permitted use |
|---|---|---|
| Study framing and contributions | `thesis/chapters/01_introduction.tex`, `03_problem_definition_study_design.tex`, `11_discussion.tex`, `12_conclusions_future_work.tex` | Condense after human approval; keep observational/associational limits |
| Background and related work | `thesis/chapters/02_background_related_work.tex`, `literature/metadata/references.bib` | Cite only entries present and verified in the approved bibliography |
| Cohort/preprocessing | `thesis/chapters/04_data_preprocessing.tex`, checked cohort/export files | Definitions and checked analysis-record counts |
| Proxy construction | `thesis/chapters/05_proxy_state_construction.tex`, checked proxy files | One-rule/four-source proxy design and checked descriptive analyses |
| Predictive modeling | `thesis/chapters/06_predictive_modeling.tex`, `checked_predictive_metrics.csv`, `checked_predictive_exports.csv` | Archived performance only; one archived run per model/dataset |
| Causal methods | `thesis/chapters/07_causal_methodology.tex`, checked CATE/matching/heterogeneity files | Estimands, estimator roles, and checked estimates with qualifications |
| Validation | `thesis/chapters/08_robustness_sensitivity_validation.tex`, checked sensitivity/permutation files | Archived validation coverage; no claim that every current test was rerun |
| Results | `thesis/chapters/10_results.tex`, checked CSVs, results source packet | Values and bounded synthesis |
| Current contract | `causal-irregular-time-series/run/router.py`, `causal-irregular-time-series/tests/test_router_contracts.py` | Static implementation/test evidence only until runtime is restored |
| Provenance | `reproducibility/*.csv`, `reproducibility/README.md`, `results/results_manifest.*` | Explicitly report both recorded lineage and missing fields |

## 3. Protected numerical baseline

All values below are transcriptions or deterministic summaries of checked files. They are protected: manuscript edits may shorten presentation but must not silently change the values, denominators, estimator sets, sampling condition, or interpretation.

### Core facts

| Fact ID | Checked fact | Source and qualification |
|---|---|---|
| N01 | Majority-vote causal analysis records: MIMIC-III `26,845`; PhysioNet 2012 `7,993` | `checked_cohort_candidates.csv`; analysis records, not raw database cohort sizes |
| N02 | Original-sampling exposures: MIMIC-III `9`; PhysioNet 2012 `10` | Unique exposure rows in `checked_cate_candidates.csv`; chronic baseline is not counted as an exposure |
| N03 | Original-sampling estimator-exposure rows: `57` | 19 dataset-exposure combinations × three estimators |
| N04 | The two DML estimators agree in direction for `19/19` original-sampling dataset-exposure combinations | Sign comparison in `checked_cate_candidates.csv` |
| N05 | All three estimators agree in direction for `18/19`; the exception is PhysioNet shock | ForestDML and LinearDML are negative; CausalPFN is positive for that row |
| N06 | Original vs outcome-downsampled sign agreement is `55/57` | Exceptions: PhysioNet LinearDML coagulation and PhysioNet CausalPFN shock |
| N07 | MIMIC-III archived predictive leader is STraTS on all four reported test metrics | Single selected archived run per model; no significance or universal-superiority claim |
| N08 | PhysioNet 2012 archived predictive leader is GRU-D on all four reported test metrics | Same qualification |
| N09 | Predictive source aggregation uses one proxy rule and four predictive model sources | Thesis/results packet and checked exports; do not imply ensemble training |
| N10 | DML sensitivity coverage reported in the archive is 8/9 MIMIC-III and 7/10 PhysioNet exposures; CausalPFN is skipped | Checked sensitivity candidates plus source packet; distinguish skipped from failed |
| N11 | Permutation diagnostics use 10 trials with seed 42 for represented DML dataset/exposure/sampling combinations; CausalPFN is skipped | Checked permutation candidates/source packet; not a universal randomization proof |

### Archived predictive test metrics

Selection is `PRIMARY_MAIN_TEXT`. Lower loss is better; higher AUROC, AUPRC, and min-recall/precision are better. Values describe the checked archive only.

| Dataset | Model | Loss | AUROC | AUPRC | Min(R,P) |
|---|---:|---:|---:|---:|---:|
| MIMIC-III | GRU | 0.385757 | 0.881119 | 0.839559 | 0.770421 |
| MIMIC-III | GRU-D | 0.404448 | 0.884277 | 0.841273 | 0.772533 |
| MIMIC-III | STraTS | 0.348136 | 0.905411 | 0.869417 | 0.795399 |
| MIMIC-III | TCN | 0.414456 | 0.866914 | 0.822642 | 0.757798 |
| PhysioNet 2012 | GRU | 0.396819 | 0.914616 | 0.897493 | 0.831044 |
| PhysioNet 2012 | GRU-D | 0.330593 | 0.918478 | 0.905105 | 0.834958 |
| PhysioNet 2012 | STraTS | 0.340692 | 0.914761 | 0.877456 | 0.818228 |
| PhysioNet 2012 | TCN | 0.476513 | 0.899103 | 0.875091 | 0.811184 |

### Original-sampling mean model-estimated CATE matrix

These are model-estimated conditional average treatment effects under the archive's proxy-exposure design. They are not randomized treatment effects, clinical recommendations, or intervention guarantees. `n` is 26,845 for every MIMIC-III model row and 7,993 for every PhysioNet model row.

| Dataset | Exposure | ForestDML | LinearDML | CausalPFN |
|---|---|---:|---:|---:|
| MIMIC-III | Cardiac | 0.220356 | 0.187634 | 0.259327 |
| MIMIC-III | Global | 0.062101 | 0.080153 | 0.073050 |
| MIMIC-III | Hepatic/coagulation | 0.097598 | 0.083017 | 0.096846 |
| MIMIC-III | Inflammation/sepsis | 0.161179 | 0.161334 | 0.148544 |
| MIMIC-III | Metabolic | 0.019743 | 0.017989 | 0.031323 |
| MIMIC-III | Neurologic | 0.034253 | 0.031550 | 0.034993 |
| MIMIC-III | Renal | 0.091290 | 0.088595 | 0.086972 |
| MIMIC-III | Respiratory | 0.036133 | 0.039098 | 0.049766 |
| MIMIC-III | Shock | 0.020994 | 0.021246 | 0.031645 |
| PhysioNet 2012 | Cardiac | 0.111831 | 0.122033 | 0.119413 |
| PhysioNet 2012 | Coagulation | 0.010794 | 0.004136 | 0.025428 |
| PhysioNet 2012 | Global | 0.107988 | 0.106740 | 0.105039 |
| PhysioNet 2012 | Hepatic | 0.090527 | 0.060184 | 0.106843 |
| PhysioNet 2012 | Inflammation | 0.071800 | 0.070872 | 0.067480 |
| PhysioNet 2012 | Metabolic | 0.077704 | 0.079738 | 0.090734 |
| PhysioNet 2012 | Neurologic | 0.081636 | 0.075728 | 0.077049 |
| PhysioNet 2012 | Renal | 0.120027 | 0.090622 | 0.110669 |
| PhysioNet 2012 | Respiratory | 0.064750 | 0.062660 | 0.062984 |
| PhysioNet 2012 | Shock | -0.013849 | -0.026944 | 0.004122 |

Full precision remains in `checked_cate_candidates.csv`. The paper table should display rounded values while calculations and sign checks use the checked precision.

## 4. Result-family evidence register

| Family | Checked source | Main-paper role | Mandatory qualification |
|---|---|---|---|
| Cohort flow | `checked_cohort_candidates.csv`, `checked_predictive_exports.csv` | Source-cohort and analysis-record accounting | Do not call analysis records unique raw patients without confirming the unit |
| Proxy prevalence/co-occurrence | `checked_proxy_prevalence.csv`, `checked_proxy_cooccurrence.csv` | Descriptive proxy behavior | Proxy labels are model-derived constructs, not adjudicated diagnoses |
| Proxy/mortality association | `checked_proxy_mortality_association.csv` | Descriptive validation | Association is not causal validity |
| Predictive metrics | `checked_predictive_metrics.csv` | Compact archived benchmark | One selected archived run; no uncertainty or significance available |
| Predictive exports | `checked_predictive_exports.csv` | Aggregation/input accounting | Exact split/checkpoint lineage is incomplete |
| Original CATE | `checked_cate_candidates.csv` | Central cross-estimator result | Observational, proxy-based, model-estimated effects |
| Matching | `checked_matching_results.csv`, `checked_matching_failures.csv` | Support/overlap diagnostic | Treat four exposure-specific failures per sampling-condition pair as warnings, not absent evidence; three successful original rows carry insufficient-support flags |
| Sensitivity | `checked_sensitivity_candidates.csv` | DML robustness | Partial coverage; CausalPFN skipped |
| Permutations | `checked_permutation_candidates.csv` | DML falsification diagnostic | 10 trials, seed 42; CausalPFN skipped |
| Heterogeneity | `checked_heterogeneity_candidates.csv` | Supplementary/exploratory | Avoid subgroup clinical recommendations |
| Figures | `checked_figure_candidates.csv`, `figure_selection_register.md` | Provenance for selected visuals | Rebuild paper visuals from checked data or clearly identify thesis-rendered reuse |

## 5. Claim-to-evidence lock

Statuses: **LOCKED** may be drafted with its qualification; **GATED** needs the named gate; **HUMAN** needs author/supervisor judgment. “Location” is the intended paper section.

| Claim ID | Candidate claim/function | Role | Location | Evidence source | Support | Confidence | Required qualification | Planned visual | Gate | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | CliniCause is an end-to-end resource/pipeline connecting irregular ICU data, proxy construction, prediction, and causal estimation | Headline framing | Abstract/Introduction | Thesis Chs. 1, 3–8; current repository layout | Design + implementation | High | Do not imply prospective deployment or randomized identification | Fig. 1 | Human wording review | HUMAN |
| C02 | Evaluation spans MIMIC-III and PhysioNet 2012 | Scope | Abstract/Intro | Thesis Chs. 3–4; checked cohort file | Dataset records | High | Use approved dataset names/citations | Fig. 1/Table 1 | None | LOCKED |
| C03 | Majority-vote causal analyses contain 26,845 and 7,993 analysis records | Quantitative scope | Source Cohorts | `checked_cohort_candidates.csv` | Checked numerical | High | Analysis records, not raw cohort sizes | Table 1 | None | LOCKED |
| C04 | The proxy layer combines one rule source with four predictive model sources | Method summary | Proxy Construction | Thesis Chs. 5–6; results packet | Recorded design | High | Do not call it a trained ensemble | Fig. 1 | None | LOCKED |
| C05 | Four predictive architectures are represented | Method scope | Proxy Construction/Evaluation | `checked_predictive_metrics.csv` | Checked archive | High | Archived selected runs only | Table 1 | None | LOCKED |
| C06 | STraTS is the checked MIMIC-III leader on all four reported metrics | Result | Predictive Results | `checked_predictive_metrics.csv` | Checked numerical | High | “Archived leader”; no significance/superiority claim | Table 1 | None | LOCKED |
| C07 | GRU-D is the checked PhysioNet leader on all four reported metrics | Result | Predictive Results | Same | Checked numerical | High | Same qualification | Table 1 | None | LOCKED |
| C08 | Causal evaluation contains 9 MIMIC-III and 10 PhysioNet proxy exposures | Scope | Causal Estimation | `checked_cate_candidates.csv` | Checked numerical | High | Chronic baseline excluded | Fig. 2/Table 2 | None | LOCKED |
| C09 | Original-sampling results contain 57 estimator-exposure rows | Scope | Evaluation | Same | Deterministic count | High | 19 combinations × three estimators | Table 2 | None | LOCKED |
| C10 | ForestDML and LinearDML agree in direction in 19/19 combinations | Central result | Causal Results | Same | Deterministic sign summary | High | Directional agreement is not causal truth or significance | Fig. 2/Table 2 | None | LOCKED |
| C11 | All three estimators agree in 18/19 combinations | Central result | Abstract/Causal Results | Same | Deterministic sign summary | High | Name the PhysioNet-shock exception | Fig. 2/Table 2 | None | LOCKED |
| C12 | PhysioNet shock is negative for both DML estimators and positive for CausalPFN | Exception | Causal Results | Same | Checked numerical | High | Values are near zero and estimator-specific | Table 2 | None | LOCKED |
| C13 | Original vs outcome-downsampled direction agrees in 55/57 estimator-exposure rows | Robustness | Validation/Results | `checked_cate_candidates.csv` | Deterministic sign summary | High | Name both exceptions; do not call this invariance | Table 2 or supplement | None | LOCKED |
| C14 | DML sensitivity coverage is partial (8/9 and 7/10) | Limitation/robustness | Validation | `checked_sensitivity_candidates.csv` | Checked diagnostic | High | Distinguish failure/missing from skip; CausalPFN skipped | Supplement | None | LOCKED |
| C15 | DML permutation diagnostics use 10 trials and seed 42 | Validation detail | Validation | `checked_permutation_candidates.csv` | Checked diagnostic | High | Limited trial count; CausalPFN skipped | Supplement | None | LOCKED |
| C16 | Matching provides support diagnostics with recorded failures/insufficient-support flags | Validation detail | Validation | Matching checked files | Checked diagnostic | High | Do not turn diagnostic success into effect confirmation | Supplement | None | LOCKED |
| C17 | Current routing code enforces canonical IDs, cohort equality, schema/probability validation, hashes, manifests, receipts, derived seeds, and dataset isolation | Current implementation | Sec. 3.5 Dataset Validation and Provenance | `router.py`; `tests/test_router_contracts.py`; relevant STraTS source/tests | Static code/test inspection | Medium | Say “current contract implements/tests”; runtime not verified in this environment; never attribute it retroactively to archived production | Fig. 1/supplement | G-RUN-01 only for test-pass wording | SUPPORTED WITH QUALIFICATION |
| C18 | Archived results are exactly reproducible from complete producing revisions/configurations | Reproducibility | Validation/checklist | Reproducibility CSVs | Explicitly incomplete | Low | Claim is prohibited until missing lineage is recovered | None | G-EVD-02 | GATED |
| C19 | CausalPFN supplies a complementary third estimator family | Contribution/method | Intro/Causal Estimation | Checked results; thesis method text | Empirical + secondary description | Medium | Primary method citation is missing; avoid novelty/theory claims | Fig. 2 | G-EVD-01 | GATED |
| C20 | Code/data/resources are publicly available at submission | Release claim | Discussion/checklist | No anonymized release artifact currently evidenced | None | Low | No URL, license, or release package may be invented | None | G-REL-01 | GATED |
| C21 | The evaluation demonstrates clinical effectiveness, treatment benefit, or deployability | Prohibited overclaim | Nowhere | No prospective/randomized evidence | Unsupported | None | Must not appear | None | Permanent | GATED |
| C22 | Cross-estimator directional concordance is evidence of stability within this archived observational design | Interpretation | Discussion | C10–C16 | Triangulated checked results | Medium | Pair with exception, partial validation coverage, and proxy/confounding limitations | Fig. 2 | Human wording review | HUMAN |
| C23 | The main contribution is a validated reusable benchmark/resource rather than a new causal estimator | Positioning | Intro/Discussion | Repository/thesis/plan | Design judgment | Medium | Authors must ratify novelty framing | Fig. 1 | G-HUM-01 | HUMAN |
| C24 | Predictive and causal stages used exact recorded splits/checkpoints from a fully linked manifest | Reproducibility | Evaluation/checklist | `predictive_run_lineage.csv`, `provenance_gaps.csv` | Incomplete | Low | Prohibited until split/checkpoint linkage is recovered | None | G-EVD-02 | GATED |
| C25 | All checked numerical claims trace to manifest/checksum-controlled files | Evidence control | Checklist/supplement | results packet, manifest, checksums | Archived integrity record | High | Integrity of available files is not complete production lineage | None | None | LOCKED |

### P3 manuscript claim register

P3 uses the status vocabulary requested for manuscript drafting: **SUPPORTED**, **SUPPORTED WITH QUALIFICATION**, **GATED**, and **EXCLUDED**. Existing `LOCKED` claims remain supported under their recorded qualification; existing permanent-prohibition claims remain excluded from manuscript prose.

| Claim ID | Manuscript claim/function | Exact manuscript location | Highest-authority source | Status | Required qualification / TODO |
|---|---|---|---|---|---|
| C26 | One analysis row represents a source time-series record or ICU stay, keyed by canonical `ts_id`, and is not assumed to be a unique person | Sec. 3.1, paragraph 1 | Thesis Ch. 3, `Units, Time Horizons, and Data Objects`; active preprocessing/data contracts | SUPPORTED | Preserve analysis-record wording; do not infer patient uniqueness |
| C27 | Irregular events retain elapsed time, variable identity, and value; record-level data supply in-hospital mortality and available source-specific baseline covariates | Sec. 3.1, paragraph 1 | Thesis Chs. 3--4; active preprocessing contracts | SUPPORTED | No unverified raw cohort size or historical temporal-window claim |
| C28 | The common interface preserves dataset-specific covariates, proxy ontologies, measurement processes, and DAGs; resources/results remain separate rather than pooled | Sec. 3 opening and Sec. 3.1, paragraph 2 | `results_decision_register.md`; thesis Chs. 4, 5, 7, and 11 | SUPPORTED | Portability is at the workflow/interface level, not construct equivalence |
| C29 | A structured design-time LLM protocol proposed ontologies, rule families, missingness considerations, and DAGs; project-selected proposals were encoded in deterministic source, and no runtime patient-level LLM was used | Sec. 3.2, paragraph 1; Fig. 1 specification | Thesis Chs. 3 and 5; `audit/llm_prompt_provenance_audit.md`; active tagger/graph source | SUPPORTED WITH QUALIFICATION | Do not claim complete proposal-to-source mapping or formal clinical approval |
| C30 | Dataset-specific deterministic rules emit canonical binary proxy fields; unavailable numeric measurements provide no positive rule evidence and are not treated as normal | Sec. 3.2, paragraph 2 | Active tagger source; thesis Ch. 5 | SUPPORTED WITH QUALIFICATION | Input availability affects the construct; proxy states are not adjudicated diagnoses |
| C31 | The predictive layer uses STraTS, GRU, GRU-D, and TCN for multi-label proxy prediction and exports per-target probabilities plus binary fields at the implementation threshold of 0.5 | Sec. 3.3, paragraphs 1--2 | Active STraTS source/tests for architecture/export contract; `checked_predictive_exports.csv` for archived schema/value checks | SUPPORTED WITH QUALIFICATION | Threshold is implementation-supported; archived checkpoint/split-to-export linkage remains `TODO-EVIDENCE G-EVD-02` |
| C32 | Archived causal runs form a deterministic aggregate from one rule-derived and four model-derived binary proxy sources | Sec. 3.3, paragraph 2; Table 1; Fig. 1 | Archived causal run summaries/logs summarized by `results_source_packet.md`; thesis Chs. 5 and 8 | SUPPORTED WITH QUALIFICATION | Algorithmic majority vote, not a learned ensemble, expert consensus, or clinical truth; voter byte/hash lineage incomplete (`TODO-EVIDENCE G-EVD-02`) |
| C33 | The estimator-ready resource joins record ID, aggregated exposure fields, mortality, available covariates, dataset/sampling metadata, graph provenance, and exposure-specific adjustment metadata | Sec. 3.4, paragraph 1 | Thesis Chs. 3, 7, and 8; archived run summaries/checked CATE schema; current implementation | SUPPORTED WITH QUALIFICATION | These elements may reside across linked tables/metadata rather than one flat file; producing lineage remains partial |
| C34 | Source-coded DAGs operationalize explicit project assumptions and make adjustment choices inspectable and replaceable | Sec. 3.4, paragraph 2 | Active graph/adjustment source; thesis Ch. 7 | SUPPORTED WITH QUALIFICATION | Graphs are assumed, not learned or clinically validated |
| C35 | The resource interface permits alternative estimators, proxy definitions, DAGs, and adjustment sets without rebuilding raw-source integration | Sec. 3.4, paragraph 2 | Resource separation and active pipeline interfaces; thesis Ch. 11 | SUPPORTED WITH QUALIFICATION | Design-supported reuse claim; no public-release/access claim (`TODO-RELEASE G-REL-01`) |
| C36 | Structural/cohort validation checks exact schemas, allowed values, complete artifact sets, canonical identifiers, duplicates, and exact cohort equality, rejecting missing/extra IDs and silent shrinkage | Sec. 3.5, paragraph 1; Fig. 1 | Current `router.py`, `tests/test_router_contracts.py`, STraTS split/identifier/artifact tests | SUPPORTED WITH QUALIFICATION | Current repaired contract only; `TODO-RUNTIME G-RUN-01` blocks test-pass wording and archived attribution |
| C37 | Artifact/provenance validation uses run-scoped dataset paths, metadata sidecars, upstream fingerprints/hashes, manifests, receipts, configuration/cohort bindings, and stable derived seeds, with stale/mutated reuse rejection | Sec. 3.5, paragraph 2 | Current root/STraTS implementation and tests | SUPPORTED WITH QUALIFICATION | Current repaired contract only; `TODO-RUNTIME G-RUN-01` blocks test-pass wording |
| C38 | Checked archived exports and aggregate tables have validated schemas/counts and result manifests/checksums, while exact producing revisions/configurations and checkpoint-to-export links remain incomplete | Sec. 3.5, paragraph 3 | `checked_predictive_exports.csv`; `checked_cohort_candidates.csv`; result manifest/checksums; reproducibility lineage/gaps | SUPPORTED WITH QUALIFICATION | `TODO-EVIDENCE G-EVD-02`; do not claim exact clean rerun |
| C39 | Both resources were exercised through predictive characterization, three effect-estimation workflows, DAG-guided adjustment, matching, and robustness diagnostics | Sec. 3.5, paragraph 4; Table 1; Fig. 1 | Checked results manifest/source packet and causal run lineage | SUPPORTED WITH QUALIFICATION | Analytical execution validates resource reuse, not clinical constructs or causal identification |
| C40 | “Validated causal-analysis datasets” means structural integrity, cohort consistency, provenance, and analytical reuse; clinical construct validity and causal identification are separate | Sec. 3 opening and Sec. 3.5, paragraphs 1--4 | C25, C36--C39; canonical operational plan terminology policy | SUPPORTED WITH QUALIFICATION | This definition bounds every normal later use of the phrase |

### P3 Table 1 and Figure 1 evidence

| Artifact | Inserted content | Authority and status |
|---|---|---|
| Table 1 | MIMIC-III: 26,845 records, 9 admitted exposures; PhysioNet 2012: 7,993 records, 10 admitted exposures; in-hospital mortality; one rule plus four models; CausalForestDML, LinearDML, CausalPFN | Counts: `checked_cohort_candidates.csv` and original-sampling rows in `checked_cate_candidates.csv` (SUPPORTED). Source/estimator sets: `results_source_packet.md` and checked run families (SUPPORTED WITH QUALIFICATION for lineage). |
| Figure 1 | Sized layout placeholder, final-quality caption, and implementable specification separating design time, construction/runtime, validation gates, central reusable resources, and downstream characterization | Thesis Chs. 3--8; C29--C39. Final artwork remains `TODO-HUMAN G-HUM-01`; test-pass labeling remains `TODO-RUNTIME G-RUN-01`. |

### P3 citation keys activated

`johnson2016mimiciii`, `silva2012physionet`, `tipirneni2022strats`, `cho2014gru`, `bai2018tcn`, and `che2018grud` are present in `literature/metadata/references.bib` and are used only for dataset or model-family attribution in Sections 3.1 and 3.3. No CausalPFN citation or unsupported method-attribution claim was added.

### P4 manuscript claim register

P4 uses the same drafting statuses as P3: **SUPPORTED**, **SUPPORTED WITH QUALIFICATION**, **GATED**, and **EXCLUDED**. Numerical findings remain reserved for Section 5.

| Claim ID | Manuscript claim/function | Exact manuscript location | Highest-authority source | Status | Required qualification / TODO |
|---|---|---|---|---|---|
| C41 | Each dataset has a separate multi-label task whose target is its deterministic proxy-state vector; STraTS, GRU, GRU-D, and TCN are evaluated without cross-dataset pooling | Sec. 4.1, paragraph 1 | `checked_predictive_metrics.csv`; thesis Chs. 3, 6, and 8 | SUPPORTED | Dataset-specific target schemas; proxy targets are not clinical labels |
| C42 | The comparison uses selected archived held-out test outputs for all eight model--dataset combinations | Sec. 4.1, paragraph 1 | `checked_predictive_metrics.csv` rows selected `PRIMARY_MAIN_TEXT`; `results_source_packet.md` | SUPPORTED WITH QUALIFICATION | One selected archived run per combination; split/checkpoint lineage remains `TODO-EVIDENCE G-EVD-02` |
| C43 | Prediction characterizes learnability and reproducibility of rule-derived constructs, without statistical-superiority or clinical-validity claims | Sec. 4.1, paragraph 1 | Thesis Ch. 6 evaluator interpretation; checked archive | SUPPORTED WITH QUALIFICATION | No repeated-run uncertainty, significance tests, or chart-adjudicated target validation |
| C44 | Reported metrics are test binary-cross-entropy loss, macro AUROC, macro AUPRC, and macro minRP; minRP is the maximum across thresholds of `min(precision, recall)` | Sec. 4.1, paragraph 2 | `STraTS/src/evaluator.py`; thesis Ch. 6; checked metric schema | SUPPORTED | Loss is sample-mean evaluator loss; do not invent uncertainty |
| C45 | AUROC, AUPRC, and minRP are averaged over non-degenerate targets; single-class targets are skipped | Sec. 4.1, paragraph 2 | `STraTS/src/evaluator.py`; thesis Ch. 6 | SUPPORTED | Degenerate-target rule applies to macro discrimination summaries, not as an asserted loss exclusion |
| C46 | Each admitted binary aggregate exposure is analyzed separately against in-hospital mortality using observed exposure-specific DAG-selected adjustment variables; all prespecified exposures are retained | Sec. 4.2, paragraph 1 | `results_decision_register.md`; thesis Chs. 7--8; checked CATE rows | SUPPORTED WITH QUALIFICATION | Project DAG is assumed, not learned/validated; no result-based exposure selection |
| C47 | Original, non-downsampled populations are primary and dataset analyses are separate and unpooled | Sec. 4.2, paragraph 1; Sec. 4.3, paragraph 3 | `results_decision_register.md`; `results_source_packet.md` | SUPPORTED | Cross-dataset comparison is workflow/interface level |
| C48 | CausalForestDML is the primary nonlinear DML estimator, with flexible nuisance models, a causal-forest final stage, and record-level fitted conditional-effect outputs | Sec. 4.2, paragraph 2 | Thesis Ch. 7; active `cate_estimation.py`; approved DML/forest/EconML references | SUPPORTED WITH QUALIFICATION | Method interpretation is assumption-bound; current code is not claimed as historical producer |
| C49 | LinearDML is the structured comparator, preserving the DML/nuisance framework while using a linear final effect model | Sec. 4.2, paragraph 2 | Thesis Ch. 7; active `cate_estimation.py`; approved DML/EconML references | SUPPORTED WITH QUALIFICATION | Cross-model-form triangulation, not an unbiased fallback claim |
| C50 | CausalPFN is a meaningful complementary estimator evaluated on the same prespecified pairs to test whether directions are DML-specific | Sec. 4.2, paragraph 2 | Checked CATE experiment matrix; `results_decision_register.md`; canonical plan | SUPPORTED WITH QUALIFICATION | No architecture, training-corpus, theory, novelty, or primary-source claim; `TODO-EVIDENCE G-EVD-01` remains |
| C51 | Results report the sample mean of record-level fitted conditional estimates as the mean model-estimated CATE over the analyzed sample | Sec. 4.2, paragraph 3 | Checked CATE schema; thesis Chs. 7 and 10; `results_decision_register.md` | SUPPORTED WITH QUALIFICATION | Not a risk/odds ratio or unqualified population ATE |
| C52 | Directional triangulation compares CausalForestDML with LinearDML and then all three estimators across every prespecified pair, retaining disagreements | Sec. 4.2, paragraph 3 | Checked CATE matrix; `results_decision_register.md` | SUPPORTED WITH QUALIFICATION | Agreement neither requires equal magnitude nor proves identification; P4 states no agreement count |
| C53 | Matching uses a median-binarized/binary representation, progressive greedy one-to-one Hamming matching, descriptive pair differences, support warnings, and explicit failure when no representation remains | Sec. 4.3, paragraph 1 | `checked_matching_results.csv`; `checked_matching_failures.csv`; thesis Chs. 7--8; active matching source | SUPPORTED WITH QUALIFICATION | Descriptive matched-pair outcome difference, not an independent causal effect or positivity proof |
| C54 | DML sensitivity evidence preserves native/recomputed/reconstructed/partial/unavailable status; treatment and outcome permutations are disruption checks rather than formal randomization tests; PFN lacks an equivalent archived package | Sec. 4.3, paragraph 2 | Checked sensitivity/permutation tables; thesis Ch. 8 | SUPPORTED WITH QUALIFICATION | Do not imply uniform exposure coverage or diagnostic parity |
| C55 | Downsampling retains outcome-positive records and samples outcome-negative records, changes population/prevalence, and is robustness-only; the shared sequence tests portability while definitions/results remain dataset specific and unpooled | Sec. 4.3, paragraph 3 | Thesis Chs. 7--8; active downsampling source; `results_decision_register.md` | SUPPORTED WITH QUALIFICATION | Magnitudes are not directly interchangeable with original-population estimates |

### P4 citation keys activated

`chernozhukov2018dml`, `wager2018causalforest`, `athey2019grf`, and `oprescu_et_al_2019_econml` are present in `literature/metadata/references.bib` and support only the DML, causal-forest, and implementation-family descriptions in Section 4.2. No CausalPFN citation or unsupported CausalPFN architecture/theory claim was added.

### P5 manuscript claim register

P5 activates the checked numerical Results claims below. Causal-source dataset
spellings are `mimic` and `physionet`; predictive-source spellings are
`mimic_iii` and `physionet_2012`.

| Claim ID | Manuscript claim/function | Exact manuscript location | Highest-authority source and selection predicate | Status | Local qualification / artifact link |
|---|---|---|---|---|---|
| C56 | Resources contain 26,845 MIMIC-III and 7,993 PhysioNet analysis records and nine and ten admitted exposures | Sec. 5 opening | `checked_cohort_candidates.csv`: original causal-analysis model-row candidates; `checked_cate_candidates.csv`: original main-text rows grouped by dataset/treatment | SUPPORTED | Analysis records, not raw-source cohort sizes; Table 1 and Sec. 5 opening |
| C57 | The evaluation sequence is applied separately and results are not pooled | Sec. 5 opening | `results_decision_register.md`, original-population/no-pooling freeze | SUPPORTED | Dataset-specific findings; no pooled clinical replication |
| C58 | Table 2 contains all eight selected held-out predictive rows and all four metrics | Sec. 5.1, Table 2 | `checked_predictive_metrics.csv`: `selection_status == PRIMARY_MAIN_TEXT`, exactly 8 rows; fields `loss`, `auroc`, `auprc`, `minrp` | SUPPORTED WITH QUALIFICATION | Three-decimal display; point estimates only; no uncertainty/significance claim |
| C59 | STraTS leads all four MIMIC-III metrics and GRU-D leads all four PhysioNet metrics | Sec. 5.1, paragraphs 1--2 and Table 2 | C58 predicate; per-dataset minimum loss and maximum AUROC/AUPRC/minRP | SUPPORTED WITH QUALIFICATION | Archived leadership, not statistical superiority |
| C60 | STraTS MIMIC-III AUROC/AUPRC are 0.905/0.869 and GRU-D PhysioNet AUROC/AUPRC are 0.918/0.905 | Sec. 5.1, paragraph 2 | C58 rows and fields; full precision retained in P5 audit | SUPPORTED WITH QUALIFICATION | Rounded point metrics against rule-derived targets |
| C61 | All nine MIMIC-III primary Forest summaries are positive; nine of ten PhysioNet summaries are positive and shock is negative | Sec. 5.2, paragraph 1 and Figure 2 | `checked_cate_candidates.csv`: `sampling_condition == original`, `estimator == CausalForestDML`, `selection_status == PRIMARY_MAIN_TEXT`; exactly 19 rows | SUPPORTED WITH QUALIFICATION | Mean model-estimated CATE over analyzed sample; no intervention/clinical recommendation claim |
| C62 | Largest primary summaries are MIMIC cardiac 0.220 and inflammation/sepsis 0.161; PhysioNet renal 0.120, cardiac 0.112, global 0.108; shock is -0.014 | Sec. 5.2, paragraph 1 | C61 predicate; decreasing full-precision `mean_cate` within dataset | SUPPORTED WITH QUALIFICATION | Three-decimal descriptive ranking |
| C63 | CausalForestDML and LinearDML agree in direction for 19/19 comparisons | Sec. 5.2, paragraph 2 and Figure 2 caption | Join original `PRIMARY_MAIN_TEXT` Forest and `SECONDARY_MAIN_TEXT` Linear rows on dataset/treatment; compare full-precision signs; 19 joins | SUPPORTED WITH QUALIFICATION | Direction only; not magnitude equality or identification |
| C64 | CausalPFN reproduces the prevailing direction in 18/19 comparisons | Sec. 5.2, paragraph 3 and Figure 2 caption | Join C63 rows to original `EXPLORATORY_MAIN_TEXT` CausalPFN rows; compare all signs; 19 complete joins | SUPPORTED WITH QUALIFICATION | Complete exposure set, not favorable subset; smaller diagnostic package |
| C65 | PhysioNet shock is the sole exception: Forest -0.014, Linear -0.027, PFN 0.004; matching is positive 0.010 | Sec. 5.2, paragraph 4 and Figure 2 | `checked_cate_candidates.csv`: original PhysioNet `LAT_SHOCK`, three estimator-specific main-text rows; `checked_matching_results.csv`: original PhysioNet `LAT_SHOCK` | SUPPORTED WITH QUALIFICATION | Matching is a descriptive outcome difference; disagreement stays visible |
| C66 | Figure 2 includes all 19 original-cohort combinations and all 57 estimator values, ordered by decreasing Forest value | Figure 2 and generation script | `checked_cate_candidates.csv`: original estimator-specific main-text statuses; require 19 combinations, 3 expected estimators, no duplicates/missing rows | SUPPORTED | Full-precision vector plot; source-read rather than transcribed matrix |
| C67 | Matching succeeds for 8/9 MIMIC and 7/10 PhysioNet exposures (15/19), and 14/15 share the Forest direction | Sec. 5.3, paragraph 1 | `checked_matching_results.csv`: original, 15 rows; `checked_matching_failures.csv`: original, 4 rows; sign join to C61 | SUPPORTED WITH QUALIFICATION | Failures are absent usable binary representations, never zero effects |
| C68 | Original/downsampled direction is preserved in 55/57; sign changes are PhysioNet LinearDML coagulation/hematologic dysfunction and PhysioNet CausalPFN shock | Sec. 5.3, paragraph 2 | Join 57 original main-text CATE rows to 57 `outcome-downsampled`/`ROBUSTNESS_APPENDIX` rows on dataset/treatment/estimator; compare full-precision signs | SUPPORTED WITH QUALIFICATION | Different population; magnitudes are not original-population estimates |
| C69 | DML sensitivity evidence spans recorded provenance classes; permutations are disruption checks; equivalent PFN stages are unarchived | Sec. 5.3, paragraph 2 | `checked_sensitivity_candidates.csv`; `checked_permutation_candidates.csv`; `results_source_packet.md` | SUPPORTED WITH QUALIFICATION | Coverage nonuniform; provenance/status classes remain distinct |
| C70 | Shared workflow operates across both resources while predictive leadership, effect ordering, and at least one primary sign differ | Sec. 5.3, paragraph 2 | C57, C59, C61--C69 and their checked sources | SUPPORTED WITH QUALIFICATION | Workflow portability, not construct equivalence or pooled replication |

### P5 Table 2 and Figure 2 evidence

| Artifact | Content and exact source | Validation/status |
|---|---|---|
| Table 2 | All 8 `PRIMARY_MAIN_TEXT` rows in `checked_predictive_metrics.csv`; model, dataset, loss, AUROC, AUPRC, and minRP; full precision rounded to three decimals | 8 rows and 32 metric cells; best values recomputed with lower loss/higher other metrics; SUPPORTED WITH QUALIFICATION |
| Figure 2 | All 57 original main-text CATE rows in `checked_cate_candidates.csv`, using estimator-specific statuses; ordered by decreasing CausalForestDML within panel | Script rejects duplicates, missing estimators, wrong dataset counts, and totals other than 19 combinations; 19/19 DML and 18/19 all-three signs rechecked; SUPPORTED WITH QUALIFICATION |

No new citation key was activated in P5. No unsupported CausalPFN methodological citation or attribution was added.

### P6 Discussion and Conclusion claim register

P6 adds interpretation only from the frozen P5 findings, construction evidence,
thesis Discussion/Conclusion, and existing gate register. It introduces no new
numerical result or citation.

| Claim ID | Manuscript claim/function | Exact manuscript location | Highest-authority source | Status | Required qualification / gate |
|---|---|---|---|---|---|
| C71 | The resources support comparison of alternative estimators and temporal representations without rebuilding every integration stage | Sec. 6.1, paragraph 1 | C35, C39--C40; thesis Ch. 11 resource/interface synthesis | SUPPORTED WITH QUALIFICATION | Interface-level reuse; no availability claim while `G-REL-01` is open |
| C72 | Deterministic construct definitions and lineage support replacement of proxies, DAGs, and adjustment sets plus cohort/support and lineage audits | Sec. 6.1, paragraph 1 | C29--C38; thesis Ch. 11 data-contract, construct, and provenance discussions | SUPPORTED WITH QUALIFICATION | Replaceability is a resource-design property, not evidence that alternatives are clinically valid |
| C73 | The shared sequence operated across both ICU sources while predictive leadership, magnitudes, and rankings remained dataset specific | Sec. 6.1, paragraph 2 | C57, C59, C61--C62, C70; checked P5 findings | SUPPORTED WITH QUALIFICATION | Workflow/interface portability only; no pooled clinical replication |
| C74 | Dataset-specific variables, measurement processes, ontologies, and graph assumptions are deliberately preserved; similarly named states are not assumed equivalent | Sec. 6.1, paragraph 2 | C28, C34, C40; thesis Ch. 11 cross-dataset interpretation | SUPPORTED | Results stay separate and unpooled |
| C75 | Complete DML sign agreement supports within-design robustness to different DML final-stage model forms | Sec. 6.2 | C63; `checked_cate_candidates.csv`; P5 numerical audit | SUPPORTED WITH QUALIFICATION | Direction only; not magnitude equality or identification |
| C76 | CausalPFN's broad concordance makes it a prominent complementary estimator result | Sec. 6.2 | C64; `checked_cate_candidates.csv`; P5 numerical audit | SUPPORTED WITH QUALIFICATION | No architecture, theory, novelty, or citation claim; `G-EVD-01` remains |
| C77 | PhysioNet shock is useful model/support-sensitivity evidence and motivates targeted proxy, support, adjustment, and estimator analysis | Sec. 6.2 | C65; checked CATE/matching records; thesis Ch. 11 | SUPPORTED WITH QUALIFICATION | Retain disagreement; do not resolve by voting or imply a clinical effect |
| C78 | Directional agreement does not establish equal magnitudes or identification, and CausalPFN has a smaller archived estimator-specific diagnostic package | Sec. 6.2 | C51--C54, C63--C65, C69; sensitivity/permutation records | SUPPORTED | Agreement is bounded within the implemented observational design |
| C79 | The LLM is a structured design-time proposal aid separated from deterministic patient-level execution and source authority | Sec. 6.3 | C29; `audit/llm_prompt_provenance_audit.md`; thesis Ch. 11 | SUPPORTED WITH QUALIFICATION | No construct-validation or patient-level effect-estimation claim; proposal-to-code lineage remains partial |
| C80 | Clinician review, expert/LLM comparison, isolated design ablation, alternative ontologies/graphs, stronger uncertainty, richer CausalPFN diagnostics, and external validation are prioritized follow-up studies | Sec. 6.3 | Thesis Ch. 12 future work; provenance gaps `GAP-016`--`GAP-020`; P5 diagnostic boundaries | SUPPORTED AS FUTURE RESEARCH | Research agenda, not completed experiments |
| C81 | Proxy, graph/identification, uncertainty/diagnostic, historical-lineage, runtime/release, access/external-validation, and LLM-ablation limitations remain centralized and actionable | Sec. 6.4 | C14--C20, C29--C40, C43, C54, C69; gate register; thesis Chs. 11--12; `provenance_gaps.csv` | SUPPORTED WITH QUALIFICATION | Current runtime and anonymous release remain separately gated; no stronger reproducibility/availability claim |
| C82 | CliniCause constructs reusable estimator-ready resources spanning MIMIC-III and PhysioNet 2012, supported by structural, cohort, provenance, and analytical validation | Sec. 7 | C02, C26--C40, C56--C57 | SUPPORTED WITH QUALIFICATION | Validation scope excludes clinical construct validity and causal identification |
| C83 | Broad DML/CausalPFN directional agreement demonstrates the value of triangulation and the resources enable tests of proxies, representations, graphs, cohorts, and estimators | Sec. 7 | C35, C63--C64, C71--C78 | SUPPORTED WITH QUALIFICATION | No new count, experiment, release claim, or clinical recommendation |

No new citation key is activated in P6. The Conclusion contains no number,
citation, public-release statement, new experiment, or clinical recommendation.

## 6. Current validation-contract evidence

Static inspection found implementation and test cases for canonical identifier normalization, duplicate rejection, exact cohort equality (including allowed reordering and rejected missing/extra IDs), split integrity, prediction-schema and probability consistency, malformed prediction rejection, metadata/fingerprint validation, manifest and receipt handling, reuse checks, derived seeds, mutation detection, and dataset isolation. This supports a paper/checklist statement only in the form “the current code contains these validation contracts.”

It does **not** support either “the archived experiments ran this exact code” or “all current tests pass.” The former is blocked by producing-revision gaps; the latter is blocked because the active environment lacks `pytest`.

## 7. Conflicts and resolutions

| Conflict/ambiguity | Resolution for the paper |
|---|---|
| The generic kit sample permits a checklist to be input or standalone, while current AAAI-27 submission instructions require a separate upload | Follow the current official instruction: do not integrate the checklist into `paper.pdf` |
| Historical `final-results/AGENTS.md` records older parent/nested revisions than the current repository | Treat those revisions as a historical audit snapshot and the values in §1 as the current baseline; neither is silently substituted for producing provenance |
| The full-run pointer commit advances nested repositories but has no root archived run manifest | Record the commit, but do not call it an evidenced complete production run |
| Current router/test code is newer than parts of the archived evidence | Describe only the current contract; do not attribute it to archived result production |
| Thesis positioning treats CausalPFN cautiously, while the paper plan gives its three-estimator concordance a central role | Use it as complementary empirical triangulation while retaining the thesis limitations and primary-reference gate |
| The operational plan's tentative AAAI page-limit/checklist questions | Resolved from the current official AAAI-27 call and submission pages: 7 technical pages, up to 9 total with references; checklist uploaded separately |
| A genre-example index and its PDF disagree by one on that example's dataset size | Do not reuse the external example's numerical claim; it has no evidentiary role in CliniCause |

## 8. Gate register

| Gate | Category | Exact missing fact/artifact | Expected source/owner | Why it matters | Blocks first draft? | Blocks submission? |
|---|---|---|---|---|---|---|
| G-EVD-01 | TODO-EVIDENCE | Verified primary bibliographic entry for CausalPFN | Authors/literature review; approved `references.bib` | Required for method attribution and any theory/novelty comparison | No, if all CausalPFN prose remains commented/gated | Yes for CausalPFN method claims |
| G-EVD-02 | TODO-EVIDENCE | Producing commit(s), numbered causal configuration files, causal source version, and predictive split/checkpoint-to-export linkage | Experiment archive owners; lineage tables; original run directories | Separates archived outputs from current code and bounds reproducibility claims | No, if claims describe checked artifacts only | No for an honestly bounded paper; yes for any exact-rerun claim/checklist answer asserting full linkage |
| G-RUN-01 | TODO-RUNTIME | Executed current root/nested test results | Maintained environment or CI with `pytest` installed | Static test presence is not a passing runtime result | No | No, unless the paper/checklist claims current tests pass |
| G-RUN-02 | TODO-RUNTIME | A complete integrated rerun manifest at the frozen current revisions | Maintained experiment environment and immutable run receipt | Needed to label the current tree as an executed end-to-end baseline | No | No, unless claiming a current full rerun |
| G-REL-01 | TODO-RELEASE | Anonymous submission package/URL, license, data-access instructions, and code/data/supplement contents | Authors/release owner | AAAI reviewers require submission-time artifacts for code/data evidence; a future promise is not evidence | No | Yes for public-availability/release claims and any corresponding checklist answer |
| G-HUM-01 | TODO-HUMAN | Final contribution hierarchy, claim strength, and selection of main-paper visuals | Authors/supervisor | Strategic framing cannot be inferred mechanically from artifacts | No for skeleton | Yes |
| G-HUM-02 | TODO-HUMAN | Author list/affiliations, track, conflicts, ethics/privacy wording, acknowledgments/funding, and final anonymization review | Authors | Identity and governance facts are absent or intentionally suppressed | No | Yes |
| G-AAAI-01 | TODO-AAAI | Final-day confirmation that official page, checklist, supplement, anonymity, and generative-AI rules have not changed | Official AAAI-27 pages | Web instructions are mutable | No | Yes until rechecked immediately before submission |

## 9. Checklist evidence ledger (not checklist answers)

| Checklist area | Available evidence | Gap/owner | State |
|---|---|---|---|
| Claims and assumptions | Thesis methods/limitations; claim lock above | Human confirmation of final wording | Partially evidenced |
| Theoretical assumptions/proofs | Not the paper's intended contribution | Verify each final method statement | Not applicable unless theory prose is added |
| Datasets | Thesis cohort/preprocessing chapters; checked cohort candidates | Anonymous access/release instructions | Partially evidenced |
| Code | Current repositories and validation contracts | Anonymous release artifact/license; runtime record | G-REL-01/G-RUN-01 |
| Experimental setup | Thesis methods; checked results; partial lineage CSVs | Numbered configs, producing revisions, split/checkpoint linkage | G-EVD-02 |
| Statistical reporting | Checked point estimates and directional summaries | No uncertainty/significance evidence for predictive leaderboard; preserve that limitation | Bounded evidence only |
| Compute/resources | `environment_lineage.csv` and thesis methods | Verify complete hardware/runtime details against actual producing runs | Human/provenance review |
| Ethics/limitations | Thesis discussion/limitations | Human privacy, intended-use, and risk review | G-HUM-02 |
| Reproducibility artifacts | Manifests, checksums, source packet | Submission package and missing lineage | G-EVD-02/G-REL-01 |

## 10. Stage readiness

- P0: repository, nested revisions, dirty-state exceptions, authoritative source hierarchy, and inspected instruction files are recorded.
- P0A: paper workspace and author kit are inventoried and hashed; no pre-existing paper artifacts were overwritten.
- P1: exact kit behavior and current official AAAI-27 constraints are recorded in `aaai_structure_notes.md`.
- P2: protected facts, result families, claim locks, conflicts, and actionable gates are recorded here.
- P5: all Results claims, Table 2 values, and the complete Figure 2 matrix are checked and linked through C56--C70 and the P5 numerical audit.
- P6: all Discussion interpretations and the one-paragraph Conclusion are mapped through C71--C83; no new result, citation, release claim, or clinical recommendation was introduced.

READY FOR STAGE P0A — PAPER BASELINE FROZEN

READY FOR STAGE P1 — AAAI GENRE AND FORMAT STUDIED

READY FOR STAGE P2 — CLAIMS AND EVIDENCE LOCKED

READY FOR STAGE P6 — RESULTS DRAFTED AND NUMERICALLY MAPPED

READY FOR STAGE P7 — INTERPRETATION AND CONCLUSION DRAFTED
