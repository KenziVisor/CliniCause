# Testbed Story Alignment — Step 4 Evidence Synthesis

## 1. Baseline

- Expected committed baseline: `92a06b2dd0aea5dc343e09de98d3e5ad50c2505d`.
- Actual starting `HEAD`: `92a06b2dd0aea5dc343e09de98d3e5ad50c2505d`; it matched the expected baseline, so no intervening commit classification or reset was needed.
- Branch: `main`.
- Recent commits at startup, newest first: `92a06b2 edit thesis step 3`; `80b2169 edit thesis step 2`; `ea77b98 edit thesis step 1`; `1b444d9 paper sync`; `d609877 sync changes`; `d7d2fd9 Remove accidental nested repository link`; `9812e1f submodules merging`; `5d43de3 submodules merging`; `0fe0649 dataset-extract addition`; `61fbf58 dataset-extraction addition`.
- Pre-existing user-owned modifications at startup: `prompt.txt`; `thesis-writing/advisor/clinical-evidence-supplement/dag_edge_evidence.csv`; `proxy_evidence.csv`; `source_registry.csv`; `thesis-writing/paper-aaai/mimic-mortality-voters.csv`; and `physionet-mortality-voters.csv`. There were no pre-existing untracked files. These files were preserved and were not edited by Step 4.
- Applicable instructions read: `prompt.txt`; `thesis-writing/THESIS_TESTBED_STORY_ALIGNMENT_PLAN.md`; the Step 1, Step 2, and Step 3 alignment reports; the complete active Chapters 1–8 and 10–12; active administrative metadata, abstracts, and keywords; `thesis-writing/general-instructions.pdf`; the BGU requirements map and university abstract requirements; the finished paper and supplement PDFs; their active source and bibliography; the focused paper evidence, reports, and evidence map; and the checked thesis evidence used below. No applicable `AGENTS.md` was present in the thesis path.

## 2. Scope and Source Authority

- Objective: align Results, Discussion, Conclusions, both abstracts, and keywords with the finished paper's testbed-first scientific contribution while retaining the thesis's richer tables and stricter admission boundaries.
- Permitted existing source files were exactly Chapters 10–12, both abstracts, keywords, and the thesis bibliography. The permitted new files were this report and one calculation CSV. Replacement of `thesis-writing/thesis/main.pdf` was permitted only after validation.
- Protected material included Chapters 1–8, appendices, title and administrative metadata, all figures and table-source evidence, code, datasets, result and checked-evidence CSVs, previous reports, finished paper/supplement artifacts, and the complete `paper-aaai` tree.
- Finished-paper authorities, in order: `thesis-writing/CausalDataGeneration.pdf`; `thesis-writing/aaai27-submission.tex`; `thesis-writing/supp.pdf`; and `thesis-writing/paper-aaai/supplementary1.tex`. The finished paper controlled public hierarchy and final claims; its source controlled exact values and wording; the supplement controlled external clinical comparisons and their qualifications.
- Checked thesis authorities included the active thesis tables, `thesis-writing/results/checked_cate_candidates.csv`, `checked_permutation_candidates.csv`, `checked_mortality_prediction.csv`, canonical `final-results` outputs, and the existing evidence maps and validation reports. These sources controlled conflicts, full precision, cohort and estimator status, and admission.
- Focused read-only supporting material under `thesis-writing/paper-aaai/evidence`, `reports`, `paper_evidence_map.md`, and the active paper source/bibliography was used only within the stated hierarchy.
- Excluded as scientific authority: `thesis-writing/paper-aaai/paper.tex`, `paper.pdf`, `thesis-writing/ignore-paper-aaai/**`, and `thesis-writing/paper-aaai/AuthorKit27/**`. No internet research or new experiment was performed.
- Step-4-created or Step-4-modified files: `thesis-writing/thesis/chapters/10_results.tex`; `11_discussion.tex`; `12_conclusions_future_work.tex`; `thesis-writing/thesis/frontmatter/abstract_primary.tex`; `abstract_secondary.tex`; `keywords.tex`; `thesis-writing/literature/metadata/references.bib`; `thesis-writing/logs/testbed_story_alignment_step_4_derived_statistics.csv`; this report; and the validated `thesis-writing/thesis/main.pdf`. No other repository file was changed by this task.

## 3. Baseline Build

- Working directory: `thesis-writing/thesis`.
- Clean output path: `/tmp/clinicause_thesis_step4_before.GyidYe`; PDF: `/tmp/clinicause_thesis_step4_before.GyidYe/main.pdf`.
- Commands:

```text
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step4_before.GyidYe main.tex
biber --input-directory=/tmp/clinicause_thesis_step4_before.GyidYe --output-directory=/tmp/clinicause_thesis_step4_before.GyidYe main
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step4_before.GyidYe main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step4_before.GyidYe main.tex
```

- Result: 115 A4 pages; SHA-256 `a3f63161c2df5eb016b62119cdf2ee235f7c592fd84affbb20ac0e577c0f2014`; 3,243,885 bytes.
- The initially tracked Step 3 PDF was also 115 pages, SHA-256 `3ab6611a0363898008fd4387887c5781ddde9ac1d0879b81e9e79c970830775b`, and 3,243,866 bytes. The two PDFs were not byte-identical. The difference was fully bounded to XeLaTeX/`xdvipdfmx` nondeterminism: creation metadata, PDF identifier, and six-letter embedded-font subset prefixes differed. Extracted text was byte-identical with SHA-256 `929390bee3540002ee4aa71ed7adcb8f90b53a675bfc661c6ea4e0cc82f993d2`, and all 115 pages rendered at 72 dpi were pixel-identical.
- Biber completed with 41 cited entries. The final baseline log had no undefined citation or reference, duplicate label, missing figure/glyph, or rerun request.
- Warnings were the existing unsupported Hebrew `biblatex` language warning, nine overfull boxes (maximum 9.51868 pt), and one bibliography underfull box (badness 1019). No blocking warning occurred.
- `qpdf --check` passed with no syntax or stream-encoding error.

## 4. Numerical Admission Decisions

### Candidate-level decisions

| Candidate | Decision and exact source | Population/model/unit | Conflict and qualification |
|---|---|---|---|
| Existing cohort and exposure counts | Already admitted and repeated without alteration from the active thesis tables: 26,845 MIMIC-III records with 9 analyzed exposures; 7,993 PhysioNet records with 10 | Separate original causal-analysis populations; records/exposures | Not raw or universally shared pipeline cohort counts; datasets remain unpooled. |
| Existing proxy recoverability | Already admitted and synthesized as test AUROC 0.867–0.918 from the active predictive table; STraTS leads archived MIMIC metrics and GRU-D leads PhysioNet | Four proxy-prediction models; test AUROC | Recoverability against rule-derived targets, not clinical validity or universal model superiority. |
| MIMIC mortality prediction | **Admitted.** Checked row: `thesis-writing/results/checked_mortality_prediction.csv`; canonical file: `final-results/causal-outputs/outputs-mimic-forest/mortality_prediction/mortality_prediction_results.txt`, SHA-256 `a1339f76d43636aef4b1e60093f75c636b87bd3957e9b0b8e90b33779a44e288`; paper table: `thesis-writing/aaai27-submission.tex` | 26,845 original records; 10 majority-vote proxy features; source-observed `in_hospital_mortality`; logistic-regression test AUROC 0.8260058670143415, displayed 0.826; MLP test AUROC 0.8309928292046938, displayed 0.831 | Checked source and paper agree at display precision. Stratified 80/10/10 split, seed 42, training-fitted `StandardScaler`, class-balanced logistic regression, and small PyTorch MLP are verified in `causal-irregular-time-series/src/mortality_prediction_using_latents.py`. This is prognostic association, not causal or clinical validation. It is intentionally absent from both abstracts. |
| PhysioNet mortality prediction | **Withheld.** Candidate paper source reports approximately 0.776/0.778; checked thesis rows in `checked_mortality_prediction.csv` record approximately 0.736–0.740 for 7,993 records, with a different voter/vector lineage | PhysioNet proxy-vector mortality AUROC | Unresolved cohort/voter lineage conflict. No value was inserted into Results, Discussion, Conclusions, or either abstract; no averaging or preferred lineage was chosen. |
| Within-resource rank correlation | **Admitted after reproduction** from original-cohort rows in `checked_cate_candidates.csv` | Three estimator pairs per resource; Spearman correlation of full-precision exposure ranks | MIMIC 0.983–1.000; PhysioNet 0.794–0.964. Stability, not estimator accuracy. |
| Within-resource RMSE | **Admitted after reproduction** from the same rows | Pairwise RMSE of mean model-estimated CATE, multiplied by 100 and reported in percentage points | MIMIC 1.35–2.57 pp; PhysioNet 1.08–2.04 pp. Estimator disagreement, not error against causal truth and not uncertainty. |
| Cross-resource correlation | **Admitted after reproduction** from nine explicit construct mappings, including shock | Spearman correlation of within-resource three-estimator mean ranks; original cohorts kept separate | Full precision 0.533333333333333, displayed 0.533. This describes resource dependence; effects were not pooled. Excluding shock produced 0.428571428571429 but was a validation-only calculation and was not admitted to thesis prose. |
| Permutation counts | **Admitted after independent recount** from `checked_permutation_candidates.csv` | Original cohorts; CausalForestDML and LinearDML; exposure × estimator × treatment/outcome permutation; 10 trials, seed 42; strict `abs(zscore_cate) > 2` | MIMIC 36/36; PhysioNet 34/40. These are disruption sanity checks, not p-values, randomization inference, or identification tests. The six PhysioNet non-passing comparisons were Forest coagulation/hematologic and shock for both targets, plus Linear coagulation/hematologic for both targets. |
| Omitted-variable sensitivity | **Unified numerical claim withheld** | Heterogeneous DML evidence classes | No paper 1% statement, no 12/19 count, and no unified threshold/count was inserted. The admitted conclusion is qualitative: agreement can coexist with fragility, while direct, reconstructed, partial, failed, and unavailable rows cannot be treated as one numerical family. |
| Clinical-comparison quantities | **Admitted with strict row-level qualification** from `supp.pdf`, `paper-aaai/supplementary1.tex`, and its verified references | Original-cohort three-estimator ranges and published absolute mortality contrasts, in percentage points | Every range is a range across estimators, never a confidence/uncertainty interval. Designs, horizons, population/construct differences, and noncommensurability are stated in Section 7 and in the Results table. |

No existing admitted table value was changed to fit a paper summary. Existing forest, linear, PFN, matching, and outcome-downsampled values retain their original sources, units, populations, and qualifications.

## 5. Derived-Statistics Reproduction

- Exact input: `thesis-writing/results/checked_cate_candidates.csv`, SHA-256 `2f550cf95e2acb9c1c7febf74735f0b36dfc2bd8592baf8e3d6dab5459252bff`; 114 data rows and 29 columns. Filtering `sampling_condition == original` selected all 57 full-precision rows: 9 MIMIC exposures × 3 estimators and 10 PhysioNet exposures × 3 estimators.
- Required columns: `dataset`, `estimator`, `sampling_condition`, `treatment`, and `mean_cate`. Joins were exact on the treatment code within a resource. No rounded LaTeX value entered a calculation.
- Spearman formula: assign ascending ranks to each estimator's `mean_cate` vector after treatment alignment, then compute Pearson correlation of the rank vectors. There were no ties.
- RMSE formula: `100 * sqrt(mean((mean_cate_a - mean_cate_b)^2))`; the factor 100 converts the archived outcome-scale proportion to percentage points.
- Cross-resource formula: map nine constructs explicitly, including shock; within each resource and mapped construct average the three original-cohort estimator means; compute Spearman correlation between the two nine-construct rank vectors. This averages estimators within a resource and construct, not patients or effects across resources.
- The reproduction was executed read-only with Ruby's standard `CSV` library from the repository root. The operative calculation was equivalent to:

```ruby
rows = CSV.read("thesis-writing/results/checked_cate_candidates.csv", headers: true)
          .select { |r| r["sampling_condition"] == "original" }
# Within each dataset: exact treatment join, ascending no-tie ranks,
# rho = Pearson(rank_a, rank_b),
# RMSE_pp = 100 * Math.sqrt(mean((mean_cate_a - mean_cate_b)**2)).
# Cross-resource: apply the nine-name mapping, average the three estimator
# means inside each resource/construct, then correlate the two rank vectors.
```

- Full-precision reproduced pairs:

| Resource | Pair | Spearman rho | RMSE (pp) |
|---|---|---:|---:|
| MIMIC | CausalForestDML–LinearDML | 0.983333333333333 | 1.348159856225453 |
| MIMIC | CausalForestDML–CausalPFN | 1.000000000000000 | 1.581648370527188 |
| MIMIC | LinearDML–CausalPFN | 0.983333333333333 | 2.573266321566426 |
| PhysioNet | CausalForestDML–LinearDML | 0.830303030303030 | 1.466655612668275 |
| PhysioNet | CausalForestDML–CausalPFN | 0.963636363636364 | 1.081537455663345 |
| PhysioNet | LinearDML–CausalPFN | 0.793939393939394 | 2.035048103464168 |

- Cross-resource full precision: 0.533333333333333 for nine mappings including shock. Eight mappings shared direction; shock remained the exception. The validation-only exclusion of shock yielded 0.428571428571429 and was deliberately not reported in the thesis.
- Paper comparison: all displayed Spearman values match within 0.0005, the half-unit tolerance for three-decimal rounding; all displayed RMSE values match within 0.005 pp, the half-unit tolerance for two-decimal rounding. Maximum absolute display differences were 0.000363636363636 for rho and 0.004951896535832 pp for RMSE. Cross-resource rho differed from the paper's 0.533 by 0.000333333333333.
- Admitted display values: MIMIC rho 0.983–1.000 and RMSE 1.35–2.57 pp; PhysioNet rho 0.794–0.964 and RMSE 1.08–2.04 pp; cross-resource rho 0.533.
- Machine-readable output: `thesis-writing/logs/testbed_story_alignment_step_4_derived_statistics.csv`; 22 data rows, 13 correctly parsed columns, SHA-256 `c2efb00f64d901fe1635221ee032155900b7f7ac369ecf0facb56358d88c7aea`.
- Permutation reproduction used `checked_permutation_candidates.csv`, SHA-256 `73d743bd76e3fbbe236c50d55d0b94c56c230d729470b011408b75d1a8539c6f`; 160 rows and 22 columns. Filtering to original cohorts and the two DML estimators selected 76 rows, and recounting `abs(zscore_cate) > 2` produced exactly 36/36 and 34/40.

## 6. Results Chapter Changes

- New hierarchy: Chapter 10 now opens as characterization of two separate observational causal-analysis testbeds. It explicitly keeps CausalForestDML primary, LinearDML secondary, CausalPFN exploratory, and original cohorts primary; integration and diagnostics are enabling evidence rather than the principal object.
- Construct plausibility: a bounded section records schema/literature grounding and informal ICU-clinician feedback while stating that no formal chart adjudication, blinded panel, inter-rater analysis, or clinical validation exists.
- Proxy recoverability: the former predictive-performance material was placed under this evaluation axis without altering its table; the 0.867–0.918 AUROC range and resource-specific leaders are synthesized as rule-target recoverability.
- Mortality information: the verified MIMIC logistic-regression and MLP AUROCs 0.826/0.831 were added as noncausal prognostic association. The analogous PhysioNet number is explicitly withheld for unresolved lineage.
- Estimator synthesis: sign, rank, and magnitude are separated. A compact new table reports within-resource sign agreement, rank-correlation ranges, and RMSE ranges without calling any of them accuracy.
- Cross-resource synthesis: the nine-construct correlation of 0.533 is presented as moderate resource dependence with an explicit no-pooling boundary.
- Clinical comparison: a ten-row contextual table compares original-cohort three-estimator ranges with verified published mortality contrasts and states that estimator ranges are not confidence intervals.
- Diagnostics/sensitivity: exact permutation units, 36/36 and 34/40 counts, strict threshold, and non-p-value interpretation were added. Omitted-confounding evidence remains qualitative because provenance classes cannot be unified.
- Provenance boundary: checked tables support transcription and artifact traceability, not a clean-checkout rerun, clinical validity, or identification.
- Old content preserved: all 113 original LaTeX table rows, all 76 checked proxy-result value rows, all original figures, cohort/proxy counts, estimator tables, matching rows, outcome-downsampled values, adjustment codes, and shock exception remain source-exact.

## 7. Clinical-Literature Comparison

Every CliniCause quantity below is an original-cohort range across CausalForestDML, LinearDML, and CausalPFN, in percentage points; it is not an uncertainty interval. MIMIC has 26,845 records and PhysioNet 7,993. Published quantities were copied only from the finished supplement and its verified bibliography.

| Proxy family | CliniCause MIMIC / PhysioNet (pp) | Published comparator, design, and horizon | Citation | Comparability limitation and interpretation |
|---|---:|---|---|---|
| Renal / AKI | 8.7–9.1 / 9.1–12.0 | 8.1 pp; propensity-score matched; 30-day mortality | `jiang2022akiattributable` | Broad scale compatibility only; AKI/proxy definitions, population, and horizon differ. |
| Hepatic / bilirubin | 8.3–9.8 / 6.0–10.7 | 7.4 pp; matched hospital-mortality contrast | `yang2021bilirubinmortality` | Overlap is contextual; the external study is a narrower bilirubin exposure from an independent team, despite a related MIMIC source and threshold. |
| Cardiac injury | 18.8–25.9 / 11.2–12.2 | 17.0 pp unadjusted; 17.9 pp matched; hospital mortality | `babuin2008troponin`; `lorenteros2020myocardial` | Broadly compatible scale, but ICU populations, troponin/myocardial-injury definitions, and adjustment differ. |
| Inflammation / sepsis | 14.9–16.1 / 6.7–7.2 | 5.0 and 9.1 pp matched; 8.9 pp matched with a three-year horizon | `shankarhari2018sepsis`; `jia2023sepsisaki`; `arbous2024sepsis` | PhysioNet overlaps part of the contextual range; MIMIC is larger. Sepsis constructs, case mix, adjustment, and horizons differ. |
| Global severity | 6.2–8.0 / 10.5–10.8 | No defensible numerical comparator retained | None | Directional clinical plausibility is not a numerical validation result; no external number was invented. |
| Shock | 2.1–3.2 / -2.7–0.4 | 11.1 pp; unadjusted; other, 90-day horizon | `lamontagne2020permissive` | Clearly discrepant and noncommensurate. PhysioNet contains negative DML and slightly positive PFN estimates; no protective effect or estimator vote is inferred. |
| Coagulation / hematologic | — / 0.4–2.5 | 19.5 pp matched; 15.3 pp unadjusted | `stephan1999thrombocytopenia`; `anthon2023ploticu` | Severe thrombocytopenia is narrower and more severe; MIMIC has no separate corresponding proxy. Discrepancy is retained. |
| Respiratory | 3.6–5.0 / 6.3–6.5 | 15.0 pp targeted minimum loss-based estimation; 10.2–21.0 pp matched; other horizons | `torres2021ards`; `saha2023ards` | ARDS definitions and mortality horizons are not equivalent to the operational proxy; values are discrepant context, not truth. |
| Neurologic | 3.2–3.5 / 7.6–8.2 | 0.9 pp; marginal structural model; other horizon | `kleinklouwenberg2014delirium` | Delirium is not the same construct; discrepancy may reflect definition, population, support, or transport differences. |
| Metabolic | 1.8–3.1 / 7.8–9.1 | 31.0 pp; unadjusted hospital-mortality contrast | `gunnerson2006acidosis` | Lactic acidosis is a narrower, more severe state than the proxy; discrepancy is not estimator-error evidence. |

No external study matches the same proxy definition, severity, population, adjustment, and mortality horizon. Compatible rows are contextual corroboration only; discrepant rows are equally retained as evidence of representation and transport challenges. None supplies causal ground truth for CliniCause.

## 8. Discussion Changes

- The main research question is now answered directly as construction and characterization of two dataset-specific observational causal-analysis testbeds from source-observed ICU records, without simulated records, assignment mechanisms, or outcomes.
- Five-SRQ mapping: SRQ-1 addresses representation instantiation; SRQ-2 covers contracts, aggregation, DAGs, and provenance as enabling machinery; SRQ-3 covers proxy recoverability and bounded mortality-relevant information; SRQ-4 integrates converging non-equivalent evidence; SRQ-5 states limitations and appropriate use.
- The principal contribution is testbed construction and characterization. Existing integration, contracts, five-source aggregation, graph interfaces, and provenance material was preserved and repositioned as what makes the representation inspectable.
- Estimator agreement is interpreted symmetrically: 19/19 two-DML sign agreement, 18/19 three-estimator agreement, high within-resource ranks, and bounded RMSE show stability under a fixed representation, not causal accuracy.
- PhysioNet shock remains central: negative Forest/Linear, slightly positive PFN, positive descriptive matching, and noncommensurate external evidence. It is not omitted, softened, averaged away, or described as protective.
- The clinical comparison gives compatible and discrepant families equal evidentiary status and treats global severity's missing comparator honestly.
- Permutation, support, matching, outcome perturbation, and heterogeneous sensitivity provenance are interpreted as limitations on convergence. Broad agreement and fragility can coexist.
- All existing limitation families were preserved: construct and measurement validity; intervention definition and causal identification; timing; positivity/support; uncertainty and modeling; external validity; computational and scientific reproducibility; LLM design risk; fairness, governance, and deployment boundaries.

## 9. Conclusions Changes

- Strongest contribution: a representation-centered framework for constructing observational causal-analysis testbeds, instantiated separately on MIMIC-III and PhysioNet, with assumptions and provenance exposed.
- Main findings: resource-dependent proxy recoverability; admitted MIMIC-only mortality association; all-positive MIMIC forest summaries; nine-positive/one-negative PhysioNet forest summaries; 19/19 DML and 18/19 three-estimator sign agreement; bounded rank/RMSE disagreement; moderate cross-resource correspondence; and PhysioNet shock as the central exception.
- Controlled-benchmark complementarity is explicit: CliniCause exposes behavior under realistic observed measurement, missingness, support, care-process, and outcome conditions, but cannot score causal error against truth and does not replace answer-key benchmarks.
- Integration remains a necessary enabling contribution, not the strongest scientific contribution.
- Future work now prioritizes blinded clinician review and chart-adjudicated labels; clinician-only/LLM/hybrid comparisons; prompt/model sensitivity; target-trial alignment; time-varying confounding; overlap, balance, uncertainty, multiplicity, measurement-error, rule-ablation, and alternative-DAG analyses; signed rerun manifests; external/prospective testbeds; fairness, governance, safety, and human factors; and a verified diagnostic plan before elevating CausalPFN.
- Closing perspective ends with the approved boundary: transparent representation and provenance make realistic observational testbeds inspectable; their value is exposing stability, disagreement, support limitations, and sensitivity under source-observed clinical conditions, not supplying causal truth.

## 10. Abstracts and Keywords

### Final claims

- The English abstract has four scientific paragraphs and 275 words by `detex`-based counting, below the university's 500-word maximum. It states the missing answer-key problem; complementary observational construction; bounded design-time LLM role; separate datasets/counts; four predictive models and three causal estimators; no pooling; proxy recoverability; sign agreement and shock exception; clinical, support, perturbation, and sensitivity findings; absent causal truth and clinical validation; prohibited treatment/deployment inference; and the controlled-benchmark complementarity contribution.
- The Hebrew abstract has the same four scientific paragraphs and 274 whitespace-delimited source tokens. It preserves the same populations, counts, models, hierarchy, metrics, exception, limitations, and contribution. English model/data names remain wrapped in `\textenglish{}` where needed.
- Neither abstract contains a citation or mortality-prediction AUROC. Both avoid claiming estimator accuracy, known truth, clinical validation, or deployment readiness.

### Claim-by-claim English–Hebrew equivalence matrix

Sentence identifiers count scientific sentences only, ignoring LaTeX heading commands.

| English claim | English sentence | Corresponding Hebrew sentence and distinctive wording | Result |
|---|---:|---|---|
| Real-world causal estimators lack an observed counterfactual answer key | E1 | H1: `אין לאומדים סיבתיים מפתח תשובות סיבתי נצפה` | Equivalent |
| Controlled benchmarks obtain known answers through simplification/generation | E1 | H1: `ערכות הערכה מבוקרות ... פישוט או ייצור` | Equivalent |
| CliniCause builds complementary observational testbeds while preserving source-observed ICU measurements, missingness, covariates, and mortality | E2 | H2: `ערכות מבחן תצפיתיות משלימות ... מדידות ... דפוסי חסר ... ותמותה` | Equivalent |
| Representations and assumptions are explicit | E2 | H2: `מציגות במפורש את הייצוגים וההנחות` | Equivalent |
| Schema/literature-grounded LLM acts only at design time | E3 | H3: `שעוגן בסכמות הנתונים ובספרות, סייע רק בשלב התכנון` | Equivalent |
| LLM proposes proxy constructs, rule families, and DAGs but sees no patient records and estimates no effects | E3 | H3: `מצבי־פרוקסי, משפחות כללים וגרפים סיבתיים; הוא לא נחשף ... ולא אמד ניגודים` | Equivalent |
| Project-selected proposals become deterministic rules/graphs | E4 | H4: `הצעות שנבחרו ... קודדו בכללים ובגרפים דטרמיניסטיים` | Equivalent |
| Separate MIMIC/PhysioNet resources have 26,845/9 and 7,993/10 | E5 | H5: `26,845 ... תשע ... MIMIC-III`, and `7,993 ... עשר ... PhysioNet 2012` | Exact numerical equivalence |
| Four predictive models are STraTS, GRU, GRU-D, TCN | E6 | H6 lists the same four models in the same role | Equivalent |
| Estimator hierarchy is primary Forest, secondary Linear, exploratory PFN; no pooling | E6 | H6: `כאומד ראשי ... כמשווה משני ... כאומד חקרני, ללא איגום` | Equivalent |
| Proxy-label test AUROC is 0.867–0.918; leaders differ by resource | E7 | H7: `טווח ... 0.867--0.918`; STraTS and GRU-D leaders named identically | Exact numerical/scientific equivalence |
| Two DML estimators agree in 19/19 directions and all three in 18/19 | E8 | H8: `בכל 19 ... ושלושת האומדים הסכימו ב־18 מתוך 19` | Exact numerical equivalence |
| PhysioNet shock is the exception: negative DML, slightly positive PFN | E9 | H9: `הלם ... היה החריג ... ה־DML היו שליליים ... CausalPFN היה חיובי קלות` | Equivalent |
| Clinical comparison contains both overlap and discrepancies | E10 | H10: `הן על חפיפה רחבה והן על פערים מהותיים` | Equivalent and symmetric |
| Agreement coexists with matching/support limitations, outcome perturbation, and omitted-confounding sensitivity | E11 | H11 lists `מגבלות התאמה ותמיכה`, `הפרעת התוצאה`, and `רגישות לערבול שהושמט` | Equivalent |
| Neither resource has known causal truth; constructs, graphs, and contrasts lack clinical validation | E12 | H12: `אין אמת סיבתית ידועה ... לא עברו תיקוף קליני` | Equivalent |
| Results do not establish treatment effects/recommendations or deployment readiness | E13 | H13: `אינן מבססות השפעות טיפול, המלצות טיפול או מוכנות להטמעה` | Equivalent |
| Integration/contracts/determinism/diagnostics/provenance make resources inspectable | E14 | H14: `אינטגרציה, חוזי נתונים מפורשים ... הופכים את המשאבים לניתנים לבדיקה` | Equivalent |
| Contribution is complementing controlled benchmarks by exposing stability, disagreement, support limits, and sensitivity under source-observed conditions | E14 | H15: `השלמת ערכות הערכה המבוקרות ... יציבות ... אי־הסכמות, מגבלות תמיכה ורגישות בתנאים קליניים שנצפו במקור` | Equivalent |

### Keywords

- Twelve aligned English terms were selected: observational causal-analysis testbeds; causal-estimator evaluation; representation-layer construction; irregular ICU time series; proxy states; LLM-assisted knowledge elicitation; causal machine learning; double machine learning; causal forests; omitted-variable sensitivity; MIMIC-III; PhysioNet 2012.
- Hebrew terms are semantically matched: `ערכות מבחן תצפיתיות לניתוח סיבתי`; `הערכת אומדים סיבתיים`; `בניית שכבת ייצוג`; `סדרות זמן לא־סדירות מטיפול נמרץ`; `מצבי־פרוקסי`; `הפקת ידע בסיוע LLM`; `למידת מכונה סיבתית`; `למידת מכונה כפולה`; `יערות סיבתיים`; `רגישות למשתנים שהושמטו`; and the two unchanged data-resource names.
- Human-review items: a native academic-Hebrew review remains required for register, punctuation, terminology preference, and final university submission styling. This is a linguistic quality gate, not a detected scientific mismatch; the source and rendered RTL layout are scientifically equivalent and visually sound.

## 11. Bibliography

- Fourteen verified entries were added by reusing the finished-paper keys and metadata: `jiang2022akiattributable`, `yang2021bilirubinmortality`, `babuin2008troponin`, `lorenteros2020myocardial`, `shankarhari2018sepsis`, `jia2023sepsisaki`, `arbous2024sepsis`, `lamontagne2020permissive`, `stephan1999thrombocytopenia`, `anthon2023ploticu`, `torres2021ards`, `saha2023ards`, `kleinklouwenberg2014delirium`, and `gunnerson2006acidosis`.
- Each key occurs exactly once in both the thesis bibliography and the finished paper bibliography. The thesis bibliography now has 62 entries.
- Normalized duplicate checks found 0 duplicate keys, 0 duplicate titles, and 0 duplicate nonempty DOIs. The `saha2023ards` author accent and metadata match the finished-paper block.
- All 14 added keys are cited in the clinical-comparison table. Final Biber output contains 55 cited entries and no unresolved citation.
- `thesis-writing/paper-aaai/references.bib` and the complete paper tree are byte-unchanged; no paper bibliography entry was edited.

## 12. Frozen-Content Verification

- Existing numerical-token inventory contained 881 occurrences. A multiset comparison found no deficit in any admitted result. The only raw-token count deficits were one standalone `6` and one standalone `7`, traced exactly to the intentionally replaced legacy headings `SRQ-6` and `SRQ-7`; they were section identifiers, not results. All new numerical occurrences were classified as repeated existing values, reproduced statistics, verified permutation counts, verified MIMIC mortality values, clinical comparators, or expected pagination/build changes.
- Table-row comparison: all 113 pre-Step-4 table rows in Chapter 10 occur byte-for-byte in the edited chapter; all 76 pre-existing proxy/result value rows are preserved. The new estimator-synthesis and clinical-context rows are additive.
- Figures: all 3 pre-existing `\includegraphics` targets in Chapters 10–12 are unchanged and still present. No figure was added, replaced, regenerated, or deleted.
- References: all 17 pre-existing `\ref{...}` targets remain present; the edited chapters now contain 19 distinct references. Build resolution passed.
- Labels: all 43 pre-existing labels remain present; the edited chapters now contain 51 distinct labels. No duplicate label was introduced.
- Citation keys: all 17 pre-existing chapter citation keys remain present; the edited chapters now contain 31 distinct keys after the 14 clinical additions.
- Estimator hierarchy is unchanged: CausalForestDML primary; LinearDML secondary; CausalPFN exploratory; original cohorts primary; outcome downsampling robustness only.
- Frozen counts and structures remain exact: 26,845 MIMIC records, 7,993 PhysioNet records, 9 and 10 exposures, four prediction models, one rule plus four predicted voters, unchanged proxy names and adjustment codes, no pooling, and the negative-DML/slightly-positive-PFN PhysioNet shock exception.
- Unexpected scientific or structural differences: 0.

## 13. Post-Edit Build

- Exact clean output path: `/tmp/clinicause_thesis_step4_exact.MtUCYs`; validated PDF: `/tmp/clinicause_thesis_step4_exact.MtUCYs/main.pdf`.
- Exact commands, run from `thesis-writing/thesis`:

```text
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step4_exact.MtUCYs main.tex
biber --input-directory=/tmp/clinicause_thesis_step4_exact.MtUCYs --output-directory=/tmp/clinicause_thesis_step4_exact.MtUCYs main
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step4_exact.MtUCYs main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/clinicause_thesis_step4_exact.MtUCYs main.tex
qpdf --check /tmp/clinicause_thesis_step4_exact.MtUCYs/main.pdf
```

- Result: 120 A4 pages; 3,265,383 bytes; SHA-256 `6f25ac51acdcc091518371dcf46d73b43d0e2e4634f3da19e9458ba133c88020`.
- Biber found and emitted 55 cited keys. XeLaTeX and Biber succeeded; `qpdf --check` found no syntax or stream-encoding error.
- Final logs contain no undefined citation/reference, duplicate label, missing glyph, missing figure, unresolved rerun request, or Type 3 font.
- Warnings exactly match the baseline warning classes and magnitudes: unsupported Hebrew `biblatex` language; nine overfull boxes at 2.32605, 6.44682, 1.61385, 9.51868, 6.368, 3.35918, 4.64316, 3.29437, and 8.91649 pt; and one bibliography underfull box at badness 1019. There is no new severe overfull box.
- Comparison with baseline: +5 pages, attributable to the bilingual abstract rewrite, Results/Discussion/Conclusions synthesis, clinical table, and 14 cited bibliography entries. Existing warning magnitudes did not worsen. Extracted final text SHA-256 is `0424cc7bcc98bf60afc27543180f9d92e65efcd0f19716f59f944a48af445866`.
- An independently isolated copied-tree release build had a different PDF byte hash solely from nondeterministic metadata/font-subset naming, but its extracted text matched and all 120 pages rendered at 200 dpi were pixel-identical to the exact prescribed build. The exact prescribed build is the tracked authority.

## 14. Visual Review

- All 120 post-edit pages were rendered individually at 200 dpi. The exact prescribed build and the previously reviewed isolated release had 0 pixel-different pages.
- Front matter reviewed individually: English title page 1; Hebrew abstract page 2; English abstract page 3; keywords page 4; table of contents pages 5–8; abbreviations/notation/list pages 9–14. The English title wraps correctly; both abstracts fit; the Hebrew abstract has correct RTL order, readable embedded English model/data names, and no missing glyph; keywords fit and align bilingually.
- Results review: every page 81–96. The new characterization hierarchy, mortality paragraph, sign/rank/magnitude table, cross-resource paragraph, diagnostics, and provenance synthesis are readable. The clinical-comparison longtable on page 92 fits, has readable columns/citations, and clearly labels estimator ranges as ranges rather than uncertainty. The final direction figure on page 96 is intact.
- Discussion review: every page 97–106. Main RQ and five-SRQ organization, clinical symmetry, shock interpretation, limitations, captions, references, and pagination are intact.
- Conclusions review: every page 107–109. The strongest-contribution reframe, future-work section, and closing perspective fit; no orphan heading or isolated closing paragraph remains.
- Pagination-moved pages reviewed: appendix pages 110–113; bibliography pages 114–119; Hebrew cover page 120. Bibliography entries and DOI/URL wrapping remain readable. The appendix remains unchanged in source.
- Regression pages reviewed individually: pipeline figure page 19; shock instantiation figure page 50; PhysioNet DAG page 64; MIMIC DAG page 65; list-of-figures/list-of-tables pages 11–14; and title/cover pages 1 and 120. Figures, captions, and list entries are unchanged and unclipped.
- Defects checked and not found: title overflow, abstract overflow, RTL reversal, missing Hebrew glyphs, table clipping, unreadable clinical rows, displaced captions, orphan headings, unintended isolated figure/table pages, new excessive whitespace, broken citations/references, incorrect figure-list entries, page-number anomalies, unintended blank pages, or new overfull-box defects.

## 15. Tracked Main PDF

- Previous tracked PDF: 115 pages; 3,243,866 bytes; SHA-256 `3ab6611a0363898008fd4387887c5781ddde9ac1d0879b81e9e79c970830775b`.
- Final tracked PDF: 120 pages; 3,265,383 bytes; SHA-256 `6f25ac51acdcc091518371dcf46d73b43d0e2e4634f3da19e9458ba133c88020`.
- `cmp` between `/tmp/clinicause_thesis_step4_exact.MtUCYs/main.pdf` and `thesis-writing/thesis/main.pdf` returned 0; they are byte-identical.
- Only `main.pdf` was copied into the repository. No `.aux`, `.bbl`, `.bcf`, `.blg`, `.lof`, `.log`, `.lot`, `.out`, `.run.xml`, or `.toc` file was copied from the build directory.

## 16. Paper Protection

All protected hashes below are identical before and after Step 4:

| Protected file | SHA-256 before and after |
|---|---|
| `thesis-writing/CausalDataGeneration.pdf` | `9c7a3473301fcab7a652985ed7f4fbf765a4de197eec53cc7ffe89a5996193f1` |
| `thesis-writing/aaai27-submission.tex` | `db42adca64a66c08152fbc214a6c144857d547700cbc59b079bc5a44301839b6` |
| `thesis-writing/supp.pdf` | `a0fa0eca32b043877dbcdb98a357cb8eb4844416c856fe8a748781ac456d72b3` |
| `thesis-writing/true-figure-1.png` | `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a` |
| `thesis-writing/paper-aaai/figures/figure3_shock_proxy_example.png` | `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295` |
| `thesis-writing/thesis/figures/clinicause_testbed_pipeline.png` | `15369f2a83ecb9c2a2ba76fc0e1efddd33a6e7934ec0f282e7536ff020b0325a` |
| `thesis-writing/thesis/figures/clinicause_shock_proxy_example.png` | `b7d7b3b5f1c52506442d847c99795d4f195f144cf19a7c61478225c64469f295` |

- Complete paper-tree manifests before and after each contain 65 files. `diff -u /tmp/testbed_alignment_step4_paper_aaai_before.txt /tmp/testbed_alignment_step4_paper_aaai_after.txt` returned 0.
- Changed protected-file count: 0.
- Thesis pipeline and shock figures are hash-identical to baseline. Both DAG source/images and every other existing thesis figure were preserved.

## 17. Git Diff Summary

- Required task-scoped `git diff --check` passes for every tracked Step 4 file. Supplemental `git diff --no-index --check /dev/null <file>` checks emitted no whitespace diagnostic for either new untracked Step 4 file; their exit status of 1 is expected because each new file differs from `/dev/null`.
- Global `git diff --check` reports trailing whitespace only in the five documented pre-existing user-owned CSV changes under `advisor/clinical-evidence-supplement` and `paper-aaai`; Step 4 did not edit or normalize them. The sixth pre-existing changed path is `prompt.txt`, which has no reported whitespace error. There is no task-caused whitespace error.
- `git diff --stat` reports 14 tracked modified files, 1,666 insertions, and 1,041 deletions. This includes the six pre-existing user-owned tracked modifications. The two new untracked Step 4 files are correctly absent from ordinary `git diff --stat` until staged; they are included in the status list below.
- Step-4 tracked changes: thesis bibliography; Chapters 10–12; English and Hebrew abstracts; keywords; and `thesis-writing/thesis/main.pdf`.
- Step-4 untracked additions: `thesis-writing/logs/testbed_story_alignment_step_4_derived_statistics.csv` and this report.
- Preserved pre-existing changes: `prompt.txt`; three advisor clinical-evidence CSVs; and two paper mortality-voter CSVs.
- Unexpected changed files: 0. No Chapter 1–8, appendix, title/administrative source, figure, paper source, code, dataset, result source, checked evidence, or previous report changed.
- Final status therefore contains 14 modified tracked paths and 2 untracked Step 4 paths. `git diff --cached --name-only` is empty.
- Nothing was staged, committed, or pushed.

## 18. Deferred Step 5 Issues

- Chapter 2 contains exactly one occurrence of the phrase `source-observed mechanisms`, at `thesis-writing/thesis/chapters/02_background_related_work.tex:31`. It was deliberately not edited and requires the mandatory Step 5 terminology audit.
- The alleged Chapter 1 `MIMIC-IV` occurrence does not exist: an exact search of `01_introduction.tex` found 0 occurrences. Step 5 should record that correction rather than assume the earlier report was accurate.
- Perform the planned global terminology audit across read-only material in Step 5, including consistent use of testbed/resource, source-observed records/outcomes, representation layer, and non-equivalent evidence.
- Obtain final native academic-Hebrew human review for wording, register, punctuation, and submission styling, even though scientific equivalence and rendered RTL passed.
- Remaining layout warnings are the pre-existing Hebrew `biblatex` language warning, nine small overfull boxes (maximum 9.51868 pt), and one bibliography underfull box (badness 1019).
- Administrative/submission metadata, ethics/governance statements, degree details, title pages, and university submission packaging remain read-only and require authoritative human/institutional confirmation where applicable.
- Unresolved numerical gates: PhysioNet mortality-prediction AUROC remains withheld until cohort/voter lineage is reconciled exactly; omitted-variable sensitivity remains qualitative until heterogeneous evidence classes can be reconciled without inventing a unified threshold/count.

## 19. Readiness

All Step 4 admission, preservation, bilingual-equivalence, bibliography, build, visual, tracked-PDF, protection, and Git gates pass. No existing admitted result changed; PhysioNet mortality was not inserted; no unified omitted-variable number was imported; every admitted derived and clinical statistic has reproducible or verified provenance and qualification; the estimator hierarchy, no-pooling policy, and shock exception remain explicit; the main RQ and strongest-contribution framing are testbed-first; the abstracts are scientifically equivalent; citations/references resolve; the paper tree is unchanged; and the tracked PDF equals the validated exact build.

READY FOR STEP 5
