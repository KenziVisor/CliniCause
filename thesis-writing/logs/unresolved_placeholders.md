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
| Chapter 10 | `chapters/10_results.tex` | Result and validation placeholders for every approved result slot. |
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
