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
