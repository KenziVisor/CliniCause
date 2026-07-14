# Citation Plan

Use `thesis-writing/literature/metadata/catalog.csv` and `thesis-writing/literature/metadata/references.bib` as source of truth. Do not edit bibliography files in Stage 3.

## By Conceptual Role

| citation_key | core_or_optional | planned_sections | claim_supported | why_this_source | alternative_or_redundant_sources | usage_limitations |
| --- | --- | --- | --- | --- | --- | --- |
| `silva2012physionet` | core | C1, C2.1, C4.1 | PhysioNet/CinC 2012 dataset/task context. | Canonical PhysioNet 2012 Challenge citation. | none | Does not prove local preprocessing execution. |
| `johnson2016mimiciii` | core | C1, C2.1, C4.2 | MIMIC-III database context. | Canonical MIMIC-III citation. | `harutyunyan_2019_mimiciii_benchmark` | Dataset citation, not code provenance. |
| `harutyunyan_2019_mimiciii_benchmark` | core | C2.1, C4.2, C6 | MIMIC-III clinical time-series benchmark context. | Supports time-series benchmark framing. | `johnson2016mimiciii` | Do not imply this thesis uses the exact benchmark tasks unchanged. |
| `sun_2026_review_irregular_medical_timeseries` | core | C1, C2.2 | Taxonomy and motivation for irregular medical time-series methods. | Recent survey. | `lipton_kale_wetzel_2016_missingness_rnns` | Background only. |
| `lipton_kale_wetzel_2016_missingness_rnns` | core | C1, C2.2 | Missingness patterns in clinical time series can carry signal. | Supports missingness discussion. | `che2018grud` | Not the implemented model unless discussing RNN missingness generally. |
| `tipirneni2022strats` | core | C2.2, C6.1, C6.2 | STraTS/iSTraTS triplet representation and self-supervised pretraining. | Primary source for implemented STraTS family. | none | Cite for method, not local performance. |
| `cho2014gru` | core | C2.2, C6.2 | GRU recurrent baseline. | Original GRU reference. | none | Does not address irregular ICU preprocessing directly. |
| `che2018grud` | core | C2.2, C6.2 | GRU-D missingness-aware baseline. | Primary GRU-D citation. | `lipton_kale_wetzel_2016_missingness_rnns` | Use for model, not all missingness claims. |
| `bai2018tcn` | core | C2.2, C6.2 | TCN sequence baseline. | Canonical TCN reference. | none | Generic sequence modeling, not ICU-specific. |
| `song2018sand` | core | C2.2, C6.2 | SAnD attention baseline. | Clinical time-series attention model citation. | none | Dense/interpolated representation differs from STraTS path. |
| `shukla2019interpolation` | core | C2.2, C6.2 | InterpNet method. | Canonical InterpNet citation. | `shukla_marlin_2018_irregular_clinical_timeseries` optional | Final InterpNet result missing; use for implemented method/future work only unless results recovered. |
| `shukla_marlin_2018_irregular_clinical_timeseries` | optional | C2.2 appendix | Earlier InterpNet background. | Optional workshop lineage. | `shukla2019interpolation` | Do not replace canonical 2019 source. |
| `banda_2018_electronic_phenotyping` | core | C2.3, C5 | Rule-based and ML EHR phenotyping context. | Broad electronic phenotyping survey. | `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping` | Does not validate this thesis' labels. |
| `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping` | core | C2.3, C5 | Rule-based respiratory-failure phenotyping example. | Concrete clinical rule-based phenotype source. | `banda_2018_electronic_phenotyping` | Respiratory failure only. |
| `ratner_et_al_2020_snorkel` | core | C2.3, C5.4 | Weak supervision and label aggregation. | Supports noisy label/source aggregation and majority-vote framing. | none | The thesis does not implement Snorkel label model. |
| `singer_2016_sepsis3` | core | C2.3, C5 | Sepsis/shock/organ dysfunction clinical grounding. | Clinical consensus source. | `vincent_et_al_1996_sofa` | Proxy labels are approximations, not formal Sepsis-3 diagnoses. |
| `kdigo_2012_acute_kidney_injury` | core | C2.3, C5 | Renal dysfunction/AKI proxy grounding. | Clinical guideline for creatinine/urine concepts. | none | Do not claim KDIGO validation was fully implemented. |
| `taylor_et_al_2001_isth_dic` | core | C2.3, C5 | Coagulation/heme dysfunction grounding. | ISTH DIC criteria source. | `vincent_et_al_1996_sofa` | Proxy rules may be partial. |
| `vincent_et_al_1996_sofa` | core | C2.3, C5 | Organ dysfunction score grounding. | SOFA source for organ dysfunction framing. | `singer_2016_sepsis3` | Catalog PDF missing; citation key exists. Do not overstate exact SOFA computation. |
| `ranieri_et_al_2012_berlin_ards` | core | C2.3, C5 | Respiratory failure/ARDS oxygenation grounding. | Berlin ARDS definition. | `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping` | Catalog PDF missing; proxy rules are not formal ARDS adjudication. |
| `pearl_1995_causal_diagrams` | core | C2.4, C3.3, C7 | DAGs and backdoor adjustment. | Foundational citation. | `sharma_kiciman_2020_dowhy` software workflow | Does not approve the specific DAG. |
| `hernan_robins_2016_target_trial` | core | C2.4, C3.3, C11 | Defining observational causal questions. | Target-trial framing. | `hernan_taubman_2008_well_defined_interventions` | The current implementation is not a full target-trial emulation. |
| `hernan_taubman_2008_well_defined_interventions` | core | C2.4, C3.3, C11 | Need for well-defined interventions. | Directly relevant to proxy-state exposure concern. | `hernan_robins_2016_target_trial` | Use to limit, not strengthen, causal language. |
| `smit_2023_causal_inference_icu_scoping_review` | core | C2.4, C11 | ICU observational causal inference context. | ICU-specific review. | `bica_2021_individualized_treatment_effects_ehr_ml` | Background/recommendations, not implemented method. |
| `chernozhukov2018dml` | core | C2.4, C7 | DML/orthogonalization and LinearDML foundation. | Primary DML source. | `oprescu_et_al_2019_econml` software | Method citation, not software. |
| `wager2018causalforest` | core | C2.4, C7 | Causal forest CATE estimation. | Primary causal forest citation. | `athey2019grf` | Use with EconML implementation caveat. |
| `athey2019grf` | core | C2.4, C7 | Generalized random forests. | Broader forest/heterogeneity foundation. | `wager2018causalforest` | Not sufficient alone for implementation details. |
| `bica_2021_individualized_treatment_effects_ehr_ml` | core | C2.4, C11 | ITE/CATE from EHR with ML context. | EHR ML treatment-effect review. | `curth_2024_ml_individualized_treatment_effects`; `lipkovich_2024_modern_hte_methods` | Review, not implemented estimator proof. |
| `lipkovich_2024_modern_hte_methods` | core | C2.4, C11 | Modern HTE concepts and evaluation. | Tutorial/review for HTE framing. | `curth_2024_ml_individualized_treatment_effects` | Avoid clinical-trial-specific overreach. |
| `curth_2024_ml_individualized_treatment_effects` | core | C2.4, C11 | ITE challenges, validation, covariate shift. | Recent review. | `bica_2021_individualized_treatment_effects_ehr_ml` | Background only. |
| `iwashyna_2015_hte_critical_care` | core | C2.4, C11 | Critical-care HTE motivation. | Domain-specific HTE perspective. | `smit_2023_causal_inference_icu_scoping_review` | Does not validate observational estimates here. |
| `crump_et_al_2009_limited_overlap` | core | C2.4, C8.1, C11 | Overlap/positivity and common support limitations. | Primary overlap source in corpus. | none | Dedicated overlap plots missing in repo. |
| `cinelli_hazlett_2020_sensitivity` | core | C2.4, C8.2, C11 | Omitted-variable-bias sensitivity and robustness values. | Primary implemented sensitivity foundation. | `chernozhukov_et_al_2026_ovb_causal_ml` | Do not replace with optional E-value sources. |
| `chernozhukov_et_al_2026_ovb_causal_ml` | core | C2.4, C8.2 | OVB sensitivity in causal ML/EconML style workflows. | Closely aligned with implemented robustness workflow. | `cinelli_hazlett_2020_sensitivity` | Recent source; cite carefully for method context. |
| `vanderweele_ding_2017_evalue` | optional | C2.4 or C11 optional | E-value background. | Optional epidemiological sensitivity context. | `ding_vanderweele_2016_sensitivity_without_assumptions` | Must not replace primary implemented RV/OVB sensitivity citations. |
| `ding_vanderweele_2016_sensitivity_without_assumptions` | optional | C11 optional | Assumption-light sensitivity bounds background. | Optional context. | `vanderweele_ding_2017_evalue` | Not implemented estimator. |
| `robins_hernan_brumback_2000_msm` | optional | C2.4 future work | Longitudinal causal-inference background. | Important for time-varying treatment-confounder feedback. | `hernan_robins_2016_target_trial` | The current implementation is not an MSM/IPTW workflow. |
| `sharma_kiciman_2020_dowhy` | core | C8.3, reproducibility/future refuters | Software workflow of modeling, identification, estimation, refutation. | Supports refutation workflow language. | `pearl_1995_causal_diagrams` | DoWhy is not necessarily the active estimator in final code. |
| `oprescu_et_al_2019_econml` | core | C7, C8 | EconML software citation. | Software library context. | DML/forest primary method papers | Separate software citation from mathematical method citation. |
| `[NEEDS CITATION]` CausalPFN | gap | C7, C9, C10 | If CausalPFN remains in main thesis, cite primary method/source. | Current corpus lacks an identified CausalPFN primary citation. | none | Do not make PFN central until citation is resolved. |

## Citation Gaps

| gap_id | gap | status |
| --- | --- | --- |
| CIT-GAP-001 | Primary CausalPFN citation if PFN remains in main methods/results. | [NEEDS CITATION] |
| CIT-GAP-002 | BGU/faculty current LaTeX/title-page source beyond local PDF and example. | [ADVISOR CHECK] |
| CIT-GAP-003 | Clinical references for any proxy-state rule not covered by current corpus. | [NEEDS CITATION] during proxy-definition table construction |
| CIT-GAP-004 | Prompt-engineering, transparent AI-assisted-research reporting, or exact ChatGPT 5.4 extended-reasoning documentation if LLM-assisted elicitation is framed as a formal methodology rather than project provenance. | [NEEDS CITATION] |

## Out of Scope

LLM model training or runtime inference remains out of scope for the implemented pipeline. LLM-assisted prompt elicitation is now in scope only as design provenance, with citation needs tracked separately and no claim that the pipeline contains an executed LLM component.
