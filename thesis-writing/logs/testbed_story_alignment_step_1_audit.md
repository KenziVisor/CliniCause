# Testbed Story Alignment — Step 1 Audit

## 1. Baseline

This is a read-only story-alignment audit. No thesis, paper, bibliography, code, figure, or generated PDF was edited. The only permitted task-created repository file is this report.

- Branch: `main`.
- HEAD: `1b444d9fdd29efa9dfaf74db001fa4915f5cba66` (`paper sync`).
- Recent commits, newest first:

  ```text
  1b444d9 paper sync
  d609877 sync changes
  d7d2fd9 Remove accidental nested repository link
  9812e1f submodules merging
  5d43de3 submodules merging
  0fe0649 dataset-extract addition
  61fbf58 dataset-extraction addition
  10de05c AAAI P9
  414b8a4 AAAI P8 repair
  0c1fd3c AAAI P8
  ```

- Pre-existing modified files at baseline:

  ```text
   M prompt.txt
   M thesis-writing/advisor/clinical-evidence-supplement/dag_edge_evidence.csv
   M thesis-writing/advisor/clinical-evidence-supplement/proxy_evidence.csv
   M thesis-writing/advisor/clinical-evidence-supplement/source_registry.csv
   M thesis-writing/paper-aaai/mimic-mortality-voters.csv
   M thesis-writing/paper-aaai/physionet-mortality-voters.csv
  ```

- Pre-existing untracked file at baseline: `thesis-writing/THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md`.
- The dirty files belong to the pre-task worktree. They were treated as read-only and were not normalized, reverted, staged, or overwritten.
- Local instructions read: repository `README.md`; `thesis-writing/thesis/README.md`; `thesis-writing/thesis/figures/README.md`; `thesis-writing/thesis/tables/README.md`; `thesis-writing/literature/README.md`; and `thesis-writing/reproducibility/README.md`. No applicable `AGENTS.md` governs the focused thesis/paper paths.
- The canonical plan `thesis-writing/THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md` and `prompt.txt` were read completely before inspection.
- Post-audit unblock event: after the original Step 1 report identified the missing final Figure 1 asset, the user added `thesis-writing/true-figure-1.png`. That user-created file was not present at the original baseline and is not a task-created change. It was inspected read-only and is incorporated into the readiness decision below.

## 2. Scope and Source Authority

### Authority order

1. The finished visible paper, `thesis-writing/CausalDataGeneration.pdf`, is the principal authority for the paper's public contribution hierarchy, claims, and figure numbering.
2. `thesis-writing/aaai27-submission.tex` and `thesis-writing/paper-aaai/aaai27-submission.tex` are byte-identical (`cmp` exit 0; SHA-256 `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6`). They are the structural authority for exact prose, equations, citations, and the inline TikZ pipeline figure.
3. `thesis-writing/supp.pdf` and `thesis-writing/paper-aaai/supplementary1.tex` control the finished supplementary evidence, especially clinical-literature comparison and rule/DAG documentation.
4. The active thesis is `thesis-writing/thesis/main.tex`, with bibliography `thesis-writing/literature/metadata/references.bib` and rendered artifact `thesis-writing/thesis/main.pdf`.
5. Checked thesis results and reproducibility records may gate whether stronger paper claims can be imported; paper prose is not by itself sufficient authority for changing frozen thesis numbers when the checked thesis artifact disagrees.

### Protected hashes at baseline

| Artifact | SHA-256 | Notes |
|---|---|---|
| `thesis-writing/CausalDataGeneration.pdf` | `9c7a3473301fcab7a652985ed7f4fbf765a4de197eec53cc7ffe89a5996193f1` | Finished paper, 9 letter-size pages |
| `thesis-writing/aaai27-submission.tex` | `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6` | Root final source copy |
| `thesis-writing/supp.pdf` | `a0fa0eca32b043877dbc98a357cb8eb4844416c856fe8a748781ac456d72b3` | Finished supplement, 82 letter-size pages |
| `thesis-writing/paper-aaai/aaai27-submission.tex` | `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6` | Byte-identical final source copy |
| `thesis-writing/paper-aaai/supplementary1.tex` | `86dea4d4a744b125d517bb9adb4628a59dddb68f52b459eff6811732db1eae3b` | Supplement source |
| `thesis-writing/paper-aaai/references.bib` | `3aa035c34a6ba801ab7019d01fa70920333f1e75d5c740f28c30ba40fcf33b4c` | Paper bibliography |
| Protected `paper-aaai` tree manifest | `8d4255c108c4417d6b21fd3e788f1582e81b6f5e27519d3a115571acf27ca008` | SHA-256 of sorted 65-file hash manifest |

### Sources actually inspected

- All active front matter, chapters, appendices, `main.tex`, figure/table READMEs, the active bibliography, and the 101-page rendered thesis.
- The complete 9-page finished paper and both byte-identical final source copies.
- The scientific portion of the finished supplement and the relevant clinical-corroboration source section in `supplementary1.tex`.
- `paper-aaai/references.bib`, `paper_evidence_map.md`, focused paper reports, all three named paper figure assets, and the active thesis result figures.
- Focused checked tables for CATE, mortality prediction, permutation, sensitivity, matching, and frozen values, plus relevant reproducibility/evidence reports.
- The user-supplied `thesis-writing/true-figure-1.png`, compared against the finished paper's rendered Figure 1 and the inline TikZ source at `aaai27-submission.tex:100-187`.
- The rendered thesis was inspected as a complete contact sheet and by selected full-resolution pages; its current 101 pages are readable, with dense DAG labels but no newly introduced layout fault. No rebuild was required or performed for this audit.
- No internet search was performed. Literature recommendations below are limited to the finished paper's verified bibliography.

### Explicitly superseded or excluded material

- `thesis-writing/paper-aaai/paper.tex` and `paper.pdf` are superseded drafts and must not control the thesis reframe.
- `thesis-writing/ignore-paper-aaai/**` is ignored evidence.
- `thesis-writing/paper-aaai/AuthorKit27/**` is template/support material, not scientific authority.
- Root and `paper-aaai` final-source duplicates are currently identical but create future divergence risk; both must remain protected.

## 3. Current Thesis Story

The current thesis is internally coherent, cautious, and evidence-tracked, but its hierarchy is different from the finished paper's.

Its present primary story is an integration and traceability contribution: irregular ICU records pass through dataset-specific data contracts, LLM-assisted design proposals, deterministic rules and graphs, four-model proxy prediction, a five-source aggregate, DAG-based adjustment, matching/CATE estimation, diagnostics, and provenance records. The title, abstracts, objective, main research question, primary-contribution paragraph, Discussion answer, and Conclusion explicitly say that the integrated framework is primary.

The thesis already contains nearly all factual safeguards needed for the paper-aligned story:

- patient measurements and mortality are source-observed rather than generated;
- PhysioNet and MIMIC produce separate, dataset-specific resources and are not pooled;
- LLM use is design-time only, while patient-level instantiation is deterministic source code;
- proxy states are analytical constructs, not diagnoses or chart-adjudicated truth;
- proxy prediction measures recoverability of rule labels, not clinical validity;
- DAGs are project assumptions, not learned or clinically validated graphs;
- agreement is not estimator accuracy, causal correctness, or interchangeable uncertainty;
- support, intervention definition, temporal order, measurement error, and unmeasured confounding remain explicit limitations.

The required change is therefore hierarchical, not a repudiation of the implemented workflow. The thesis should present CliniCause primarily as construction and characterization of clinically grounded observational causal-analysis testbeds. Integration, data contracts, prediction, aggregation, DAGs, and provenance remain important enabling mechanisms and evidence, but not the top-line intellectual proposition.

## 4. Finished Paper Story

The finished paper's title and narrative are: **“CliniCause: Constructing Clinically Grounded Observational Testbeds for Causal Analysis.”** Its contribution hierarchy is:

1. Causal-estimator evaluation is difficult because observational clinical data do not reveal counterfactual answer keys.
2. Existing evaluation settings span fully synthetic, semi-synthetic, RCT-derived, and empirically anchored designs. Each trades causal control against clinical/measurement realism.
3. CliniCause shifts the controlled design intervention to the representation layer: clinical schema and literature guide candidate constructs, rules, and DAGs; deterministic code instantiates those designs on source-observed patient measurements, missingness, support, and mortality.
4. The pipeline produces two separate observational resources—MIMIC-III and PhysioNet—not a pooled dataset and not data with known causal truth.
5. Testbed usefulness is characterized by converging, non-equivalent evidence: construct plausibility, proxy recoverability, mortality-relevant information, estimator sign/rank/magnitude stability, clinical-literature comparison, permutation disruption, and omitted-variable sensitivity.
6. Strong within-resource agreement coexists with cross-resource and exposure-specific discrepancies, especially PhysioNet shock, and with sensitivity to modest unobserved confounding.
7. CliniCause complements controlled benchmarks; it does not replace them or validate estimator accuracy.

Paper resource facts that are compatible with the thesis are 26,845 MIMIC analysis records with 9 analyzed proxy exposures and 7,993 PhysioNet records with 10 analyzed proxy exposures. The paper reports proxy-prediction AUROC in the approximate range 0.867–0.918; 19/19 DML directional agreement; 18/19 all-estimator directional agreement; within-resource Spearman agreement from 0.794 to 1.000; pairwise RMSE from 1.08 to 2.57 percentage points; and cross-resource rank correlation of approximately 0.533 over shared constructs. These remain model- and resource-characterization results, not causal accuracy results.

## 5. Passage-Level Thesis Story Map

Classification is about rhetorical role. “Retain unchanged” means the passage is already scientifically bounded; “retain but subordinate” means preserve its substance under the testbed proposition; “reframe” means its primary claim must change; “add paper-derived context” means insert missing comparison/evaluation framing; and “remove only if redundant” permits deletion only after a replacement makes the sentence duplicative.

| File and passage | Current role | Classification | Later intervention |
|---|---|---|---|
| `frontmatter/administrative_metadata.tex:3-4` | LLM/deep prediction/effect-estimation title | Reframe | Replace with testbed-construction title; keep English/Hebrew scientifically equivalent. |
| `frontmatter/abstract_primary.tex:4` | Integration and traceability are the goal | Reframe | Lead with the evaluation gap and observational-testbed contribution. |
| `frontmatter/abstract_primary.tex:6-8` | Methods and bounded empirical summary | Retain but subordinate | Keep as construction/characterization mechanics and evidence. |
| `frontmatter/abstract_primary.tex:10` | Integrated workflow is the contribution | Reframe | Make testbed construction primary; integration/provenance enable it. |
| `frontmatter/abstract_secondary.tex:14` | Hebrew integration-first objective | Reframe | Mirror the final English scientific hierarchy. |
| `frontmatter/abstract_secondary.tex:16-18` | Hebrew methods/results | Retain but subordinate | Preserve facts and boundaries. |
| `frontmatter/abstract_secondary.tex:20` | Hebrew integration-first contribution | Reframe | Mirror the final English contribution claim. |
| `frontmatter/keywords.tex:5,9` | No testbed/evaluation vocabulary | Add paper-derived context | Add observational testbed/causal-method evaluation vocabulary without implying truth. |
| `chapters/01_introduction.tex:4-21` | Irregular ICU representation and inspectable handoffs | Retain but subordinate; add paper-derived context | Precede with the missing estimator-evaluation problem; preserve the measurement-process motivation. |
| `chapters/01_introduction.tex:23-38` | Integration gap, objective, and framework defense | Reframe | Replace integration gap with observational evaluation/testbed gap; keep safeguards and design/execution distinction. |
| `chapters/01_introduction.tex:34-36` | Repeats benefits of inspectable integration | Remove only if redundant | Keep the strongest version; trim only after replacement paragraphs cover the same boundaries. |
| `chapters/01_introduction.tex:40-58` | Integration-first main RQ and seven SRQs | Reframe | Use one testbed-construction/evaluation main question and a smaller secondary set. |
| `chapters/01_introduction.tex:61-67` | Integrated framework explicitly primary | Reframe | Make two resources plus converging characterization primary; subordinate infrastructure. |
| `chapters/01_introduction.tex:63,65` | Estimator hierarchy, empirical and provenance details | Retain but subordinate | Preserve exact hierarchy and evidence boundaries. |
| `chapters/01_introduction.tex:69` | Safe empirical orientation | Retain unchanged | Directional agreement is already carefully bounded. |
| `chapters/02_background_related_work.tex:4-53` | Dataset/irregular-sampling context | Retain but subordinate; add paper-derived context | Add a focused controlled-to-observational evaluation spectrum. |
| `chapters/02_background_related_work.tex:204-208` | Contribution positioned as component integration | Reframe | Position CliniCause relative to synthetic, semi-synthetic, RCT-derived, and empirically anchored evaluation. |
| `chapters/03_problem_definition_study_design.tex:9-19` | Units and source-observed objects | Retain unchanged | This is core proof that patient records/outcomes are not generated. |
| `chapters/03_problem_definition_study_design.tex:21-26` | Design-time versus execution | Retain but subordinate | Recast as representation design followed by deterministic testbed instantiation. |
| `chapters/03_problem_definition_study_design.tex:33-37` | Prediction and five analytical tasks | Retain but subordinate | Organize as resource construction and characterization axes. |
| `chapters/03_problem_definition_study_design.tex:39-48` | Observational causal boundaries | Retain unchanged | Essential distinction from truth-known benchmarks. |
| `chapters/03_problem_definition_study_design.tex:50` | Repeats integration-first RQ | Reframe | Synchronize with Chapter 1. |
| `chapters/04_data_preprocessing.tex:9,20` | Datasets “exercise the pipeline” | Reframe | Say they instantiate separate source-observed testbeds. |
| `chapters/04_data_preprocessing.tex:28-60` | Contracts, identifiers, provenance | Retain but subordinate | Preserve as enabling resource integrity. |
| `chapters/05_proxy_state_construction.tex:4-22` | Proxy rationale and LLM design provenance | Reframe lightly; retain safeguards | Explain controlled representation-layer design and deterministic instantiation. |
| `chapters/05_proxy_state_construction.tex:24-109` | Active rules and missingness semantics | Retain unchanged | Core resource definitions; later add shock illustration. |
| `chapters/05_proxy_state_construction.tex:111-131` | Predicted/aggregated labels | Retain but subordinate | Preserve exact one-rule/four-model aggregation. |
| `chapters/06_predictive_modeling.tex:4-6` | Prediction as pipeline layer | Reframe lightly | Present as proxy recoverability characterization. |
| `chapters/06_predictive_modeling.tex:30-53` | Target/export mechanics and boundaries | Retain unchanged | Especially preserve “not clinical ground truth/validity.” |
| `chapters/07_causal_methodology.tex:4-34` | DAG role and figures | Retain unchanged with small contextual addition | Describe DAGs as representation-layer assumptions, not answer keys. |
| `chapters/07_causal_methodology.tex:36-104` | Adjustment, assumptions, estimator hierarchy | Retain unchanged | Do not change primary/secondary/exploratory hierarchy. |
| `chapters/08_robustness_sensitivity_validation.tex:7-87` | Diagnostics/provenance design | Retain but subordinate; add paper-derived context | Reorganize as converging evidence; add clinical-comparison method and evidence-class separation. |
| `chapters/10_results.tex:4` | Evidence hierarchy starts from pipeline/result admission | Reframe | Introduce characterization of the two testbeds. |
| `chapters/10_results.tex:6-58` | Counts and proxy prediction | Retain but subordinate | Label prediction as recoverability; add mortality prediction only after provenance gate. |
| `chapters/10_results.tex:60-281` | CATE, matching, estimator comparisons | Retain unchanged | Add sign/rank/magnitude synthesis without altering current tables. |
| `chapters/10_results.tex:286-340` | Cross-dataset and diagnostic status | Retain but subordinate; add paper-derived context | Add clinical corroboration and verified permutation summary; gate OVB numbers. |
| `chapters/10_results.tex:343-345` | Provenance boundary | Retain but subordinate | Keep as enabling credibility rather than principal contribution. |
| `chapters/11_discussion.tex:4-18` | Central result and main-RQ answer are integration feasibility | Reframe | Answer testbed-construction and usefulness question. |
| `chapters/11_discussion.tex:20-27` | Contracts and aggregation | Retain but subordinate | Preserve as construction evidence. |
| `chapters/11_discussion.tex:32-57` | Empirical answers | Retain but reorganize | Organize under converging evidence and disagreement, not pipeline stages. |
| `chapters/11_discussion.tex:68-73` | Contribution lies in connecting layers | Reframe | State representation-layer/testbed contribution first. |
| `chapters/11_discussion.tex:75-145` | Threats, clinical/causal/provenance boundaries | Retain unchanged | These prevent testbed framing from becoming benchmark/truth overclaim. |
| `chapters/11_discussion.tex:116` | Cross-dataset result framed as engineering portability | Reframe | Call it resource/testbed portability with no pooling or common estimand. |
| `chapters/12_conclusions_future_work.tex:9-11` | Study summarized as connected workflow | Reframe | Lead with construction of two observational testbeds. |
| `chapters/12_conclusions_future_work.tex:16` | “Strongest contribution” is integration | Reframe | Make testbed construction and characterization strongest. |
| `chapters/12_conclusions_future_work.tex:18-20` | Prediction and estimator results | Retain unchanged | Already bounded. |
| `chapters/12_conclusions_future_work.tex:22` | Results support connecting components | Reframe; remove only if redundant | Replace with usefulness/limitations conclusion. |
| `chapters/12_conclusions_future_work.tex:27-38` | Limitations and future work | Retain unchanged | Essential research boundary. |
| `chapters/12_conclusions_future_work.tex:43` | Integration itself is the object of evidence | Reframe | Transparency remains enabling; observational testbed is the object. |
| `appendices/appendices.tex:4-13,93-165` | Reproducibility interface and reusable datasets | Retain but subordinate | Call these release/reproduction interfaces for the testbeds. |

## 6. Chapter-by-Chapter Intervention Map

| Active file | Exact target | Intended conceptual change | Preserve | Scale |
|---|---|---|---|---|
| `thesis/main.tex` | Include order only | No edit expected | Complete document order | None |
| `frontmatter/administrative_metadata.tex` | English title in Step 2; Hebrew title after translation review | Testbed construction primary | Author/supervisor metadata | Small |
| `frontmatter/title_pages.tex` | Macro consumer | Layout verification only | Existing title-page mechanics | None |
| `frontmatter/hebrew_cover.tex` | Macro consumer | Layout verification only | Existing cover mechanics | None |
| `frontmatter/abstract_primary.tex` | Entire short abstract | Evaluation gap → construction → converging evidence → limits | All exact facts and cautions | Major-but-localized |
| `frontmatter/abstract_secondary.tex` | Entire short Hebrew abstract | Mirror final English hierarchy | Scientific equivalence and boundaries | Major-but-localized |
| `frontmatter/keywords.tex` | Keyword lines | Add testbed/evaluation terms | Existing domain/method terms | Small |
| `frontmatter/nomenclature.tex` | Optional definitions | Define observational testbed/answer key if used | Existing notation | Small |
| `chapters/01_introduction.tex` | Motivation; gap/objective; RQs/contributions | Establish evaluation problem and testbed proposition | ICU irregularity, deterministic/LLM boundary, no-truth/no-clinical claims | Major-but-localized |
| `chapters/02_background_related_work.tex` | Opening positioning and closing synthesis | Add evaluation-design spectrum and gap | ICU, irregular time series, phenotyping, DAG/HTE background | Medium |
| `chapters/03_problem_definition_study_design.tex` | Design/execution and task framing; closing RQ | Define two observational resources and representation intervention | Source-observed objects, five tasks, causal assumptions | Medium |
| `chapters/04_data_preprocessing.tex` | Dataset opening sentences | “Exercise pipeline” → instantiate separate resources | Contracts and provenance | Small |
| `chapters/05_proxy_state_construction.tex` | Opening/rationale plus shock-figure insertion | Controlled representation design; concrete deterministic example | Rules, missingness semantics, five-source aggregation | Medium |
| `chapters/06_predictive_modeling.tex` | Opening and interpretation sentence | Prediction as recoverability evidence | Model/training/export details | Small |
| `chapters/07_causal_methodology.tex` | DAG opening/captions context | DAGs as explicit testbed assumptions | All assumptions and estimator hierarchy | Small |
| `chapters/08_robustness_sensitivity_validation.tex` | Chapter framing and evaluation method | Define converging-evidence axes and clinical-comparison protocol | Support, sensitivity, permutation, provenance distinctions | Medium |
| `chapters/10_results.tex` | Opening; new localized synthesis subsections/table | Report resource characterization, agreement, clinical comparison, diagnostics | Every admitted existing number/table and estimator hierarchy | Major-but-localized |
| `chapters/11_discussion.tex` | Main answer/contribution synthesis | Interpret usefulness and limitations of testbeds | Full threat-to-validity analysis | Major-but-localized |
| `chapters/12_conclusions_future_work.tex` | Summary, strongest contribution, closing | Testbed contribution primary | Results, limitations, future work | Major-but-localized |
| `appendices/appendices.tex` | Reusable-dataset/reproduction framing | Reproduction interface for resources | Exact status/provenance boundaries | Small |
| `literature/metadata/references.bib` | Five verified missing paper entries | Support evaluation-spectrum discussion | All current keys/entries | Small |

No broad rewrite is justified. Most technical chapters require only a new governing sentence or a localized synthesis; equations, tables, rules, estimator mechanics, and existing limitations should remain stable.

## 7. Contribution-Hierarchy Map

| Rank | Current thesis hierarchy | Recommended hierarchy | Disposition |
|---|---|---|---|
| 1 | Integrated, evidence-tracked end-to-end framework | Two clinically grounded observational causal-analysis testbeds constructed from source-observed irregular ICU data | Replace top-level claim |
| 2 | LLM-guided rules/DAGs and shared proxy interface | Controlled representation-layer design plus deterministic patient-level instantiation | Elevate and sharpen |
| 3 | Four-model prediction and five-source aggregation | Transparent construction mechanism and proxy-recoverability characterization | Retain, subordinate |
| 4 | DAG adjustment, matching, three estimators | Converging characterization of usefulness and failure modes | Retain, reorganize |
| 5 | Evidence infrastructure and provenance | Auditability/reproducibility infrastructure enabling credible resource release | Retain, subordinate |

The core proposition should be: CliniCause offers observational realism without claiming a counterfactual answer key. Its value comes from exposing method behavior under clinically and operationally plausible measurement, missingness, support, proxy, graph, and confounding difficulties. The integration story remains the mechanism that makes this evaluation object inspectable.

## 8. Research-Question Recommendation

### Recommended main research question

> How can clinically grounded observational causal-analysis testbeds be constructed from source-observed irregular ICU records without generating exposure assignments or outcomes, and what converging evidence can characterize their usefulness and limitations for evaluating causal estimators?

This wording makes construction and evaluation primary, explicitly distinguishes the resources from synthetic truth-known benchmarks, and does not imply that “usefulness” is causal correctness.

### Recommended secondary questions

1. How can clinically and literature-grounded representation designs be instantiated deterministically and separately in MIMIC-III and PhysioNet while retaining source-specific measurement and missingness processes?
2. Which data contracts, normalization, aggregation, DAG, adjustment, and provenance mechanisms make the constructed resources auditable and reproducible?
3. How recoverable are the deterministic proxy labels from irregular time series, and how much mortality-relevant predictive information do the constructed proxy representations retain?
4. What converging evidence—estimator sign/rank/magnitude agreement, clinical-literature comparison, matching/support, permutation disruption, and omitted-variable sensitivity—characterizes each resource?
5. Which limitations prevent the resources from being interpreted as clinical validation, known causal truth, or proof of estimator correctness?

### Mapping from current SRQs

| Current SRQ | Recommendation |
|---|---|
| SRQ-1 data contracts | Merge into recommended SQ2; subordinate enabling contribution |
| SRQ-2 LLM proposals/encoding/provenance | Rewrite and merge into SQ1/SQ2 |
| SRQ-3 model performance | Rewrite as SQ3 proxy recoverability and mortality-relevant information |
| SRQ-4 normalization/aggregation | Merge into SQ2 |
| SRQ-5 DAG adjustment | Merge into SQ2 and treat graphs as assumptions |
| SRQ-6 matching/CATE/sensitivity/permutation | Rewrite and broaden as SQ4 converging evidence |
| SRQ-7 limitations | Retain and sharpen as SQ5 |

## 9. Title Recommendation

Preferred thesis title:

> **CliniCause: Constructing Clinically Grounded Observational Testbeds for Causal Analysis from Irregular ICU Time Series**

The paper's shorter exact title is rhetorically stronger, but the suffix “from Irregular ICU Time Series” is appropriate thesis-level domain specificity and accurately reflects the active work. Avoid retaining “causal effect estimation” as an unqualified title claim because the primary scientific object is the testbed and the thesis repeatedly acknowledges intervention/identification limitations.

The title macros are centralized in `frontmatter/administrative_metadata.tex:3-4` and consumed by `title_pages.tex` and `hebrew_cover.tex`. There is no separate active PDF-title metadata string to synchronize. The current English title already wraps across several lines, so both title pages must be visually checked after the change.

The Hebrew title should be a scientifically equivalent, idiomatic translation of the final English title, reviewed by a fluent domain reader. It should preserve “observational,” “testbeds,” “causal analysis,” and “irregular ICU time series” without translating testbed as a benchmark with known truth. Step 2 may safely change only the English macro if Hebrew review is deliberately deferred and the temporary mismatch is logged; final release may not retain a mismatch.

## 10. Benchmark/Testbed Literature Gap

The current thesis has good background on ICU datasets, irregular time series, phenotyping, DAGs, HTE, overlap, and sensitivity, but it does not frame causal-method evaluation across degrees of synthetic control and observational realism. The word `testbed` does not occur in the active thesis.

Five paper bibliography entries are directly needed and currently absent from `thesis-writing/literature/metadata/references.bib`:

| Paper key | Role in the new framing | Thesis-bib status |
|---|---|---|
| `shalit2017ite` | Semi-synthetic IHDP-style evaluation using empirical covariates and simulated outcomes | Missing; exact-title search found no duplicate |
| `shi2019dragonnet` | ACIC/semi-synthetic treatment-effect evaluation | Missing; exact-title search found no duplicate |
| `alaa2019validating` | Validation/evaluation of causal models on semi-synthetic competition datasets | Missing; exact-title search found no duplicate |
| `gentzel2021experimental` | RCT-derived/OSRCT evaluation and the role of experimental data | Missing; exact-title search found no duplicate |
| `parikh2022validating` | Empirically anchored generated mechanisms/validation framework | Missing; exact-title search found no duplicate |

The paper names the Jobs/LaLonde setting but its final bibliography does not provide a dedicated citation key. Do not invent an entry or raw URL. Either discuss it generically under a verified cited source or defer it until a primary bibliographic record is supplied. Fully synthetic evaluation can be explained conceptually without adding an unverified citation. Optional model examples such as CEVAE/GANITE are not required for the minimum comparison and should not be added merely to enlarge the bibliography.

Insertion rule for Step 2: copy verified bibliographic metadata from the finished paper bibliography, search the thesis bibliography by key, DOI, and normalized title immediately before insertion, and preserve all 36 currently active citation keys.

## 11. Converging-Evidence Coverage Matrix

| Evaluation axis | Finished paper | Current thesis | Gap/action | What it can establish |
|---|---|---|---|---|
| Construct plausibility | Schema/literature design and informal ICU consultation | Literature-grounded rationale; no result-level consultation rating | Add a cautious qualitative result; state that no formal rating/adjudication was performed | Design plausibility only |
| Proxy recoverability | Four-model AUROC/AUPRC/minRP summary | Detailed Chapter 6 and Chapter 10 metrics | Reframe existing results as recoverability | Learnability/reproduction of rules, not construct validity |
| Mortality prediction | Logistic/MLP proxy-vector AUROC | Task mentioned; numeric result absent | Add only after numerical-lineage gate | Prognostic association, not causality |
| DML sign agreement | 19/19 | Present and frozen | Retain; move into converging-evidence synthesis | Directional stability under two models |
| All-estimator sign agreement | 18/19; PhysioNet shock exception | Present and frozen | Retain; do not call it voting or correctness | Bounded triangulation |
| Rank agreement | Spearman 0.983–1.000 MIMIC; 0.794–0.964 PhysioNet | Qualitative ranking differences only | Add after deriving from checked original-cohort rows with a frozen calculation record | Relative-order stability within resource |
| Magnitude agreement | Pairwise RMSE 1.08–2.57 percentage points | Exposure-level values and qualitative differences | Add verified summary; retain important outliers | Approximate model-scale agreement, not estimand identity |
| Cross-resource comparison | Shared-construct rank correlation about 0.533 | No pooled analysis; qualitative comparison | Add as contextual difference, not reproducibility failure | Resource dependence |
| Clinical-literature corroboration | Supplement table and interpretation | Absent | Add method in Chapter 8, compact result in Chapter 10, interpretation in Chapter 11 | Contextual compatibility/discrepancy, not causal validation |
| Matching | Secondary descriptive evidence | Rich, cautious section | Retain as supporting axis | Local descriptive comparison/support warning |
| Overlap/support | Limited paper treatment | Rich thesis design/results/limits | Retain; keep prominent | Empirical support constraints |
| Permutation disruption | `36/36` MIMIC and `34/40` PhysioNet DML comparisons at `|z|>2` | Availability/status only | The checked CSV exactly reproduces these counts; add as diagnostic, not p-values | Pipeline behavior under disruption |
| Outcome downsampling | Secondary | Rich and correctly secondary | Retain as robustness only | Population sensitivity |
| Omitted-variable sensitivity | Two intervals already include zero; first additional interval crosses near 1%; 12/19 remain at 5%-by-5% | Partial/failure statuses; no admitted unified numeric family | Do not import until exact calculation inputs/code/provenance are supplied and reconciled | Fragility under one sensitivity model, not confounding absence |
| Provenance/reproducibility | Concise | Much richer | Retain as enabling evidence | Auditability, not scientific validity by itself |

Two numerical gates require special care:

1. The paper reports PhysioNet proxy-vector mortality AUROC near 0.776/0.778, whereas `results/checked_mortality_prediction.csv` records original-cohort PhysioNet test AUROC approximately 0.736 for logistic regression and 0.738–0.740 for the MLP, on 7,993 records. MIMIC aligns at approximately 0.826/0.831. The pre-existing dirty paper voter CSVs also indicate a different cohort lineage. No PhysioNet mortality number should enter the thesis until the cohort, voter construction, producing command, split, and authoritative output are reconciled.
2. The current checked sensitivity table deliberately preserves partial/failed and reconstructed/native distinctions and says a single numerical family is not admitted. The paper's concise 1% and 12/19 claims require their exact scenario computation and input lineage before thesis insertion.

## 12. Clinical-Evidence Corroboration Map

The supplement compares CliniCause model-estimated mortality differences with selected published mortality contrasts. These are heterogeneous external reference points, not commensurate estimates and not a validation set.

| Construct | CliniCause range (percentage points) | Published comparator(s) | Comparability limits | Recommended use |
|---|---:|---|---|---|
| Renal/AKI | MIMIC 8.7–9.1; PhysioNet 9.1–12.0 | 8.1 matched, 30-day | Horizon/definition/adjustment differ | Compatible magnitude context |
| Hepatic/bilirubin | MIMIC 8.3–9.8; PhysioNet 6.0–10.7 | 7.4 matched | Same source database in one study but independent team; bilirubin threshold and combined proxy differ | Useful but not independent-dataset replication |
| Cardiac injury | MIMIC 18.8–25.9; PhysioNet 11.2–12.2 | 17.0 unadjusted; 17.9 matched | Cohorts/definitions/adjustment differ | Broad contextual overlap |
| Inflammation/sepsis | MIMIC 14.9–16.1; PhysioNet 6.7–7.2 | 5.0 matched; 9.1 matched; 8.9 matched/non-hospital setting | Sepsis populations, timing, and horizons differ | Mixed but informative context |
| Global severity | CliniCause estimates available | No defensible numeric comparator | Construct is broad and operationalized differently | State “no comparable numeric reference” |
| Shock | MIMIC 2.1–3.2; PhysioNet -2.7–0.4 | 11.1 unadjusted/non-hospital comparator | Strong cohort, intervention, support, and definition mismatch | Highlight discrepancy and PhysioNet instability |
| Coagulation/hematologic | PhysioNet 0.4–2.5; no separate MIMIC proxy | 19.5 matched; 15.3 unadjusted | MIMIC combines hepatic/coagulation; comparator cohorts differ | Highlight major discrepancy; do not diagnose cause |
| Respiratory failure | MIMIC 3.6–5.0; PhysioNet 6.3–6.5 | 15.0 other horizon/TMLE; 10.2–21 matched/non-hospital | Different ARDS definitions, horizons, and methods | Context with explicit non-equivalence |
| Neurologic dysfunction | MIMIC 3.2–3.5; PhysioNet 7.6–8.2 | 0.9 other horizon/marginal structural model | Delirium definition and horizon differ | Discrepancy context |
| Metabolic derangement | MIMIC 1.8–3.1; PhysioNet 7.8–9.1 | 31 unadjusted | Acidosis definition and confounding differ | Large discrepancy; hypothesis-generation only |

Source methods include mostly matching or unadjusted comparisons, plus two stronger but still non-commensurate TMLE/marginal-structural-model references. Populations include sepsis, surgical, COVID-era, older, and vasopressor-defined cohorts; outcomes span ICU, in-hospital, 28-, 30-, 90-day, and post-discharge horizons. Thresholds, observation windows, treatment-mediated measurements, missingness, DAGs, adjustment sets, support, and estimators all differ.

Recommended later integration:

- Chapter 8: one methods subsection defining source selection, extraction fields, and non-equivalence rules.
- Chapter 10: one compact synthesis table/subsection, not the full supplement table.
- Chapter 11: interpret both overlap and discrepancies as contextual evidence about the resources.
- Mandatory wording: “clinical-literature comparison,” “contextual corroboration,” or “broadly compatible/discrepant.” Prohibited wording: “causal validation,” “calibration to clinical truth,” “confirmed effect,” or any diagnosis of why a discrepancy occurred without an analysis.

## 13. Figure Integration Map

| Source asset / visible paper object | Verification | Recommended thesis destination and placement | Caption/label plan | Decision |
|---|---|---|---|---|
| Finished-paper Figure 1, inline TikZ in final source; user-supplied standalone copy `true-figure-1.png` | The new PNG matches the finished paper's rendered Figure 1 and inline TikZ content/flow exactly: all Design, Instantiate, and Evaluate nodes, labels, stage colors, within-stage arrows, and cross-stage arrows are present. SHA-256 `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a`; 1102×373 RGBA, fully opaque, 63,112 bytes. | Exact-copy to new `thesis/figures/clinicause_testbed_pipeline.png`, Chapter 1 after the testbed proposition | Caption: controlled schema/literature design is instantiated deterministically on source-observed ICU records, then characterized without a causal answer key; the LLM receives schema rather than patient records. Label `fig:clinicause-testbed-pipeline`. | **Approved source for Step 2; original blocker resolved** |
| `paper-aaai/figures/figure1_pipeline.pdf` | SHA-256 `3c1c0c63e04dfdba9d7aada3245948f3de59add7e6eb2bd4db1ded99d814c836`; vector PDF, 512.64×324 pt. It instead shows an older integration-heavy, dataset-lane pipeline with four models, five-source voting, DAG/provenance, and downstream diagnostics. | None | None | **Do not copy.** Filename is stale relative to the finished PDF. |
| Finished-paper Figure 2 / `figure3_shock_proxy_example.png` | SHA-256 `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295`; 1629×661 RGB; matches visible paper Figure 2 despite stale filename numbering | `thesis/figures/clinicause_shock_proxy_example.png`, Chapter 5 after design-time selection or MIMIC shock rule | Caption should say five observed-evidence clauses feed a deterministic selected rule; zero means the rule was not satisfied by observed evidence, not clinical absence. Label `fig:clinicause-shock-proxy-example`. | Exact copy in Step 3, not Step 2 |
| `paper-aaai/figures/figure2_estimator_agreement.pdf` | SHA-256 `335a8685d0794f68f158b98110d94b2a43d5617c8a1452c0787a872ee9055423`; vector PDF, 500.88×258.18 pt; shows 57 estimator/resource markers. It is not used in the visible finished paper, whose agreement synthesis is Table 3. | If admitted, `thesis/figures/clinicause_estimator_agreement.pdf`, Chapter 10 estimator-comparison synthesis | Caption must distinguish sign, rank, and magnitude and retain PhysioNet shock disagreement. Label `fig:clinicause-estimator-agreement`. | Prefer **replacement** of the simplistic direction-only figure, not an additional redundant figure; verify exact numeric source first |
| Active thesis direction-only figure | SHA-256 `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` | Current Chapter 10 | `fig:results-three-estimator-direction` | Candidate for replacement, with cross-reference migration |
| Active MIMIC/PhysioNet ranking figures | SHA-256 `e87b0d...` and `1a64ad...` | Current Chapter 10 | `fig:results-mimic-forest-ranking`; `fig:results-physionet-forest-ranking` | Retain unless later layout review finds redundancy |
| MIMIC/PhysioNet DAG figures | SHA-256 `79fa7209...` and `67d545d6...`; byte-identical to the paper/support sources | Current Chapter 7 | `fig:mimic-causal-dag`; `fig:physionet-causal-dag` | Do not duplicate or recopy; captions already say assumptions, not learned truth |

Readability notes: the shock raster is adequate at thesis page width, and the estimator-agreement asset is vector. The new pipeline PNG is sharp and readable at its native resolution; at the thesis's approximately 170 mm full text width it provides roughly 165 pixels per inch. That is adequate for the current line art and text but less robust than a vector export, so the compiled thesis page must be inspected at actual size and 100% zoom. Existing DAGs are high resolution but their labels are dense at page width; duplication would add pages without improving legibility. Every imported/replaced figure requires list-of-figures, caption, label, cross-reference, and page-break inspection.

Resolved discrepancy: the canonical plan named `paper-aaai/figures/figure1_pipeline.pdf`, but visual and source verification showed that file is not the finished paper's Figure 1. The user subsequently supplied the correct standalone rendering as `thesis-writing/true-figure-1.png`. The Step 1 boundary therefore supersedes the plan's stale source path and PDF destination extension: Step 2 must exact-copy the user-supplied PNG, verify matching source/destination hashes, and must not import the stale PDF.

## 14. Frozen-Content Inventory

### Story-bearing text

- Current English title: “CliniCause: An LLM-Guided Framework for Deep Proxy-State Prediction and Causal Effect Estimation in Multivariate Irregular ICU Time Series.”
- Current Hebrew title: the Hebrew macro at `frontmatter/administrative_metadata.tex:4`, expressing the same integration/LLM/deep-prediction/effect-estimation title.
- English abstract: `frontmatter/abstract_primary.tex`, SHA-256 `a79c0aa9830abc2173db57d3bee0c5d84982f90823306d32e1b0c75640d98513`.
- Hebrew abstract: `frontmatter/abstract_secondary.tex`, SHA-256 `9122dd2c1fc82d0bcb60dda5ad6a2ba233399d10207a31c4ff45d7e5e28e5a2c`.
- Main RQ: `chapters/01_introduction.tex:43-47`; mirrored in `chapters/03_problem_definition_study_design.tex:50`.
- Primary contribution: `chapters/01_introduction.tex:61-67`.
- Discussion main answer: `chapters/11_discussion.tex:6-18`.
- Strongest-contribution sentence: `chapters/12_conclusions_future_work.tex:16`.
- Machine-readable baseline for later numeric/text comparison: `logs/stage_5_5_frozen_content_snapshot.csv`, with table/figure value packets under `logs/stage_5_2_table_values/` and `logs/stage_5_2_figure_values/`.

### Fixed scientific facts and hierarchies

- Original causal-analysis records: MIMIC 26,845; PhysioNet 7,993. These are analysis rows, not raw-source totals.
- Prespecified analyzed proxy exposures: MIMIC 9; PhysioNet 10. Do not merge or pool them.
- Learned proxy models: STraTS, GRU, GRU-D, TCN.
- Archived aggregate: exactly five aligned sources—one deterministic rule-derived source plus four thresholded learned predictions.
- Estimator hierarchy: CausalForestDML primary; LinearDML secondary comparator; CausalPFN exploratory.
- Original-cohort signs: primary forest 9/9 positive MIMIC and 9/10 positive PhysioNet; PhysioNet shock negative.
- DML direction: 19/19 shared. All three estimators: 18/19; PhysioNet shock is the sole all-three exception.
- Matching is descriptive support and is not an independent causal validator.
- Outcome-downsampled analyses are robustness populations, not pooled with originals.
- Sensitivity/permutation source/status distinctions must remain intact.

### Active source hashes

| Source group | SHA-256 |
|---|---|
| `chapters/01_introduction.tex` | `7243065c927133cc045c7dac4c3e8dfaff8108ae689efce599e7cf5f7879205e` |
| `chapters/02_background_related_work.tex` | `84e51da713d5f8ebec9889d98ce3b523b4fc25f4519fc8ad8460569ec4fcc309` |
| `chapters/03_problem_definition_study_design.tex` | `6d2d2e1e6d1ae22106f513d483dbf3bc710699b3d289243f62f0da452a163521` |
| `chapters/04_data_preprocessing.tex` | `bd31df8a70b6e39df36eaa873f97c129ccc213f38142f7a2ebd853431f7a07d1` |
| `chapters/05_proxy_state_construction.tex` | `62382e2192d549c2a6e9573df0dd0379ff7e2aa1c13ee443115d6ad5236e2b9d` |
| `chapters/06_predictive_modeling.tex` | `65924f09d50a7940f87e7d3e18605dbf02864316ff316b2957584fd4e1166475` |
| `chapters/07_causal_methodology.tex` | `4a27307f796a3f48882a4e157ee0df685894311611f87d9580f9c5d920db8c7f` |
| `chapters/08_robustness_sensitivity_validation.tex` | `b071703b8e0333a1b013846add098b4da00d2b66c9cb1e812ddd3326d503acd8` |
| `chapters/10_results.tex` | `8245ca5e1e096b5990cc743dcae47dc250fa4144e11fd2d58f5bdb0c0d24730f` |
| `chapters/11_discussion.tex` | `21d91aea4e718cda3b93fb648764c5ff9b0fc0f3f00fe34ad491ecea87a289d9` |
| `chapters/12_conclusions_future_work.tex` | `2f4d51da337537e4e855ca88cb98260d9e1b8069c28063fdf87fd576ecf66c73` |
| `appendices/appendices.tex` | `1dbc796f65dbec8919fd44a7bbddd74089db07ec71ff2a67e49bc93ee62d99e4` |
| Active thesis bibliography | `15e59c0f6fd13056259716b3da31244c11c94b0d2e7460f46ea117451d44dbd2` |
| Current `thesis/main.pdf` | `ed7b1b9891f56dfe2775a5412c0c188711c0b8a4fd856cb2b75279fd192c26a4` (101 A4 pages) |

### Figures, labels, citations, and structure

- Five active scientific figures: two DAGs; MIMIC and PhysioNet primary-forest rankings; and original-cohort three-estimator direction agreement. Their exact paths, labels, and hashes are recorded in Section 13.
- Active labels total 98. Chapter labels include `chap:introduction`, `chap:background-related-work`, `chap:problem-definition-study-design`, `chap:data-preprocessing`, `chap:clinical-proxy-state-construction`, `chap:predictive-modeling-proxy-states`, `chap:causal-graph-effect-estimation-methodology`, `chap:experimental-design`, `chap:robustness-sensitivity-validation-design`, `chap:results`, `chap:discussion`, and `chap:conclusions-future-work`. The two Chapter 8 labels are aliases in one active chapter and should not be casually removed.
- Active citation keys total 36: `athey2019grf`, `bai2018tcn`, `banda_2018_electronic_phenotyping`, `bica_2021_individualized_treatment_effects_ehr_ml`, `che2018grud`, `chernozhukov2018dml`, `chernozhukov_et_al_2026_ovb_causal_ml`, `cho2014gru`, `cinelli_hazlett_2020_sensitivity`, `crump_et_al_2009_limited_overlap`, `curth_2024_ml_individualized_treatment_effects`, `darvariu_et_al_2024_llm_causal_graph_priors`, `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping`, `harutyunyan_2019_mimiciii_benchmark`, `hernan_robins_2016_target_trial`, `hernan_taubman_2008_well_defined_interventions`, `iwashyna_2015_hte_critical_care`, `johnson2016mimiciii`, `kdigo_2012_acute_kidney_injury`, `lipkovich_2024_modern_hte_methods`, `lipton_kale_wetzel_2016_missingness_rnns`, `oprescu_et_al_2019_econml`, `pearl_1995_causal_diagrams`, `ranieri_et_al_2012_berlin_ards`, `ratner_et_al_2016_data_programming`, `ratner_et_al_2020_snorkel`, `sharma_kiciman_2020_dowhy`, `silva2012physionet`, `singer_2016_sepsis3`, `singhal_et_al_2023_llm_clinical_knowledge`, `smit_2023_causal_inference_icu_scoping_review`, `sun_2026_review_irregular_medical_timeseries`, `taylor_et_al_2001_isth_dic`, `tipirneni2022strats`, `vincent_et_al_1996_sofa`, and `wager2018causalforest`.
- Rendered chapter numbering is sequential despite filenames skipping 09: the source `10_results.tex` renders as Chapter 9, Discussion as Chapter 10, and Conclusions as Chapter 11.

## 15. Terminology Audit

### Current counts and patterns

Case-insensitive occurrence counts across active thesis TeX provide orientation, not semantic judgment: `testbed` 0; `benchmark` 20; `ground truth` 4; `causal truth` 0; `validated` 28; `validation` 56; `causal effect` 7; `CATE` 90; `agreement` 20; `corroboration` 0; `recoverability` 0; `robust` 33; `robustness` 33; `LLM` 90; `expert` 7; `diagnosis` 6; `clinical validation` 12; `causal identification` 6; `pooling` 8.

Most existing uses of “ground truth,” “clinical validation,” “diagnosis,” “agreement,” and “causal identification” are safe because they explicitly deny stronger status. Existing safe examples include Chapter 1's statement that a proxy is not a diagnosis or ground truth; Chapter 6's statement that prediction metrics quantify learnability rather than construct validity; DAG captions stating arrows are assumed; Chapter 10's “model-estimated CATE” and agreement disclaimers; and Chapters 11–12 on no pooling, no causal validity, and no clinical validation.

Potentially unsafe after reframing are unqualified uses of “benchmark,” “validation,” “causal effect,” and “robust.” Readers may infer that the new testbeds contain truth, validate estimators, identify effects, or are robust in an absolute sense. Current integration-first passages are not unsafe factually, but they would misstate the primary contribution if left governing the narrative.

### Standard definitions and wording rules

- **Observational testbed:** a reusable, inspectable observational resource for studying causal-analysis method behavior under realistic measurement, missingness, proxy, graph, support, and confounding challenges. It does not contain a known causal answer key.
- **Benchmark with known causal truth:** reserve for synthetic/semi-synthetic settings where the generating mechanism or counterfactual target is controlled and known. Never apply this phrase to CliniCause.
- **Model-estimated CATE:** retain for archived estimator outputs. Do not shorten to “causal effect” where the causal interpretation would become unconditional.
- **Proxy recoverability:** predictive performance against deterministic rule-derived proxy labels. It is not clinical validity, diagnostic accuracy, or construct correctness.
- **Clinical-literature comparison/contextual corroboration:** comparison with heterogeneous published mortality contrasts. It is not effect replication, clinical calibration, or causal validation.
- **Agreement:** always name the dimension—sign, rank, or magnitude—and the resource/estimators. Add that agreement does not establish accuracy, equivalence, or correctness.
- **Robustness/sensitivity:** identify the perturbation or model. Prefer “stable across the compared estimators” or “remains separated under the specified 5%-by-5% sensitivity scenario” over “robust.”
- **Validated:** reserve for a named validation act and object, such as schema validation or a checked source row. Do not let implementation validation imply clinical or causal validation.
- **LLM/expert:** use “LLM-assisted design proposal” and “project-selected/source-encoded.” Never call the LLM a clinical or causal expert on the evidence available.
- **Diagnosis/clinical validation:** proxy tags are not diagnoses; clinical validation remains future work.
- **Source-observed:** use for patient measurements, missingness patterns, support, and mortality. This does not mean error-free or causally sufficient.
- **Resource/testbed:** use “resource” for the released dataset/artifact package and “testbed” for its intended evaluation role. Use plural where referring jointly to MIMIC and PhysioNet.

## 16. Risk Register

| Risk | Severity | Likelihood | Affected files | Mitigation | Responsible step |
|---|---|---:|---|---|---|
| Accidental edit to finished paper | Critical | Low | `CausalDataGeneration.pdf`, root final TeX, `paper-aaai/**`, `supp.pdf` | Hash manifests before/after every step; no writes under protected paths | Every step |
| Superseded `paper.tex` controls edits | High | Medium | `paper-aaai/paper.tex`, thesis prose | Keep it explicitly excluded; use finished PDF/final TeX | Every step |
| Duplicate final source copies diverge | High | Medium | Root and `paper-aaai` final TeX | Compare bytes/hashes before and after | Every step |
| Broad thesis rewrite loses correct detail | High | Medium | All chapters | Follow localized intervention map; freeze methods/numbers/limits by default | Steps 2–4 |
| Numerical drift | Critical | Medium | Ch. 10, abstracts, Discussion, Conclusion | Compare to frozen snapshot and checked tables; calculate summaries reproducibly | Steps 3–5 |
| Bibliography duplication | Medium | Medium | `references.bib` | Key/DOI/title duplicate search before insertion | Step 2 |
| Unsupported benchmark claims | High | Medium | Chs. 1–3 | Define observational testbed vs truth-known benchmark; cite only verified entries | Step 2 |
| Clinical corroboration overstated | Critical | Medium | Chs. 8, 10, 11, abstracts | Preserve method/population/horizon mismatches; ban validation/calibration language | Steps 3–4 |
| Estimator agreement overstated | Critical | Medium | Chs. 10–12 | State sign/rank/magnitude separately; retain shock exception and no-accuracy caveat | Step 4 |
| Integration/provenance detail lost | High | Medium | Chs. 1–8, appendix | Subordinate rather than delete; retain contracts and evidence classes | Steps 2–4 |
| English/Hebrew abstract mismatch | High | High | Both abstracts | Finalize English, then domain-aware Hebrew synchronization and side-by-side review | Step 4/5 |
| English/Hebrew title mismatch | High | High | Administrative metadata/title pages | Translate after English title freeze; inspect both covers | Step 2/4/5 |
| Wrong pipeline figure imported | Critical | Low after resolution | Paper figure asset; Ch. 1 | Exact-copy only user-supplied `true-figure-1.png` at SHA-256 `15369f2a...`; never copy stale named PDF | Step 2 |
| Imported figure unreadable | Medium | Medium | Chs. 1, 5, 10; LoF | Prefer vector; inspect at actual page size and 100% zoom | Steps 2–5 |
| Duplicate/redundant figures | Medium | Medium | Chs. 7, 10 | Do not duplicate DAGs; replace direction-only agreement if using richer asset | Steps 3–4 |
| LoF/cross-reference breakage | High | Medium | Figure labels and references | Unique labels; compile; scan undefined/duplicate refs and LoF | Steps 2–5 |
| Page-layout regression | Medium | High | Title, abstracts, figure pages | Visual PDF diff/review after each step | Steps 2–5 |
| Raw URLs replace bibliography entries | Medium | Low | Chs. 1–3, bibliography | Use verified BibTeX entries and citations only | Step 2 |
| Model hierarchy changes accidentally | Critical | Low | Chs. 1, 7, 8, 10–12 | Freeze forest primary, linear secondary, PFN exploratory wording | Steps 2–5 |
| Testbeds implied to have causal truth | Critical | Medium | Title, abstracts, Chs. 1–3, 10–12 | Repeat no-answer-key/no-estimator-accuracy distinction at governing passages | Steps 2–5 |
| Mortality-prediction lineage mixed | Critical | High | Chs. 10–12, abstract | Reconcile 7,993 vs dirty voter/cohort lineage before importing PhysioNet AUROC | Before Step 4 |
| OVB summary imported without admitted source | Critical | High | Chs. 8, 10–12 | Supply exact scenario inputs/code/output and evidence-class decision | Before Step 4 |

## 17. Recommended Step 2 Boundary

Step 2 should remain the intellectual-proposition reframe only. Once the pipeline-figure blocker is resolved, the exact allowed-file list should be:

```text
thesis-writing/thesis/frontmatter/administrative_metadata.tex
thesis-writing/thesis/chapters/01_introduction.tex
thesis-writing/thesis/chapters/02_background_related_work.tex
thesis-writing/thesis/chapters/03_problem_definition_study_design.tex
thesis-writing/literature/metadata/references.bib
thesis-writing/thesis/figures/clinicause_testbed_pipeline.png   # new; exact copy of user-supplied true-figure-1.png only
```

Step 2 may update the English title macro. The Hebrew title should remain untouched until an equivalent translation is ready, with the temporary mismatch explicitly logged; alternatively, include a reviewed Hebrew title in the same step. No other front matter belongs in Step 2.

Step 2 must keep frozen:

- all finished paper/supplement files and the entire `paper-aaai` tree;
- `thesis/main.tex`, title-page/cover implementation, both abstracts, keywords, nomenclature, acknowledgements;
- Chapters 4–8 and 10–12;
- appendices, active tables, existing figures, all code/results/reproducibility records;
- the shock and estimator-agreement figure imports, which belong to later evidence-focused steps;
- every existing numerical value, estimator hierarchy, citation key, label, and section heading outside the six allowed paths.

The standalone pipeline asset is part of the minimum Step 2 story. Its authority is now resolved: source `thesis-writing/true-figure-1.png`, SHA-256 `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a`. Step 2 must copy those exact bytes to the allowed thesis figure destination and record equal hashes. The stale `paper-aaai/figures/figure1_pipeline.pdf` remains prohibited.

## 18. Paper Protection Verification

Protected hashes before the task are recorded in Section 2. The required post-write commands produced:

| Protected artifact | SHA-256 after | Matches before |
|---|---|---|
| `thesis-writing/CausalDataGeneration.pdf` | `9c7a3473301fcab7a652985ed7f4fbf765a4de197eec53cc7ffe89a5996193f1` | Yes |
| `thesis-writing/aaai27-submission.tex` | `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6` | Yes |
| `thesis-writing/supp.pdf` | `a0fa0eca32b043877dbc98a357cb8eb4844416c856fe8a748781ac456d72b3` | Yes |
| Sorted 65-file `paper-aaai` hash manifest | `8d4255c108c4417d6b21fd3e788f1582e81b6f5e27519d3a115571acf27ca008` | Yes |

- `diff -u /tmp/testbed_alignment_paper_aaai_hashes_before.txt /tmp/testbed_alignment_paper_aaai_hashes_after.txt` returned exit 0 and no output.
- Changed protected-file count relative to the captured task baseline: **0**.
- Two files inside `paper-aaai` were already modified at baseline (`mimic-mortality-voters.csv` and `physionet-mortality-voters.csv`); their exact baseline bytes were preserved. The zero count above is a before/after task comparison, not a claim that the user's worktree is globally clean.

## 19. Git Diff and Worktree Verification

Final command results after writing this report:

- `git diff --check`: exit 2, with 172 trailing-whitespace findings in five **pre-existing modified CSVs**: the three `advisor/clinical-evidence-supplement` CSVs and the two `paper-aaai/*-mortality-voters.csv` files. This report has zero trailing-whitespace lines. The task did not alter or repair the user's pre-existing files.
- `git diff --stat` (tracked files only):

  ```text
   prompt.txt                                         | 1074 +++++++++++---------
   .../dag_edge_evidence.csv                          |  206 ++--
   .../proxy_evidence.csv                             |   40 +-
   .../source_registry.csv                            |   46 +-
   .../paper-aaai/mimic-mortality-voters.csv          |   26 +-
   .../paper-aaai/physionet-mortality-voters.csv      |   26 +-
   6 files changed, 775 insertions(+), 643 deletions(-)
  ```

- `git diff --name-only` lists only the six pre-existing tracked modifications:

  ```text
  prompt.txt
  thesis-writing/advisor/clinical-evidence-supplement/dag_edge_evidence.csv
  thesis-writing/advisor/clinical-evidence-supplement/proxy_evidence.csv
  thesis-writing/advisor/clinical-evidence-supplement/source_registry.csv
  thesis-writing/paper-aaai/mimic-mortality-voters.csv
  thesis-writing/paper-aaai/physionet-mortality-voters.csv
  ```

- Final `git status --short`:

  ```text
   M prompt.txt
   M thesis-writing/advisor/clinical-evidence-supplement/dag_edge_evidence.csv
   M thesis-writing/advisor/clinical-evidence-supplement/proxy_evidence.csv
   M thesis-writing/advisor/clinical-evidence-supplement/source_registry.csv
   M thesis-writing/paper-aaai/mimic-mortality-voters.csv
   M thesis-writing/paper-aaai/physionet-mortality-voters.csv
  ?? thesis-writing/THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md
  ?? thesis-writing/logs/testbed_story_alignment_step_1_audit.md
  ?? thesis-writing/true-figure-1.png
  ```

- The baseline-to-final worktree delta introduced by the Step 1 task is exactly one untracked repository file: `thesis-writing/logs/testbed_story_alignment_step_1_audit.md`. The later `thesis-writing/true-figure-1.png` addition was explicitly made by the user and was only inspected by this task.
- Ordinary `git diff` excludes both untracked files, so `git status --short` is authoritative for their presence. The plan was pre-existing; the report is task-created.
- Nothing was staged, committed, or pushed.

## 20. Readiness

Step 1 is complete and the former Step 2 figure blocker is resolved. The user-supplied `thesis-writing/true-figure-1.png` has been verified against both the finished paper's rendered Figure 1 and the byte-identical final TeX source. It is now the authoritative source for the Step 2 pipeline-figure copy; the stale `paper-aaai/figures/figure1_pipeline.pdf` remains excluded.

No unresolved issue prevents the narrow Step 2 boundary in Section 17. The PhysioNet mortality-prediction and omitted-variable numerical discrepancies remain mandatory gates for Step 4 and must not be imported during Step 2.

READY FOR STEP 2
