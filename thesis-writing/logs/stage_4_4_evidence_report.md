# Stage 4.4 Evidence Report

## 23.1 Git State

- Parent branch: `main`.
- Parent HEAD verified during Stage 4.4: `30f137efe3c2a6f1c0fc63481f4f9b5d54d75cf3`.
- Verified Stage 4.3R commit: `30f137e step 4.3 repair`.  It follows the Stage 4.3 commit and includes the LLM prompt-provenance repair.
- Nested causal repository branch: `main`.
- Nested causal repository HEAD: `417bb322fd43ddc4caea1e83529b3462b25eaaf5`.
- Parent gitlink SHA for `causal-irregular-time-series`: `417bb322fd43ddc4caea1e83529b3462b25eaaf5`.
- Initial parent worktree was dirty before Stage 4.4.  Unrelated pre-existing modifications included root documentation, router/test/requirements files, `prompt.txt`, important-md copies, `thesis-writing/literature/metadata/catalog.csv`, `tmp_verify_router.py`, and the modified nested repository checkout.
- Initial nested worktree modification: `causal-irregular-time-series/src/preprocess_mimic_iii_large.py`.  Stage 4.4 did not edit it.
- Final non-auxiliary Stage 4.4 changes:
  - `thesis-writing/thesis/chapters/07_causal_methodology.tex`
  - `thesis-writing/logs/unresolved_placeholders.md`
  - `thesis-writing/logs/deferred_fixes.md`
  - `thesis-writing/planning/figure_plan.md`
  - `thesis-writing/thesis/figures/README.md`
  - `thesis-writing/logs/stage_4_4_evidence_report.md`
  - `thesis-writing/thesis/figures/physionet_causal_dag.png`
  - `thesis-writing/thesis/figures/mimic_causal_dag.png`
  - `thesis-writing/thesis/main.pdf`
- No commit, push, staging, reset, research-code edit, config edit, result-artifact edit, prompt-artifact edit, or bibliography edit was performed.

## 23.2 Baseline Build

- Baseline commands:
  - `cd thesis-writing/thesis`
  - `latexmk -C`
  - `latexmk -xelatex main.tex`
  - `test -f main.pdf`
  - `pdfinfo main.pdf`
- Baseline result: success.
- Baseline PDF path: `thesis-writing/thesis/main.pdf`.
- Baseline page count before Stage 4.4 edits: 54 pages.
- Baseline errors: no fatal LaTeX errors, unresolved citations, or unresolved references in the final build scan.
- Baseline warnings: nonfatal layout warnings only.  The prior Stage 4.3R build report recorded 23 overfull and 274 underfull hbox warnings.

## 23.3 Files Inspected

- Thesis and logs: `prompt.txt`, `thesis-writing/thesis/main.tex`, `thesis-writing/thesis/chapters/07_causal_methodology.tex`, previous drafted chapters for style, `unresolved_placeholders.md`, `deferred_fixes.md`, and prior Stage 4 reports.
- Planning: `thesis_story.md`, `thesis_outline.md`, `chapter_evidence_map.md`, `terminology_and_notation.md`, `citation_plan.md`, `table_plan.md`, `figure_plan.md`, `writing_order.md`, and `stage4_prompt_queue.md`.
- Audit: `repository_map.md`, `evidence_inventory.md`, `experiment_inventory.csv`, `claim_evidence_ledger.csv`, `terminology_map.md`, `unresolved_questions.md`, and `llm_prompt_provenance_audit.md`.
- Literature: `thesis-writing/literature/metadata/references.bib` and citation planning notes.
- Prompts and generated reports: final and old dataset prompts, final prompt-run PDFs, prompt manager summaries, and clinical CATE manager summary under `thesis-writing/prompts-and-documents/`.
- Graph source: `causal-irregular-time-series/src/physionet2012_causal_graph.py`, `causal-irregular-time-series/src/mimiciii_causal_graph.py`, and `dataset_config.py`.
- Adjustment source: `matching_causal_effect.py` and `cate_estimation.py`.
- Matching source: `matching_causal_effect.py`.
- Estimator source: `cate_estimation.py` and `requirements.txt`.
- Configs: `configs/physionet-global-variables.csv`, `configs/mimic-global-variables.csv`, and `docs/global-variables-parameters.txt`.
- Orchestration: `main.py`, `scripts/run_main.sh`, `router.py`, and all 12 causal `run_summary.json` files.
- Graph artifacts: 12 DAG PNGs and 12 graph pickles under `final-results/causal-outputs/outputs-*/graph/`.
- Matching/CATE schemas: matching per-treatment outputs, CATE per-treatment CSV schema, CATE global summaries, CATE control messages, manager summaries, and run summaries.

## 23.4 LLM-to-DAG Traceability Matrix

Prompt artifacts and manager summaries support design provenance only.  They do not validate the DAGs clinically, do not prove graph correctness, and do not override the active graph-construction source.  Human-review evidence exists as summaries and project documents, but row-level accepted/rejected DAG decisions remain incomplete; see `DF-4.3R-002` and `DF-4.4-003`.

Traceability status key:

- DIRECT: same clinical construct or edge family appears in the final prompt output or manager summary and in source.
- PARTIAL: same concept appears, but active source changes the exact name, aggregation, split/merge, or endpoint.
- IMPLEMENTATION MODIFIED: active source adds source-specific graph detail not found as an exact prompt row.
- UNCLEAR: prompt counterpart is broad or not found in inspected text.

### PhysioNet Node Traceability

| family | implemented nodes | LLM/design counterpart | status | confidence |
| --- | --- | --- | --- | --- |
| Background | `BG_Age`, `BG_Gender`, `BG_HeightWeightBMI`, `BG_ICUType` | Age, gender, height/weight/BMI, ICU type baseline variables. | DIRECT/PARTIAL for aggregate `BG_HeightWeightBMI`. | high |
| Latent/proxy | `LAT_CHRONIC_BASELINE_RISK`, `LAT_INFLAMMATION_SEPSIS_BURDEN`, `LAT_GLOBAL_SEVERITY`, `LAT_SHOCK`, `LAT_RESPIRATORY_FAILURE`, `LAT_RENAL_DYSFUNCTION`, `LAT_HEPATIC_DYSFUNCTION`, `LAT_COAG_HEME_DYSFUNCTION`, `LAT_NEUROLOGIC_DYSFUNCTION`, `LAT_CARDIAC_INJURY_STRAIN`, `LAT_METABOLIC_DERANGEMENT` | Final PhysioNet prompt output includes these or directly corresponding constructs. | DIRECT, with source-specific split between hepatic and coagulation/hematologic dysfunction and source-specific cardiac name. | high |
| Observed | `OBS_TempWBCInflam`, `OBS_TroponinHR`, `OBS_RespiratoryGasExchange`, `OBS_Hemodynamics`, `OBS_RenalLabsUrine`, `OBS_LiverLabs`, `OBS_CBCPlatelets`, `OBS_GCS`, `OBS_MetabolicLabsABG`, `OBS_AvailabilityCounts` | Prompt output includes observed measurement families and availability counts. | PARTIAL because names are source aggregates. | medium |
| Treatment/care | `TRT_MechanicalVentilation` | Mechanical ventilation/care-process concept. | DIRECT/PARTIAL because it is care process, not randomized treatment. | high |
| Missingness/process | `MISS_LactateABGOrdering`, `MISS_TroponinOrdering`, `MISS_MeasurementIntensity` | Prompt output includes measurement intensity and ordering/missingness reasoning. | PARTIAL. | medium |
| Outcome | `OUT_InHospitalMortality` | In-hospital mortality. | DIRECT. | high |

### PhysioNet Edge Traceability

Human-review status for all edge rows: manager summaries exist, but no row-level approval manifest was found.

| implemented edge | design counterpart | status |
| --- | --- | --- |
| `BG_Age -> LAT_CHRONIC_BASELINE_RISK` | Baseline age contributes to chronic/baseline risk. | DIRECT |
| `BG_Gender -> LAT_CHRONIC_BASELINE_RISK` | Demographic baseline contributes to risk. | DIRECT |
| `BG_HeightWeightBMI -> LAT_CHRONIC_BASELINE_RISK` | Height/weight/BMI baseline contributes to risk. | DIRECT/PARTIAL |
| `BG_ICUType -> LAT_CHRONIC_BASELINE_RISK` | ICU type context contributes to baseline risk. | PARTIAL |
| `BG_ICUType -> LAT_CARDIAC_INJURY_STRAIN` | ICU type as cardiac-risk context. | IMPLEMENTATION MODIFIED |
| `BG_ICUType -> MISS_MeasurementIntensity` | Unit type affects measurement process. | IMPLEMENTATION MODIFIED |
| `LAT_CHRONIC_BASELINE_RISK -> LAT_GLOBAL_SEVERITY` | Chronic risk affects global severity. | DIRECT |
| `LAT_CHRONIC_BASELINE_RISK -> OUT_InHospitalMortality` | Baseline risk affects mortality. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS_BURDEN -> LAT_GLOBAL_SEVERITY` | Sepsis/inflammation contributes to severity. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS_BURDEN -> LAT_SHOCK` | Sepsis/inflammation contributes to shock. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS_BURDEN -> LAT_COAG_HEME_DYSFUNCTION` | Sepsis/inflammation contributes to coagulopathy. | DIRECT/PARTIAL |
| `LAT_INFLAMMATION_SEPSIS_BURDEN -> OBS_TempWBCInflam` | Sepsis/inflammation manifests in temperature/WBC observations. | DIRECT/PARTIAL |
| `LAT_GLOBAL_SEVERITY -> OUT_InHospitalMortality` | Global severity affects mortality. | DIRECT |
| `LAT_GLOBAL_SEVERITY -> TRT_MechanicalVentilation` | Severity drives respiratory support/care process. | PARTIAL |
| `LAT_GLOBAL_SEVERITY -> MISS_MeasurementIntensity` | Severity drives measurement intensity. | DIRECT/PARTIAL |
| `LAT_SHOCK -> LAT_RENAL_DYSFUNCTION` | Shock contributes to renal dysfunction. | DIRECT |
| `LAT_SHOCK -> LAT_HEPATIC_DYSFUNCTION` | Shock contributes to hepatic dysfunction. | DIRECT |
| `LAT_SHOCK -> LAT_METABOLIC_DERANGEMENT` | Shock contributes to metabolic derangement. | DIRECT |
| `LAT_SHOCK -> OUT_InHospitalMortality` | Shock contributes to mortality. | DIRECT |
| `LAT_SHOCK -> OBS_Hemodynamics` | Shock manifests in hemodynamics. | DIRECT |
| `LAT_SHOCK -> MISS_LactateABGOrdering` | Shock drives lactate/ABG ordering. | PARTIAL |
| `LAT_RESPIRATORY_FAILURE -> LAT_METABOLIC_DERANGEMENT` | Respiratory failure contributes to metabolic/acid-base derangement. | DIRECT |
| `LAT_RESPIRATORY_FAILURE -> TRT_MechanicalVentilation` | Respiratory failure drives mechanical ventilation. | DIRECT |
| `LAT_RESPIRATORY_FAILURE -> OUT_InHospitalMortality` | Respiratory failure contributes to mortality. | DIRECT |
| `LAT_RESPIRATORY_FAILURE -> OBS_RespiratoryGasExchange` | Respiratory failure manifests in gas exchange. | DIRECT |
| `LAT_RENAL_DYSFUNCTION -> LAT_METABOLIC_DERANGEMENT` | Renal dysfunction contributes to metabolic derangement. | DIRECT |
| `LAT_RENAL_DYSFUNCTION -> OUT_InHospitalMortality` | Renal dysfunction contributes to mortality. | DIRECT |
| `LAT_RENAL_DYSFUNCTION -> OBS_RenalLabsUrine` | Renal dysfunction manifests in renal labs/urine. | DIRECT |
| `LAT_HEPATIC_DYSFUNCTION -> LAT_COAG_HEME_DYSFUNCTION` | Hepatic dysfunction contributes to coagulation/hematologic dysfunction. | DIRECT/PARTIAL |
| `LAT_HEPATIC_DYSFUNCTION -> OBS_LiverLabs` | Hepatic dysfunction manifests in liver labs. | DIRECT |
| `LAT_COAG_HEME_DYSFUNCTION -> OUT_InHospitalMortality` | Coagulation/hematologic dysfunction contributes to mortality. | DIRECT/PARTIAL |
| `LAT_COAG_HEME_DYSFUNCTION -> OBS_CBCPlatelets` | Coagulation/hematologic dysfunction manifests in CBC/platelets. | DIRECT/PARTIAL |
| `LAT_NEUROLOGIC_DYSFUNCTION -> OUT_InHospitalMortality` | Neurologic dysfunction contributes to mortality. | DIRECT |
| `LAT_NEUROLOGIC_DYSFUNCTION -> OBS_GCS` | Neurologic dysfunction manifests in GCS. | DIRECT |
| `LAT_CARDIAC_INJURY_STRAIN -> LAT_SHOCK` | Cardiac injury/strain contributes to shock. | DIRECT/PARTIAL |
| `LAT_CARDIAC_INJURY_STRAIN -> OUT_InHospitalMortality` | Cardiac injury/strain contributes to mortality. | DIRECT/PARTIAL |
| `LAT_CARDIAC_INJURY_STRAIN -> OBS_TroponinHR` | Cardiac injury/strain manifests in troponin/heart rate. | DIRECT/PARTIAL |
| `LAT_CARDIAC_INJURY_STRAIN -> MISS_TroponinOrdering` | Cardiac concern drives troponin ordering. | PARTIAL |
| `LAT_METABOLIC_DERANGEMENT -> OUT_InHospitalMortality` | Metabolic derangement contributes to mortality. | DIRECT |
| `LAT_METABOLIC_DERANGEMENT -> OBS_MetabolicLabsABG` | Metabolic derangement manifests in labs/ABG. | DIRECT |
| `TRT_MechanicalVentilation -> OBS_RespiratoryGasExchange` | Mechanical ventilation changes observed respiratory measurements. | PARTIAL |
| `MISS_LactateABGOrdering -> OBS_MetabolicLabsABG` | Ordering process affects observed metabolic/ABG availability. | PARTIAL |
| `MISS_LactateABGOrdering -> OBS_RespiratoryGasExchange` | ABG ordering affects observed respiratory gas data. | PARTIAL |
| `MISS_TroponinOrdering -> OBS_TroponinHR` | Troponin ordering affects observed cardiac data. | PARTIAL |
| `MISS_MeasurementIntensity -> OBS_AvailabilityCounts` | Measurement intensity affects availability counts. | DIRECT/PARTIAL |

### MIMIC Node Traceability

| family | implemented nodes | LLM/design counterpart | status | confidence |
| --- | --- | --- | --- | --- |
| Background | `BG_AGE`, `BG_SEX`, `BG_ETHNICITY_INSURANCE_LANGUAGE`, `BG_ADMISSION_CONTEXT`, `BG_ICU_UNIT` | Demographics, social/administrative context, admission context, ICU unit. | DIRECT/PARTIAL because source aggregates ethnicity/insurance/language. | high |
| Latent/proxy | `LAT_CHRONIC_BURDEN`, `LAT_INFLAMMATION_SEPSIS`, `LAT_GLOBAL_SEVERITY`, `LAT_CARDIAC_STRAIN`, `LAT_SHOCK`, `LAT_RESPIRATORY_FAILURE`, `LAT_RENAL_DYSFUNCTION`, `LAT_HEPATIC_COAG_DYSFUNCTION`, `LAT_NEUROLOGIC_DYSFUNCTION`, `LAT_METABOLIC_DERANGEMENT` | Final MIMIC prompt output and manager summary list these or directly corresponding constructs. | DIRECT. | high |
| Observed | `OBS_BLOOD_PRESSURE`, `OBS_LACTATE`, `OBS_OXYGENATION`, `OBS_VENTILATOR_SETTINGS`, `OBS_CREATININE_BUN_URINE`, `OBS_BILIRUBIN_PLATELETS_INR`, `OBS_GCS_RASS`, `OBS_PH_ELECTROLYTES_GLUCOSE`, `OBS_TEMP_WBC_CULTURES`, `OBS_TROPONIN_ECG`, `OBS_CULTURES_MEDICATIONS`, `OBS_CREATININE_BUN_ELECTROLYTES`, `OBS_AVAILABILITY`, `OBS_LAB_COUNTS`, `OBS_VITAL_COUNTS` | Prompt output includes observed manifestations, labs, vitals, cultures, treatments, and availability. | PARTIAL because active source uses compact aggregate names. | medium |
| Treatment/care | `TRT_ANTIBIOTICS`, `TRT_VASOPRESSORS`, `TRT_MECH_VENT`, `TRT_DIALYSIS` | MIMIC care-process/treatment concepts. | DIRECT/PARTIAL because they are downstream care processes in source, not randomized assignments. | high |
| Missingness/process | `MISS_MEASUREMENT_INTENSITY` | Measurement intensity/missingness process. | DIRECT/PARTIAL. | medium |
| Outcome | `OUT_MORTALITY` | Mortality outcome. | DIRECT. | high |

### MIMIC Edge Traceability

Human-review status for all edge rows: manager summaries exist, but no row-level approval manifest was found.

| implemented edge | design counterpart | status |
| --- | --- | --- |
| `BG_AGE -> LAT_CHRONIC_BURDEN` | Age contributes to chronic burden. | DIRECT |
| `BG_AGE -> OUT_MORTALITY` | Age as baseline mortality risk. | PARTIAL |
| `BG_SEX -> LAT_CHRONIC_BURDEN` | Sex/demographic baseline contributes to chronic burden. | DIRECT/PARTIAL |
| `BG_ETHNICITY_INSURANCE_LANGUAGE -> MISS_MEASUREMENT_INTENSITY` | Administrative/social context affects measurement process. | PARTIAL |
| `BG_ETHNICITY_INSURANCE_LANGUAGE -> OUT_MORTALITY` | Administrative/social context associated with mortality risk. | IMPLEMENTATION MODIFIED |
| `BG_ADMISSION_CONTEXT -> LAT_INFLAMMATION_SEPSIS` | Admission context affects sepsis/inflammation burden. | PARTIAL |
| `BG_ADMISSION_CONTEXT -> LAT_GLOBAL_SEVERITY` | Admission context affects severity. | PARTIAL |
| `BG_ADMISSION_CONTEXT -> MISS_MEASUREMENT_INTENSITY` | Admission context affects measurement intensity. | PARTIAL |
| `BG_ICU_UNIT -> LAT_GLOBAL_SEVERITY` | ICU unit reflects severity/case mix. | PARTIAL |
| `BG_ICU_UNIT -> MISS_MEASUREMENT_INTENSITY` | ICU unit affects measurement intensity. | PARTIAL |
| `LAT_CHRONIC_BURDEN -> LAT_GLOBAL_SEVERITY` | Chronic burden contributes to global severity. | DIRECT |
| `LAT_CHRONIC_BURDEN -> LAT_RENAL_DYSFUNCTION` | Chronic burden contributes to renal dysfunction risk. | PARTIAL |
| `LAT_CHRONIC_BURDEN -> LAT_CARDIAC_STRAIN` | Chronic burden contributes to cardiac strain. | PARTIAL |
| `LAT_CHRONIC_BURDEN -> OUT_MORTALITY` | Chronic burden contributes to mortality. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS -> LAT_GLOBAL_SEVERITY` | Sepsis/inflammation contributes to severity. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS -> LAT_SHOCK` | Sepsis/inflammation contributes to shock. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS -> LAT_HEPATIC_COAG_DYSFUNCTION` | Sepsis/inflammation contributes to hepatic/coagulation dysfunction. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS -> TRT_ANTIBIOTICS` | Sepsis/infection drives antibiotics. | DIRECT/PARTIAL |
| `LAT_INFLAMMATION_SEPSIS -> OUT_MORTALITY` | Sepsis/inflammation contributes to mortality. | DIRECT |
| `LAT_INFLAMMATION_SEPSIS -> OBS_TEMP_WBC_CULTURES` | Sepsis/inflammation manifests in temperature/WBC/cultures. | DIRECT/PARTIAL |
| `LAT_GLOBAL_SEVERITY -> LAT_RESPIRATORY_FAILURE` | Global severity contributes to respiratory failure. | DIRECT/PARTIAL |
| `LAT_GLOBAL_SEVERITY -> LAT_NEUROLOGIC_DYSFUNCTION` | Global severity contributes to neurologic dysfunction. | DIRECT/PARTIAL |
| `LAT_GLOBAL_SEVERITY -> LAT_METABOLIC_DERANGEMENT` | Global severity contributes to metabolic derangement. | DIRECT/PARTIAL |
| `LAT_GLOBAL_SEVERITY -> MISS_MEASUREMENT_INTENSITY` | Severity drives measurement intensity. | DIRECT |
| `LAT_GLOBAL_SEVERITY -> OUT_MORTALITY` | Global severity contributes to mortality. | DIRECT |
| `LAT_CARDIAC_STRAIN -> LAT_SHOCK` | Cardiac strain contributes to shock. | DIRECT |
| `LAT_CARDIAC_STRAIN -> OUT_MORTALITY` | Cardiac strain contributes to mortality. | DIRECT |
| `LAT_CARDIAC_STRAIN -> OBS_TROPONIN_ECG` | Cardiac strain manifests in troponin/ECG. | DIRECT/PARTIAL |
| `LAT_SHOCK -> LAT_RENAL_DYSFUNCTION` | Shock contributes to renal dysfunction. | DIRECT |
| `LAT_SHOCK -> LAT_HEPATIC_COAG_DYSFUNCTION` | Shock contributes to hepatic/coagulation dysfunction. | DIRECT |
| `LAT_SHOCK -> LAT_METABOLIC_DERANGEMENT` | Shock contributes to metabolic derangement. | DIRECT |
| `LAT_SHOCK -> TRT_VASOPRESSORS` | Shock drives vasopressors. | DIRECT |
| `LAT_SHOCK -> OUT_MORTALITY` | Shock contributes to mortality. | DIRECT |
| `LAT_SHOCK -> OBS_BLOOD_PRESSURE` | Shock manifests in blood pressure. | DIRECT |
| `LAT_SHOCK -> OBS_LACTATE` | Shock manifests in lactate. | DIRECT |
| `LAT_RESPIRATORY_FAILURE -> LAT_METABOLIC_DERANGEMENT` | Respiratory failure contributes to metabolic/acid-base derangement. | DIRECT |
| `LAT_RESPIRATORY_FAILURE -> TRT_MECH_VENT` | Respiratory failure drives mechanical ventilation. | DIRECT |
| `LAT_RESPIRATORY_FAILURE -> OUT_MORTALITY` | Respiratory failure contributes to mortality. | DIRECT |
| `LAT_RESPIRATORY_FAILURE -> OBS_OXYGENATION` | Respiratory failure manifests in oxygenation. | DIRECT |
| `LAT_RENAL_DYSFUNCTION -> LAT_METABOLIC_DERANGEMENT` | Renal dysfunction contributes to metabolic derangement. | DIRECT |
| `LAT_RENAL_DYSFUNCTION -> TRT_DIALYSIS` | Renal dysfunction drives dialysis. | DIRECT/PARTIAL |
| `LAT_RENAL_DYSFUNCTION -> OUT_MORTALITY` | Renal dysfunction contributes to mortality. | DIRECT |
| `LAT_RENAL_DYSFUNCTION -> OBS_CREATININE_BUN_URINE` | Renal dysfunction manifests in creatinine/BUN/urine. | DIRECT |
| `LAT_HEPATIC_COAG_DYSFUNCTION -> OUT_MORTALITY` | Hepatic/coagulation dysfunction contributes to mortality. | DIRECT |
| `LAT_HEPATIC_COAG_DYSFUNCTION -> OBS_BILIRUBIN_PLATELETS_INR` | Hepatic/coagulation dysfunction manifests in bilirubin/platelets/INR. | DIRECT |
| `LAT_NEUROLOGIC_DYSFUNCTION -> OUT_MORTALITY` | Neurologic dysfunction contributes to mortality. | DIRECT |
| `LAT_NEUROLOGIC_DYSFUNCTION -> OBS_GCS_RASS` | Neurologic dysfunction manifests in GCS/RASS. | DIRECT/PARTIAL |
| `LAT_METABOLIC_DERANGEMENT -> OUT_MORTALITY` | Metabolic derangement contributes to mortality. | DIRECT |
| `LAT_METABOLIC_DERANGEMENT -> OBS_PH_ELECTROLYTES_GLUCOSE` | Metabolic derangement manifests in pH/electrolytes/glucose. | DIRECT |
| `TRT_ANTIBIOTICS -> OBS_CULTURES_MEDICATIONS` | Antibiotics/cultures affect observed medication/culture process. | PARTIAL |
| `TRT_VASOPRESSORS -> OBS_BLOOD_PRESSURE` | Vasopressors affect observed blood pressure. | PARTIAL |
| `TRT_MECH_VENT -> OBS_OXYGENATION` | Mechanical ventilation affects oxygenation observations. | PARTIAL |
| `TRT_MECH_VENT -> OBS_VENTILATOR_SETTINGS` | Mechanical ventilation affects ventilator settings. | DIRECT |
| `TRT_DIALYSIS -> OBS_CREATININE_BUN_ELECTROLYTES` | Dialysis affects renal/electrolyte observations. | PARTIAL |
| `MISS_MEASUREMENT_INTENSITY -> OBS_AVAILABILITY` | Measurement intensity affects availability. | DIRECT |
| `MISS_MEASUREMENT_INTENSITY -> OBS_LAB_COUNTS` | Measurement intensity affects lab counts. | DIRECT/PARTIAL |
| `MISS_MEASUREMENT_INTENSITY -> OBS_VITAL_COUNTS` | Measurement intensity affects vital counts. | DIRECT/PARTIAL |

### Traceability Summary

- Directly aligned elements: core latent/proxy constructs, mortality outcomes, most clinical latent-to-latent edges, latent-to-observed manifestations, and major care-process links.
- Modified elements: source-specific node names, PhysioNet hepatic/coagulation split, MIMIC combined hepatic/coagulation node, aggregate observed-node names, and administrative/context edges.
- Prompt-only elements: prompt language contains broader clinical and causal aspirations, including validation-like wording, that are not thesis claims.
- Implementation-only or unclear elements: several exact background-to-process, background-to-mortality, ICU-type, and measurement-order edges were not found as exact prompt-output rows.
- Human-review evidence: prompt manager summaries exist, but no complete row-level clinical review manifest was found.

## 23.5 DAG Implementation Matrix

| dataset | source file | graph function | background nodes | proxy-state nodes | observed nodes | treatment/care nodes | missingness nodes | outcome node | node count | edge count | acyclic | pickle output | PNG output | artifact provenance | clinical-review status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- | --- |
| PhysioNet 2012 | `src/physionet2012_causal_graph.py` | `create_physionet2012_causal_graph` | 4 | 11 latent nodes; 10 configured analyzed exposures exclude chronic baseline risk | 10 | 1 | 3 | `OUT_InHospitalMortality` | 30 | 45 | yes | `graph/physionet_causal_graph.pkl` in final outputs | `graph/physionet_causal_dag.png` in final outputs | Six duplicate PNGs and six duplicate pickles hash-match; pickle matches active source node/edge/attribute structure. | Incomplete; advisor/clinical row-level approval needed. |
| MIMIC-III | `src/mimiciii_causal_graph.py` | `create_mimiciii_causal_graph` | 5 | 10 latent nodes; 9 configured analyzed exposures exclude chronic burden | 15 | 4 | 1 | `OUT_MORTALITY` | 36 | 57 | yes | `graph/mimic_causal_graph.pkl` in final outputs | `graph/mimic_causal_dag.png` in final outputs | Six duplicate PNGs and six duplicate pickles hash-match; pickle matches active source node/edge/attribute structure. | Incomplete; advisor/clinical row-level approval needed. |

## 23.6 DAG Figure Audit

| dataset | candidate/canonical source | SHA-256 | dimensions | duplicate status | source-script agreement | run-summary evidence | visual readability | destination path | destination hash | insertion status | limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PhysioNet 2012 | `final-results/causal-outputs/outputs-physionet-forest/graph/physionet_causal_dag.png` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` | 2200 x 1800 RGBA | All six PhysioNet DAG PNGs byte-identical; all six PhysioNet pickles byte-identical. | Active source rebuild has same nodes, edges, DAG status, and attributes as pickle. | All 12 causal runs record successful graph stage; PhysioNet run summaries reference graph script path under `/truenas/...`. | Present in compiled PDF page 39; title/legend/caption visible; observed layer labels dense. | `thesis-writing/thesis/figures/physionet_causal_dag.png` | same SHA-256 | Inserted as `fig:physionet-causal-dag`. | Orientation figure; exact edge/node authority remains source and tables. |
| MIMIC-III | `final-results/causal-outputs/outputs-mimic-forest/graph/mimic_causal_dag.png` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` | 5258 x 3940 RGBA | All six MIMIC DAG PNGs byte-identical; all six MIMIC pickles byte-identical. | Active source rebuild has same nodes, edges, DAG status, and attributes as pickle. | All 12 causal runs record successful graph stage; MIMIC run summaries reference graph script path under `/truenas/...`. | Present in compiled PDF page 40; title/legend/caption visible; dense labels limit readability. | `thesis-writing/thesis/figures/mimic_causal_dag.png` | same SHA-256 | Inserted as `fig:mimic-causal-dag`. | Orientation figure; exact edge/node authority remains source and tables. |

## 23.7 Adjustment-Logic Matrix

| step | matching implementation | CATE implementation | agreement | difference | causal interpretation | limitation |
| --- | --- | --- | --- | --- | --- | --- |
| Alias mapping | Maps dataframe columns to graph nodes and graph nodes to available dataframe aliases. | Same conceptual mapping. | Same source pattern. | Available columns differ by dataframe construction. | Only mapped available background/latent nodes can be adjusted for. | Missing graph variables remain missing candidates. |
| Allowed nodes | Keeps graph nodes typed `background` or `latent` and present in dataframe. | Same. | yes | none material. | Observed, care-process, missingness, and outcome nodes are excluded. | Exclusion depends on source node typing. |
| Candidate pool | Allowed nodes intersect ancestors of exposure and ancestors of outcome in outgoing-edge-removed graph, minus descendants, exposure, and outcome. | Same. | yes | none material. | Candidate set is graph/source defined. | Not proof all real confounders are observed. |
| Backdoor graph | Removes outgoing treatment edges. | Removes outgoing treatment edges. | yes | Variable name resembles `G_do`. | Thesis calls it outgoing-edge-removed/backdoor helper graph. | Terminology mismatch deferred as `DF-4.4-001`. |
| Path enumeration | Enumerates undirected simple paths whose first directed edge points into treatment. | Same. | yes | none material. | Encoded backdoor paths under project DAG. | Compact-graph routine, not arbitrary graph scalability claim. |
| Collider handling | Non-collider in adjustment blocks; collider not in ancestors of adjusted nodes blocks. | Same. | yes | none material. | Standard graphical blocking logic as implemented. | Relies on graph correctness. |
| Expanded-safe mode | Starts from candidate pool, removes colliders and descendants, tests blocking. | Same. | yes | none material. | Main safe-expanded set. | May fail and fall back. |
| Minimal fallback | Greedily removes sorted variables while preserving blocking. | Same. | yes | none material. | Deterministic inclusion-minimal set under ordering. | Not unique minimal set. |
| Observed-column mapping | Reports observed confounders available in dataframe. | Reports observed confounders in control messages/model metadata. | yes | Output locations differ. | Source-level data availability diagnostic. | Needs selected-run review. |
| Missing candidates | Records graph candidates not available in dataframe. | Same. | yes | Output locations differ. | Missing graph nodes are not silently adjusted for. | May limit identification. |
| Open paths | Records open paths if available mapped nodes do not block them. | Same. | yes | Output locations differ. | Internal warning for project-DAG path blocking. | Must not be overclaimed as full causal identification. |
| Identification diagnostic | `identifiable_with_available_nodes` records if encoded paths are blocked. | Same. | yes | Output locations differ. | Project-DAG availability diagnostic. | Not definitive clinical identification. |

## 23.8 Backdoor-Terminology Audit

- Edges removed by code: outgoing edges from the treatment/proxy exposure node.
- Source naming: helper variables use names such as `G_do`, which can imply an intervention graph.
- Correct terminology for thesis: outgoing-edge-removed graph used by the project backdoor candidate routine; not the standard intervention graph that removes incoming arrows into treatment.
- Thesis wording used: "graph `G_{\underline{A}}` by removing outgoing edges from `A`" and explicit warning that it should not be confused with usual intervention graph notation.
- Deferred source-documentation issue: `DF-4.4-001`.

## 23.9 Estimator Implementation Matrix

| method | implementation file | exposure | outcome | W | X | nuisance models | treatment handling | missing-value handling | effect output | interval support | saved artifacts | diagnostic support | primary citation | limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Matching | `matching_causal_effect.py` | Binary proxy-state treatment column. | `in_hospital_mortality`. | Observed DAG-selected confounders converted to binary matching columns. | not used. | none. | Requires binary treatment; treated-control greedy Hamming pairs; no default control replacement. | Drops missing exposure/outcome; numeric confounders median-imputed; all-missing columns can become zero; non-binary numeric columns median-thresholded. | Pair effect `treated outcome - control outcome`; mean matched-pair difference. | none. | `matched_pairs.csv`, `summary_results.txt`, `global_summary.csv`, `confounder_analysis.txt`. | Match counts, match rate, allowed distance, observed confounders. | Source-only method description; no new citation inserted. | Descriptive matched contrast; not automatically ATE/ATT. |
| LinearDML | `cate_estimation.py` | Binary proxy-state treatment column. | `in_hospital_mortality`. | DAG-selected observed confounders. | Configured effect modifiers. | RandomForestRegressor for outcome and RandomForestClassifier for treatment. | `discrete_treatment=True`. | Numeric matrix construction with fill values saved in model artifact. | Patient-level CATE and `mean_cate`. | Attempts `effect_interval`; fills missing if unavailable/fails. | CATE CSV, model artifact, feature/coefficient diagnostics when aligned, global and manager summaries, control messages. | EconML direct residual/sensitivity artifacts for non-PFN branches when downstream stages run. | `chernozhukov2018dml`, `oprescu_et_al_2019_econml`. | W/X overlap possible; `mean_cate` not automatically ATE. |
| CausalForestDML | `cate_estimation.py` | Binary proxy-state treatment column. | `in_hospital_mortality`. | DAG-selected observed confounders. | Configured effect modifiers. | RandomForestRegressor for outcome and RandomForestClassifier for treatment; causal forest final stage. | `discrete_treatment=True`. | Numeric matrix construction with fill values saved in model artifact. | Patient-level CATE, feature importance, `mean_cate`. | Attempts `effect_interval`; fills missing if unavailable/fails. | CATE CSV, model artifact, feature importance, global and manager summaries, control messages. | EconML direct residual/sensitivity artifacts for non-PFN branches when downstream stages run. | `wager2018causalforest`, `athey2019grf`, `oprescu_et_al_2019_econml`. | Flexible model diagnostic outputs do not prove mechanisms. |
| CausalPFN | `cate_estimation.py` | Binary proxy-state treatment column. | `in_hospital_mortality`. | Deduplicated into feature set with effect modifiers. | Deduplicated into feature set with confounders. | CausalPFN estimator; no EconML nuisance model. | Float treatment input to PFN estimator. | Feature matrix uses deduplicated confounders plus effect modifiers; constant feature if none. | Patient-level CATE and normalized CATE. | No interval support in this pipeline; interval columns are missing. | CATE CSV and metadata artifact with estimator omitted from pickle. | EconML sensitivity and permutation stages skipped for PFN runs. | Citation gap remains; no primary CausalPFN key inserted. | Secondary/exploratory until citation and uncertainty/sensitivity support are added. |

## 23.10 Output-Schema Audit

No result values were copied into Chapter 7.

- `matched_pairs.csv`: treated/control row identifiers, treated/control `ts_id`, treated/control outcome, `pair_effect`, `hamming_distance`, and treated/control confounder values.
- Matching `global_summary.csv`: treatment, sample size, outcome rate, treatment rate, pair count, match rate, mean pair effect, standard deviation, normalized pair effect, final allowed distance, sufficient-pair flags, observed confounders, and binary matching columns.
- CATE per-treatment `*_cate.csv`: `ts_id`, treatment, `in_hospital_mortality`, `CATE`, `normalized_CATE`, interval columns for CATE and normalized CATE when available.
- Matching `summary_results.txt`: human-readable per-treatment matching summary and caveats.
- Model artifact pickle: estimator or metadata, confounders, effect modifiers, fill values, diagnostics, and run metadata; PFN skips estimator pickling.
- CATE `global_summary.csv`: treatment, model type, estimator class, counts/rates, CATE distribution summaries, normalized CATE summaries, observed/missing confounder counts, observed/missing candidates, and direct diagnostic fields.
- `control_messages_cate_estimation.csv`: run-control/provenance and diagnostic fields, including observed confounders, missing graph candidates, output paths, and estimator messages.
- `manager_global_summary.csv`: manager-level aggregation of CATE summaries.

## 23.11 Citations Used

- `pearl_1995_causal_diagrams`: DAG/backdoor graphical language only, not approval of local DAG correctness.
- `hernan_taubman_2008_well_defined_interventions`: caution around proxy exposures and well-defined interventions.
- `chernozhukov2018dml`: double machine learning concept.
- `oprescu_et_al_2019_econml`: EconML implementation family.
- `wager2018causalforest`: causal forest/heterogeneous effect method background.
- `athey2019grf`: generalized random forest background.
- `smit_2023_causal_inference_icu_scoping_review`: ICU causal-inference context.
- `bica_2021_individualized_treatment_effects_ehr_ml`: EHR individualized treatment-effect context.
- `lipkovich_2024_modern_hte_methods`: modern HTE context.
- `curth_2024_ml_individualized_treatment_effects`: ML individualized-effect context.
- `iwashyna_2015_hte_critical_care`: critical-care HTE context.
- No CausalPFN citation key was invented.
- No LLM-methodology citation key was invented.

## 23.12 Figures and Tables

- Copied figures:
  - `physionet_causal_dag.png`: source and destination SHA-256 `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2`; inserted as `fig:physionet-causal-dag`.
  - `mimic_causal_dag.png`: source and destination SHA-256 `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8`; inserted as `fig:mimic-causal-dag`.
- Inserted table labels:
  - `tab:dag-node-families`
  - `tab:adjustment-set-logic`
  - `tab:causal-assumptions`
  - `tab:causal-estimator-methods`
- Blocked figures:
  - `F-LLM-ELICITATION-01` remains planned only.  It was not generated in Stage 4.4 because the required figures for this stage are the two dataset DAG figures.
  - No dataflow, overlap, CATE, feature-importance, sensitivity, or permutation figure was generated.

## 23.13 Placeholders

- Resolved generic placeholders:
  - C7.1 `[STAGE 4 DRAFT REQUIRED]`
  - C7.1 generic `[SUPERVISOR DECISION REQUIRED]`
  - C7.1 figure comment `[FIGURE REQUIRED]`
  - C7.2 `[STAGE 4 DRAFT REQUIRED]`
  - C7.2 generic `[VALIDATION REQUIRED]`
  - C7.3 `[STAGE 4 DRAFT REQUIRED]`
  - C7.3 generic `[CITATION REQUIRED]`
  - C7.3 generic `[SUPERVISOR DECISION REQUIRED]`
- Retained/new precise Chapter 7 placeholders:
  - `[SUPERVISOR DECISION REQUIRED: approve the causal interpretation and clinical plausibility of the PhysioNet and MIMIC project DAGs]`
  - `[VALIDATION REQUIRED: document the human and clinical review decisions applied to the LLM-assisted DAG proposals]`
  - `[VALIDATION REQUIRED: recover the exact graph source commit, config, command, and output hashes for the canonical DAG artifacts]`
  - `[SUPERVISOR DECISION REQUIRED: approve the final estimand wording for proxy-state exposures]`
  - `[VALIDATION REQUIRED: validate treatment-specific adjustment sets against the selected final run artifacts]`
  - `[SUPERVISOR DECISION REQUIRED: review the use of overlapping variables in W and X]`
  - `[SUPERVISOR DECISION REQUIRED: approve or replace the interpretation of normalized\_CATE]`
  - `[CITATION REQUIRED: validated primary source for the CausalPFN method before treating it as a main thesis estimator]`
- Planned resolution stage: advisor/citation/result-manifest review before final causal results and methods freeze.

## 23.14 Deferred Fixes

- Existing relevant issues confirmed:
  - `DF-4.0-003` CausalPFN citation gap.
  - `DF-4.0-004` ignored/untracked final result archive lacks a complete manifest.
  - `DF-4.0-005` numbered final-run config CSVs are missing locally.
  - `DF-4.0-007` dedicated overlap diagnostics were not found.
  - `DF-4.3R-001` prompt execution provenance incomplete.
  - `DF-4.3R-002` human/clinical review record incomplete.
  - `DF-4.3R-003` LLM methodology citation gap if formalized.
- Newly added issues:
  - `DF-4.4-001` backdoor helper naming/terminology mismatch.
  - `DF-4.4-002` graph artifact provenance.
  - `DF-4.4-003` DAG row-level review evidence.
  - `DF-4.4-004` graph-to-data availability.
  - `DF-4.4-005` treatment-specific adjustment validation.
  - `DF-4.4-006` CATE W/X overlap.
  - `DF-4.4-007` missing-value handling.
  - `DF-4.4-008` matching order dependence.
  - `DF-4.4-009` matching binarization.
  - `DF-4.4-010` matching estimand wording.
  - `DF-4.4-011` mean CATE wording.
  - `DF-4.4-012` normalized CATE wording.
  - `DF-4.4-013` CausalPFN status.
  - `DF-4.4-014` DAG figure readability.
- Issues resolved through evidence only:
  - DAG PNG duplicate status and source-pickle agreement were verified for all 12 graph artifacts.
  - The two canonical DAG images were copied without modification and inserted into Chapter 7.

## 23.15 Final Build

- Final build commands:
  - `cd thesis-writing/thesis`
  - `latexmk -C`
  - `latexmk -xelatex main.tex`
  - `test -f main.pdf`
  - `pdfinfo main.pdf`
- Return status: success (`0`) after fixing one LaTeX placeholder underscore.
- Final PDF path: `thesis-writing/thesis/main.pdf`.
- Final page count: 64 pages.
- Final PDF SHA-256: `d3a9606ac1f7b57b055cdc60c10e9c9a24cd70da089a2b01ab382abcfb250933`.
- Citation status: final scan found no unresolved citations.
- Reference status: final scan found no unresolved references.
- Duplicate-label status: final scan found no multiply defined labels.
- Fatal errors: none in final scan.
- Biber errors: none in final scan.
- Nonfatal warnings: 27 overfull hbox warnings and 417 underfull hbox warnings.  These are layout warnings, mostly dense tables; Chapter 7 contributes expected table warnings and no fatal errors.
- Figure inclusion: `fig:physionet-causal-dag` appears on compiled PDF page 39 and `fig:mimic-causal-dag` appears on compiled PDF page 40.  Rendered page checks confirmed both figures and captions are present.
- Cleanup: `latexmk -c` was run after validation to remove generated aux files while keeping `main.pdf`.

## 23.16 Readiness

READY WITH NON-BLOCKING WARNINGS

Stage 4.4 is complete for drafting and validation.  Stage 4.5 should not begin until separately requested.  Remaining warnings are layout/provenance/citation/advisor-review issues, not build blockers.
