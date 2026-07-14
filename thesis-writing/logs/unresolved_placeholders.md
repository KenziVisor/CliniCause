# Stage 4.0 Unresolved Placeholders

This inventory covers placeholders present in the Stage 4.0 LaTeX skeleton under `thesis-writing/thesis/`.

## Placeholder Classes

| placeholder | meaning | resolution gate |
| --- | --- | --- |
| `[STAGE 4 DRAFT REQUIRED]` | A later Stage 4 drafting prompt must write this section from the approved evidence packet. | Matching Stage 4 prompt and review gate. |
| `[RESULT REQUIRED]` | Numerical, tabular, figure, or result-specific material is unavailable or not yet approved. | Checked result artifact/table/figure package. |
| `[CITATION REQUIRED]` | Citation coverage must be added or verified before drafting this section. | Citation-plan validation; CausalPFN gap if applicable. |
| `[FIGURE REQUIRED]` | A planned figure slot exists, but the figure source/provenance/caption is not yet approved. | Figure plan validation. |
| `[TABLE REQUIRED]` | A planned table slot exists, but the table source/provenance/content is not yet approved. | Table plan validation. |
| `[VALIDATION REQUIRED]` | Source, result, wording, visual, or schema validation is required before final prose. | Stage-specific validation. |
| `[SUPERVISOR DECISION REQUIRED]` | Advisor or supervisor decision is required before drafting or final wording. | Human approval gate. |
| `[ADMINISTRATIVE DETAILS REQUIRED]` | Thesis administrative details are missing. | Current BGU/faculty forms and user details. |
| `[AUTHOR DETAILS REQUIRED]` | Author information is missing. | User/admin input. |
| `[SUPERVISOR DETAILS REQUIRED]` | Supervisor information is missing. | User/admin input. |
| `[DEPARTMENT DETAILS REQUIRED]` | Department/faculty wording is missing. | User/admin input and BGU forms. |
| `[APPROVAL TEXT REQUIRED]` | Approval/signature wording is missing. | Current BGU/faculty forms. |

## Inventory Summary

Generated with:

```bash
rg -o '\[[A-Z0-9 -]+ REQUIRED\]' thesis-writing/thesis/main.tex thesis-writing/thesis/frontmatter thesis-writing/thesis/chapters thesis-writing/thesis/appendices | sed 's/^.*://' | sort | uniq -c
```

| placeholder | count |
| --- | ---: |
| `[ADMINISTRATIVE DETAILS REQUIRED]` | 3 |
| `[APPROVAL TEXT REQUIRED]` | 1 |
| `[AUTHOR DETAILS REQUIRED]` | 2 |
| `[CITATION REQUIRED]` | 2 |
| `[DEPARTMENT DETAILS REQUIRED]` | 2 |
| `[FIGURE REQUIRED]` | 7 |
| `[RESULT REQUIRED]` | 19 |
| `[STAGE 4 DRAFT REQUIRED]` | 46 |
| `[SUPERVISOR DECISION REQUIRED]` | 12 |
| `[SUPERVISOR DETAILS REQUIRED]` | 2 |
| `[TABLE REQUIRED]` | 3 |
| `[VALIDATION REQUIRED]` | 32 |

## Main Locations

| area | files | placeholder focus |
| --- | --- | --- |
| Front matter | `frontmatter/title_pages.tex`, `abstract_primary.tex`, `abstract_secondary.tex`, `keywords.tex`, `acknowledgements.tex`, `nomenclature.tex` | Administrative details, language/order decisions, abstracts, keywords, acknowledgements, abbreviations, notation. |
| Chapters 1-9 | `chapters/01_*.tex` through `chapters/09_*.tex` | Drafting placeholders plus targeted result, citation, figure, table, validation, and supervisor-decision placeholders. |
| Chapter 10 | `chapters/10_results.tex` | Stage 4.6B resolved the generic result/validation skeleton; Stage 4.6B-R repaired the three blocked main-result figures. External provenance/review gates remain tracked below. |
| Chapters 11-12 | `chapters/11_discussion.tex`, `chapters/12_conclusions_future_work.tex` | Result-dependent synthesis and final conclusion placeholders. |
| Appendices | `appendices/appendices.tex` | Appendix drafting, validation, figure/table slots, and supervisor-decision placeholders. |

No generic task-marker text, dummy Latin text, or filler thesis prose was found in `thesis-writing/thesis/` during Stage 4.0 validation.

## Stage 4.1 Update

Stage 4.1 drafted Chapter 3 and Chapter 4.  The broad `[STAGE 4 DRAFT REQUIRED]` placeholders in those chapters were removed where the corresponding sections were drafted.  Generic Chapter 4 placeholders were replaced by actionable placeholders tied to missing evidence or later review gates.

### Resolved During Stage 4.1

| file | chapter and section | exact placeholder resolved | reason | supporting evidence | status |
| --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex` | Chapter 3, Section C3.1 | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from approved Stage 3 terminology and source-code contracts. | Causal preprocessing contract, STraTS loader, terminology plan. | resolved |
| `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex` | Chapter 3, Section C3.2 | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from STraTS loader/export behavior and approved task framing. | `STraTS/src/dataset.py`, `STraTS/src/main.py`, planning files. | resolved |
| `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex` | Chapter 3, Section C3.3 | `[STAGE 4 DRAFT REQUIRED]` | Section drafted at high-level study-design scope without estimator details. | Causal config fields, matching/CATE loaders, approved causal wording guidance. | resolved |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, Section C4.1 | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from PhysioNet preprocessing implementation and dataset citation. | `causal-irregular-time-series/src/preprocess_physionet_2012.py`, `silva2012physionet`. | resolved |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, Section C4.2 | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from MIMIC preprocessing implementation, canonical contract helper, and dataset citations. | `preprocess_mimic_iii_large.py`, `preprocess_mimic_iii_large_contract.py`, `johnson2016mimiciii`, `harutyunyan_2019_mimiciii_benchmark`. | resolved |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, Section C4.3 | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from STraTS loader/source and router bridge behavior. | `STraTS/src/dataset.py`, `STraTS/src/dataset_pretrain.py`, `STraTS/src/main.py`, `router.py`. | resolved |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, Section C4.1 | `[RESULT REQUIRED]` | Replaced with a precise cohort-count placeholder. | Final processed PhysioNet artifact or manifest not present. | replaced |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, Section C4.2 | `[VALIDATION REQUIRED]` | Replaced with precise data-artifact and split-provenance placeholders. | Processed artifact hashes and split-generation provenance remain absent. | replaced |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, Section C4.3 comment | `[FIGURE REQUIRED]` | Replaced with an actionable dataflow-figure placeholder. | Figure plan includes F-DATAFLOW-01 but no audited figure source is approved. | replaced |

### Remaining Chapter 3 and 4 Placeholders

| file | chapter and section | exact placeholder | reason | evidence needed | expected resolution stage | status |
| --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex` | Chapter 3, C3.3 Causal Question, Exposures, Outcome, Estimands, Assumptions | `[SUPERVISOR DECISION REQUIRED: final estimand wording for proxy-state exposures and aggregated CATE summaries]` | Causal estimand wording remains an advisor-level interpretation decision because proxy states are not necessarily well-defined interventions. | Supervisor-approved wording for exposure/intervention language, `mean_cate`, and matching contrasts. | Stage 4.7 or Stage 4.9 before causal result prose | open |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, C4.1 PhysioNet 2012 Pipeline | `[RESULT REQUIRED: final number of included PhysioNet records after preprocessing]` | Raw data and processed pickle are not tracked in Git, and no approved cohort manifest is present. | Verified processed PhysioNet artifact, cohort manifest, or reproducible extraction log. | Stage 4.10 or result-manifest preparation | open |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, C4.2 MIMIC-III Pipeline | `[RESULT REQUIRED: final number of included MIMIC-III ICU stays after preprocessing]` | Raw data and processed pickle are not tracked in Git, and the active MIMIC source has a preprocessing contract issue to resolve. | Verified processed MIMIC artifact, cohort manifest, and corrected or documented producing code state. | Stage 4.10 or result-manifest preparation | open |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, C4.3 STraTS Split-Aware Artifacts Versus Causal Artifacts | `[FIGURE REQUIRED: audited dataflow diagram linking raw data, causal artifacts, STraTS artifacts, proxy labels, and causal analysis]` | The dataflow figure is planned but no audited figure source is approved for inclusion. | Approved figure source or generated figure with validated labels and artifact contracts. | Later methods-figure pass | open |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, C4.3 STraTS Split-Aware Artifacts Versus Causal Artifacts | `[VALIDATION REQUIRED: checksums for processed PhysioNet and MIMIC-III dataset artifacts]` | Processed pickles are external or absent from the audited repository. | Non-sensitive processed-artifact manifest with paths, hashes, generation commands, and source code state. | Result-manifest preparation before Chapter 10 | open |
| `thesis-writing/thesis/chapters/04_data_preprocessing.tex` | Chapter 4, C4.3 STraTS Split-Aware Artifacts Versus Causal Artifacts | `[VALIDATION REQUIRED: provenance of train/validation/test split generation for final STraTS artifacts]` | STraTS split-aware pickles and archived prediction exports lack a complete copy/run manifest. | Split-generation command, random seed, source artifact hash, and archive-copy provenance. | Predictive result-manifest preparation before Chapter 6/10 result claims | open |

## Stage 4.2 Update

Stage 4.2 drafted Chapter 6.  The broad Chapter 6 drafting placeholders were removed and replaced, where evidence remains incomplete, by precise predictive-modeling placeholders.

### Resolved During Stage 4.2

| file | chapter and section | exact placeholder resolved | reason | supporting evidence | status |
| --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.1 Self-Supervised STraTS Pretraining | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from verified STraTS pretraining source. | `STraTS/src/dataset_pretrain.py`, `STraTS/src/modeling_strats.py`, `STraTS/src/models.py`, `STraTS/src/main.py`. | resolved |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.2 Supervised Multi-Label Models | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from verified supervised loaders, model implementations, and evaluator. | `STraTS/src/dataset.py`, `STraTS/src/models.py`, model source files, `STraTS/src/evaluator.py`. | resolved |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.2 Supervised Multi-Label Models | `[RESULT REQUIRED]` | Replaced with a precise InterpNet artifact placeholder. | InterpNet implementation exists, but no final InterpNet result artifact was found in `final-results/strats-outputs/`. | replaced |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.3 Prediction Export and Normalization | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from export code, router behavior, and downstream voter-input scripts. | `STraTS/src/main.py`, `router.py`, `split_predicted_latent_tags.py`, `majority_vote_latents.py`. | resolved |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.3 Prediction Export and Normalization | `[VALIDATION REQUIRED]` | Replaced with a precise export-provenance placeholder. | Export logs and final CSVs support schema and `predict_split=all`, but not full processed-pickle/checkpoint/archive provenance. | replaced |

### Remaining Chapter 6 Placeholders

| file | chapter and section | exact placeholder | reason | evidence needed | expected resolution stage | status |
| --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.1 Self-Supervised STraTS Pretraining | `[VALIDATION REQUIRED: recover a predictive manifest linking each final STraTS-family supervised checkpoint, pretraining checkpoint, export command, and exported CSV]` | Source-level warm-start loading is implemented, but final exported CSVs are not fully mapped to the intended pretraining and supervised checkpoints. | Predictive manifest with commands, checkpoint paths and hashes, source code state, processed artifact hashes, and archive-copy records. | Predictive result-manifest preparation before final Chapter 6/10 result claims | open |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.2 Supervised Multi-Label Models | `[RESULT REQUIRED: approved final InterpNet evaluation artifact before inclusion in the predictive performance comparison]` | InterpNet is implemented and wrapped, but no approved final InterpNet prediction CSV or training summary was found in the final archive. | Approved InterpNet run artifact or explicit decision to exclude InterpNet from final numerical comparisons. | Chapter 10 result selection and manifest preparation | open |
| `thesis-writing/thesis/chapters/06_predictive_modeling.tex` | Chapter 6, C6.3 Prediction Export and Normalization | `[VALIDATION REQUIRED: record the final export split, source processed-pickle hash, split-generation seed or ID manifest, source checkpoint, and archive-copy provenance for each prediction CSV]` | The schema and wrapper/export setting are source-supported, but exact final export provenance remains incomplete. | Per-CSV manifest covering split, source processed pickle, split IDs or seed, checkpoint hash, export command, and archive copy path. | Predictive result-manifest preparation before Chapter 10 | open |

## Stage 4.3 Update

Stage 4.3 drafted Chapter 5.  The broad Chapter 5 drafting placeholders were removed where each section was drafted.  Generic validation and table placeholders were replaced by source-backed prose, proxy-definition tables, and precise evidence gates.

### Resolved During Stage 4.3

| file | chapter and section | exact placeholder resolved | reason | supporting evidence | status |
| --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.1 Rationale and Terminology | `[STAGE 4 DRAFT REQUIRED]` | Section drafted with conservative proxy-state terminology and implementation-name boundaries. | Terminology plan, audit terminology map, active tagger/voter/export source, `banda_2018_electronic_phenotyping`, `ratner_et_al_2020_snorkel`. | resolved |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.1 Rationale and Terminology | `[VALIDATION REQUIRED]` | Replaced by a precise supervisor terminology and construct-review placeholder. | No chart-review or clinical adjudication artifact found. | replaced |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from active PhysioNet tagger and artifact schema. | `tagging_latent_variables_physionet.py`, PhysioNet config, `physionet-latent-tags.csv`. | resolved |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[TABLE REQUIRED]` | Replaced by `tab:physionet-proxy-definitions`. | Active source thresholds and artifact header. | resolved |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.3 MIMIC Proxy-State Rules and Validation Artifacts | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from active MIMIC tagger, MIMIC config, and validation artifact schemas. | `tagging_latent_variables_mimiciii.py`, `mimic-global-variables.csv`, MIMIC tag and validation artifacts. | resolved |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.3 MIMIC Proxy-State Rules and Validation Artifacts | `[VALIDATION REQUIRED]` | Replaced by a precise MIMIC input-mode/provenance placeholder. | Archived MIMIC schema exists, but producing command/input hash/source commit were not found. | replaced |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.3 MIMIC Proxy-State Rules and Validation Artifacts | `[TABLE REQUIRED]` | Replaced by `tab:mimic-proxy-definitions`. | Active source thresholds and artifact header. | resolved |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.4 Predicted and Majority-Vote Proxy States | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from STraTS export, split helper, router normalization, majority-vote source, and run summaries. | `STraTS/src/main.py`, `split_predicted_latent_tags.py`, `majority_vote_latents.py`, `router.py`, `run_summary.json`. | resolved |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.4 Predicted and Majority-Vote Proxy States | `[VALIDATION REQUIRED]` | Replaced by a precise per-run voter-manifest placeholder. | Run summaries record absolute voter directories, but voter files and hashes are not archived locally. | replaced |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.4 comment | `[FIGURE REQUIRED]` | Removed rather than inserted because no audited dataflow or tree figure source was approved for this chapter. | Figure plan marks F-DATAFLOW-01/F-TREE-* as planned or provenance-unclear. | resolved |

### Remaining Chapter 5 Placeholders

| file | chapter and section | exact placeholder | reason | evidence needed | expected resolution stage | status |
| --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.1 Rationale and Terminology | `[SUPERVISOR DECISION REQUIRED: approve proxy state as the primary thesis term and review construct-level clinical wording]` | The terminology is methodologically conservative, but final clinical construct wording needs human approval. | Supervisor/clinician approval of proxy-state terminology and construct descriptions. | Advisor review before final thesis polishing | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[VALIDATION REQUIRED: identify whether the archived PhysioNet proxy-state CSV used default or externally optimized thresholds and record the threshold-file provenance]` | The active tagger supports default and externally optimized thresholds, but archived artifact provenance does not identify the mode. | Producing command, threshold file if used, threshold-file hash, input pickle hash, and source commit. | Result-manifest preparation before final methods/results freeze | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[CITATION REQUIRED: clinical grounding for PhysioNet chronic baseline-risk BMI, albumin, and ICU-type clauses]` | Current literature supports phenotyping generally, but not these exact baseline-risk clauses. | Clinical citation or supervisor decision to keep clauses as project-specific. | Citation review before final submission | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[CITATION REQUIRED: clinical grounding for hepatic transaminase, alkaline phosphatase, and albumin clauses in proxy-state rules]` | SOFA covers bilirubin broadly; transaminase, ALP, and albumin clauses need stronger grounding or explicit project-specific status. | Clinical hepatology/critical-care citation or clinical review note. | Citation review before final submission | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[CITATION REQUIRED: clinical grounding for cardiac injury or strain proxy thresholds]` | Troponin and hemodynamic thresholds are implemented, but no verified cardiac-specific citation was available in the current corpus. | Cardiac biomarker/critical-care citation or explicit project-specific limitation. | Citation review before final submission | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[CITATION REQUIRED: clinical grounding for metabolic, electrolyte, and acid-base proxy thresholds]` | Implemented thresholds are source-confirmed but not covered by current clinical citation set. | Acid-base/electrolyte clinical citation or clinical review note. | Citation review before final submission | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.2 PhysioNet Proxy-State Rules | `[VALIDATION REQUIRED: verify the provenance and active-rule correspondence of the planned proxy-state decision-tree figures]` | Tree PNGs and pickles exist, but pickle provenance, source correspondence, and figure approval are incomplete. | Trusted render command, source commit, pickle hash, active-rule comparison, and legibility check. | Later figure/appendix pass | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.3 MIMIC Proxy-State Rules and Validation Artifacts | `[VALIDATION REQUIRED: identify the MIMIC tagger input mode, source artifact hash, producing command, and source commit for the archived tag CSV]` | MIMIC supports three input modes and the archive does not record which produced `latent_tags.csv`. | Producing command, input mode, input path/hash, source commit, and output hash. | Result-manifest preparation before final methods/results freeze | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.3 MIMIC Proxy-State Rules and Validation Artifacts | `[CITATION REQUIRED: clinical grounding for MIMIC chronic burden rule clauses]` | Chronic burden combines age, comorbidity, ICD helpers, malignancy/immunosuppression, and admission type; current corpus supports phenotyping generally but not the exact construct. | Clinical comorbidity/burden citation or supervisor-approved project-specific limitation. | Citation review before final submission | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.3 MIMIC Proxy-State Rules and Validation Artifacts | `[CITATION REQUIRED: clinical grounding for MIMIC metabolic, electrolyte, and acid-base proxy thresholds]` | Implemented thresholds are source-confirmed but not covered by current clinical citation set. | Acid-base/electrolyte clinical citation or clinical review note. | Citation review before final submission | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.3 MIMIC Proxy-State Rules and Validation Artifacts | `[CITATION REQUIRED: clinical grounding for MIMIC cardiac strain proxy thresholds]` | Troponin, CK-MB, arrhythmia, HR, and cardiac context clauses need cardiac-specific citation coverage. | Cardiac biomarker/critical-care citation or explicit project-specific limitation. | Citation review before final submission | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.4 Predicted and Majority-Vote Proxy States | `[VALIDATION REQUIRED: create a per-run majority-vote voter manifest listing every binary voter CSV, source predictive model, export split, checkpoint hash, input-artifact hash, row count, latent ordering, and majority-vote output hash]` | Run summaries identify absolute voter directories and majority-vote outputs, but not the exact voter files and hashes. | Per-run voter manifest and file hashes. | Result-manifest preparation before causal result drafting | open |

## Stage 4.3R LLM Prompt-Provenance Update

Stage 4.3R added a Chapter 5 LLM-assisted elicitation subsection and converted prompt artifacts into design-provenance evidence rather than validation or implementation authority.

### Added During Stage 4.3R

| file | chapter and section | exact placeholder | reason | evidence needed | expected resolution stage | status |
| --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.1 LLM-Assisted Ontology and Rule Elicitation | `[VALIDATION REQUIRED: record the final prompt execution settings, research or browsing mode, follow-up prompts, and output-export procedure for the ChatGPT 5.4 extended-reasoning runs]` | User supplied model metadata, but exact execution settings and export procedure are not fully recorded in the inspected artifacts. | Prompt-run manifest or project note with model/product, settings, research mode, dates, follow-up prompts, and export procedure. | Prompt provenance cleanup before final methods freeze | open |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Chapter 5, C5.1 LLM-Assisted Ontology and Rule Elicitation | `[SUPERVISOR DECISION REQUIRED: document the human and clinical review applied to the LLM-generated proxy-state and DAG design proposals]` | Prompt outputs are design proposals; final clinical and causal authority requires documented human review. | Advisor/clinical review record, accepted/rejected design decisions, and final wording approval. | Advisor review before final thesis polishing | open |

## Stage 4.4 Update

Stage 4.4 drafted Chapter 7.  The broad Chapter 7 drafting placeholders were removed where each section was drafted.  Generic validation, citation, figure, and supervisor placeholders were replaced by source-backed prose, DAG figures, method tables, and precise review gates.

### Resolved During Stage 4.4

| file | chapter and section | exact placeholder resolved | reason | supporting evidence | status |
| --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.1 Dataset-Specific DAGs | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from active graph source, prompt-provenance audit, run summaries, graph artifacts, and conservative DAG terminology. | `physionet2012_causal_graph.py`, `mimiciii_causal_graph.py`, prompt PDFs, manager summaries, run summaries, copied DAG figures. | resolved |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.1 Dataset-Specific DAGs | `[SUPERVISOR DECISION REQUIRED]` | Replaced by precise DAG clinical-plausibility and human-review placeholders. | LLM prompt-provenance audit and Stage 4.4 DAG traceability report. | replaced |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.1 comment | `[FIGURE REQUIRED]` | Replaced by inserted verified thesis-local copies of the PhysioNet and MIMIC DAG figures. | `fig:physionet-causal-dag`, `fig:mimic-causal-dag`, figure hashes in `stage_4_4_evidence_report.md`. | resolved |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.2 Adjustment-Set Logic | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from matching and CATE adjustment helpers. | `matching_causal_effect.py`, `cate_estimation.py`, DAG source, adjustment audit. | resolved |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.2 Adjustment-Set Logic | `[VALIDATION REQUIRED]` | Replaced by a treatment-specific adjustment-set validation placeholder. | Adjustment logic was source-verified, but selected final run adjustment sets still need per-treatment artifact review. | replaced |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.3 Matching and Heterogeneous-Effect Estimators | `[STAGE 4 DRAFT REQUIRED]` | Section drafted from matching, LinearDML, CausalForestDML, and CausalPFN implementation. | `matching_causal_effect.py`, `cate_estimation.py`, causal run summaries, literature citation keys. | resolved |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.3 Matching and Heterogeneous-Effect Estimators | `[CITATION REQUIRED]` | Replaced by inserted validated citations for DAG/backdoor, well-defined interventions, DML, causal forests, EconML, and HTE reviews, plus a precise CausalPFN citation-gap placeholder. | `references.bib`; Stage 4.4 citation validation. | replaced |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.3 Matching and Heterogeneous-Effect Estimators | `[SUPERVISOR DECISION REQUIRED]` | Replaced by precise W/X overlap and normalized-CATE interpretation placeholders. | Source inspection found overlap is possible and normalized CATE is implementation-defined. | replaced |

### Remaining Chapter 7 Placeholders

| file | chapter and section | exact placeholder | reason | evidence needed | expected resolution stage | status |
| --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.1 Dataset-Specific DAGs | `[SUPERVISOR DECISION REQUIRED: approve the causal interpretation and clinical plausibility of the PhysioNet and MIMIC project DAGs]` | The DAGs are project-specified assumptions informed by LLM-assisted design and source code, not clinically validated DAGs. | Advisor/clinical approval of graph node families, edge directions, and causal wording. | Advisor review before final methods freeze | open |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.1 Dataset-Specific DAGs | `[VALIDATION REQUIRED: document the human and clinical review decisions applied to the LLM-assisted DAG proposals]` | Prompt artifacts provide design provenance, but accepted/rejected DAG suggestions and reviewer roles remain incompletely recorded. | Human-review manifest linking prompt proposals, manager summaries, source implementation decisions, and final approvals. | Prompt/DAG provenance cleanup before final methods freeze | open |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.1 Dataset-Specific DAGs | `[VALIDATION REQUIRED: recover the exact graph source commit, config, command, and output hashes for the canonical DAG artifacts]` | The copied DAG PNGs and pickles are internally consistent, but run summaries reference external `/truenas` source/config paths without a local producing-command manifest. | Producing command, graph script commit, numbered config CSVs, source and output hashes, and archive-copy record for each canonical graph artifact. | Result-manifest preparation before final methods freeze | open |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.2 Adjustment-Set Logic | `[SUPERVISOR DECISION REQUIRED: approve the final estimand wording for proxy-state exposures]` | Proxy states are condition/severity constructs and may not correspond to well-defined assignable interventions. | Supervisor-approved wording for proxy exposure contrasts, intervention analogies, and aggregation claims. | Advisor review before causal results prose | open |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.2 Adjustment-Set Logic | `[VALIDATION REQUIRED: validate treatment-specific adjustment sets against the selected final run artifacts]` | Source logic is documented, but selected final per-treatment adjustment sets, missing graph candidates, and open-path diagnostics still need artifact-level review. | Per-treatment confounder-analysis files, observed confounder lists, missing candidates, open-path diagnostics, and run selection decision. | Stage 4.8 or Chapter 10 result selection | open |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.3 Matching and Heterogeneous-Effect Estimators | `[SUPERVISOR DECISION REQUIRED: review the use of overlapping variables in W and X]` | CATE source may include the same column in adjustment variables and effect modifiers; the methodological interpretation needs approval. | Estimator-design review or source change documenting how overlapping \(W\) and \(X\) should be interpreted. | Causal methods review before final results prose | open |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.3 Matching and Heterogeneous-Effect Estimators | `[SUPERVISOR DECISION REQUIRED: approve or replace the interpretation of normalized\_CATE]` | `normalized_CATE` is an implementation-defined CATE divided by the sample outcome rate, not a risk ratio or relative risk. | Supervisor-approved wording or decision to omit normalized CATE from main interpretation. | Chapter 10 result-selection review | open |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.3 Matching and Heterogeneous-Effect Estimators | `[CITATION REQUIRED: validated primary source for the CausalPFN method before treating it as a main thesis estimator]` | The current literature corpus has no approved CausalPFN primary citation. | Vetted CausalPFN citation or explicit decision to keep CausalPFN secondary/exploratory. | Citation review before final methods freeze | open |

## Stage 4.4S Update

Stage 4.4S added the missing outcome-downsampling analysis condition and its target-population implications to Chapter 7.  The focused review introduced one new decision gate and did not resolve or duplicate the existing normalized-CATE and proxy-exposure estimand placeholders.

| file | chapter and section | exact placeholder | reason | evidence or decision needed | expected resolution stage | status |
| --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | Chapter 7, C7.3 Matching and Heterogeneous-Effect Estimators | `[SUPERVISOR DECISION REQUIRED: determine the methodological role and target-population interpretation of the original and outcome-downsampled causal analyses]` | Outcome-negative sampling occurs before treatment-specific estimation and changes both the empirical population and sample mortality prevalence; original and downsampled summaries therefore do not automatically estimate the same population quantity. | Supervisor-approved choice of primary, sensitivity-only, or excluded status for downsampled runs; explicit target population and estimand; and, if direct comparison is intended, a justified weighting, sampling, or transport argument. | Causal result-design review before selecting or interpreting final causal summaries | open |

## Stage 4.5 Update

Stage 4.5 drafted Chapters 8 and 9 as diagnostic and experimental-design chapters.  Generic Chapter 8 and 9 drafting placeholders were removed.  The following precise gates remain; equivalent pre-existing manifest, configuration, CausalPFN, predictive-provenance, and downsampling placeholders were not duplicated.

| file | chapter and section | exact placeholder | reason | evidence or decision needed | expected resolution stage | status |
| --- | --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex` | Chapter 8, C8.1 Overlap and Support Diagnostics | `[RESULT-SELECTION REQUIRED: select the thesis-primary overlap and support diagnostics after the Stage 4.6A manifest audit]` | Matching fields are indirect support evidence and no thesis display has been selected. | Validated manifest, matching schema/status review, and approved presentation role. | Stage 4.6A | open |
| `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex` | Chapter 8, C8.1 Overlap and Support Diagnostics | `[FIGURE REQUIRED: generate or recover a dedicated overlap/common-support diagnostic before claiming empirical positivity]` | Dedicated propensity/common-support and balance diagnostics were not found in the approved archive. | Approved diagnostic artifact with source, population, and interpretation validation. | Later approved diagnostic-generation/recovery task | open |
| `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex` | Chapter 8, C8.2 Sensitivity and Robustness Values | `[RESULT-SELECTION REQUIRED: identify the thesis-primary estimator, dataset, sampling condition, exposure, and source status for any sensitivity contour]` | Existing contours are per-treatment diagnostic artifacts and can be reconstructed/fallback-derived. | Primary-analysis decision plus per-treatment source/status, artifact, and contour provenance validation. | Stage 4.6A | open |
| `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex` | Chapter 8, C8.2 Sensitivity and Robustness Values | `[VALIDATION REQUIRED: distinguish estimator-native, saved-training, recomputed, and fallback sensitivity outputs for every selected treatment]` | Non-null sensitivity fields require source/status interpretation; partial and fallback paths exist. | Control-message CSV, report, saved-artifact metadata, and selected-treatment review. | Stage 4.6A | open |
| `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex` | Chapter 8, C8.3 Permutation Checks and Reproducibility Validation | `[VALIDATION REQUIRED: verify archived permutation trial counts, seeds, estimator type, and subprocess status for every selected run]` | Aggregate files record trial/seed fields, but result admission needs run-specific configuration and warning review. | Selected run summary, permutation CSV, log, config recovery, and subprocess-status validation. | Stage 4.6A | open |
| `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex` | Chapter 8, C8.3 Permutation Checks and Reproducibility Validation | `[SUPERVISOR DECISION REQUIRED: determine whether permutation checks are main-text evidence or appendix diagnostics]` | Their role is a presentation and interpretation decision, not established by file existence. | Supervisor-approved reporting policy. | Results-design review | open |
| `thesis-writing/thesis/chapters/09_experimental_design.tex` | Chapter 9, C9.2 Causal Experiment Matrix | `[SUPERVISOR DECISION REQUIRED: select the primary causal estimator and sampling condition]` | Archived run families are competing designs; this drafting stage selects none. | Supervisor-approved estimator and population/estimand policy. | Before Chapter 10 result selection | open |
| `thesis-writing/thesis/chapters/09_experimental_design.tex` | Chapter 9, C9.2 Causal Experiment Matrix | `[SUPERVISOR DECISION REQUIRED: determine the role of outcome-downsampled analyses]` | Outcome-class downsampling changes the empirical analysis population and is not exposure balancing. | Supervisor-approved primary/sensitivity/exclusion role and target-population argument. | Before Chapter 10 causal results | open |
| `thesis-writing/thesis/chapters/09_experimental_design.tex` | Chapter 9, C9.3 Computational Environment and Reproducibility | `[VALIDATION REQUIRED: document the producing hardware and software environment for final runs]` | Requirements and active metadata collection do not prove every producing environment. | Archived environment/hardware record or documented irrecoverability. | Stage 4.6A | open |

## Stage 4.6A-R Update

The author recorded the Chapter 10 results hierarchy in the repaired results packet. This is an **AUTHOR DECISION RECORDED**, not supervisor approval. Existing evidence and provenance limitations remain open.

| file | chapter and section | exact placeholder / decision gate | status after repair | remaining requirement |
| --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/09_experimental_design.tex` | C9.2 Causal Experiment Matrix | primary causal estimator and sampling condition | AUTHOR DECISION RECORDED: original cohort; CausalForestDML primary, LinearDML secondary, CausalPFN exploratory; outcome-downsampled analyses robustness/supplementary only. | Supervisor ratification of the results hierarchy. |
| `thesis-writing/thesis/chapters/07_causal_methodology.tex` | C7.2--C7.3 causal result wording | proxy-exposure, matching, mean-CATE, and normalized-CATE interpretation gates | AUTHOR DECISION RECORDED: report all prespecified original-cohort exposures; use descriptive matched-pair outcome difference and mean model-estimated CATE over the analyzed sample; omit normalized CATE from Chapter 10. | Supervisor ratification and all prior causal/provenance limitations. |
| `thesis-writing/thesis/chapters/08_robustness_sensitivity_validation.tex` | C8.1--C8.3 display-selection gates | overlap, sensitivity, and permutation presentation role | AUTHOR DECISION RECORDED: appendix/supporting role for selected diagnostics; the supplied cross-model direction figure is blocked for mixing sampling modes. | Recover or approve a replacement for the blocked direction-count figure if it is needed. |

## Stage 4.6B Update

Stage 4.6B replaced the generic Chapter 10 skeleton with checked numerical prose and tables in the frozen eight-section order.  No generic `\StagePlaceholder` remains in `chapters/10_results.tex`.

### Resolved During Stage 4.6B

| file | chapter scope | placeholder class resolved | evidence | status |
| --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/10_results.tex` | Analysis populations and predictive performance | Generic result and validation placeholders | `checked_cohort_candidates.csv`, `checked_predictive_metrics.csv` | resolved |
| `thesis-writing/thesis/chapters/10_results.tex` | Primary Forest, matching, Linear, and PFN results | Generic result, validation, and hierarchy placeholders | Frozen Stage 4.6A hierarchy plus checked CATE and matching rows | resolved with frozen qualifications |
| `thesis-writing/thesis/chapters/10_results.tex` | Cross-dataset and robustness sections | Generic result, validation, and supervisor-decision placeholders | Checked CATE, sensitivity, permutation, and support rows | resolved with frozen qualifications |

### Retained Gates After Stage 4.6B

| gate | current status | required resolution |
| --- | --- | --- |
| Supervisor ratification of the result hierarchy | Author decision is frozen; supervisor ratification is still absent. | Record supervisor approval or requested hierarchy revisions before final submission. |
| Supplementary figures and exact-value tables | Appendix candidates are selected but not inserted in this stage. | Complete the approved appendix-placement pass. |
| Raw cohort totals | Original causal-analysis counts are reported, but reconstructed raw-source cohort totals remain unavailable. | Recover raw/processed data manifests and hashes; do not relabel causal-analysis counts. |
| Exact causal configurations | Numbered producing configuration files remain unavailable locally. | Recover and archive the exact configurations or document irrecoverability. |
| Predictive split/checkpoint lineage | Test summaries are checked, but split and checkpoint-to-export provenance remains incomplete. | Recover split manifests, producing commands, and checkpoint/export hashes. |
| Overlap evidence | Matching remains indirect support evidence; no dedicated overlap/propensity figure exists. | Recover or generate an approved diagnostic before any positivity claim. |
| Clinical validation | Proxy states and DAGs lack complete clinician/chart-review validation. | Complete and record clinical/supervisor review before strengthening causal or clinical language. |
| CausalPFN citation and diagnostics | CausalPFN remains exploratory; its primary citation and DML-equivalent diagnostic family are absent. | Add a vetted primary citation and uncertainty/diagnostic plan, or retain the exploratory boundary. |

## Stage 4.6B-R Figure Repair Update

The three main-result figure placeholders are resolved. `generate_stage_4_6B_main_figures.py` generated two source-exact original-cohort CausalForestDML rankings and one original-cohort three-estimator direction-agreement figure directly from `checked_cate_candidates.csv`. All three passed numerical validation and were inserted in Chapter 10 with bounded captions and cross-references. The original conflicting PNGs remain unchanged, `BLOCKED_VALUE_CONFLICT`, and `EXCLUDED_FROM_THESIS` as provenance artifacts.

This repair does not resolve supervisor ratification, the CausalPFN primary-citation limitation, missing numbered causal configurations, predictive split/checkpoint lineage, raw cohort-total limitations, appendix placement, or the final causal-language review.

## Stage 4.7 Update

Stage 4.7 replaced the generic Chapter 11 skeleton with an evidence-bounded Discussion.  The two generic drafting placeholders, two generic result placeholders, and two generic validation placeholders previously attached to Chapter 11 are resolved by the completed research-question synthesis and limitations analysis.  The following precise gates remain open; they identify evidence or review that cannot be supplied by prose alone.

| file | chapter and section | exact placeholder / decision gate | current evidence status | required resolution | status |
| --- | --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.1 Main Research Question | `[SUPERVISOR RATIFICATION REQUIRED: final causal-language and results hierarchy]` | The author-frozen hierarchy is documented and used consistently; independent supervisor ratification is absent. | Record supervisor approval or requested revisions, then repeat the causal-language audit. | open |
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.1 Proxy-State Construction | `[CLINICAL REVIEW REQUIRED: proxy-state definitions and clinical interpretation]` | Active rule code and literature grounding exist; chart adjudication and final clinical review do not. | Record qualified clinical review of definitions, timing, likely misclassification, and permitted interpretation. | open |
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.1 Adjusted Effect Estimation | `[CITATION REQUIRED: primary CausalPFN method source]` | CausalPFN is bounded as exploratory; no vetted primary method source exists in the approved corpus. | Add a verified primary source and reconcile method/version details, or retain the explicit citation gap. | open |
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.2 Reproducibility and Provenance | `[PROVENANCE REQUIRED: exact numbered causal configurations]` | Run summaries identify absolute producing paths, but the numbered configuration files are unavailable locally. | Recover and hash the exact resolved configurations or formally document irrecoverability. | open |
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.1 Data Contracts and Integration | `[PROVENANCE REQUIRED: predictive split and checkpoint-to-export lineage]` | Export schemas and checked metrics are available; split IDs, checkpoint hashes, and per-export commands are incomplete. | Archive a per-export split/checkpoint/command/copy-lineage manifest. | open |
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.2 Reproducibility and Provenance | `[PROVENANCE REQUIRED: exact producing commits and archive-copy history]` | Local artifact hashes exist; producing commits and archive-copy chronology remain incomplete. | Recover producer commits and a signed copy/history manifest, or mark missing fields irrecoverable. | open |
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.2 Ethical and Clinical-Deployment Considerations | `[ETHICS DOCUMENTATION REQUIRED: institutional approval and data-governance wording]` | The repository does not establish an approval number, consent basis, ethics-board determination, or data-use wording. | Supply language from authoritative institutional and dataset-governance records. | open |

## Stage 4.8 Update

Stage 4.8 replaced the four generic Chapter 1 drafting placeholders and its two generic supervisor-decision placeholders with a completed Introduction.  The chapter now contains the approved main research question, SRQ-1 through SRQ-7, a bounded contribution hierarchy, findings preview, and organization roadmap.  No generic `\StagePlaceholder` remains in `chapters/01_introduction.tex`.

The thesis-wide gates below remain open and are intentionally retained in their Chapter 11 locations: final supervisor ratification of the contribution hierarchy and causal-language framing; clinical review of proxy-state definitions and interpretation; the primary CausalPFN citation; predictive split/checkpoint lineage; exact producing commits and archive-copy history; and institutional ethics and data-governance wording.  They are not repeated in Chapter 1 because the Introduction states the corresponding boundaries without displaying internal review markers.
| `thesis-writing/thesis/chapters/11_discussion.tex` | C11.2 Ethical and Clinical-Deployment Considerations | `[VALIDATION REQUIRED: subgroup fairness and external clinical validation]` | No subgroup fairness study, prospective validation, or independent clinical validation is archived. | Conduct and document approved subgroup and external validation before any deployment or general clinical-validity claim. | open |

## Stage 4.9A Update

Stage 4.9A replaced the four generic Chapter 2 drafting placeholders, the generic validation placeholder, and the generic citation placeholder with a completed Background and Related Work chapter.  Chapter 2 now contains exactly four top-level sections, two synthesis tables, a five-family predictive-model review, proxy-phenotyping and weak-supervision background, and an identification-before-estimation causal synthesis.  No generic `\StagePlaceholder` remains in `chapters/02_background_related_work.tex`.

### Resolved During Stage 4.9A

| file | chapter scope | exact placeholder class resolved | evidence | status |
| --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/02_background_related_work.tex` | C2.1--C2.4 | Four `[STAGE 4 DRAFT REQUIRED]` markers | Completed literature synthesis using the canonical local corpus. | resolved |
| `thesis-writing/thesis/chapters/02_background_related_work.tex` | C2.3 | Generic `[VALIDATION REQUIRED]` marker | Replaced by bounded proxy-validity prose and precise review gates retained in this log. | resolved |
| `thesis-writing/thesis/chapters/02_background_related_work.tex` | C2.4 | Generic `[CITATION REQUIRED]` marker | All inserted Chapter 2 citations resolve to verified catalog and bibliography keys; the specific CausalPFN gap remains open. | resolved |

### Precise Gates Retained for Stage 4.9B or Later Review

| exact gate | current location or tracking status | evidence needed | status |
| --- | --- | --- | --- |
| `[CITATION REQUIRED: primary CausalPFN method source]` | Existing Chapter 11 and deferred-fix records; Chapter 2 uses no technical CausalPFN claim. | Verified primary method source and method/version reconciliation. | open |
| `[CLINICAL REVIEW REQUIRED: proxy-state definitions and clinical interpretation]` | Existing Chapter 11 and deferred-fix records. | Qualified clinician review and, where feasible, chart-adjudicated validation. | open |
| `[LITERATURE REVIEW REQUIRED: verify whether any rule family lacks an adequate clinical source]` | Stage 4.9A literature audit; several rule families remain explicitly project-specific in Chapter 5. | Rule-family-to-primary-clinical-source matrix with gaps retained as project-specific or filled from vetted literature. | open |
| `[LITERATURE REVIEW REQUIRED: decide whether formal LLM-assisted-design literature is needed]` | Stage 4.9A literature audit; no approved LLM methodology source is in the canonical corpus. | Supervisor-approved scope decision and, only if needed, a separately authorized corpus addition. | open |
| `[SUPERVISOR RATIFICATION REQUIRED: final related-work framing]` | Stage 4.9A Chapter 2 synthesis. | Supervisor review of emphasis, boundaries, and cross-chapter balance. | open |

## Stage 4.9B Update

The Stage 4.9B audit removed reader-facing citation-gap markers where the same limitation is already stated in prose and tracked precisely here.  This does not resolve the underlying evidence gaps.

| file | former reader-facing marker or decision | tracking disposition | status |
| --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/05_proxy_state_construction.tex` | Four `[CITATION REQUIRED]` markers for chronic baseline-risk, hepatic, cardiac, and metabolic PhysioNet clauses | Replaced by a project-specific-rule sentence; exact gaps and clinical-review requirements are recorded in `stage_4_9B_proxy_rule_citation_matrix.csv`, `DF-4.3-004`, `DF-4.3-005`, and `DF-4.7-002`. | MOVE_TO_TRACKING_LOG |
| `thesis-writing/thesis/chapters/11_discussion.tex` | `[CITATION REQUIRED: primary CausalPFN method source]` | Removed because the exploratory limitation is explicit in prose and remains tracked by `DF-4.7-003` and `DF-4.9A-001`. | MOVE_TO_TRACKING_LOG |
| Chapters 1, 2, 5, 7, and 11 | Formal LLM-assisted-design literature | `NO FORMAL LLM-ASSISTED-DESIGN LITERATURE ADDED IN THE CURRENT THESIS; PROVENANCE-ONLY FRAMING RETAINED PENDING SEPARATE AUTHOR APPROVAL.` The prompt-run and human-review manifest remains `DF-4.7-011`. | open |
| All drafted chapters | Generic drafting markers | None remain. Remaining markers are specific supervisor, clinical-review, provenance, validation, ethics, or administrative gates and are retained where reader-facing qualification is necessary. | RESOLVED |
