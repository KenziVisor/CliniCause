# Thesis Outline

Readiness statuses used: `READY FOR METHODS DRAFT`, `READY WITH QUALIFICATIONS`, `BLOCKED BY RESULTS`, `BLOCKED BY PROVENANCE`, `BLOCKED BY ADVISOR DECISION`, `APPENDIX ONLY`, `FUTURE WORK`.

## Planned Chapter Set

| chapter_id | chapter_title | role | readiness |
| --- | --- | --- | --- |
| FM | Front Matter | Required BGU front matter, abstracts, keywords, TOC, lists. | BLOCKED BY ADVISOR DECISION |
| C1 | Introduction | Motivate irregular ICU time series, proxy-state representation, and assumption-guided causal analysis. | READY WITH QUALIFICATIONS |
| C2 | Background and Related Work | Synthesize datasets, irregular time-series models, proxy phenotyping, DAGs, DML/HTE, overlap/sensitivity. | READY WITH QUALIFICATIONS |
| C3 | Problem Definition and Study Design | Define units, tasks, estimands, assumptions, and boundaries between prediction and causal analysis. | READY FOR METHODS DRAFT |
| C4 | Data and Preprocessing | Describe PhysioNet/MIMIC data contracts and preprocessing differences. | READY WITH QUALIFICATIONS |
| C5 | Clinical Proxy-State Construction | Define rule-based proxy labels and limitations. | READY WITH QUALIFICATIONS |
| C6 | Predictive Modeling of Proxy States | Explain STraTS and baseline multi-label prediction. | READY FOR METHODS DRAFT |
| C7 | Causal Graph and Effect-Estimation Methodology | Explain DAGs, adjustment, matching, DML/forest/PFN. | READY WITH QUALIFICATIONS |
| C8 | Robustness, Sensitivity, and Validation Design | Explain diagnostics, not final conclusions. | READY WITH QUALIFICATIONS |
| C9 | Experimental Design | Define experiment matrix and decision criteria. | READY WITH QUALIFICATIONS |
| C10 | Results | Reserve result slots and statuses only. | BLOCKED BY RESULTS |
| C11 | Discussion | Interpret only after results stabilized. | BLOCKED BY RESULTS |
| C12 | Conclusions and Future Work | Summarize demonstrated and unresolved pieces. | BLOCKED BY RESULTS |
| APP | Appendices | Proxy definitions, configs, commands, extra tables/figures, reproducibility notes. | READY WITH QUALIFICATIONS |

## Front Matter

### FM.1 Required Administrative Pages

| field | plan |
| --- | --- |
| Purpose | Provide BGU-compliant cover/title/approval pages. |
| Key questions | Is English thesis approved? Which current faculty forms are mandatory? |
| Planned claims | None. |
| Evidence class | Official BGU instructions; example thesis pattern. |
| Primary repository sources | `thesis-writing/general-instructions.pdf`; `thesis-writing/example-omri-thesis/main.tex`. |
| Primary literature themes or citation keys | None. |
| Candidate figures | BGU logo only if official/current asset approved; example asset is formatting only. |
| Candidate tables | None. |
| Dependencies | Current BGU forms; supervisor/department wording. |
| Known risks | Example title pages may be outdated or project-specific. |
| Open questions | Final language, title, supervisor titles, approval wording. |
| Drafting readiness | BLOCKED BY ADVISOR DECISION. |
| Maximum scope | Administrative pages only. |

### FM.2 Abstracts, Keywords, Acknowledgements, Contents, Lists

| field | plan |
| --- | --- |
| Purpose | Meet BGU abstract, keyword, TOC, terminology, figure/table list requirements. |
| Key questions | Abstract order; bilingual keyword handling; TOC depth. |
| Planned claims | Abstracts will be written last from final evidence. |
| Evidence class | Official BGU instructions; example thesis pattern. |
| Primary repository sources | `thesis-writing/general-instructions.pdf`; `thesis-writing/example-omri-thesis/main.tex`; `thesis-writing/planning/terminology_and_notation.md`. |
| Primary literature themes or citation keys | None. |
| Candidate figures | None. |
| Candidate tables | Abbreviation and notation lists. |
| Dependencies | Final results and final title. |
| Known risks | Abstract >500 words; keywords missing; example lacks clear keyword page. |
| Open questions | Whether keywords should appear after both abstracts. |
| Drafting readiness | BLOCKED BY ADVISOR DECISION for ordering; READY for abbreviation/notation planning. |
| Maximum scope | Summaries only; no new claims. |

## Chapter 1 - Introduction

### C1.1 Motivation: Irregular ICU Time-Series Analysis

| field | plan |
| --- | --- |
| Purpose | Explain why sparse, irregular ICU measurements motivate representation and causal-analysis challenges. |
| Key questions | Why not analyze raw measurements directly? Why ICU mortality? |
| Planned claims | ICU EHR time series are irregular, sparse, high-dimensional, and clinically heterogeneous; representation and adjustment choices matter. |
| Evidence class | Literature; repository data contracts. |
| Primary repository sources | `README.md`; `causal-irregular-time-series/README.md`; preprocessing source. |
| Primary literature themes or citation keys | `silva2012physionet`, `johnson2016mimiciii`, `harutyunyan_2019_mimiciii_benchmark`, `sun_2026_review_irregular_medical_timeseries`, `lipton_kale_wetzel_2016_missingness_rnns`. |
| Candidate figures | F-WORKFLOW-01 if provenance current; otherwise planned pipeline schematic later. |
| Candidate tables | None. |
| Dependencies | None for methods-level motivation. |
| Known risks | Avoid numerical dataset claims unless verified. |
| Open questions | Whether to foreground both datasets equally. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Motivation, not results. |

### C1.2 Thesis Gap and Objective

| field | plan |
| --- | --- |
| Purpose | Define the gap between proxy phenotyping, irregular sequence prediction, and causal estimation. |
| Key questions | What is new about connecting these layers? |
| Planned claims | The thesis studies a pipeline connecting derived proxy-state labels, multi-label prediction, and DAG-guided effect estimation. |
| Evidence class | Repository implementation; literature synthesis. |
| Primary repository sources | `router.py`; `causal-irregular-time-series/main.py`; `STraTS/src/main.py`; audit CLM-001. |
| Primary literature themes or citation keys | `banda_2018_electronic_phenotyping`, `ratner_et_al_2020_snorkel`, `pearl_1995_causal_diagrams`, `chernozhukov2018dml`, `wager2018causalforest`. |
| Candidate figures | F-WORKFLOW-02 planned from verified pipeline. |
| Candidate tables | T-CONTRIB-01 contribution matrix. |
| Dependencies | Story approval. |
| Known risks | Do not imply all stages were run by the same router for final results. |
| Open questions | Primary framing: prediction-to-causality pipeline vs proxy-state construction. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Objectives and contributions only. |

### C1.3 Research Questions and Contributions

| field | plan |
| --- | --- |
| Purpose | Introduce main RQ/SRQs and contribution hierarchy. |
| Key questions | Which empirical questions can actually be answered? |
| Planned claims | Contributions are methodological/engineering plus empirical artifacts with provenance caveats. |
| Evidence class | Stage 2 audit and planning. |
| Primary repository sources | `thesis-writing/audit/claim_evidence_ledger.csv`; `thesis-writing/planning/thesis_story.md`. |
| Primary literature themes or citation keys | None unless explaining context. |
| Candidate figures | None. |
| Candidate tables | T-CONTRIB-01. |
| Dependencies | Advisor decision on title/story. |
| Known risks | Intro can overpromise results. |
| Open questions | Which causal result concepts to highlight. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Claims must be high-level and qualified. |

### C1.4 Thesis Organization

| field | plan |
| --- | --- |
| Purpose | Summarize final chapter order. |
| Key questions | Should experimental design be integrated or separate? |
| Planned claims | Chapters move from evidence base to methods to design/results/discussion. |
| Evidence class | Planning. |
| Primary repository sources | This outline. |
| Primary literature themes or citation keys | None. |
| Candidate figures | None. |
| Candidate tables | None. |
| Dependencies | Final approved outline. |
| Known risks | None. |
| Open questions | Final chapter count may be reduced in LaTeX implementation. |
| Drafting readiness | BLOCKED BY ADVISOR DECISION until outline approved. |
| Maximum scope | One short roadmap. |

## Chapter 2 - Background and Related Work

### C2.1 ICU EHR Datasets and Irregular Sampling

| field | plan |
| --- | --- |
| Purpose | Position PhysioNet 2012 and MIMIC-III. |
| Key questions | What dataset properties affect modeling and causal claims? |
| Planned claims | Both datasets support ICU time-series research but have different raw structures and contracts. |
| Evidence class | Literature; code contracts. |
| Primary repository sources | `preprocess_physionet_2012.py`; `preprocess_mimic_iii_large.py`; `preprocess_mimic_iii_large_contract.py`. |
| Primary literature themes or citation keys | `silva2012physionet`, `johnson2016mimiciii`, `harutyunyan_2019_mimiciii_benchmark`. |
| Candidate figures | None. |
| Candidate tables | T-DATASET-01. |
| Dependencies | No final cohort counts unless artifacts verified. |
| Known risks | Do not claim raw data is included locally. |
| Open questions | Exact cohort counts/hashes. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Dataset context and contracts. |

### C2.2 Irregular Time-Series Representation Models

| field | plan |
| --- | --- |
| Purpose | Synthesize STraTS, GRU, GRU-D, TCN, SAnD, InterpNet, and missingness. |
| Key questions | Why compare irregular and dense sequence models? |
| Planned claims | Models differ in how they encode irregular sampling, masks, deltas, interpolation, attention, or temporal convolutions. |
| Evidence class | Literature and implementation. |
| Primary repository sources | `STraTS/src/dataset.py`; `STraTS/src/models.py`; `STraTS/src/modeling_*.py`. |
| Primary literature themes or citation keys | `tipirneni2022strats`, `cho2014gru`, `che2018grud`, `bai2018tcn`, `song2018sand`, `shukla2019interpolation`, `lipton_kale_wetzel_2016_missingness_rnns`, `sun_2026_review_irregular_medical_timeseries`. |
| Candidate figures | None. |
| Candidate tables | T-MODEL-01 architecture comparison. |
| Dependencies | InterpNet final results missing; include as implemented/method background only. |
| Known risks | Avoid saying all models completed final comparison. |
| Open questions | Whether InterpNet belongs in main results or appendix/future work. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Conceptual synthesis, not code tutorial. |

### C2.3 Proxy Phenotyping and Weak Supervision

| field | plan |
| --- | --- |
| Purpose | Ground rule-based proxy labels and majority voting. |
| Key questions | How should proxy states be interpreted? |
| Planned claims | Rule-based EHR phenotyping and weak labels can create useful proxy tasks, but they are not verified diagnoses without validation. |
| Evidence class | Literature; tagger source. |
| Primary repository sources | `tagging_latent_variables_physionet.py`; `tagging_latent_variables_mimiciii.py`; `majority_vote_latents.py`. |
| Primary literature themes or citation keys | `banda_2018_electronic_phenotyping`, `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping`, `ratner_et_al_2020_snorkel`, `singer_2016_sepsis3`, `kdigo_2012_acute_kidney_injury`, `taylor_et_al_2001_isth_dic`, `vincent_et_al_1996_sofa`, `ranieri_et_al_2012_berlin_ards`. |
| Candidate figures | Decision-tree figures as appendix candidates. |
| Candidate tables | T-PROXY-01 definition summary. |
| Dependencies | Clinical/advisor review. |
| Known risks | Missing PDFs for SOFA/ARDS do not block citation keys, but note corpus PDF status. |
| Open questions | How much clinical-detail belongs in main text vs appendix. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Proxy rationale and limitations. |

### C2.4 Causal Diagrams, Identification, HTE, Overlap, and Sensitivity

| field | plan |
| --- | --- |
| Purpose | Provide foundations for DAG-guided adjustment and heterogeneous-effect estimation. |
| Key questions | What assumptions are needed for causal language? |
| Planned claims | Causal diagrams and target-trial-style thinking help structure observational analyses; DML/causal forests estimate effects under assumptions; overlap and sensitivity diagnostics are necessary. |
| Evidence class | Literature. |
| Primary repository sources | `physionet2012_causal_graph.py`; `mimiciii_causal_graph.py`; `cate_estimation.py`; `analyze_cate_results.py`; `permutations_test.py`. |
| Primary literature themes or citation keys | `pearl_1995_causal_diagrams`, `hernan_robins_2016_target_trial`, `hernan_taubman_2008_well_defined_interventions`, `chernozhukov2018dml`, `wager2018causalforest`, `athey2019grf`, `crump_et_al_2009_limited_overlap`, `cinelli_hazlett_2020_sensitivity`, `chernozhukov_et_al_2026_ovb_causal_ml`, `smit_2023_causal_inference_icu_scoping_review`, `bica_2021_individualized_treatment_effects_ehr_ml`, `iwashyna_2015_hte_critical_care`. |
| Candidate figures | DAG figures. |
| Candidate tables | T-ASSUMPTIONS-01. |
| Dependencies | None for background; advisor for application-specific assumptions. |
| Known risks | Do not describe marginal structural models or E-values as implemented estimators. |
| Open questions | Role of CausalPFN citation [NEEDS CITATION] if retained as main method. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Synthesis, not mathematical proof. |

## Chapter 3 - Problem Definition and Study Design

### C3.1 Units, Time Horizons, and Data Objects

| field | plan |
| --- | --- |
| Purpose | Define patient/stay/record unit, `ts_id`, irregular event tuples, static covariates, and outcomes. |
| Key questions | What is the analysis unit across datasets? |
| Planned claims | The analysis joins measurement events, outcomes, proxy labels, predictions, and causal artifacts by normalized `ts_id`. |
| Evidence class | Code contracts. |
| Primary repository sources | `preprocess_mimic_iii_large_contract.py`; `STraTS/src/dataset.py`; `matching_causal_effect.py`; terminology map. |
| Primary literature themes or citation keys | Dataset citations. |
| Candidate figures | F-DATAFLOW-01 planned. |
| Candidate tables | T-DATA-CONTRACT-01. |
| Dependencies | None. |
| Known risks | MIMIC `icustay_id` aliases and split-aware vs unsplit artifacts can be conflated. |
| Open questions | Whether to call unit "stay" consistently for both datasets. |
| Drafting readiness | READY FOR METHODS DRAFT. |
| Maximum scope | Definitions and notation only. |

### C3.2 Prediction Task

| field | plan |
| --- | --- |
| Purpose | Define multi-label proxy-state prediction from irregular events. |
| Key questions | What are labels, outputs, thresholds, and metrics? |
| Planned claims | Supervised STraTS-family models predict a vector of proxy-state labels from measurement history; exports include probabilities and thresholded labels. |
| Evidence class | Implementation-confirmed. |
| Primary repository sources | `STraTS/src/main.py`; `STraTS/src/dataset.py`; `STraTS/src/evaluator.py`. |
| Primary literature themes or citation keys | Model citations. |
| Candidate figures | None. |
| Candidate tables | T-PRED-TASK-01. |
| Dependencies | Result claims wait for summaries. |
| Known risks | Prediction performance does not validate proxy labels clinically. |
| Open questions | Exact train/val/test split provenance for final archive. |
| Drafting readiness | READY FOR METHODS DRAFT. |
| Maximum scope | Task definition, not result comparison. |

### C3.3 Causal Question, Exposures, Outcome, Estimands, Assumptions

| field | plan |
| --- | --- |
| Purpose | Define exposure proxy states, mortality outcome, effect modifiers, adjustment variables, potential outcomes, and assumption boundaries. |
| Key questions | Are proxy states meaningful interventions? What does each estimate target? |
| Planned claims | Selected proxy-state columns are analyzed as exposure variables for in-hospital mortality; estimates are interpretable only under consistency, exchangeability, positivity, model, and measurement assumptions. |
| Evidence class | Implementation plus causal literature. |
| Primary repository sources | `cate_estimation.py`; `matching_causal_effect.py`; configs. |
| Primary literature themes or citation keys | `hernan_taubman_2008_well_defined_interventions`, `hernan_robins_2016_target_trial`, `pearl_1995_causal_diagrams`, `chernozhukov2018dml`. |
| Candidate figures | None. |
| Candidate tables | T-ASSUMPTIONS-01; T-EXPOSURE-01. |
| Dependencies | Advisor estimand/intervention approval. |
| Known risks | Illness states are not necessarily manipulable treatments. |
| Open questions | `mean_cate` vs ATE wording; matching ATT-style wording. |
| Drafting readiness | BLOCKED BY ADVISOR DECISION for final causal wording; methods definitions ready. |
| Maximum scope | Formal problem setup and assumptions. |

## Chapter 4 - Data and Preprocessing

### C4.1 PhysioNet 2012 Pipeline

| field | plan |
| --- | --- |
| Purpose | Describe raw files to `[ts, oc, ts_ids]`. |
| Key questions | What fields are cleaned/encoded? |
| Planned claims | PhysioNet preprocessing reads set-a/b/c, filters invalid rows, converts time to minutes, encodes ICUType one-hot variables, and writes the causal-pipeline pickle contract. |
| Evidence class | Implementation-confirmed. |
| Primary repository sources | `causal-irregular-time-series/src/preprocess_physionet_2012.py`. |
| Primary literature themes or citation keys | `silva2012physionet`. |
| Candidate figures | None. |
| Candidate tables | T-DATA-CONTRACT-01. |
| Dependencies | Raw data unavailable locally. |
| Known risks | No final cohort counts unless processed artifacts verified. |
| Open questions | Processed pickle hashes. |
| Drafting readiness | READY FOR METHODS DRAFT. |
| Maximum scope | Contract and cleaning logic. |

### C4.2 MIMIC-III Pipeline

| field | plan |
| --- | --- |
| Purpose | Describe chunked raw table extraction and canonicalization to PhysioNet-compatible contract. |
| Key questions | How are MIMIC identifiers normalized? |
| Planned claims | MIMIC preprocessing builds canonical `ts`, `oc`, and sorted `ts_ids`, removes internal MIMIC identifiers from the exported main artifact, and normalizes stay IDs. |
| Evidence class | Implementation-confirmed with dirty nested source caveat. |
| Primary repository sources | `preprocess_mimic_iii_large.py`; `preprocess_mimic_iii_large_contract.py`. |
| Primary literature themes or citation keys | `johnson2016mimiciii`, `harutyunyan_2019_mimiciii_benchmark`. |
| Candidate figures | None. |
| Candidate tables | T-DATA-CONTRACT-01. |
| Dependencies | Nested repo dirty; raw data external. |
| Known risks | Local source modified; exact producing commit for final results unknown. |
| Open questions | Producing-machine code state. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Contract and limitations. |

### C4.3 STraTS Split-Aware Artifacts Versus Causal Artifacts

| field | plan |
| --- | --- |
| Purpose | Prevent artifact-contract conflation. |
| Key questions | Why do STraTS and causal scripts use different pickles? |
| Planned claims | STraTS expects `[events, oc, train_ids, val_ids, test_ids]`; causal scripts use `[ts, oc, ts_ids]`; the parent router can bridge by creating split-aware STraTS input from causal output. |
| Evidence class | Implementation-confirmed. |
| Primary repository sources | `router.py`; `STraTS/src/dataset.py`; `causal-irregular-time-series/src/preprocess_mimic_iii_large_contract.py`. |
| Primary literature themes or citation keys | None. |
| Candidate figures | F-DATAFLOW-01. |
| Candidate tables | T-DATA-CONTRACT-01. |
| Dependencies | None. |
| Known risks | Final archived STraTS data provenance still partial. |
| Open questions | Exact final split construction. |
| Drafting readiness | READY FOR METHODS DRAFT. |
| Maximum scope | Artifact contracts and leakage safeguards. |

## Chapter 5 - Clinical Proxy-State Construction

### C5.1 Rationale and Terminology

| field | plan |
| --- | --- |
| Purpose | Explain derived proxy states and restrict diagnosis language. |
| Key questions | What is a proxy state? |
| Planned claims | Proxy states are clinically inspired labels from measurements and rules, not chart-adjudicated diagnoses. |
| Evidence class | Code; literature; terminology map. |
| Primary repository sources | `terminology_map.md`; tagger source. |
| Primary literature themes or citation keys | Proxy phenotyping and clinical criteria keys. |
| Candidate figures | None. |
| Candidate tables | T-PROXY-01. |
| Dependencies | Advisor review. |
| Known risks | Repository uses `latent` names. |
| Open questions | Final term: "proxy state" vs "proxy phenotype". |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Terminology and rationale. |

### C5.2 PhysioNet Proxy-State Rules

| field | plan |
| --- | --- |
| Purpose | Summarize PhysioNet `LAT_*` rules. |
| Key questions | Which variables/threshold families define each state? |
| Planned claims | Active PhysioNet tagger defines chronic baseline risk, global severity, shock, respiratory, renal, hepatic, coag/heme, inflammation/sepsis burden, neurologic, cardiac, and metabolic proxy states. |
| Evidence class | Implementation-confirmed. |
| Primary repository sources | `tagging_latent_variables_physionet.py`; `configs/physionet-global-variables.csv`; `final-results/trees/physionet-tags/physionet-latent-tags.csv`. |
| Primary literature themes or citation keys | `singer_2016_sepsis3`, `kdigo_2012_acute_kidney_injury`, `taylor_et_al_2001_isth_dic`, `vincent_et_al_1996_sofa`, `ranieri_et_al_2012_berlin_ards`. |
| Candidate figures | F-TREE-PHY-*. |
| Candidate tables | T-PROXY-01. |
| Dependencies | Tree figure provenance/visual check. |
| Known risks | Clinical thresholds approximate source criteria. |
| Open questions | How much rule detail in main text vs appendix. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Definition summary. |

### C5.3 MIMIC Proxy-State Rules and Validation Artifacts

| field | plan |
| --- | --- |
| Purpose | Summarize MIMIC proxy-state definitions and validation outputs. |
| Key questions | How does MIMIC differ from PhysioNet? |
| Planned claims | MIMIC tagger supports summary/pickle/raw-concept inputs and outputs tags plus validation/prevalence/mortality/cooccurrence summaries. |
| Evidence class | Implementation and result artifact. |
| Primary repository sources | `tagging_latent_variables_mimiciii.py`; `configs/mimic-global-variables.csv`; `final-results/trees/mimic-tags/*`. |
| Primary literature themes or citation keys | Same clinical/proxy keys as C5.2. |
| Candidate figures | F-TREE-MIMIC-*. |
| Candidate tables | T-PROXY-01; T-PROXY-PREV-01; T-PROXY-COOC-01. |
| Dependencies | Validate numeric tables before use. |
| Known risks | `mortality_by_tag.csv` is association only. |
| Open questions | Clinical review of combined hepatic/coag state. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Definition and diagnostic support. |

### C5.4 Predicted and Majority-Vote Proxy States

| field | plan |
| --- | --- |
| Purpose | Explain predicted proxy states and algorithmic aggregation. |
| Key questions | What is being voted, and how are IDs aligned? |
| Planned claims | Prediction exports are split/normalized into binary voters; majority vote aligns on shared `ts_id` and resolves ties to 1. |
| Evidence class | Implementation-confirmed; final voter provenance partial. |
| Primary repository sources | `STraTS/src/main.py`; `split_predicted_latent_tags.py`; `majority_vote_latents.py`; audit CLM-006/010. |
| Primary literature themes or citation keys | `ratner_et_al_2020_snorkel` for weak supervision/aggregation background. |
| Candidate figures | F-DATAFLOW-01. |
| Candidate tables | T-PRED-EXPORT-01. |
| Dependencies | Voter input manifest. |
| Known risks | Majority vote is not clinical consensus truth. |
| Open questions | Exact final voter files and export split. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Algorithmic description and limitations. |

## Chapter 6 - Predictive Modeling of Proxy States

### C6.1 Self-Supervised STraTS Pretraining

| field | plan |
| --- | --- |
| Purpose | Explain forecasting-based pretraining for STraTS/iSTraTS. |
| Key questions | What is forecasted and from which window? |
| Planned claims | Pretraining predicts near-future measurement values from irregular histories; only STraTS/iSTraTS support pretraining. |
| Evidence class | Implementation-confirmed; result summaries exist. |
| Primary repository sources | `STraTS/src/dataset_pretrain.py`; `STraTS/src/main.py`; `STraTS/src/evaluator_pretrain.py`. |
| Primary literature themes or citation keys | `tipirneni2022strats`. |
| Candidate figures | Learning curves as appendix. |
| Candidate tables | T-TRAIN-CFG-01. |
| Dependencies | Pretraining result role in final narrative. |
| Known risks | Pretraining artifacts are support, not supervised performance. |
| Open questions | Whether iSTraTS appears in final results. |
| Drafting readiness | READY FOR METHODS DRAFT. |
| Maximum scope | Method design. |

### C6.2 Supervised Multi-Label Models

| field | plan |
| --- | --- |
| Purpose | Describe model families, shared head, loss, class weights, and metrics. |
| Key questions | How were scalar mortality models adapted? |
| Planned claims | Supervised backends predict all proxy labels using a shared multi-label BCE head and evaluate per-target AUROC/AUPRC/minRP averaged over non-degenerate targets. |
| Evidence class | Implementation-confirmed. |
| Primary repository sources | `STraTS/src/models.py`; `STraTS/src/dataset.py`; `STraTS/src/evaluator.py`; `STraTS/src/modeling_*.py`. |
| Primary literature themes or citation keys | `tipirneni2022strats`, `cho2014gru`, `che2018grud`, `bai2018tcn`, `song2018sand`, `shukla2019interpolation`. |
| Candidate figures | None. |
| Candidate tables | T-MODEL-01; T-PRED-METRICS-01. |
| Dependencies | InterpNet result missing. |
| Known risks | Warm-start limitations; degenerate labels skipped in metrics. |
| Open questions | How to present missing InterpNet. |
| Drafting readiness | READY FOR METHODS DRAFT. |
| Maximum scope | Methods and planned metric table. |

### C6.3 Prediction Export and Normalization

| field | plan |
| --- | --- |
| Purpose | Define exported prediction CSVs and downstream normalization. |
| Key questions | What is exported and thresholded? |
| Planned claims | Exports contain `ts_id`, `<label>_prob`, and binary label columns thresholded at 0.5; majority voting expects binary-only CSVs. |
| Evidence class | Implementation-confirmed; final archive provenance partial. |
| Primary repository sources | `STraTS/src/main.py`; `split_predicted_latent_tags.py`; `final-results/strats-outputs/predicted*_latent_tags*.csv`. |
| Primary literature themes or citation keys | None. |
| Candidate figures | None. |
| Candidate tables | T-PRED-EXPORT-01. |
| Dependencies | Export command manifest. |
| Known risks | Do not claim exported predictions are out-of-sample unless verified. |
| Open questions | Exact `predict_split` for all archived exports. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Artifact schema. |

## Chapter 7 - Causal Graph and Causal-Effect Methodology

### C7.1 Dataset-Specific DAGs

| field | plan |
| --- | --- |
| Purpose | Describe authored PhysioNet/MIMIC DAG abstractions. |
| Key questions | What node families and edges matter? |
| Planned claims | Dataset-specific DAGs encode background, latent/proxy, observed/process, treatment/care-process, missingness, and mortality nodes. |
| Evidence class | Implementation-confirmed; assumptions require review. |
| Primary repository sources | `physionet2012_causal_graph.py`; `mimiciii_causal_graph.py`; `final-results/causal-outputs/outputs-*/graph/*_causal_dag.png`. |
| Primary literature themes or citation keys | `pearl_1995_causal_diagrams`, `smit_2023_causal_inference_icu_scoping_review`. |
| Candidate figures | F-DAG-PHY-01; F-DAG-MIMIC-01. |
| Candidate tables | T-DAG-NODES-01. |
| Dependencies | Visual validation and advisor approval of DAG assumptions. |
| Known risks | DAG is not learned or proven complete. |
| Open questions | Clinical approval status. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Structural assumptions and limitations. |

### C7.2 Adjustment-Set Logic

| field | plan |
| --- | --- |
| Purpose | Explain observed confounder selection, collider/descendant handling, and missing candidates. |
| Key questions | Which variables can be adjusted for? |
| Planned claims | Code maps available dataframe columns to graph nodes, restricts to observed/background/proxy candidates, removes forbidden collider/descendant nodes, and records observed/missing confounders. |
| Evidence class | Implementation-confirmed. |
| Primary repository sources | `matching_causal_effect.py`; `cate_estimation.py`; cross-run tables with confounder columns. |
| Primary literature themes or citation keys | `pearl_1995_causal_diagrams`. |
| Candidate figures | None. |
| Candidate tables | T-ADJUST-01. |
| Dependencies | Treatment-specific selected artifacts. |
| Known risks | Available adjustment variables may not block all real confounding. |
| Open questions | Minimal vs expanded safe confounders. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Algorithmic logic and limitations. |

### C7.3 Matching and Heterogeneous-Effect Estimators

| field | plan |
| --- | --- |
| Purpose | Explain matching, LinearDML, CausalForestDML, and CausalPFN role. |
| Key questions | What does each estimator output? |
| Planned claims | Matching produces matched-pair outcome differences; DML/forest/PFN produce patient-level CATE estimates and summary rows; PFN lacks sensitivity/permutation diagnostics by design. |
| Evidence class | Implementation; result artifacts. |
| Primary repository sources | `matching_causal_effect.py`; `cate_estimation.py`; `run_summary.json`; cross-run CSVs. |
| Primary literature themes or citation keys | `chernozhukov2018dml`, `wager2018causalforest`, `athey2019grf`, `oprescu_et_al_2019_econml`, `bica_2021_individualized_treatment_effects_ehr_ml`, `[NEEDS CITATION]` for CausalPFN if retained. |
| Candidate figures | Feature importance only as diagnostic/appendix. |
| Candidate tables | T-MATCH-01; T-CATE-01. |
| Dependencies | Primary estimator/sampling advisor decision. |
| Known risks | `mean_cate` not automatically ATE; matching not automatically ATE. |
| Open questions | Role of PFN and primary estimator. |
| Drafting readiness | READY WITH QUALIFICATIONS for methods; BLOCKED BY ADVISOR DECISION for result framing. |
| Maximum scope | Estimator definitions and output schemas. |

## Chapter 8 - Robustness, Sensitivity, and Validation Design

### C8.1 Overlap and Support Diagnostics

| field | plan |
| --- | --- |
| Purpose | Explain available and missing support checks. |
| Key questions | How is positivity assessed? |
| Planned claims | The current archive contains indirect support diagnostics via matching rates/failures; dedicated overlap plots were not found. |
| Evidence class | Diagnostic evidence; missing result. |
| Primary repository sources | `cate_cross_run_matching_table.csv`; `cate_cross_run_matching_failures.csv`; unresolved questions. |
| Primary literature themes or citation keys | `crump_et_al_2009_limited_overlap`. |
| Candidate figures | F-OVERLAP-01 [NEEDS RESULT]. |
| Candidate tables | T-OVERLAP-01. |
| Dependencies | Decide whether to generate dedicated diagnostics later. |
| Known risks | Matching support is not proof of positivity. |
| Open questions | Dedicated propensity/support diagnostics. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Limitation/design, not final proof. |

### C8.2 Sensitivity and Robustness Values

| field | plan |
| --- | --- |
| Purpose | Explain `analyze_cate_results.py`, benchmark confounders, RV fields, and contour plots. |
| Key questions | What diagnostics are estimator-native versus fallback? |
| Planned claims | Non-PFN runs have sensitivity/benchmark artifacts; reports may be partial and must be checked per treatment before numerical claims. |
| Evidence class | Diagnostic result artifacts. |
| Primary repository sources | `analyze_cate_results.py`; `benchmark_summary.csv`; `control_messages_analyze_cate_results.csv`. |
| Primary literature themes or citation keys | `cinelli_hazlett_2020_sensitivity`, `chernozhukov_et_al_2026_ovb_causal_ml`. |
| Candidate figures | F-SENS-*. |
| Candidate tables | T-SENS-01. |
| Dependencies | Per-treatment report validation. |
| Known risks | Fallback diagnostics can be misreported as estimator-native. |
| Open questions | Which sensitivity rows/contours are thesis-primary. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Diagnostic design and caveats. |

### C8.3 Permutation Checks and Reproducibility Validation

| field | plan |
| --- | --- |
| Purpose | Explain treatment/outcome permutations and configuration validation. |
| Key questions | What does a permutation check rule out? |
| Planned claims | Non-PFN permutation checks shuffle treatment or outcome, rerun CATE, and aggregate metrics; these are sanity diagnostics, not identification proof. |
| Evidence class | Diagnostic result artifacts. |
| Primary repository sources | `permutations_test.py`; `treatment_permutation_results.csv`; `outcome_permutation_results.csv`; config validation scripts. |
| Primary literature themes or citation keys | `sharma_kiciman_2020_dowhy` for refutation workflow background; method-specific sensitivity keys. |
| Candidate figures | F-PERM-01, planned from verified data, or appendix. |
| Candidate tables | T-PERM-01; T-REPRO-01. |
| Dependencies | Trial-count validation and selected runs. |
| Known risks | PFN permutations skipped by design. |
| Open questions | Whether to include permutation plots or tables only. |
| Drafting readiness | READY WITH QUALIFICATIONS. |
| Maximum scope | Diagnostics and limitations. |

## Chapter 9 - Experimental Design

### C9.1 Prediction Experiment Matrix

| field | plan |
| --- | --- |
| Purpose | Define datasets, models, train fraction, run index, metrics, and missing InterpNet status. |
| Key questions | Which runs are final candidates? |
| Planned claims | Ten supervised predictive summaries exist for STraTS/GRU/GRU-D/TCN/SAnD across both datasets; InterpNet final results are missing. |
| Evidence class | Result artifacts with provenance caveat. |
| Primary repository sources | `experiment_inventory.csv`; `final-results/strats-outputs/**/training_summary.txt`. |
| Primary literature themes or citation keys | Model citations. |
| Candidate figures | Learning curves diagnostic only. |
| Candidate tables | T-PRED-METRICS-01; T-TRAIN-CFG-01. |
| Dependencies | Approved-run decision and manifest. |
| Known risks | STraTS archive copy provenance partial. |
| Open questions | Whether pretrain summaries are reported. |
| Drafting readiness | BLOCKED BY PROVENANCE for numeric results; methods matrix ready. |
| Maximum scope | Design matrix. |

### C9.2 Causal Experiment Matrix

| field | plan |
| --- | --- |
| Purpose | Define dataset x estimator x sampling matrix and outputs. |
| Key questions | Which estimator/sampling is primary? |
| Planned claims | Twelve causal run folders exist across MIMIC/PhysioNet, forest/linear/PFN, and original/downsampled conditions. |
| Evidence class | Execution-confirmed by run summaries/logs; config missing. |
| Primary repository sources | `final-results/causal-outputs/outputs-*`; `experiment_inventory.csv`; run summaries. |
| Primary literature themes or citation keys | Estimator/sensitivity keys. |
| Candidate figures | None. |
| Candidate tables | T-CAUSAL-MATRIX-01. |
| Dependencies | Advisor decision on primary estimator/sampling. |
| Known risks | Numbered configs missing; downsample/original not interchangeable. |
| Open questions | Whether to present parallel or select primary. |
| Drafting readiness | READY WITH QUALIFICATIONS for design; BLOCKED BY ADVISOR DECISION for result hierarchy. |
| Maximum scope | Design and artifact matrix. |

## Chapter 10 - Results

| result_section | planned slot | status | evidence source | risks |
| --- | --- | --- | --- | --- |
| C10.1 Data/cohort summary | Dataset row counts, split sizes, outcome rates. | IMPLEMENTED - RESULT MISSING for clean thesis table | Processed pickles external; some run summaries/cross-run tables have analyzed `n`. | Do not invent cohort counts. |
| C10.2 Proxy prevalence/cooccurrence | Rule and majority-vote prevalence/cooccurrence. | RESULT ARTIFACT EXISTS - PROVENANCE REVIEW NEEDED | `final-results/trees/mimic-tags/prevalence.csv`, `cooccurrence_phi.csv`; PhysioNet equivalent limited. | Association/proxy only. |
| C10.3 Predictive performance | AUROC/AUPRC/minRP by dataset/model. | RESULT ARTIFACT EXISTS - PROVENANCE REVIEW NEEDED | `training_summary.txt` files. | InterpNet missing; manifest needed. |
| C10.4 Learning curves | Diagnostic curves. | VERIFIED RESULT AVAILABLE WITH CAVEATS | Learning-curve CSV/PNG. | Appendix likely. |
| C10.5 Mortality prediction from proxy states | Logistic/MLP association support. | RESULT ARTIFACT EXISTS - PROVENANCE REVIEW NEEDED | causal-run `mortality_prediction_results.txt`. | Not causal evidence; duplicates across runs. |
| C10.6 Matching results | Matched-pair baseline summaries. | RESULT ARTIFACT EXISTS - PROVENANCE REVIEW NEEDED | `cate_cross_run_matching_table.csv`. | Do not call ATE. |
| C10.7 CATE estimates | Selected `mean_cate` and heterogeneity summaries. | BLOCKED BY ADVISOR DECISION | `cate_cross_run_unified_table.csv`, per-run summaries. | Primary estimator/sampling unresolved. |
| C10.8 Heterogeneity diagnostics | Feature importance/CATE distributions. | RESULT ARTIFACT EXISTS - PROVENANCE REVIEW NEEDED | patient CATE and feature importance CSVs. | Diagnostic, not mechanism. |
| C10.9 Overlap/support | Match rates/failures; dedicated plots missing. | IMPLEMENTED - RESULT MISSING for dedicated plots | matching tables/failures. | Positivity not proven. |
| C10.10 Sensitivity | Non-PFN RV/benchmark/contours. | RESULT ARTIFACT EXISTS - PROVENANCE REVIEW NEEDED | benchmark summaries/reports/contours. | Partial statuses. |
| C10.11 Permutation | Non-PFN treatment/outcome permutation aggregate tables. | RESULT ARTIFACT EXISTS - PROVENANCE REVIEW NEEDED | permutation CSVs. | Diagnostic only. |
| C10.12 Cross-dataset comparison | Concept-level comparison if approved. | BLOCKED BY ADVISOR DECISION | cross-run summary tables. | Concept harmonization risk. |

## Chapter 11 - Discussion

### C11.1 Answer Research Questions

| field | plan |
| --- | --- |
| Purpose | Answer RQ/SRQs only from verified results. |
| Key questions | What was demonstrated, and what remains implementation-only? |
| Planned claims | To be drafted after Chapter 10 validation. |
| Evidence class | Final result package. |
| Primary repository sources | Chapter 10 tables/figures; claim ledger. |
| Primary literature themes or citation keys | Contextual comparison citations. |
| Candidate figures | None. |
| Candidate tables | T-LIMIT-01. |
| Dependencies | Results approval. |
| Known risks | Overstating causal/clinical meaning. |
| Open questions | Clinical interpretation boundaries. |
| Drafting readiness | BLOCKED BY RESULTS. |
| Maximum scope | Interpretation only. |

### C11.2 Limitations and Threats to Validity

| field | plan |
| --- | --- |
| Purpose | Discuss proxy-label, measurement, missingness, overlap, confounding, reproducibility, and ethical limitations. |
| Key questions | Which limitations are fundamental vs fixable? |
| Planned claims | Proxy labels and observational estimates require strict qualification; reproducibility needs manifest/config recovery. |
| Evidence class | Audit; methods; literature. |
| Primary repository sources | `unresolved_questions.md`; validation report; final result artifacts. |
| Primary literature themes or citation keys | `hernan_taubman_2008_well_defined_interventions`, `crump_et_al_2009_limited_overlap`, `cinelli_hazlett_2020_sensitivity`, `smit_2023_causal_inference_icu_scoping_review`. |
| Candidate figures | None. |
| Candidate tables | T-LIMIT-01. |
| Dependencies | Final result choices. |
| Known risks | Limitations should not bury missing evidence. |
| Open questions | Advisor-approved clinical language. |
| Drafting readiness | READY WITH QUALIFICATIONS for skeleton; final text BLOCKED BY RESULTS. |
| Maximum scope | Threats to validity. |

## Chapter 12 - Conclusions and Future Work

### C12.1 Contribution Summary and Future Work

| field | plan |
| --- | --- |
| Purpose | Close thesis with demonstrated contributions, unresolved evidence, and next steps. |
| Key questions | What was built, what was shown, what remains? |
| Planned claims | The thesis demonstrates a pipeline subject to evidence/provenance limits; future work includes clinical validation, manifests, overlap diagnostics, target-trial refinement, and extended experiments. |
| Evidence class | Final validated thesis body. |
| Primary repository sources | All final planning/result chapters. |
| Primary literature themes or citation keys | No new citations unless already introduced. |
| Candidate figures | None. |
| Candidate tables | None. |
| Dependencies | Results/discussion complete. |
| Known risks | Conclusion must not introduce new evidence. |
| Open questions | Final approved contributions. |
| Drafting readiness | BLOCKED BY RESULTS. |
| Maximum scope | Concise close and future work. |

## Appendices

| appendix_id | appendix_title | purpose | sources | readiness |
| --- | --- | --- | --- | --- |
| APP-A | Complete Proxy-State Definitions | Full rule/threshold tables by dataset. | Tagger source; configs; clinical citations. | READY WITH QUALIFICATIONS |
| APP-B | DAG Node and Edge Inventory | Full PhysioNet/MIMIC node families and edge lists. | Graph scripts; DAG images. | READY WITH QUALIFICATIONS |
| APP-C | Configuration Fields and Resolved Run Settings | Document config schema and missing numbered configs. | `configs/*.csv`; run summaries; unresolved questions. | READY WITH QUALIFICATIONS |
| APP-D | Model Hyperparameters and Training Commands | Shell wrapper and CLI matrix. | STraTS wrappers; `STraTS/src/main.py`. | READY WITH QUALIFICATIONS |
| APP-E | Additional Figures/Tables | Learning curves, sensitivity contours, permutation plots. | Figure/table plan. | BLOCKED BY PROVENANCE |
| APP-F | Reproducibility and Environment Notes | Git state, ignored archive, absolute paths, dependencies. | Git commands; requirements; audit. | READY WITH QUALIFICATIONS |
| APP-G | Legacy Code and Excluded Artifacts | Explain `src/draft/`, example-thesis figures, binary artifacts. | Audit; AGENTS. | READY WITH QUALIFICATIONS |
