# Thesis Story

## A. One-Paragraph Thesis Statement

This thesis presents CliniCause as an evidence-driven, LLM-guided methodological framework for irregular ICU time series. At design time, LLM-assisted clinical and causal knowledge elicitation informed candidate proxy-state ontologies, deterministic threshold rules, missingness reasoning, and dataset-specific DAG proposals. Accepted designs were encoded in source code; the resulting rule-derived proxy labels supervise deep time-series models, whose binary proxy-state predictions are normalized. In all twelve archived final causal runs, a deterministic vote then combines the rule-derived table with GRU, GRU-D, STraTS, and TCN predicted-label tables before selected aggregate columns enter DAG-guided analyses of in-hospital mortality using matching baselines and heterogeneous-effect estimators. The substantive contribution is this linked design-to-supervision-to-prediction-to-causal-analysis framework. It is not proof of validated diagnoses, autonomous causal discovery, clinical treatment recommendations, or unconditional causal effects.

## B. Main Research Question

How can LLM-assisted design-time knowledge elicitation be combined with deterministic weak supervision and deep prediction to construct clinically interpretable proxy-state representations from irregular ICU time series and support DAG-guided adjusted effect estimation for in-hospital mortality under explicit causal assumptions?

## C. Secondary Research Questions

| id | question | answerability |
| --- | --- | --- |
| SRQ-1 | Which data contracts are needed to connect PhysioNet 2012, MIMIC-III, STraTS, and the causal-analysis pipeline? | READY WITH QUALIFICATIONS; raw data and processed pickles are external. |
| SRQ-2 | How were LLM-assisted proxy-state and DAG proposals translated into deterministic rule-derived labels and project-encoded graphs? | READY WITH QUALIFICATIONS; archived prompts and source support the design/implementation account, while exact settings, output-to-code decisions, and clinical review remain [PROVENANCE UNCLEAR] / [ADVISOR CHECK]. |
| SRQ-3 | How do STraTS and implemented sequence baselines perform on multi-label proxy-state prediction? | BLOCKED BY PROVENANCE for final numeric claims; summaries exist but archive manifest is missing. |
| SRQ-4 | How are predictions of rule-derived proxy states normalized and algorithmically aggregated before downstream analysis? | READY WITH QUALIFICATIONS; the five voter filenames are known, but external voter bytes, hashes, and checkpoint lineage remain [PROVENANCE UNCLEAR], and majority vote is not clinical consensus. |
| SRQ-5 | What adjustment sets are selected by the LLM-informed, project-encoded dataset-specific DAGs for proxy-state exposure analyses? | READY FOR METHODS DRAFT; graph validity remains assumption-bound and exact treatment-specific results need selected artifact validation. |
| SRQ-6 | What matching, CATE, sensitivity, and permutation evidence exists for selected proxy-state exposures? | BLOCKED BY RESULTS/ADVISOR DECISION for main result narrative; result artifacts exist but primary estimator/sampling choices are unresolved. |
| SRQ-7 | What limitations follow from proxy labels, intervention definition, overlap, measurement error, and unmeasured confounding? | READY WITH QUALIFICATIONS; advisor wording required for clinical interpretation. |

## D. Contribution Hierarchy

| class | proposed contribution | evidence status |
| --- | --- | --- |
| primary contribution | End-to-end LLM-guided research framework linking design-time clinical/causal knowledge elicitation, irregular ICU preprocessing, deterministic proxy-state supervision, deep prediction, aggregation, DAG-guided adjustment, and effect-estimation diagnostics. | Design and implementation are supported; final archive execution is partially confirmed; prompt-to-code and full run provenance remain [PROVENANCE UNCLEAR]. |
| secondary methodological contribution | A substantive design-time LLM-assisted elicitation layer for proposing proxy-state ontology/rules, missingness handling, and dataset-specific causal structures. | Prompt artifacts and encoded source exist; exact run settings, acceptance decisions, and human/clinical review require additional evidence. |
| secondary methodological contribution | Clinically inspired, deterministic rule-derived proxy labels used as prediction targets and, after prediction/aggregation, structured causal-analysis variables. | Rule, prediction, and aggregation implementations/artifacts exist; validation and diagnosis language require [ADVISOR CHECK]. |
| secondary methodological contribution | Adjustment-set selection from LLM-informed, project-encoded DAGs for proxy-state exposure/outcome analyses. | Implemented in graph/matching/CATE code; graph approval and causal assumptions require [ADVISOR CHECK]. |
| engineering/reproducibility contribution | Parent router plus nested causal/STraTS workflows, manifests/resolved configs for local router runs, and stage-wise outputs. | Implemented; final external run configs and archive manifest missing. |
| empirical contribution | Twelve causal run families across two datasets, three estimators, and original/downsampled conditions. | Run summaries/logs support execution; primary analysis role unresolved. |
| supporting analysis | Matching, sensitivity, benchmark, and permutation diagnostics for non-PFN causal runs. | Diagnostic artifacts exist; selected rows need per-treatment validation. |
| future work | Dedicated overlap plots, recovered numbered configs, results manifest/checksums, clinical validation/chart review, InterpNet final results, stronger target-trial definition. | [NEEDS RESULT], [NEEDS EVIDENCE] for missing configs, [ADVISOR CHECK]. |

## E. Evidence Boundary

Currently supported:

- The repository implements preprocessing, proxy-state construction, proxy-state prediction, majority voting, DAG generation, matching, CATE estimation, sensitivity analysis, permutation checks, and routing/orchestration components.
- The repository audit inventories eight final predictive supervised summaries for STraTS, GRU, GRU-D, and TCN, twelve causal run folders, rule/proxy tag artifacts, DAG images, learning curves, sensitivity contours, and cross-run CSVs.
- The literature corpus contains citation keys for implemented sequence models, datasets, causal foundations, DML/causal forests, programmatic weak supervision, LLM clinical knowledge, LLM-generated causal-graph priors, overlap, and sensitivity analysis.
- The prompt-document archive supports a substantive design-method claim for LLM-assisted proxy-state and DAG elicitation; accepted executable behavior is defined by tagger and graph source code. Final runs were reported by the user as ChatGPT 5.4 with extended reasoning, but exact system/run metadata remain unresolved.
- The example thesis demonstrates practical LaTeX patterns only.

Not currently supported without caveats:

- Unqualified final numerical claims from `final-results/`, because the archive is ignored/untracked and lacks a manifest/checksums.
- Exact final causal run configuration claims, because numbered config CSVs referenced by `run_summary.json` are missing locally.
- Out-of-sample claims for exported predicted proxy states without verified export commands for each archived CSV.
- Any claim that proxy states are verified diagnoses or validated phenotypes.
- Exact prompt/model/version settings, complete conversational turns, proposal-to-code acceptance decisions, or human/clinical approval unless separately documented.
- Any claim that LLM prompt outputs are clinical validation, source-code execution, learned causal discovery, or by themselves the authoritative implemented DAG.
- Any claim that `mean_cate` or `mean_pair_effect` is a formal ATE/ATT without advisor-approved estimand wording.
- Any claim that CausalPFN has sensitivity/permutation diagnostics in this pipeline.

## F. Terminology Risks

| term | risk | safe handling |
| --- | --- | --- |
| latent variable | Sounds like a validated hidden construct; repository uses `LAT_*` historically. | Prefer "derived proxy state"; use "repository latent tag" only when naming code artifacts. |
| diagnosis | Implies chart-adjudicated clinical truth. | Avoid unless quoting external clinical literature or discussing unavailable validation. |
| treatment | Many `LAT_*` variables are illness-state proxies, not manipulable interventions. | Use "exposure/proxy-state treatment variable"; mark intervention-definition concern. |
| causal effect | Overstates estimates from observational proxy variables. | Use "adjusted effect estimate under DAG/model assumptions" unless assumptions are explicitly argued. |
| ATE | Not a direct artifact name. | Use "mean estimated CATE" or "matched-pair outcome difference" until estimand is approved. |
| validation | Could imply clinical validation. | Specify "schema validation", "diagnostic validation", "prediction evaluation", or [ADVISOR CHECK]. |
| majority vote | Could imply clinical consensus. | Describe as algorithmic aggregation of voter CSVs. |
| LLM-assisted design | Could imply autonomous discovery, runtime execution, or validation. | Describe a substantive design-time elicitation method that informed candidate ontology, rules, missingness choices, and DAG proposals; identify accepted source-code artifacts separately and preserve validation limits. |

## G. Approved Thesis Titles

| language | title |
| --- | --- |
| English | **CliniCause: An LLM-Guided Framework for Deep Proxy-State Prediction and Causal Effect Estimation in Multivariate Irregular ICU Time Series** |
| Hebrew | **CliniCause: מסגרת מונחית מודל שפה גדול לחיזוי מצבי פרוקסי בלמידה עמוקה ולאמידת השפעות סיבתיות בסדרות זמן רב־משתניות ולא־סדירות מטיפול נמרץ** |

Use these strings consistently in administrative metadata, title pages, abstracts, and planning records. In the body, qualify “causal effect estimation” through the explicit observational assumptions and proxy-exposure limitations documented above.
