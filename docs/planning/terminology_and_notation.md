# Terminology and Notation Plan

## A. Preferred Terminology

| term | preferred definition |
| --- | --- |
| irregular clinical time series | A patient/stay sequence of measurement events observed at nonuniform times. |
| measurement event | A tuple containing stay identifier, time since admission, measurement variable, and numeric value. |
| patient/stay/record | Use "stay" or "record" for the analysis unit; avoid implying unique human identity across admissions. |
| derived proxy state | A binary state derived from rules, predictions, or aggregation to summarize a clinically meaningful construct. |
| proxy phenotype | A phenotype-like construct derived from EHR data without chart-adjudicated validation. |
| clinically inspired proxy label | A weak label based on clinical thresholds/rules rather than verified diagnosis. |
| rule-derived proxy label | Preferred term for a proxy label assigned by deterministic source-code rules; it denotes supervision provenance rather than clinical ground truth. |
| rule-based proxy label | Acceptable synonym when emphasizing the labeling mechanism; prefer “rule-derived proxy label” when describing prediction targets. |
| predicted proxy state | A proxy-state label predicted by a time-series model. |
| aggregated predicted proxy-label representation | A binary downstream aggregate; in all archived final causal runs, the implemented vote combines one rule-derived source with four aligned predicted-label sources (GRU, GRU-D, STraTS, and TCN). |
| latent-tag prediction | Repository term for multi-label prediction of `LAT_*` proxy labels. |
| LLM-assisted clinical and causal knowledge elicitation | A substantive design-time method in which LLM output informed candidate proxy-state ontology, threshold rules, missingness reasoning, and DAG proposals. |
| LLM-generated design proposal | A candidate design artifact that requires project selection, source-code encoding, and separate validation; not an implemented rule or accepted causal graph by itself. |
| design-time LLM assistance | LLM use during framework design; distinct from runtime prediction, label aggregation, causal estimation, clinical validation, and data-driven causal discovery. |
| exposure | Preferred causal-analysis term for a `LAT_*` proxy state when intervention meaning is questionable. |
| treatment | Use only for code/config variables or when explaining estimator input; qualify as "proxy-state treatment variable". |
| outcome | In-hospital mortality (`in_hospital_mortality`). |
| confounder | Observed adjustment variable selected under the project-specified DAG and available in data. |
| project-encoded DAG | Preferred implementation term for a directed acyclic graph informed by LLM-assisted and other project design work, then explicitly encoded in source for adjustment logic. |
| project-specified DAG | Acceptable conceptual synonym for the accepted graph design; name the encoded source artifact when making an implementation claim. |
| adjustment set | The selected observed covariates used for matching/CATE adjustment. |
| effect modifier | Feature used to model heterogeneous effects/CATE variation. |
| matching estimate | Matched-pair outcome difference or mean matched-pair contrast. |
| average treatment effect | Use only if the estimand is formally approved; otherwise avoid. |
| conditional average treatment effect | Estimated per-row or feature-conditional effect under assumptions. |
| heterogeneous treatment effect | Variation in estimated effects across rows/features, not a treatment recommendation. |
| overlap | Support comparability between exposure groups in covariate space. |
| positivity | Assumption that exposure groups are available across covariate strata. |
| sensitivity analysis | Diagnostic analysis for unmeasured-confounding robustness. |
| robustness value | OVB/RV diagnostic from sensitivity workflow. |
| permutation check | Sanity check using shuffled treatment or outcome; not identification proof. |

## B. Prohibited or Restricted Terminology

| restricted term | condition for use |
| --- | --- |
| diagnosis | Only when referring to external clinical criteria or explicitly saying proxy labels are not diagnoses. |
| ground truth clinical state | Avoid for repository labels; use only for unavailable chart/adjudicated validation. |
| validated phenotype | Only after external validation/chart review evidence exists. |
| causal effect | Use as "estimated effect under assumptions"; avoid unconditional phrasing. |
| treatment recommendation | Do not use; clinical actionability is not established. |
| clinical actionability | Only in limitations/future work as not yet established. |
| latent variable | Use only when naming repository `LAT_*` artifacts; preferred thesis term is "proxy state". |
| LLM-discovered DAG | Avoid; use “LLM-informed, project-encoded DAG” and state that the proposal was not data-driven causal discovery or ground truth. |
| AI-validated proxy state / medically validated by the LLM | Avoid; LLM-assisted elicitation is not clinical validation or chart adjudication. |
| autonomous LLM design | Avoid unless a fully autonomous, documented workflow is evidenced; current artifacts support assisted design with unresolved selection/review provenance. |
| LLM-executed pipeline | Avoid; the LLM role is design-time, while source code performs labeling, prediction, aggregation, and causal estimation. |
| unbiased estimate | Avoid unless a formal estimator/assumption proof is provided. |
| proof | Avoid for empirical/diagnostic findings; use "evidence", "support", or "diagnostic". |

## C. Dataset Identifiers

| identifier | standard use |
| --- | --- |
| `ts_id` | Canonical join key for measurement events, outcomes, proxy labels, prediction exports, and causal outputs. |
| patient | Use sparingly; can imply a real individual rather than analysis record. |
| ICU stay | Preferred for MIMIC when `icustay_id` lineage matters. |
| record | Acceptable for PhysioNet `RecordID` lineage. |
| `icustay_id`, `ICUSTAY_ID` | Boundary aliases normalized to `ts_id` in MIMIC/STraTS loaders. |
| PhysioNet 2012 | Dataset in causal configs as `physionet`, in STraTS as `physionet_2012`. |
| MIMIC-III | Dataset in causal configs as `mimic`, in STraTS as `mimic_iii`. |
| causal processed artifact | `[ts, oc, ts_ids]`, unsplit. |
| STraTS processed artifact | `[events, oc, train_ids, val_ids, test_ids]`, split-aware. |

## D. Mathematical Notation

| object | notation | implementation alignment |
| --- | --- | --- |
| stays/records | \(i = 1,\ldots,n\) | Rows indexed by normalized `ts_id`. |
| measurement event | \((i, t, v, x)\) | `ts_id`, `minute`, `variable`, `value`. |
| measurement variables | \(v \in \mathcal{V}\) | Event `variable` names. |
| timestamps | \(t_{ij}\) | Minutes since admission. |
| static covariates | \(S_i\) | Age, Gender, Weight, ICUType variables, dataset-dependent. |
| rule-derived proxy label | \(L^{rule}_{ik}\) | Deterministic source-code `LAT_*` value used as weak supervision. |
| predicted probability | \(\hat p_{ik}^{(m)}\) | `<LATENT>_prob` from model \(m\). |
| binary predicted label | \(\hat L_{ik}^{(m)} = 1[\hat p_{ik}^{(m)} \ge 0.5]\) | Export threshold in STraTS. |
| aggregated predicted proxy-label representation | \(\widetilde L_{ik}\) | Majority vote across one rule-derived and four normalized binary prediction CSVs in the archived final runs; the generic implementation maps ties to 1. |
| exposure | \(A_i\) | Selected `LAT_*` proxy-state column in causal run. |
| outcome | \(Y_i\) | In-hospital mortality. |
| confounders | \(W_i\) | DAG-derived observed adjustment variables. |
| effect modifiers | \(X_i\) | CATE heterogeneity features. |
| potential outcomes | \(Y_i(a)\) | Conceptual only; intervention definition is [ADVISOR CHECK]. |
| ATE | \(\mathbb{E}[Y(1)-Y(0)]\) | Do not use for `mean_cate` unless approved. |
| CATE | \(\tau(x)=\mathbb{E}[Y(1)-Y(0)\mid X=x]\) | Estimated by DML/forest/PFN under assumptions. |
| mean estimated CATE | \(\bar{\hat\tau}\) | `mean_cate` over analyzed rows. |
| matching contrast | \(\bar\Delta_{match}\) | `mean_pair_effect`. |
| confidence interval | \([l,u]\) | Only where estimator/source provides interval fields. |
| sensitivity parameters | \(c_y, c_t, \rho\), RV | `cf_y`, `cf_d`/`cf_t`, robustness values depending on script output. |

## E. Abbreviation List

| abbreviation | meaning |
| --- | --- |
| ICU | Intensive Care Unit |
| EHR | Electronic Health Record |
| BGU | Ben-Gurion University |
| LLM | Large Language Model |
| DAG | Directed Acyclic Graph |
| STraTS | Self-Supervised Transformer for Sparse and Irregularly Sampled Multivariate Clinical Time-Series |
| GRU | Gated Recurrent Unit |
| GRU-D | Gated Recurrent Unit with Decay |
| TCN | Temporal Convolutional Network |
| DML | Double/Debiased Machine Learning |
| CATE | Conditional Average Treatment Effect |
| HTE | Heterogeneous Treatment Effect |
| ATE | Average Treatment Effect; use carefully |
| ATT | Average Treatment Effect on the Treated; use carefully |
| AUROC | Area Under the Receiver Operating Characteristic Curve |
| AUPRC | Area Under the Precision-Recall Curve |
| minRP | Maximum minimum of precision and recall |
| OVB | Omitted Variable Bias |
| RV | Robustness Value |
| PFN | Prior-Data Fitted Network, only if CausalPFN citation is resolved |
| SOFA | Sequential Organ Failure Assessment |
| AKI | Acute Kidney Injury |
| ARDS | Acute Respiratory Distress Syndrome |
