# Thesis Story

## A. One-Paragraph Thesis Statement

This thesis should be framed as an evidence-driven methodological framework for causal analysis of irregular ICU time series: raw PhysioNet 2012 and MIMIC-III measurement events are transformed into patient/stay-level data contracts, clinically inspired rule-based proxy states are generated and then predicted from irregular time-series models, prediction outputs are aggregated into majority-vote proxy states, and selected proxy states are analyzed as exposure variables for in-hospital mortality using clinician-authored DAGs, DAG-guided adjustment logic, matching baselines, and heterogeneous-effect estimators. The contribution is the construction and evaluation of this linked prediction-to-causal-analysis pipeline, not proof of validated diagnoses, clinical treatment recommendations, or unconditional causal effects.

## B. Main Research Question

How can irregular ICU time-series data be converted into clinically interpretable proxy-state representations and used, under explicit causal assumptions, to support DAG-guided adjusted effect estimation for in-hospital mortality?

## C. Secondary Research Questions

| id | question | answerability |
| --- | --- | --- |
| SRQ-1 | Which data contracts are needed to connect PhysioNet 2012, MIMIC-III, STraTS, and the causal-analysis pipeline? | READY WITH QUALIFICATIONS; raw data and processed pickles are external. |
| SRQ-2 | Can rule-based proxy states be constructed consistently enough to serve as prediction labels and causal-pipeline inputs? | READY WITH QUALIFICATIONS; clinical validity remains [ADVISOR CHECK]. |
| SRQ-3 | How do STraTS and implemented sequence baselines perform on multi-label proxy-state prediction? | BLOCKED BY PROVENANCE for final numeric claims; summaries exist but archive manifest is missing. |
| SRQ-4 | How are predicted proxy states normalized or aggregated before downstream analysis? | READY WITH QUALIFICATIONS; voter input provenance is [PROVENANCE UNCLEAR]. |
| SRQ-5 | What adjustment sets are selected by the dataset-specific DAGs for proxy-state exposure analyses? | READY FOR METHODS DRAFT; exact treatment-specific results need selected artifact validation. |
| SRQ-6 | What matching, CATE, sensitivity, and permutation evidence exists for selected proxy-state exposures? | BLOCKED BY RESULTS/ADVISOR DECISION for main result narrative; result artifacts exist but primary estimator/sampling choices are unresolved. |
| SRQ-7 | What limitations follow from proxy labels, intervention definition, overlap, measurement error, and unmeasured confounding? | READY WITH QUALIFICATIONS; advisor wording required for clinical interpretation. |

## D. Contribution Hierarchy

| class | proposed contribution | evidence status |
| --- | --- | --- |
| primary contribution | End-to-end research framework linking irregular ICU preprocessing, proxy-state construction/prediction, DAG-guided adjustment, and effect-estimation diagnostics. | Implementation-confirmed; final archive execution partially confirmed; full provenance [PROVENANCE UNCLEAR]. |
| secondary methodological contribution | Clinically inspired proxy-state layer used as both prediction target and structured causal-analysis variable. | Rule implementation and artifacts exist; validation and diagnosis language require [ADVISOR CHECK]. |
| secondary methodological contribution | DAG-guided observed adjustment-set selection for proxy-state exposure/outcome analyses. | Implemented in matching/CATE code; causal assumptions require [ADVISOR CHECK]. |
| engineering/reproducibility contribution | Parent router plus nested causal/STraTS workflows, manifests/resolved configs for local router runs, and stage-wise outputs. | Implemented; final external run configs and archive manifest missing. |
| empirical contribution | Archived predictive summaries for STraTS, GRU, GRU-D, TCN, and SAnD across PhysioNet/MIMIC. | Result artifacts exist; archive copy provenance partial. |
| empirical contribution | Twelve causal run families across two datasets, three estimators, and original/downsampled conditions. | Run summaries/logs support execution; primary analysis role unresolved. |
| supporting analysis | Matching, sensitivity, benchmark, and permutation diagnostics for non-PFN causal runs. | Diagnostic artifacts exist; selected rows need per-treatment validation. |
| future work | Dedicated overlap plots, recovered numbered configs, results manifest/checksums, clinical validation/chart review, InterpNet final results, stronger target-trial definition. | [NEEDS RESULT], [NEEDS EVIDENCE] for missing configs, [ADVISOR CHECK]. |

## E. Evidence Boundary

Currently supported:

- The repository implements preprocessing, proxy-state construction, proxy-state prediction, majority voting, DAG generation, matching, CATE estimation, sensitivity analysis, permutation checks, and routing/orchestration components.
- The Stage 2 audit inventories ten final predictive supervised summaries, twelve causal run folders, rule/proxy tag artifacts, DAG images, learning curves, sensitivity contours, and cross-run CSVs.
- The literature corpus contains validated citation keys for implemented sequence models, datasets, causal foundations, DML/causal forests, weak supervision, overlap, and sensitivity analysis.
- The example thesis demonstrates practical LaTeX patterns only.

Not currently supported without caveats:

- Unqualified final numerical claims from `final-results/`, because the archive is ignored/untracked and lacks a manifest/checksums.
- Exact final causal run configuration claims, because numbered config CSVs referenced by `run_summary.json` are missing locally.
- Out-of-sample claims for exported predicted proxy states without verified export commands for each archived CSV.
- Any claim that proxy states are verified diagnoses or validated phenotypes.
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

## G. Candidate Thesis Titles

| candidate | assessment |
| --- | --- |
| A DAG-Guided Framework for Proxy-State Effect Estimation in Irregular ICU Time Series | Safest; emphasizes framework, proxy states, and assumptions. |
| Clinically Inspired Proxy States for Prediction and Causal Analysis of Irregular ICU Time Series | Accurate; foregrounds the proxy layer. |
| From Irregular ICU Measurements to DAG-Guided Heterogeneous Effect Estimates | Strong engineering/methods framing; less explicit about proxy labels. |
| Proxy-State Prediction and Assumption-Guided Causal Analysis in Critical-Care Time Series | Good balance; "causal analysis" is safer than "causal discovery". |
| Building an Evidence-Tracked Pipeline for Causal Analysis of Irregular Clinical Time Series | Very conservative; emphasizes reproducibility. |

Recommended working title: **A DAG-Guided Framework for Proxy-State Effect Estimation in Irregular ICU Time Series**.

Why: it avoids diagnosis, deployment, and treatment-recommendation language; it names the DAG and proxy-state layers; and it leaves result strength conditional on evidence and assumptions.
