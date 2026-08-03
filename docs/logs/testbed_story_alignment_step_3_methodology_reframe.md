# Testbed Story Alignment — Step 3 Methodology Reframe

## 1. Baseline

- Expected baseline: `80b2169fcc0282ef12277e2a4fa88e0592fccaaf` (`edit thesis step 2`).
- Actual `HEAD`: `80b2169fcc0282ef12277e2a4fa88e0592fccaaf`; the expected and actual baselines matched.
- Branch: `main`.
- Recent commits, newest first: `80b2169 edit thesis step 2`; `ea77b98 edit thesis step 1`; `1b444d9 paper sync`; `d609877 sync changes`; `d7d2fd9 Remove accidental nested repository link`; `9812e1f submodules merging`; `5d43de3 submodules merging`; `0fe0649 dataset-extract addition`; `61fbf58 dataset-extraction addition`; `10de05c AAAI P9`.
- Pre-existing modified files were `prompt.txt`, the three CSVs under `thesis-writing/advisor/clinical-evidence-supplement/`, and `thesis-writing/paper-aaai/{mimic,physionet}-mortality-voters.csv`. There were no pre-existing untracked files. These changes were treated as user-owned and were not edited.
- Applicable instructions read: `prompt.txt`; `thesis-writing/clinicause_thesis_operational_plan.md`; the Step 1 and Step 2 alignment reports; repository, thesis, figure, table, literature, and reproducibility README files; the thesis guide/plan; Chapters 1--8; and the authoritative paper materials identified below. No applicable `AGENTS.md` governed the thesis files.

## 2. Scope and Source Authority

- Objective: reframe Chapters 4--8 from a predominantly pipeline-first description into a testbed-construction and converging-evidence methodology, without changing the frozen scientific design or adding Step 4 results.
- Permitted existing files were the five chapter sources, the tracked thesis PDF, and the two prescribed new paths for the shock figure and this report.
- Protected files included Chapters 1--3, Chapters 9--12, abstracts, keywords, appendices, bibliography data, pipeline figures, final-paper sources/artifacts, and all files outside the explicit Step 3 allowlist.
- Sources inspected: `prompt.txt`; the canonical thesis plan; Step 1 and Step 2 reports; Chapters 1--8; `thesis-writing/CausalDataGeneration.pdf`; `thesis-writing/aaai27-submission.tex`; `thesis-writing/supp.pdf`; the final-paper tree where mandated; and the exact shock-proxy source image.
- Superseded plans, intermediate drafts, and non-authoritative paper variants were excluded as claim authorities. The `paper-aaai` tree was accessed only for the mandated finished-paper/figure verification and protection audit.
- Files actually changed or created by this step: Chapters 4--8, `thesis-writing/thesis/figures/clinicause_shock_proxy_example.png`, `thesis-writing/thesis/main.pdf`, and this report. No other repository file was changed by Step 3.

## 3. Step 2 Baseline Build

- Commands, run from `thesis-writing/thesis`, were three explicit XeLaTeX passes with Biber between the first and second: `xelatex -interaction=nonstopmode -halt-on-error -output-directory=<temp> main.tex`; `biber --input-directory=<temp> --output-directory=<temp> main`; then the XeLaTeX command twice more.
- Temporary build path: `/tmp/clinicause_thesis_step3_before.xWaYux`.
- PDF: `/tmp/clinicause_thesis_step3_before.xWaYux/main.pdf`.
- Result: 108 A4 pages, 3,088,260 bytes, SHA-256 `610a5b8190bef563308d86a31f0cbba55b82970cc8694deb38021ebeb1d125a6`.
- `qpdf --check` passed with no syntax or stream-encoding errors.
- Biber 2.19 processed 41 citekeys. No unresolved citations, references, duplicate labels, missing glyphs, or rerun requests remained.
- Pre-existing warnings: the biblatex Hebrew-language warning; overfull boxes of 2.32605 pt (list of tables), 6.44682 pt and 1.61385 pt (Chapter 5), 9.51868 pt (Chapter 7), 6.368 pt, 3.35918 pt, 4.64316 pt, and 3.29437 pt (results), and 8.91649 pt (discussion); plus one bibliography underfull box with badness 1019.

## 4. Chapter 4 Changes

- The opening now defines preprocessing as the observational-testbed instantiation layer and distinguishes source availability, cohort construction, measurement, and transformation.
- The two cohorts are described as separate observational resources with dataset-specific measurement processes; no cross-dataset pooling or implied interchangeability was introduced.
- Source-observed variables are distinguished from derived, harmonized, imputed, and otherwise transformed variables. The chapter ends with the required boundary that “observational data-generating and measurement processes remain unknown”.
- Existing cohort definitions, extraction rules, temporal alignment, missingness handling, quality checks, tables, numeric values, and preprocessing contracts were preserved.

## 5. Chapter 5 Changes

- The representation hierarchy is explicit: semantic design, deterministic executable instantiation, learned proxy annotations, and one downstream aggregate interface.
- LLM-assisted materials are described as design inputs rather than runtime inference. Active source code remains the authority for executable proxy definitions.
- Zero, missing, unavailable, and unobserved inputs are not conflated with a negative clinical state. Learned predictions are bounded as model annotations rather than diagnoses or ground truth.
- The aggregate is described as the fixed interface combining exactly one rule branch with STraTS, GRU, GRU-D, and TCN; it is not a consensus label, diagnosis, or validated clinical construct.
- All exact proxy rules, thresholds, labels, missingness behavior, aggregation composition, model scopes, and tables were deliberately preserved.

## 6. Shock-Proxy Figure

- Finished-paper verification: physical page 4 of `CausalDataGeneration.pdf` embeds the same 1629 by 661 RGB raster; pixel comparison against the source image produced absolute error zero.
- Source: `thesis-writing/paper-aaai/figures/figure3_shock_proxy_example.png`.
- Destination: `thesis-writing/thesis/figures/clinicause_shock_proxy_example.png`.
- Expected source SHA-256: `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295`.
- Actual source SHA-256: `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295`.
- Destination SHA-256: `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295`.
- Equality: `cmp` passed; source and destination are byte-identical.
- Placement: Chapter 5, immediately after the design-to-instantiation explanation, on physical PDF page 50 (thesis page 36), with a preceding prose reference.
- Caption: identifies the shock-proxy example and explicitly bounds rules as transparent instantiations, learned outputs as model annotations, and the aggregate as a downstream interface rather than ground truth or clinical validation.
- Label: `fig:clinicause-shock-proxy-example`.
- Visual review found the figure sharp, readable, unclipped, and correctly captioned at the rendered page size.
- The source figure and all other final-paper files remained unchanged.

## 7. Chapter 6 Changes

- Predictive modeling is framed as a proxy-recoverability experiment: it asks whether proxy annotations can be recovered from the implemented data representation.
- Existing architectures, inputs, splits, loss/metric descriptions, output schemas, and dataset-specific model selection were preserved. Dataset-specific leaders are not presented as universal superiority.
- Predictive performance is explicitly not clinical diagnosis, clinical construct validation, or evidence that a proxy is causally correct.
- Probabilities and binary exports have separate roles; exported annotations and their errors feed the fixed aggregate and therefore can propagate to downstream causal analyses.

## 8. Chapter 7 Changes

- The DAGs are project-specified, source-encoded representation assumptions. They were not learned from the observational data, validated edge by edge, guaranteed complete, or treated as clinical ground truth.
- Adjustment sets remain graph-derived interfaces under those assumptions; their use does not establish exchangeability or identification.
- The estimator hierarchy is unchanged: CausalForestDML is primary, LinearDML is the secondary comparator, and CausalPFN is exploratory with non-equivalent diagnostic support.
- Matching remains a secondary empirical-support diagnostic, not proof of positivity, balance, exchangeability, identification, or causal accuracy.
- All formulas, temporal assumptions, estimands, treatment/outcome definitions, DAG edges, adjustment sets, estimator configurations, uncertainty procedures, and diagnostic definitions were preserved.
- No graph, estimator, or executable method was changed. Agreement in sign, rank, or magnitude is bounded as converging evidence under a fixed representation and population, not causal accuracy.

## 9. Chapter 8 Changes

- Title decision: renamed to “Converging-Evidence Evaluation, Robustness, and Sensitivity” to make the non-answer-key evaluation role explicit.
- The chapter now organizes ten non-equivalent axes: construct plausibility; proxy recoverability; mortality-relevant predictive information; cross-estimator sign/rank/magnitude stability; clinical-literature comparison; matching/support; permutation/disruption; omitted-variable sensitivity; population perturbation; and provenance/evidence admission.
- Every axis states both its evidential role and its prohibited inference. The chapter explicitly rejects a single validation score or causal answer key.
- Clinical-literature comparison is specified as a structured contextual comparison recording proxy/relationship, population/setting, direction, effect measure or outcome, uncertainty, applicability, and limitations. It is not a meta-analysis, clinical validation, or causal validation.
- Empirical synthesis, clinical-comparison numbers, mortality-prediction numbers, estimator rank/RMSE results, and omitted-variable numerical summaries are deliberately deferred to Step 4.
- Formerly broad validation language was removed, qualified, or paired with explicit limits. Predictive recoverability, estimator agreement, clinical comparison, and sensitivity are never described as clinical validation, causal accuracy, causal validation, or proof against confounding.

## 10. Evaluation-Axis Coverage Matrix

| Method | Source chapter | Evidential role | Prohibited inference | Later result location |
|---|---|---|---|---|
| Construct plausibility | Chapters 5 and 8 | Makes proxy rationale and implementation inspectable | Clinical construct validity or diagnosis | Step 4, Chapter 9 synthesis |
| Proxy recoverability | Chapters 6 and 8 | Characterizes learnability from the implemented representation | Clinical correctness or diagnosis | Step 4, Section 9.2 |
| Mortality-relevant predictive information | Chapter 8 | Characterizes prognostic/resource information carried by annotations | Causal relevance or clinical validation | Step 4, Chapter 9 |
| Cross-estimator sign/rank/magnitude stability | Chapters 7 and 8 | Characterizes method dependence and converging behavior | Causal accuracy, identification, or a common estimand | Step 4, Sections 9.5--9.7 |
| Clinical-literature comparison | Chapter 8 | Provides contextual, population-aware corroboration or discrepancy | Meta-analysis, clinical validation, or causal validation | Step 4, Chapter 9 |
| Matching and empirical support | Chapters 7 and 8 | Describes pair availability and observed-support limitations | Positivity, balance, exchangeability, or identification | Step 4, Sections 9.4 and 9.8.2 |
| Permutation/disruption | Chapter 8 | Tests behavior after deliberately breaking labels or outcomes | Randomization, identification, or validity of the original analysis | Step 4, Section 9.8.2 |
| Omitted-variable sensitivity | Chapter 8 | Evaluates response to a specified confounding model | Actual confounding strength or proof against confounding | Step 4, Section 9.8.2 |
| Population perturbation | Chapters 7 and 8 | Characterizes dependence on the sampled population | External validity or absence of bias in the original population | Step 4, Section 9.8.1 |
| Provenance and evidence admission | Chapter 8 | Establishes traceability and claim admissibility | Scientific, clinical, or causal validity | Step 4, Section 9.8.3 |

## 11. Frozen-Content Verification

- Numeric-token comparison found one added occurrence of `2012`, solely in new dataset-framing prose; no technical numeric token was changed or removed.
- Proxy names, rule definitions, thresholds, label semantics, and executable/source-authority descriptions were compared. The proxy-name multiset is unchanged and no threshold changed.
- Preprocessing tables, longtables, and displayed equation blocks are byte-identical before and after; their combined SHA-256 is `34056661bf07facabc974df085728eb369d16f4032d482e63ca5ec0b90c7726d` in both inventories.
- Model names increased only where the new framing restated the fixed set: CausalForestDML 9 to 10, CausalPFN 11 to 12, GRU 11 to 12, GRU-D 10 to 11, LinearDML 10 to 11, STraTS 26 to 27, and TCN 10 to 11; EconML remained 7. No model scope, architecture, split, metric, or selection rule changed.
- Aggregation remained exactly one rule branch plus STraTS, GRU, GRU-D, and TCN. No vote composition or semantics changed.
- DAG edges and adjustment sets were not edited. Added prose only bounds their source-encoded role and assumptions.
- Estimator hierarchy, treatment/outcome definitions, estimands, formulas, uncertainty procedures, and exports were not changed.
- Matching, permutation/disruption, omitted-variable sensitivity, population perturbation, and provenance diagnostics retained their technical definitions; only evidential roles and limits were made explicit.
- Citation commands and citekeys are identical. The only added label is `fig:clinicause-shock-proxy-example`; added references are narrative cross-references and the new figure reference. No existing label, citation, or reference was removed.
- Unexplained frozen-content differences: none.

## 12. Post-Edit Build

- Exact commands, from `thesis-writing/thesis`: `xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step3_final4.Bjq1Oz main.tex`; `biber --input-directory=/tmp/clinicause_thesis_step3_final4.Bjq1Oz --output-directory=/tmp/clinicause_thesis_step3_final4.Bjq1Oz main`; then the same XeLaTeX command twice more.
- Temporary build path: `/tmp/clinicause_thesis_step3_final4.Bjq1Oz`.
- Validated PDF: `/tmp/clinicause_thesis_step3_final4.Bjq1Oz/main.pdf`.
- Result: 115 A4 pages, 3,243,866 bytes, SHA-256 `3ab6611a0363898008fd4387887c5781ddde9ac1d0879b81e9e79c970830775b`.
- `qpdf --check` passed with no syntax or stream-encoding errors.
- Biber 2.19 completed without errors and processed all 41 citekeys.
- No unresolved citation, reference, duplicate-label, missing-glyph, or rerun warning remained.
- Warning set is exactly the Step 2 baseline set listed in Section 3. The temporary Chapter 7 sub-point overflow found during drafting was removed before this final build.
- Compared with the Step 2 baseline, the final artifact adds seven pages because of the bounded methodology framing and exact shock figure; it introduces no new build warning.

## 13. Visual Review

- Changed page ranges: physical pages 44--80, corresponding to thesis pages 30--66 and Chapters 4--8.
- All 115 final pages were rendered as 1654 by 2339 PNGs at 200 dpi. Every changed page was inspected at original render resolution; representative front matter and every downstream chapter boundary were also checked.
- Chapter 4, physical pages 44--47: headings, paragraphs, citations, and chapter-ending whitespace are clean.
- Chapter 5, physical pages 48--56: representation prose and all landscape tables fit; no table or caption clipping was found.
- Shock figure, physical page 50: sharp, readable, correctly referenced and captioned, with prose following it and no isolated float page.
- Chapter 6, physical pages 57--61: the recoverability framing and export boundaries fit without new layout defects.
- Chapter 7, physical pages 62--72: both DAGs, estimator table, and final boundary paragraph are readable; the final page has no overflow.
- Chapter 8, physical pages 73--80: all evaluation-axis headings, long tables, and synthesis paragraphs fit and remain readable.
- Table of contents, physical page 7 onward, correctly shows the revised Chapter 8 title and section structure.
- List of figures, physical page 11, contains the shock-proxy entry with thesis page 36.
- Float movement is limited to the intended new Chapter 5 figure and consequent seven-page pagination shift; no unexpected float isolation or blank page was found.
- Title page (physical page 1), pipeline figure (physical page 19), downstream Chapters 9--12/appendix/bibliography (physical pages 81--114), and Hebrew cover (physical page 115) passed regression review. Downstream content matches the baseline apart from the expected page-number shift; the Hebrew cover is pixel-identical.
- Unresolved layout defects: none introduced by Step 3. The remaining warnings are the documented pre-existing baseline warnings.

## 14. Tracked Main PDF

- Old tracked `main.pdf`: 101 pages, 3,001,531 bytes, SHA-256 `ed7b1b9891f56dfe2775a5412c0c188711c0b8a4fd856cb2b75279fd192c26a4`.
- Step 2 baseline temporary PDF: 108 pages, SHA-256 `610a5b8190bef563308d86a31f0cbba55b82970cc8694deb38021ebeb1d125a6`.
- Final Step 3 PDF: 115 pages, 3,243,866 bytes, SHA-256 `3ab6611a0363898008fd4387887c5781ddde9ac1d0879b81e9e79c970830775b`.
- The validated temporary PDF and tracked `thesis-writing/thesis/main.pdf` pass `cmp` and have the same SHA-256.
- No `.aux`, `.bcf`, `.bbl`, `.blg`, `.log`, `.out`, `.run.xml`, `.toc`, or other build auxiliary was copied into the repository.

## 15. Paper Protection

- Before and after hashes are identical: `CausalDataGeneration.pdf` `9c7a3473301fcab7a652985ed7f4fbf765a4de197eec53cc7ffe89a5996193f1`; `aaai27-submission.tex` `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6`; `supp.pdf` `a0fa0eca32b043877dbcdb98a357cb8eb4844416c856fe8a748781ac456d72b3`; `true-figure-1.png` `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a`; and the shock source `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295`.
- A SHA-256 manifest comparison of all 65 files under `thesis-writing/paper-aaai` is identical before and after.
- Changed protected-file count: zero.
- The thesis pipeline figure remains SHA-256 `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a`, equal to `true-figure-1.png`.
- Shock source and thesis copy are byte-identical and both have SHA-256 `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295`.

## 16. Git Diff Summary

- Task-scoped `git diff --check` passes for all eight allowed Step 3 paths.
- Global `git diff --check` fails only on trailing whitespace already present in the five pre-existing modified CSVs: the three advisor evidence CSVs and the two paper mortality-voter CSVs. Those user-owned files were not modified to make the global check pass.
- `git diff --stat` reports 12 tracked modified files, 1,103 insertions, and 878 deletions across the combined pre-existing and Step 3 working tree; untracked files are not represented by that command. Within the five chapter sources, Step 3 has 80 insertions and 19 deletions, plus the binary `main.pdf` replacement.
- Step 3 changed-file list: `thesis-writing/thesis/chapters/04_data_preprocessing.tex`, `05_proxy_state_construction.tex`, `06_predictive_modeling.tex`, `07_causal_methodology.tex`, `08_robustness_sensitivity_validation.tex`, `thesis-writing/thesis/figures/clinicause_shock_proxy_example.png`, `thesis-writing/thesis/main.pdf`, and this report.
- Unexpected changes: none. A temporary comparison image accidentally created at repository root during visual auditing was immediately removed and is absent from final status.
- Final status also retains the six documented pre-existing modified files; the eight Step 3 paths are the only new task-owned modifications/untracked files.
- Nothing was staged, committed, or pushed.

## 17. Deferred Issues

- Step 4: empirical synthesis and result-bearing integration in Chapter 9.
- Step 4: disputed or gated numerical claims, including clinical comparison, mortality prediction, estimator ranking/RMSE, and omitted-variable summaries.
- Abstracts and keywords remain unchanged and deferred to their designated later step.
- Discussion and conclusions remain unchanged and deferred to their designated later step.
- Step 5 terminology/layout audit should revisit the out-of-scope Chapter 2 phrase “source-observed mechanisms” and the Chapter 1 occurrence of “MIMIC-IV”; neither could be edited in Step 3. Existing baseline layout warnings may also be revisited then.
- Hebrew front matter requires the planned human language review even though the rendered cover passed visual regression.

## 18. Readiness

READY FOR STEP 4
