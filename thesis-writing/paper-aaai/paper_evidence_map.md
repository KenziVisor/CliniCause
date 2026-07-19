# CliniCause AAAI-27 paper evidence map

Status: P0/P0A/P2 baseline, frozen 2026-07-19

Scope: evidence control for the AAAI-27 manuscript; this file is not manuscript prose.
Canonical plan: `clinicause_aaai27_paper_operational_plan.md`.

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
| Canonical operational plan | `e70a485146631a3edf3f5358ec5e047e97db0967cd12a50a0388eed745f31b25` |

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
| C17 | Current routing code enforces canonical IDs, cohort equality, schema/probability validation, hashes, manifests, receipts, derived seeds, and dataset isolation | Current implementation | Validation | `router.py`; `test_router_contracts.py` | Static code/test inspection | Medium | Say “current contract implements/tests”; runtime not verified in this environment | Supplement/checklist | G-RUN-01 | GATED |
| C18 | Archived results are exactly reproducible from complete producing revisions/configurations | Reproducibility | Validation/checklist | Reproducibility CSVs | Explicitly incomplete | Low | Claim is prohibited until missing lineage is recovered | None | G-EVD-02 | GATED |
| C19 | CausalPFN supplies a complementary third estimator family | Contribution/method | Intro/Causal Estimation | Checked results; thesis method text | Empirical + secondary description | Medium | Primary method citation is missing; avoid novelty/theory claims | Fig. 2 | G-EVD-01 | GATED |
| C20 | Code/data/resources are publicly available at submission | Release claim | Discussion/checklist | No anonymized release artifact currently evidenced | None | Low | No URL, license, or release package may be invented | None | G-REL-01 | GATED |
| C21 | The evaluation demonstrates clinical effectiveness, treatment benefit, or deployability | Prohibited overclaim | Nowhere | No prospective/randomized evidence | Unsupported | None | Must not appear | None | Permanent | GATED |
| C22 | Cross-estimator directional concordance is evidence of stability within this archived observational design | Interpretation | Discussion | C10–C16 | Triangulated checked results | Medium | Pair with exception, partial validation coverage, and proxy/confounding limitations | Fig. 2 | Human wording review | HUMAN |
| C23 | The main contribution is a validated reusable benchmark/resource rather than a new causal estimator | Positioning | Intro/Discussion | Repository/thesis/plan | Design judgment | Medium | Authors must ratify novelty framing | Fig. 1 | G-HUM-01 | HUMAN |
| C24 | Predictive and causal stages used exact recorded splits/checkpoints from a fully linked manifest | Reproducibility | Evaluation/checklist | `predictive_run_lineage.csv`, `provenance_gaps.csv` | Incomplete | Low | Prohibited until split/checkpoint linkage is recovered | None | G-EVD-02 | GATED |
| C25 | All checked numerical claims trace to manifest/checksum-controlled files | Evidence control | Checklist/supplement | results packet, manifest, checksums | Archived integrity record | High | Integrity of available files is not complete production lineage | None | None | LOCKED |

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

READY FOR STAGE P0A — PAPER BASELINE FROZEN

READY FOR STAGE P1 — AAAI GENRE AND FORMAT STUDIED

READY FOR STAGE P2 — CLAIMS AND EVIDENCE LOCKED
