# Stage 4.10C Front and Back Matter Decision Brief

Prepared before LaTeX edits.  Authorities inspected: Chapters 1, 3, 5, 7, 10, 11, and 12; the Stage 4.10B conclusion audit; the terminology and appendix planning records; the frozen result packet; and the local BGU requirements map.

## 1. Title audit

| field | decision |
| --- | --- |
| Current title | *A DAG-Guided Framework for Proxy-State Effect Estimation in Irregular ICU Time Series* |
| Claims implied by the title | A framework; project-specified DAG guidance; proxy-state rather than diagnosis-level analysis; effect estimation; irregular ICU time series. |
| Alignment with Chapter 1 objective | Aligned: Chapter 1 describes an evidence-tracked framework using clinically inspired proxy states under explicit causal assumptions for DAG-guided adjusted mortality contrasts. |
| Alignment with Chapters 10--12 | Aligned when ``effect estimation'' is read as model-estimated, observational, and conditional.  The title does not state clinical validation, an intervention effect, or deployment. |
| Potential overstatement | ``Effect estimation'' can be misread as an established causal effect unless the thesis boundaries remain prominent. |
| Potential understatement | The title does not name evidence tracking or prediction, but those are supporting components rather than a reason to broaden the title. |
| Recommended title | Retain the current title, marked **provisional pending author/supervisor approval**. |
| Alternative title candidates | (1) *An Evidence-Tracked Framework for Proxy-State Analysis in Irregular ICU Time Series*; (2) *DAG-Guided Observational Analysis of Proxy States in Irregular ICU Time Series*. |
| Human approval required | Yes: final English title, official Hebrew title, and whether the retained wording is acceptable for the approved degree/faculty form. |

No rendered title change is recommended: the current title materially aligns with the validated body and a stylistic change could alter its approved meaning.

## 2. Abstract claim set

| claim_id | claim | source chapter and exact location | number included | required qualification | English wording | Hebrew-equivalence note |
| --- | --- | --- | --- | --- | --- |
| ABS-01 | ICU records are irregular and missingness-aware representation matters. | Ch. 1, Motivation, lines 3--18. | No | Motivation only; not a causal finding. | ``Irregular ICU records...'' | States the same methodological motivation. |
| ABS-02 | The objective is an evidence-tracked framework connecting preprocessing, proxy states, prediction, and DAG-guided adjusted analysis. | Ch. 1, Thesis Gap and Objective, lines 26--38; Ch. 12, lines 9--16. | No | Proxy states are rule-derived analytical constructs. | ``constructs and evaluates...'' | Uses a faithful Hebrew equivalent for evidence-tracked workflow. |
| ABS-03 | The workflow is evaluated separately in PhysioNet 2012 and MIMIC-III and compares five predictive families. | Ch. 1, lines 19--21 and 65; Ch. 10, predictive-results section. | ``five'' | No pooling and no construct-equivalence claim. | ``evaluated separately...'' | Same datasets, separate analysis, and five-family scope. |
| ABS-04 | Primary forest summaries: all nine MIMIC-III positive; nine of ten PhysioNet positive; shock negative. | Ch. 11, lines 52--55; Ch. 12, Main Findings. | 9/9, 9/10 | Mean model-estimated CATEs under project assumptions; not clinical or causal proof. | ``primary CausalForestDML summaries...'' | Keeps the exact counts and negative shock exception. |
| ABS-05 | Directional agreement: CausalForestDML/LinearDML 19/19; all three estimators 18/19. | Ch. 10, LinearDML/CausalPFN comparison; Ch. 12, Main Findings. | 19/19, 18/19 | Agreement does not establish correctness, equal uncertainty, or identification; CausalPFN exploratory. | ``directional comparison...'' | Retains both limits. |
| ABS-06 | Matching is descriptive; cross-dataset results are not pooled; causal/clinical/deployment claims are excluded. | Ch. 1, lines 34--38 and 65; Ch. 11, lines 52--79 and 117--176; Ch. 12, limitations. | No | State the boundaries directly. | ``Matching is descriptive...'' | Same hierarchy and limitations. |
| ABS-07 | Numerical traceability is stronger than clean-checkout reproducibility. | Ch. 1, line 65; Ch. 11, reproducibility section; Ch. 12, limitations. | No | Do not assert rerun reproducibility. | ``provenance records support...'' | Same limited claim. |

## 3. Keyword set

| English item | Hebrew counterpart |
| --- | --- |
| irregular clinical time series | סדרות זמן קליניות לא סדירות |
| intensive care | טיפול נמרץ |
| electronic health records | רשומות בריאות אלקטרוניות |
| proxy states | מצבי פרוקסי |
| multi-label prediction | חיזוי רב-תוויתי |
| missingness-aware modeling | מידול מודע לחוסרים |
| directed acyclic graphs | גרפים מכוונים חסרי מעגלים |
| observational causal inference | הסקה סיבתית תצפיתית |
| double machine learning | למידת מכונה כפולה |
| causal forests | יערות סיבתיים |
| heterogeneous effect estimation | אמידת השפעות הטרוגניות |
| sensitivity analysis | ניתוח רגישות |
| evidence provenance | פרובננס ראייתי |
| MIMIC-III | MIMIC-III |
| PhysioNet 2012 | PhysioNet 2012 |

## 4. Abbreviation and notation set

The final reader-facing list will include only items found in the body.  Included abbreviations are ICU, EHR, DAG, STraTS, GRU, GRU-D, TCN, SAnD, DML, CATE, HTE, AUROC, AUPRC, minRP, SOFA, ARDS, and CausalPFN (as an unresolved-name entry rather than an unsupported expansion).  ATE, ATT, OVB, RV, and AKI are excluded: they are absent, restricted, or not needed for reader comprehension in the final body.

Included notation is verified in Chapter 3 and, for the analysis quantities, Chapter 7: \(i\), \(n_i\), \(t_{ij}\), \(v_{ij}\), \(x_{ij}\), \(\mathcal{V}\), \(\mathcal{O}_i\), \(L^{rule}_{ik}\), \(\hat p^{(m)}_{ik}\), \(\hat L^{(m)}_{ik}\), \(A_i\), \(Y_i\), \(W_i\), \(X_i\), and \(Y_i(a)\).  Proposed planning symbols not used in the body (including \(S_i\), \(L^{vote}_{ik}\), \(\tau(x)\), \(\bar{\hat\tau}\), and \(\bar\Delta_{match}\)) are excluded.

## 5. Administrative-input inventory

| required input | status |
| --- | --- |
| official author name | unavailable |
| author identification details, if required | unavailable |
| department | unavailable |
| faculty wording | unavailable current-form wording |
| degree wording | unavailable |
| supervisor name and title | unavailable |
| co-supervisor, if applicable | unavailable |
| submission month and year | unavailable |
| approval/signature wording | unavailable current form |
| institutional approval wording | unavailable |
| English-thesis authorization | not established by repository |
| official Hebrew title | unavailable |
| official English title | provisional; approval unavailable |
| acknowledgements | no approved text available |
| current faculty form version | unavailable locally |

## 6. Appendix disposition matrix

| appendix_id | reader purpose | authoritative evidence | supported content | unsupported content / provenance risk | disposition | planned figures | planned tables | maximum scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APP-A | Full proxy-state definitions. | Ch. 5 active-tagger tables. | Definitions already supplied in Ch. 5. | Duplicate presentation would repeat methods; clinical validation and some grounding remain incomplete. | OMIT | none | none | Keep the Ch. 5 tables as the complete reader-facing definitions. |
| APP-B | DAG inventory. | Ch. 7 node-family table and active graph source. | Node families and explicit graph limitations already supplied. | Full edge inventory would duplicate methods and remains project-specified rather than validated. | OMIT | none | none | Refer readers to Ch. 7. |
| APP-C | Configuration recoverability. | Result source packet and Chs. 9, 11. | Schema/record distinction and gaps. | Exact numbered configurations are missing. | MERGE into APP-F | none | none | Only state recoverability boundary. |
| APP-D | Executed settings/commands. | Ch. 9, source packet, wrappers. | Implemented versus archived distinction. | No verified producing command/checkpoint lineage. | MERGE into APP-F | none | none | Do not print commands. |
| APP-E | Additional evidence displays. | Figure register and checked figure candidates. | Candidates are registered as supporting. | New figure insertion requires external review and would duplicate body evidence; excluded figures remain excluded. | OMIT | none | none | No new figures or tables in this stage. |
| APP-F | Concise reproducibility and evidence boundary. | Results manifest, checksums, source packet, decision register; Chs. 1, 9, 11. | Available evidence records, external data dependency, and explicit limits. | Exact data/configuration/split/checkpoint/source-version history incomplete. | KEEP | none | none | One concise narrative appendix, no numerical claims. |
| APP-G | Legacy/excluded artifacts. | Audit records. | Internal distinction is documented outside the thesis. | Repository-housekeeping material has no necessary scholarly reader role. | OMIT | none | none | Keep in audit logs only. |

## 7. Figure plan

| figure | classification | disposition |
| --- | --- | --- |
| Existing Chapter 10 figures | EXISTING_REGISTERED | Not newly referenced in an appendix. |
| `mimic_all_run_stability.png`, `physionet_all_run_stability.png`, `mortality_prediction_true_auroc_auprc.png`, `permutation_null_check.png`, `sensitivity_intervals.png`, `shock_rule_tree.png` | NOT_REQUIRED | Supporting candidates are not inserted; no duplicate appendix display. |
| `cross_model_direction_counts.png`, both non-downsampled CATE rankings, `mortality_prediction_metrics.png`, `sensitivity_intervals_trimmed.png`, `causal_dag_overview.png`, `correlation_vs_causation.png` | EXCLUDED | Remain excluded under their figure-register dispositions. |

