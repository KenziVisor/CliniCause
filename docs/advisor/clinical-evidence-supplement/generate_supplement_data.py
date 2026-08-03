#!/usr/bin/env python3
"""Generate the auditable CSV and LaTeX row layers for the clinical-evidence supplement."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]

MIMIC_TAGGER = "causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py"
PHYS_TAGGER = "causal-irregular-time-series/src/tagging_latent_variables_physionet.py"
MIMIC_EDGE_INVENTORY = "thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-edges.csv"
PHYS_EDGE_INVENTORY = "thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-edges.csv"

PROVENANCE_EXACT = "CONFIRMED EXACT ORIGINAL CHATGPT MAPPING"
PROVENANCE_FAMILY = "CONFIRMED FAMILY-LEVEL ORIGINAL CHATGPT SOURCE"
PROVENANCE_PRESENT = "SOURCE PRESENT IN CHATGPT EXPORT, EXACT MAPPING NOT RECOVERABLE"
PROVENANCE_NONE = "NO ORIGINAL CHATGPT SOURCE FOUND"

V_SUPPORT = "VERIFIED — SUPPORTS THE STATED CLAIM"
V_PARTIAL = "VERIFIED — PARTIALLY SUPPORTS THE STATED CLAIM"
V_BROAD = "VERIFIED — SUPPORTS THE BROAD CONSTRUCT, NOT THE EXACT CUTOFF"
V_ASSOC = "VERIFIED — SUPPORTS ASSOCIATION, NOT DIRECTED CAUSALITY"
V_NO_SUPPORT = "VERIFIED — DOES NOT SUPPORT THE STATED CLAIM"
V_NO_TEXT = "NOT VERIFIED — FULL TEXT UNAVAILABLE"
V_NO_SOURCE = "NOT VERIFIED — NO SPECIFIC SOURCE MAPPED"
V_NOT_INSPECTED = "NOT VERIFIED — SOURCE NOT INSPECTED"


SOURCE_FIELDS = [
    "source_id",
    "title",
    "authors",
    "year",
    "doi",
    "stable_url",
    "local_pdf_path",
    "full_text_locally_available",
    "source_origin",
    "original_chatgpt_dataset",
    "original_chatgpt_response_locator",
    "phase2_manifest_status",
    "intended_support_role",
    "independent_verification_status",
    "notes",
]


def source(
    source_id,
    title,
    authors,
    year,
    doi,
    stable_url,
    local_pdf_path,
    full_text,
    origin,
    dataset,
    chatgpt_locator,
    phase2_status,
    role,
    verification,
    notes,
):
    return dict(zip(SOURCE_FIELDS, [
        source_id, title, authors, year, doi, stable_url, local_pdf_path,
        full_text, origin, dataset, chatgpt_locator, phase2_status, role,
        verification, notes,
    ]))


SOURCES = [
    source(
        "O_SOFA_MSD",
        "Sequential Organ Failure Assessment (SOFA) score table",
        "MSD Manuals",
        "",
        "",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score",
        "",
        "No",
        "ORIGINAL_CHATGPT_SOURCE_CONFIRMED",
        "MIMIC-III; PhysioNet 2012",
        "mimic-prompt-running.pdf pp. 19, 24, 28; physionet-prompt-running.pdf pp. 20, 23-31, 44",
        "Direct final-export link; not a Phase 2 manifest record",
        "Original family-level clinical rationale for SOFA-like organ domains",
        V_NO_TEXT,
        "The export supplied an MSD derivative table, not the original 1996 paper.",
    ),
    source(
        "O_BERLIN_MSD",
        "Berlin Definition of ARDS table",
        "MSD Manuals",
        "",
        "",
        "https://www.msdmanuals.com/professional/multimedia/table/berlin-definition-of-ards",
        "",
        "No",
        "ORIGINAL_CHATGPT_SOURCE_CONFIRMED",
        "MIMIC-III",
        "mimic-prompt-running.pdf p. 26, respiratory-failure rationale",
        "Direct final-export link; not a Phase 2 manifest record",
        "Original proxy-family rationale for oxygenation thresholds",
        V_NO_TEXT,
        "The original mapping is to the MSD table; the Berlin paper was inspected later.",
    ),
    source(
        "O_KDIGO_MSD",
        "Staging criteria for acute kidney injury (KDIGO 2012) table",
        "MSD Manuals",
        "2012",
        "",
        "https://www.msdmanuals.com/professional/multimedia/table/staging-criteria-for-acute-kidney-injury-kdigo-2012",
        "",
        "No",
        "ORIGINAL_CHATGPT_SOURCE_CONFIRMED",
        "MIMIC-III",
        "mimic-prompt-running.pdf pp. 19, 27, renal-dysfunction rationale",
        "Direct final-export link; related to Phase 2 S03",
        "Original proxy-family rationale for creatinine and urine-output criteria",
        V_NO_TEXT,
        "The original mapping is to the MSD table; the KDIGO guideline was inspected later.",
    ),
    source(
        "O_SEPSIS3",
        "The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)",
        "Singer M; Deutschman CS; Seymour CW; et al.",
        "2016",
        "10.1001/jama.2016.0287",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC4968574/",
        "thesis-writing/literature/papers/clinical_sepsis3_singer_et_al_2016.pdf",
        "Yes",
        "ORIGINAL_CHATGPT_SOURCE_CONFIRMED",
        "MIMIC-III; PhysioNet 2012",
        "mimic-prompt-running.pdf pp. 19, 25; physionet-prompt-running.pdf pp. 20, 30",
        "Phase 2 S04; local corpus record",
        "Original family-level rationale for sepsis-like burden, organ dysfunction and shock",
        V_BROAD,
        "Inspected local full text, PDF p. 1 (journal p. 801) and definitions section; it does not validate either local composite.",
    ),
    source(
        "O_SISK2021",
        "Informative presence and observation in routine health data: a review of methodology for clinical risk prediction",
        "Sisk R; Sperrin M; Peek N; et al.",
        "2021",
        "10.1093/jamia/ocaa242",
        "https://academic.oup.com/jamia/article/28/1/155/5961436",
        "",
        "No",
        "ORIGINAL_CHATGPT_SOURCE_FAMILY_LEVEL",
        "MIMIC-III",
        "mimic-prompt-running.pdf p. 36, missingness discussion",
        "Phase 2 S11; no local PDF",
        "Original family-level source for informative observation and monitoring intensity",
        V_NO_TEXT,
        "Link is preserved in the final export; full text was not locally available for this build.",
    ),
    source(
        "O_JMIR2025",
        "JMIR Medical Informatics article e79307 (title/authors not recoverable from local metadata)",
        "",
        "2025",
        "",
        "https://medinform.jmir.org/2025/1/e79307",
        "",
        "No",
        "ORIGINAL_CHATGPT_SOURCE_FAMILY_LEVEL",
        "PhysioNet 2012",
        "physionet-prompt-running.pdf pp. 16, 38, missingness discussion",
        "Direct final-export link; not a Phase 2 manifest record",
        "Original family-level source for care-generated informative missingness",
        V_NO_TEXT,
        "No outside metadata resolution was performed.",
    ),
    source(
        "O_DAG_PRIMER",
        "Causal-DAG document hosted by Oxford Research Archive (metadata not recoverable locally)",
        "",
        "",
        "",
        "https://ora.ox.ac.uk/objects/uuid%3A36b9a9af-309a-4dc8-943c-64287a72702a/files/m33f79696823b697eb8c57db1364b021a",
        "",
        "No",
        "ORIGINAL_CHATGPT_SOURCE_UNMAPPED",
        "PhysioNet 2012",
        "physionet-prompt-running.pdf pp. 38-39, general DAG/backdoor discussion",
        "Direct final-export link; not a Phase 2 manifest record",
        "General DAG/confounder/mediator/collider rationale, not clinical edge support",
        V_NO_TEXT,
        "Not mapped to any particular implemented edge.",
    ),
    source(
        "V_SOFA1996",
        "The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure",
        "Vincent JL; Moreno R; Takala J; et al.",
        "1996",
        "10.1007/BF01709751",
        "https://link.springer.com/article/10.1007/BF01709751",
        "thesis-writing/advisor/41786868.pdf",
        "Yes",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S01; local PDF later supplied",
        "Independent verification of SOFA organ domains and their published thresholds",
        V_BROAD,
        "Inspected pp. 1-4; Table 3 on PDF p. 2. Not part of the preserved original ChatGPT source link.",
    ),
    source(
        "V_BERLIN2012",
        "Acute Respiratory Distress Syndrome: The Berlin Definition",
        "ARDS Definition Task Force",
        "2012",
        "10.1001/jama.2012.5669",
        "https://jamanetwork.com/journals/jama/fullarticle/1160659",
        "thesis-writing/advisor/4.-acute-respiratory-distress-syndromethe-berlin-definition.pdf",
        "Yes",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S02; local PDF later supplied",
        "Independent verification of ARDS timing, imaging, edema-exclusion, PEEP and P/F criteria",
        V_BROAD,
        "Inspected PDF pp. 4-6; the CliniCause respiratory proxy omits several Berlin requirements.",
    ),
    source(
        "V_KDIGO2012",
        "KDIGO Clinical Practice Guideline for Acute Kidney Injury",
        "KDIGO Acute Kidney Injury Work Group",
        "2012",
        "",
        "https://kdigo.org/guidelines/acute-kidney-injury/",
        "thesis-writing/literature/papers/clinical_kdigo_acute_kidney_injury_2012.pdf",
        "Yes",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S03; local corpus record",
        "Independent verification of AKI creatinine-change and urine-output criteria",
        V_BROAD,
        "Inspected PDF p. 11, section 2.1 and Table 2; the local renal composites add non-KDIGO clauses.",
    ),
    source(
        "V_DIC2001",
        "Towards definition, clinical and laboratory criteria, and a scoring system for disseminated intravascular coagulation",
        "Taylor FB Jr; Toh CH; Hoots WK; Wada H; Levi M",
        "2001",
        "10.1055/s-0037-1616068",
        "https://pubmed.ncbi.nlm.nih.gov/11816725/",
        "thesis-writing/literature/papers/clinical_dic_isth_taylor_et_al_2001.pdf",
        "Yes",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S05; local corpus record",
        "Independent verification of overt-DIC laboratory scoring concepts",
        V_BROAD,
        "Inspected PDF pp. 1-3, especially Table 2 on p. 2; local mixed composites are not the ISTH score.",
    ),
    source(
        "V_GCS1974",
        "Assessment of coma and impaired consciousness: a practical scale",
        "Teasdale G; Jennett B",
        "1974",
        "10.1016/S0140-6736(74)91639-0",
        "https://pubmed.ncbi.nlm.nih.gov/4136544/",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S06; metadata only",
        "Potential verification of GCS as a structured consciousness measure",
        V_NO_TEXT,
        "Not used to claim support for the multi-clause neurological proxies.",
    ),
    source(
        "V_UDMI2018",
        "Fourth Universal Definition of Myocardial Infarction (2018)",
        "Thygesen K; Alpert JS; Jaffe AS; et al.",
        "2018",
        "10.1161/CIR.0000000000000617",
        "https://www.ahajournals.org/doi/10.1161/CIR.0000000000000617",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S07; metadata only",
        "Potential verification of assay-specific troponin myocardial-injury concepts",
        V_NO_TEXT,
        "No local full text; fixed project cutoffs remain unverified.",
    ),
    source(
        "V_TROPONIN2015",
        "Raised cardiac troponin in intensive care patients with sepsis: a systematic review",
        "Zochios V; Valchanov K",
        "2015",
        "",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC5593290/",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S08; no local PDF",
        "Potential context for troponin elevation in critical illness",
        V_NO_TEXT,
        "No local full text was inspected.",
    ),
    source(
        "V_ELECTROLYTES2010",
        "Fluid and Electrolyte Disturbances in Critically Ill Patients",
        "Lee JW",
        "2010",
        "",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC3043756/",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S09; no local PDF",
        "Potential broad support for electrolyte and acid-base derangement",
        V_NO_TEXT,
        "No local full text was inspected; exact composite remains unsupported.",
    ),
    source(
        "V_MISSING2019",
        "A New Insight Into Missing Data in Intensive Care Unit Patient Profiles: Observational Study",
        "Sharafoddini A; Dubin JA; Maslove DM; Lee J",
        "2019",
        "10.2196/11605",
        "https://medinform.jmir.org/2019/1/e11605/",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S10; no local PDF",
        "Potential independent support for informative ICU missingness",
        V_NO_TEXT,
        "No local full text was inspected.",
    ),
    source(
        "V_BANDA2018",
        "Advances in Electronic Phenotyping: From Rule-Based Definitions to Machine Learning Models",
        "Banda JM; Seneviratne M; Hernandez-Boussard T; Shah NH",
        "2018",
        "10.1146/annurev-biodatasci-080917-013315",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC6583807/",
        "thesis-writing/literature/papers/phenotyping_ehr_banda_et_al_2018.pdf",
        "Yes",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S12; local corpus record",
        "Independent support for explicit rule-based EHR phenotyping and validation needs",
        V_SUPPORT,
        "Inspected PDF pp. 1-6 and validation discussion; it supports the method class, not any local threshold.",
    ),
    source(
        "V_ESSAY2020",
        "Rule-Based Cohort Definitions for Acute Respiratory Failure: Electronic Phenotyping Algorithm",
        "Essay P; Mosier J; Subbian V",
        "2020",
        "10.2196/18402",
        "https://medinform.jmir.org/2020/4/e18402/",
        "thesis-writing/literature/papers/phenotyping_respiratory_failure_essay_et_al_2020.pdf",
        "Yes",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S13; local corpus record",
        "Independent support for rule-based respiratory phenotyping from structured EHR data",
        V_BROAD,
        "Inspected PDF pp. 1-4; its ventilation-therapy phenotypes do not validate CliniCause gas thresholds.",
    ),
    source(
        "V_ELIXHAUSER1998",
        "Comorbidity measures for use with administrative data",
        "Elixhauser A; Steiner C; Harris DR; Coffey RM",
        "1998",
        "10.1097/00005650-199801000-00004",
        "https://pubmed.ncbi.nlm.nih.gov/9431328/",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S14; metadata only",
        "Potential broad support for administrative comorbidity measurement",
        V_NO_TEXT,
        "No local full text and no support for the project cutoff.",
    ),
    source(
        "V_CHARLSON1987",
        "A new method of classifying prognostic comorbidity in longitudinal studies",
        "Charlson ME; Pompei P; Ales KL; MacKenzie CR",
        "1987",
        "",
        "https://pubmed.ncbi.nlm.nih.gov/3558716/",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S15; metadata only",
        "Potential broad support for weighted comorbidity concepts",
        V_NO_TEXT,
        "No local full text and no support for the project composite.",
    ),
    source(
        "V_ALBUMIN2003",
        "Hypoalbuminemia in acute illness: is there a rationale for intervention?",
        "Vincent JL; Dubois MJ; Navickis RJ; Wilkes MM",
        "2003",
        "",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC1514323/",
        "",
        "No",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Phase 2 S16; no local PDF",
        "Potential association evidence for low albumin in acute illness",
        V_NO_TEXT,
        "No local full text was inspected for this build.",
    ),
    source(
        "V_LIPTON2016",
        "Modeling Missing Data in Clinical Time Series with RNNs",
        "Lipton ZC; Kale DC; Wetzel R",
        "2016",
        "",
        "https://proceedings.mlr.press/v56/Lipton16.html",
        "thesis-writing/literature/papers/model_missingness_rnn_lipton_et_al_2016.pdf",
        "Yes",
        "NEW_INDEPENDENT_VERIFICATION_SOURCE",
        "",
        "",
        "Existing local literature corpus; not in Phase 2 manifest",
        "Independent verification that ICU observation patterns can be care-generated and predictive",
        V_ASSOC,
        "Inspected PDF pp. 1-3; predictive informativeness does not establish the final DAG directions.",
    ),
]


PROXY_FIELDS = [
    "dataset",
    "proxy_name",
    "source_columns",
    "aggregation_or_window",
    "exact_rule",
    "clinical_interpretation",
    "current_implementation_path",
    "implementation_locator",
    "implementation_mode_status",
    "original_chatgpt_source_ids",
    "original_chatgpt_mapping_status",
    "original_chatgpt_locator",
    "support_paraphrase",
    "doi_or_url",
    "independent_verification_source_ids",
    "verification_verdict",
    "verification_locator",
    "limitations",
]


def proxy(*values):
    assert len(values) == len(PROXY_FIELDS)
    return dict(zip(PROXY_FIELDS, values))


M_MODE = (
    "Current default: canonical pickle; whole-record minima/maxima/first values and any-flags, "
    "except explicit first-24h and rolling-6h urine features. Summary-CSV and raw-concept modes "
    "also exist; historical producing input mode/revision not verified."
)
P_MODE = (
    "Current used mode: default thresholds (optimization excluded by project-owner clarification); "
    "whole first-48h record summarized by min/max/mean/first/last. Historical producing input "
    "artifact/revision not verified."
)
M_WINDOW = "Whole available ICU record summaries; urine sum at 0-24h and minimum rolling 6h mL/kg/h; missing clauses do not fire."
P_WINDOW = "Whole first-48h Challenge record; min/max/mean/first/last summaries; missing clauses do not fire."


PROXIES = [
    proxy(
        "MIMIC-III", "LAT_INFLAMMATION_SEPSIS",
        "Temperature_min/max; WBC_min/max; Lactate_max; CultureOrdered_any; CulturePositive_any; SuspectedInfection_any; AntibioticStarted_any/Antibiotics_any",
        M_WINDOW,
        "Five indicators: temperature >=38.3 or <36; WBC >12 or <4; lactate >2; culture/suspected-infection; antibiotic/suspected-infection. Positive if score >=2 and a culture, antibiotic, temperature or WBC anchor is present.",
        "Inflammation or suspected-infection/sepsis burden; not confirmed sepsis.",
        MIMIC_TAGGER, "lines 588-616", M_MODE,
        "O_SEPSIS3", PROVENANCE_EXACT, "mimic-prompt-running.pdf pp. 19, 22-23",
        "Sepsis-3 supports infection-related dysregulated host response and organ dysfunction, but not this five-clause score.",
        "10.1001/jama.2016.0287", "O_SEPSIS3", V_BROAD,
        "Sepsis-3 local PDF p. 1 (journal p. 801) and definitions section",
        "Temperature/WBC are nonspecific; treatment and culture fields encode clinician suspicion; the exact score is not validated.",
    ),
    proxy(
        "MIMIC-III", "LAT_GLOBAL_SEVERITY",
        "MAP_min; SBP_min; Vasopressors_any; SpO2_min; PF_ratio_min; MechanicalVentilation_any; GCS_min; RASS_min/max; Creatinine_max; UrineOutput_sum_24h; Lactate_max; pH_min; Bicarbonate_min; Temperature_min/max; WBC_min/max; Bilirubin_max; Platelets_min; INR_max",
        M_WINDOW,
        "Seven Boolean domains (circulatory, respiratory, neurologic, renal, metabolic, inflammatory, hepatic/coagulation); positive if at least 3 domains are abnormal.",
        "Multi-domain acute physiological severity.",
        MIMIC_TAGGER, "lines 619-679", M_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "mimic-prompt-running.pdf p. 24",
        "The original source presents SOFA organ domains. The original SOFA paper verifies six domains and daily worst values, not the local seven-domain Boolean composite.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1007/BF01709751",
        "V_SOFA1996", V_BROAD, "SOFA local PDF pp. 1-2, Table 3 on p. 2",
        "Local substitutions, inflammatory domain and score >=3 are project choices; whole-record aggregation differs from daily SOFA scoring.",
    ),
    proxy(
        "MIMIC-III", "LAT_SHOCK",
        "MAP_min; SBP_min; MAP_sustained_lt70_any; Vasopressors_any; Lactate_max; UrineOutput_sum_24h; UrineOutput_mlkg_6h_min; pH_min; BaseExcess_min",
        M_WINDOW,
        "Five indicators: hypotension (MAP <65, SBP <=90 or sustained MAP <70), vasopressor, lactate >2, oliguria (<0.5 mL/kg/h over 6h or <500 mL/24h), acidosis (pH <7.30 or base excess <=-5). Positive if score >=2, or vasopressor plus hypoperfusion/acidosis/hypotension.",
        "Circulatory shock or clinically meaningful hemodynamic instability.",
        MIMIC_TAGGER, "lines 682-710", M_MODE,
        "O_SEPSIS3; O_SOFA_MSD", PROVENANCE_EXACT, "mimic-prompt-running.pdf pp. 24-25",
        "Sepsis-3 supports vasopressor-dependent hypotension with lactate >2 for septic shock; it does not support the project's any-two composite.",
        "10.1001/jama.2016.0287; https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score",
        "O_SEPSIS3; V_SOFA1996", V_BROAD,
        "Sepsis-3 local PDF p. 1; SOFA local PDF p. 2, Table 3",
        "Rule is broader than septic shock and mixes treatment, perfusion, urine and acid-base evidence.",
    ),
    proxy(
        "MIMIC-III", "LAT_RESPIRATORY_FAILURE",
        "SpO2_min; PF_ratio_min; FiO2_max; MechanicalVentilation_any; NonInvasiveVentilation_any; RR_min/max; PaCO2_max; pH_min",
        M_WINDOW,
        "Five indicators: SpO2 <92; P/F <=300; respiratory support or FiO2 >=0.5; RR >=30 or <=8; PaCO2 >=50 with pH <7.30. Positive if score >=2, or support plus hypoxemia/PF/ventilatory failure.",
        "Hypoxemic or ventilatory failure and/or substantial respiratory support.",
        MIMIC_TAGGER, "lines 713-741", M_MODE,
        "O_BERLIN_MSD", PROVENANCE_EXACT, "mimic-prompt-running.pdf p. 26",
        "Berlin supports P/F severity categories under PEEP/CPAP plus timing, imaging and edema-origin requirements; the project proxy is broader.",
        "https://www.msdmanuals.com/professional/multimedia/table/berlin-definition-of-ards; 10.1001/jama.2012.5669",
        "V_BERLIN2012; V_ESSAY2020", V_BROAD,
        "Berlin local PDF pp. 4-6; Essay local PDF pp. 1-4",
        "Not an ARDS diagnosis; several Berlin criteria are absent and ventilation may reflect treatment/case mix.",
    ),
    proxy(
        "MIMIC-III", "LAT_RENAL_DYSFUNCTION",
        "Creatinine_max/delta; BUN_max; UrineOutput_sum_24h; UrineOutput_mlkg_6h_min; Potassium_max; Bicarbonate_min; DialysisOrCRRT_any",
        M_WINDOW,
        "Five indicators: creatinine >=2 or rise >=0.3; BUN >=40; oliguria (<0.5 mL/kg/h over 6h or <500 mL/24h); K >=5.5 or HCO3 <18; dialysis. Positive if score >=2 or dialysis.",
        "Acute or clinically important renal dysfunction.",
        MIMIC_TAGGER, "lines 744-771", M_MODE,
        "O_KDIGO_MSD", PROVENANCE_EXACT, "mimic-prompt-running.pdf p. 27",
        "KDIGO supports a >=0.3 mg/dL creatinine rise, baseline-relative changes and urine-output criteria; it does not validate this composite or BUN/electrolyte clauses.",
        "https://www.msdmanuals.com/professional/multimedia/table/staging-criteria-for-acute-kidney-injury-kdigo-2012; https://kdigo.org/guidelines/acute-kidney-injury/",
        "V_KDIGO2012", V_BROAD, "KDIGO local PDF p. 11, section 2.1 and Table 2",
        "Baseline creatinine may be unavailable; absolute creatinine, BUN and metabolic additions are project choices.",
    ),
    proxy(
        "MIMIC-III", "LAT_HEPATIC_COAG_DYSFUNCTION",
        "Bilirubin_max; AST_max; ALT_max; Platelets_min; INR_max; PTProlonged_any; PTTProlonged_any; Albumin_min/first",
        M_WINDOW,
        "Five indicators: bilirubin >=2; AST or ALT >=120; platelets <100; INR >=1.5 or prolonged PT/PTT; albumin <2.5. Positive if score >=2.",
        "Combined hepatic injury/reserve and coagulation dysfunction.",
        MIMIC_TAGGER, "lines 774-798", M_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "mimic-prompt-running.pdf p. 28",
        "SOFA supports bilirubin and platelets as separate organ domains; ISTH DIC uses a different multi-test algorithm. Neither validates the combined local score.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1007/BF01709751",
        "V_SOFA1996; V_DIC2001", V_BROAD,
        "SOFA local PDF p. 2, Table 3; ISTH DIC local PDF p. 2, Table 2",
        "Combines distinct constructs; anticoagulation, chronic liver disease, dilution and nutrition can trigger clauses.",
    ),
    proxy(
        "MIMIC-III", "LAT_NEUROLOGIC_DYSFUNCTION",
        "GCS_min; GCSComponentAbnormal_any; RASS_min/max; PupilOrFocalNeuroAbnormal_any; SedationOrIntubation_any",
        M_WINDOW,
        "GCS <=8 contributes 2; else GCS <=13 contributes 1; abnormal GCS component, RASS <=-3 or >=2, and pupil/focal abnormality each contribute 1. Positive if score >=2; sedation/intubation with an isolated one-point score is forced negative.",
        "Depressed consciousness or focal/behavioral neurological dysfunction.",
        MIMIC_TAGGER, "lines 801-823", M_MODE,
        "O_SOFA_MSD", PROVENANCE_PRESENT, "mimic-prompt-running.pdf: SOFA source present; no proxy-specific source chip recovered",
        "SOFA uses GCS as its neurological domain, but does not support the RASS, focal-sign or sedation-exclusion composite.",
        "10.1007/BF01709751", "V_SOFA1996", V_BROAD,
        "SOFA local PDF p. 2, Table 3",
        "Sedation/intubation can confound GCS/RASS; exact weighting and exclusions lack direct literature validation.",
    ),
    proxy(
        "MIMIC-III", "LAT_METABOLIC_DERANGEMENT",
        "pH_min/max; Bicarbonate_min/max; BaseExcess_min; Lactate_max; Potassium_min/max; Sodium_min/max; Glucose_min/max",
        M_WINDOW,
        "Six domains: pH <7.30 or >7.55; HCO3 <18 or >35 or base excess <=-5; lactate >2; K <3 or >=5.5; Na <130 or >150; glucose <70 or >250. Positive if at least 2 domains are abnormal.",
        "Acid-base, lactate, electrolyte or glucose derangement.",
        MIMIC_TAGGER, "lines 826-873", M_MODE,
        "", PROVENANCE_NONE, "No proxy-specific source mapped in preserved final export",
        "No locally inspected paper validates the exact six-domain score.",
        "", "", V_NO_SOURCE, "",
        "Broad construct is plausible but all cutoffs and the any-two combination remain unverified.",
    ),
    proxy(
        "MIMIC-III", "LAT_CARDIAC_STRAIN",
        "TroponinPositive/AboveULN flags; TroponinT_max; TroponinI_max; CKMB_max/AboveULN; Arrhythmia_any; HR_min/max; MAP_min; SBP_min; FirstCareUnit; CardiacSurgeryContext_any",
        M_WINDOW,
        "Five indicators: troponin abnormal (or T >=0.1/I >=0.4 fallback); CK-MB abnormal; arrhythmia or HR >150/<40; HR >130 or <40 with hypotension; CCU/CSRU or cardiac-surgery context. Positive if score >=2 and troponin or rhythm anchor.",
        "Myocardial injury, rhythm instability or severe cardiac strain.",
        MIMIC_TAGGER, "lines 876-908", M_MODE,
        "", PROVENANCE_NONE, "No proxy-specific source mapped in preserved final export",
        "Phase 2 identified myocardial-injury sources, but their full text was not locally available and they were not original ChatGPT sources.",
        "10.1161/CIR.0000000000000617", "V_UDMI2018; V_TROPONIN2015", V_NO_TEXT, "",
        "Assay-specific troponin thresholds, CK-MB >0, unit/care-context points and the composite are not verified.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_GLOBAL_SEVERITY",
        "MAP/NIMAP/SysABP/NISysABP_min; MechVent_max; PF_min or PaO2/FiO2 approximation; SaO2_min; RespRate_max; GCS_min; Creatinine/BUN_max; urine summary; Bilirubin_max; Platelets_min; Lactate_max; pH_min; HCO3_min; TropI/T_max; HR_max",
        P_WINDOW,
        "Seven domains (hemodynamic, respiratory, neurologic, renal, hepatic/coagulation, metabolic, cardiac). Positive if score >=3, or score >=2 plus lactate >=4, pH <7.20, ventilation, GCS <=8 or MAP <60.",
        "Multi-domain first-48h acute physiological severity.",
        PHYS_TAGGER, "lines 421-478", P_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "physionet-prompt-running.pdf pp. 20, 23",
        "SOFA supports six organ domains and published ordinal thresholds, not the project's seven Boolean domains or critical override.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1007/BF01709751",
        "V_SOFA1996", V_BROAD, "SOFA local PDF pp. 1-2, Table 3",
        "Adds cardiac/metabolic substitutions and uses whole-48h summaries rather than daily SOFA scoring.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_SHOCK",
        "MAP/NIMAP/SysABP/NISysABP_min; Lactate_max; HR_max; urine summary; pH_min; HCO3_min",
        P_WINDOW,
        "Six indicators: MAP/NIMAP <70; SBP/NISBP <=90; lactate >2; HR >=110; urine <500; pH <7.30 or HCO3 <18. Positive if score >=2 or low MAP with lactate >=4.",
        "Circulatory shock or hemodynamic instability without vasopressor data.",
        PHYS_TAGGER, "lines 481-506", P_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "physionet-prompt-running.pdf p. 24",
        "SOFA supports MAP <70 as cardiovascular dysfunction; it does not support the complete any-two score or lactate override.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1007/BF01709751",
        "V_SOFA1996; O_SEPSIS3", V_BROAD,
        "SOFA local PDF p. 2, Table 3; Sepsis-3 local PDF p. 1",
        "No vasopressor field; low BP, tachycardia, oliguria and acidosis are nonspecific.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_RESPIRATORY_FAILURE",
        "MechVent_max; PF_min or PaO2/FiO2 approximation; SaO2_min; PaO2_min; RespRate_min/max; PaCO2_max; pH_min",
        P_WINDOW,
        "Five indicators: ventilation; P/F <300; SaO2 <92 or PaO2 <60; RR >=22 or <8; PaCO2 >=50 or PaCO2 >=45 with pH <7.30. Positive if score >=2 or ventilation plus P/F <300.",
        "Hypoxemic or ventilatory respiratory failure/support.",
        PHYS_TAGGER, "lines 509-535", P_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "physionet-prompt-running.pdf p. 25",
        "SOFA supports P/F oxygenation scoring; Berlin and Essay support narrower respiratory/ventilation constructs, not this full composite.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1001/jama.2012.5669",
        "V_SOFA1996; V_BERLIN2012; V_ESSAY2020", V_BROAD,
        "SOFA p. 2 Table 3; Berlin pp. 4-6; Essay pp. 1-4",
        "P/F may be approximated from non-paired extrema; not an ARDS diagnosis.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_RENAL_DYSFUNCTION",
        "Creatinine_first/max; BUN_max; urine summary; K_max; HCO3_min",
        P_WINDOW,
        "Five indicators: creatinine >=2; creatinine rise >=0.3; BUN >=40; urine <500; K >=5.5 or HCO3 <18. Positive if score >=2 or creatinine >=3.5.",
        "Acute or clinically important renal dysfunction.",
        PHYS_TAGGER, "lines 538-561", P_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "physionet-prompt-running.pdf p. 27",
        "SOFA supports creatinine/urine domains; KDIGO supports >=0.3 rise and timed urine criteria, not the whole local score.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; https://kdigo.org/guidelines/acute-kidney-injury/",
        "V_SOFA1996; V_KDIGO2012", V_BROAD,
        "SOFA p. 2 Table 3; KDIGO p. 11 section 2.1/Table 2",
        "Current urine helper accepts precomputed summary names that the simple summarizer does not itself create; baseline CKD is unresolved.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_HEPATIC_DYSFUNCTION",
        "Bilirubin_max; AST_max; ALT_max; ALP_max; Albumin_min; Platelets_min",
        P_WINDOW,
        "Weighted score: bilirubin >=2 contributes 2; AST/ALT >=200, ALP >=250, albumin <2.5 and platelets <100 each contribute 1. Positive if score >=2.",
        "Cholestatic/hepatocellular injury or impaired hepatic reserve.",
        PHYS_TAGGER, "lines 564-579", P_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "physionet-prompt-running.pdf p. 28",
        "SOFA supports bilirubin as a liver-domain marker; the added enzymes, albumin and platelet weighting are not the SOFA definition.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1007/BF01709751",
        "V_SOFA1996", V_BROAD, "SOFA local PDF p. 2, Table 3",
        "Chronic liver disease, hemolysis and acute inflammation can trigger clauses; exact composite unsupported.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_COAG_HEME_DYSFUNCTION",
        "Platelets_first/min; HCT_min/max; WBC_min/max",
        P_WINDOW,
        "Weighted score: platelets <100 contributes 2; platelets <150, HCT <25/>55, WBC <4/>20, and platelet drop >=50 each contribute 1. Positive if score >=2.",
        "Thrombocytopenia, anemia/polycythemia or hematologic stress.",
        PHYS_TAGGER, "lines 582-606", P_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "physionet-prompt-running.pdf p. 29",
        "SOFA supports platelet thresholds; ISTH DIC uses platelets with PT, fibrin-related markers and fibrinogen, not HCT/WBC additions.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1055/s-0037-1616068",
        "V_SOFA1996; V_DIC2001", V_BROAD,
        "SOFA p. 2 Table 3; ISTH DIC p. 2 Table 2",
        "Not a DIC diagnosis; overlapping platelet weights and non-coagulation HCT/WBC clauses are project choices.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_INFLAMMATION_SEPSIS_BURDEN",
        "Temp_min/max; WBC_min/max; HR_max; RespRate_max; PaCO2_min; Lactate_max; Platelets_min",
        P_WINDOW,
        "Six indicators: temperature >38.3 or <36; WBC >12 or <4; HR >90; RR >20 or PaCO2 <32; lactate >2; platelets <150. Positive if score >=3, or temperature/WBC abnormal plus lactate and score >=2.",
        "Systemic inflammatory or sepsis-like host response; not confirmed sepsis.",
        PHYS_TAGGER, "lines 609-632", P_MODE,
        "O_SEPSIS3", PROVENANCE_EXACT, "physionet-prompt-running.pdf p. 30",
        "Sepsis-3 requires infection-related organ dysfunction and explicitly supersedes a simple inflammation-only framing; the local dataset lacks an infection anchor.",
        "10.1001/jama.2016.0287", "O_SEPSIS3", V_BROAD,
        "Sepsis-3 local PDF p. 1 and definitions section",
        "False positives include sterile inflammation; exact SIRS-like score is not Sepsis-3.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_NEUROLOGIC_DYSFUNCTION",
        "GCS_min; Na_min/max; Glucose_min/max; PaCO2_max; SaO2_min; pH_min",
        P_WINDOW,
        "GCS <=12 contributes 2; GCS <15, sodium <130/>150 or glucose <70/>300, and PaCO2 >=50/SaO2 <90/pH <7.25 each contribute 1. Positive if score >=2.",
        "Depressed consciousness or neurological dysfunction with metabolic/gas contributors.",
        PHYS_TAGGER, "lines 635-655", P_MODE,
        "O_SOFA_MSD", PROVENANCE_EXACT, "physionet-prompt-running.pdf p. 31",
        "SOFA supports GCS as a neurological domain; it does not support adding electrolyte/gas clauses to the same weighted proxy.",
        "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score; 10.1007/BF01709751",
        "V_SOFA1996", V_BROAD, "SOFA local PDF p. 2, Table 3",
        "Sedation/ventilation context is not used by the current function; metabolic/gas abnormalities can create nonspecific positives.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_CARDIAC_INJURY_STRAIN",
        "TropI/T_max; ICUType_first; HR_min/max; MAP_min; SysABP_min; Lactate_max",
        P_WINDOW,
        "Weighted score: troponin I >0.1 or T >0.01 contributes 2; ICU type 1/2, HR >=130/<50, MAP <70 or SBP <=90, and lactate >2 each contribute 1. Positive if score >=2.",
        "Myocardial injury, ischemia or severe cardiac strain.",
        PHYS_TAGGER, "lines 658-679", P_MODE,
        "", PROVENANCE_NONE, "No proxy-specific source mapped in preserved final export",
        "Phase 2 identified myocardial-injury sources, but no local full text was available and no original source was mapped.",
        "10.1161/CIR.0000000000000617", "V_UDMI2018; V_TROPONIN2015", V_NO_TEXT, "",
        "Troponin assay thresholds are not harmonized; ICU type can make the proxy positive with one additional nonspecific signal.",
    ),
    proxy(
        "PhysioNet 2012", "LAT_METABOLIC_DERANGEMENT",
        "pH_min/max; HCO3_min/max; Lactate_max; Na_min/max; K_min/max; Mg_min/max; Glucose_min/max; PaCO2_min/max",
        P_WINDOW,
        "Six domains: pH <7.30/>7.50; HCO3 <18/>32; lactate >2; Na <130/>150, K <3/>5.5 or Mg <0.6/>1.2; glucose <70/>250; PaCO2 <32/>50. Positive if score >=2 or pH <7.20, lactate >=4 or K >=6.",
        "Acid-base, lactate, electrolyte or glucose derangement.",
        PHYS_TAGGER, "lines 682-720", P_MODE,
        "", PROVENANCE_NONE, "No proxy-specific source mapped in preserved final export",
        "No locally inspected paper validates this exact multi-domain score or critical overrides.",
        "", "", V_NO_SOURCE, "",
        "Cutoffs, domain grouping and sufficient conditions are project choices.",
    ),
]


DAG_FIELDS = [
    "dataset",
    "edge_number",
    "parent",
    "child",
    "edge_inventory_path",
    "clinical_rationale",
    "rationale_origin",
    "original_chatgpt_source_ids",
    "original_chatgpt_mapping_status",
    "original_chatgpt_locator",
    "doi_or_url",
    "independent_verification_source_ids",
    "independent_verification_status",
    "support_verdict",
    "verification_locator",
    "limitations",
]


def edge_rationale(parent: str, child: str) -> str:
    if parent.startswith("BG_") and child.startswith("LAT_"):
        return "Project assumption: baseline/case-mix context precedes and influences the downstream proxy state."
    if parent.startswith("BG_") and child.startswith("MISS_"):
        return "Project assumption: case mix and care setting influence monitoring or test-ordering intensity."
    if parent.startswith("BG_") and child.startswith("OUT_"):
        return "Project assumption: baseline risk can affect mortality through measured and unmeasured pathways."
    if parent.startswith("LAT_") and child.startswith("LAT_"):
        return "Project structural hypothesis: the parent physiological state is upstream of the child state."
    if parent.startswith("LAT_") and child.startswith("OBS_"):
        return "Measurement-model edge: the observed group is treated as a manifestation or measurement of the parent proxy state."
    if parent.startswith("LAT_") and child.startswith("TRT_"):
        return "Care-process edge: evidence of the parent state is assumed to prompt or indicate the recorded treatment."
    if parent.startswith("LAT_") and child.startswith("MISS_"):
        return "Observation-process edge: the parent state is assumed to influence selective ordering or monitoring."
    if parent.startswith("LAT_") and child.startswith("OUT_"):
        return "Outcome edge: the parent state is assumed to represent pathophysiologic burden related to mortality."
    if parent.startswith("MISS_") and child.startswith("OBS_"):
        return "Observation-process edge: ordering or measurement intensity determines recorded availability/counts."
    if parent.startswith("TRT_") and child.startswith("OBS_"):
        return "Treatment/recording edge: delivered care changes or generates the recorded observed-data group."
    return "Project-specified directed relationship; no more specific rationale was recovered."


def original_edge_mapping(dataset: str, parent: str, child: str):
    locator = (
        "mimic-prompt-running.pdf sections 6 and 10"
        if dataset == "MIMIC-III"
        else "physionet-prompt-running.pdf sections 6 and 10"
    )
    if "INFLAMMATION_SEPSIS" in parent:
        return "O_SEPSIS3", PROVENANCE_FAMILY, locator, "10.1001/jama.2016.0287"
    if parent.startswith("MISS_") or child.startswith("MISS_") or "MEASUREMENT_INTENSITY" in parent.upper():
        if dataset == "MIMIC-III":
            return "O_SISK2021", PROVENANCE_FAMILY, locator, "10.1093/jamia/ocaa242"
        return "O_JMIR2025", PROVENANCE_FAMILY, locator, "https://medinform.jmir.org/2025/1/e79307"
    if parent.startswith("LAT_GLOBAL_SEVERITY"):
        return "O_SOFA_MSD", PROVENANCE_PRESENT, locator, "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score"
    if parent.startswith("LAT_RESPIRATORY_FAILURE"):
        source_id = "O_BERLIN_MSD" if dataset == "MIMIC-III" else "O_SOFA_MSD"
        return source_id, PROVENANCE_PRESENT, locator, (
            "https://www.msdmanuals.com/professional/multimedia/table/berlin-definition-of-ards"
            if dataset == "MIMIC-III"
            else "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score"
        )
    if parent.startswith("LAT_RENAL_DYSFUNCTION"):
        source_id = "O_KDIGO_MSD" if dataset == "MIMIC-III" else "O_SOFA_MSD"
        return source_id, PROVENANCE_PRESENT, locator, (
            "https://www.msdmanuals.com/professional/multimedia/table/staging-criteria-for-acute-kidney-injury-kdigo-2012"
            if dataset == "MIMIC-III"
            else "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score"
        )
    if any(key in parent for key in ("HEPATIC", "COAG", "NEUROLOGIC", "SHOCK")):
        return "O_SOFA_MSD", PROVENANCE_PRESENT, locator, "https://www.msdmanuals.com/professional/multimedia/table/sequential-organ-failure-assessment-sofa-score"
    return "", PROVENANCE_NONE, locator, ""


def verification_for_edge(parent: str, child: str):
    if parent.startswith("MISS_") and child.startswith("OBS_"):
        return (
            "V_LIPTON2016",
            V_ASSOC,
            "Lipton et al. local PDF pp. 1-2",
            "Paper shows care-generated observation patterns can be predictive; it does not establish this dataset-specific arrow.",
        )
    if parent.startswith("LAT_INFLAMMATION_SEPSIS"):
        verdict = V_ASSOC if (child.startswith("LAT_") or child.startswith("OUT_")) else V_PARTIAL
        return (
            "O_SEPSIS3",
            verdict,
            "Sepsis-3 local PDF p. 1 and definitions section",
            "Sepsis-3 supports infection-related organ dysfunction/shock concepts, not the exact directed project edge.",
        )
    if parent.startswith("LAT_SHOCK") and child.startswith("OBS_"):
        return (
            "O_SEPSIS3; V_SOFA1996",
            V_PARTIAL,
            "Sepsis-3 local PDF p. 1; SOFA local PDF p. 2 Table 3",
            "Sources support blood-pressure/lactate or cardiovascular criteria, not a complete causal measurement model.",
        )
    if parent.startswith("LAT_RESPIRATORY_FAILURE") and child.startswith("OBS_"):
        return (
            "V_SOFA1996; V_BERLIN2012",
            V_PARTIAL,
            "SOFA local PDF p. 2 Table 3; Berlin local PDF pp. 4-6",
            "Sources support oxygenation measurements, but Berlin requires additional diagnostic conditions.",
        )
    if parent.startswith("LAT_RENAL_DYSFUNCTION") and child.startswith("OBS_"):
        return (
            "V_KDIGO2012; V_SOFA1996",
            V_PARTIAL,
            "KDIGO local PDF p. 11; SOFA local PDF p. 2 Table 3",
            "Sources support creatinine/urine measures, not every grouped observation or direction.",
        )
    if any(key in parent for key in ("LAT_HEPATIC", "LAT_COAG")) and child.startswith("OBS_"):
        return (
            "V_SOFA1996; V_DIC2001",
            V_PARTIAL,
            "SOFA local PDF p. 2 Table 3; ISTH DIC local PDF p. 2 Table 2",
            "Sources support selected laboratory domains, not the exact project grouping.",
        )
    if parent.startswith("LAT_NEUROLOGIC") and child.startswith("OBS_"):
        return (
            "V_SOFA1996",
            V_PARTIAL,
            "SOFA local PDF p. 2 Table 3",
            "SOFA supports GCS as a neurological measure; it does not establish all grouped observations.",
        )
    if parent.startswith("LAT_") and child.startswith("OUT_"):
        if "INFLAMMATION_SEPSIS" in parent or "SHOCK" in parent:
            return (
                "O_SEPSIS3",
                V_ASSOC,
                "Sepsis-3 local PDF p. 1",
                "The source reports mortality risk/association; observational evidence does not establish the project arrow.",
            )
        if any(key in parent for key in ("GLOBAL_SEVERITY", "RESPIRATORY", "RENAL", "HEPATIC", "COAG", "NEUROLOGIC")):
            return (
                "V_SOFA1996",
                V_ASSOC,
                "SOFA local PDF pp. 2-3",
                "SOFA describes organ dysfunction and mortality association, not directed causality for this edge.",
            )
    return "", V_NO_SOURCE, "", "No edge-specific locally verified source was mapped."


def build_edges():
    rows = []
    for dataset, inventory in [
        ("MIMIC-III", MIMIC_EDGE_INVENTORY),
        ("PhysioNet 2012", PHYS_EDGE_INVENTORY),
    ]:
        with (REPO / inventory).open(newline="", encoding="utf-8") as handle:
            source_rows = list(csv.DictReader(handle))
        for number, row in enumerate(source_rows, 1):
            parent, child = row["source"], row["target"]
            source_ids, mapping, original_locator, doi_url = original_edge_mapping(dataset, parent, child)
            verify_ids, verdict, verify_locator, limitations = verification_for_edge(parent, child)
            rows.append({
                "dataset": dataset,
                "edge_number": number,
                "parent": parent,
                "child": child,
                "edge_inventory_path": inventory,
                "clinical_rationale": edge_rationale(parent, child),
                "rationale_origin": "Current graph source/final ChatGPT mechanism table; project structural assumption",
                "original_chatgpt_source_ids": source_ids,
                "original_chatgpt_mapping_status": mapping,
                "original_chatgpt_locator": original_locator,
                "doi_or_url": doi_url,
                "independent_verification_source_ids": verify_ids,
                "independent_verification_status": verdict,
                "support_verdict": verdict,
                "verification_locator": verify_locator,
                "limitations": limitations,
            })
    return rows


def write_csv(path: Path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


LATEX_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
    "≥": r"$\geq$",
    "≤": r"$\leq$",
    "→": r"$\rightarrow$",
    "—": r"---",
    "Δ": r"$\Delta$",
}


def tex(value) -> str:
    value = str(value or "")
    return "".join(LATEX_REPLACEMENTS.get(char, char) for char in value)


def tex_urls(value) -> str:
    if not value:
        return "None"
    parts = [part.strip() for part in str(value).split(";") if part.strip()]
    output = []
    for part in parts:
        if part.startswith(("http://", "https://")):
            output.append(r"\url{" + part + "}")
        elif re.fullmatch(r"10\.\S+", part):
            output.append(r"\href{https://doi.org/" + part + r"}{\nolinkurl{doi:" + part + "}}")
        else:
            output.append(tex(part))
    return r"; \allowbreak ".join(output)


def tex_source_ids(value) -> str:
    if not value:
        return "None found"
    return r"; \allowbreak ".join(
        r"\nolinkurl{" + source_id.strip() + "}"
        for source_id in str(value).split(";")
        if source_id.strip()
    )


def write_proxy_tex(rows):
    rendered_rows = []
    dataset_counts = Counter()
    for row in rows:
        dataset_counts[row["dataset"]] += 1
        prefix = "M" if row["dataset"] == "MIMIC-III" else "P"
        key = f"{prefix}{dataset_counts[row['dataset']]:02d}"
        rendered_rows.append([
            rf"\textbf{{{key} --- \nolinkurl{{{row['proxy_name']}}}}} \hfill \textit{{Dataset:}} {tex(row['dataset'])}\par"
            rf"\textbf{{Clinical interpretation:}} {tex(row['clinical_interpretation'])} "
            rf"\textbf{{Original ChatGPT source IDs:}} {tex_source_ids(row['original_chatgpt_source_ids'])}. "
            rf"\textbf{{DOI/stable URL:}} {tex_urls(row['doi_or_url'])}. "
            rf"\textbf{{Verdict:}} {tex(row['verification_verdict'])}.\par"
            rf"\textbf{{Inputs:}} {tex(row['source_columns'])}.\par"
            rf"\textbf{{Rule/window:}} {tex(row['exact_rule'])} "
            rf"\textit{{Aggregation:}} {tex(row['aggregation_or_window'])}\par"
            rf"\textbf{{Independent support:}} {tex(row['support_paraphrase'])} "
            rf"\textbf{{Qualification:}} {tex(row['limitations'])} \\",
            r"\addlinespace[3pt]",
        ])
    lines = []
    chunk_sizes = (3, 3, 3, 3, 3, 3, 1)
    start = 0
    for chunk_index, chunk_size in enumerate(chunk_sizes):
        chunk = rendered_rows[start:start + chunk_size]
        start += chunk_size
        if chunk_index == 0:
            lines.append(r"\begin{center}\textit{Table 1: Proxy-definition evidence: 19 admitted proxy exposures.}\end{center}")
        else:
            lines.append(r"\textit{Table 1 continued}\par")
        lines.extend([
            r"\begin{tabular}{@{}L{23.4cm}@{}}",
            r"\toprule",
            r"\textbf{Proxy, current rule, provenance, independent verification, and qualification}\\",
            r"\midrule",
        ])
        for row_lines in chunk:
            lines.extend(row_lines)
            lines.append(r"\midrule")
        lines.extend([r"\bottomrule", r"\end{tabular}"])
        if chunk_index < len(chunk_sizes) - 1:
            lines.append(r"\clearpage")
    (HERE / "proxy_definition_rows.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_edge_tex(rows, dataset, filename):
    rendered_rows = []
    selected = [row for row in rows if row["dataset"] == dataset]
    for row in selected:
        label = f"{'M' if dataset == 'MIMIC-III' else 'P'}{int(row['edge_number']):02d}"
        rendered_rows.append([
            rf"\textbf{{{label}:}} \nolinkurl{{{row['parent']}}} $\rightarrow$ \nolinkurl{{{row['child']}}} "
            rf"\hfill \textit{{Dataset:}} {tex(row['dataset'])}\par"
            rf"\textbf{{Rationale:}} {tex(row['clinical_rationale'])} "
            rf"\textbf{{Original ChatGPT source IDs:}} {tex_source_ids(row['original_chatgpt_source_ids'])}. "
            rf"\textbf{{DOI/stable URL:}} {tex_urls(row['doi_or_url'])}.\par"
            rf"\textbf{{Independent check/verdict:}} {tex(row['independent_verification_status'])}. "
            rf"\textbf{{Qualification:}} {tex(row['limitations'])} \\",
            r"\addlinespace[2pt]",
        ])
    lines = []
    caption = (
        "MIMIC-III DAG-edge evidence (57 edges)."
        if dataset == "MIMIC-III"
        else "PhysioNet 2012 DAG-edge evidence (45 edges)."
    )
    label_name = "tab:mimic-edges" if dataset == "MIMIC-III" else "tab:phys-edges"
    table_number = "2" if dataset == "MIMIC-III" else "3"
    chunks = [rendered_rows[index:index + 5] for index in range(0, len(rendered_rows), 5)]
    for chunk_index, chunk in enumerate(chunks):
        if chunk_index == 0:
            lines.append(rf"\begin{{center}}\textit{{Table {table_number}: {caption}}}\end{{center}}")
        else:
            lines.append(rf"\textit{{Table {table_number} continued}}\par")
        lines.extend([
            r"\begin{tabular}{@{}L{23.4cm}@{}}",
            r"\toprule",
            r"\textbf{Edge, rationale, provenance, independent check, and qualification}\\",
            r"\midrule",
        ])
        for row_lines in chunk:
            lines.extend(row_lines)
            lines.append(r"\midrule")
        lines.extend([r"\bottomrule", r"\end{tabular}"])
        if chunk_index < len(chunks) - 1:
            lines.append(r"\clearpage")
    (HERE / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate(sources, proxies, edges):
    assert len(proxies) == 19
    assert Counter(row["dataset"] for row in proxies) == Counter({"MIMIC-III": 9, "PhysioNet 2012": 10})
    assert len({(row["dataset"], row["proxy_name"]) for row in proxies}) == 19
    assert len(edges) == 102
    assert Counter(row["dataset"] for row in edges) == Counter({"MIMIC-III": 57, "PhysioNet 2012": 45})
    assert len({(row["dataset"], row["parent"], row["child"]) for row in edges}) == 102
    source_ids = {row["source_id"] for row in sources}
    assert len(source_ids) == len(sources)
    for row in proxies + edges:
        for field in ("original_chatgpt_source_ids", "independent_verification_source_ids"):
            for source_id in [part.strip() for part in row[field].split(";") if part.strip()]:
                assert source_id in source_ids, (field, source_id)
        if row.get("verification_verdict", row.get("support_verdict", "")).startswith("VERIFIED"):
            assert row.get("verification_locator"), row
    # Exact equality and order against authoritative inventories.
    for dataset, inventory in [
        ("MIMIC-III", MIMIC_EDGE_INVENTORY),
        ("PhysioNet 2012", PHYS_EDGE_INVENTORY),
    ]:
        with (REPO / inventory).open(newline="", encoding="utf-8") as handle:
            expected = [(row["source"], row["target"]) for row in csv.DictReader(handle)]
        actual = [(row["parent"], row["child"]) for row in edges if row["dataset"] == dataset]
        assert actual == expected


def main():
    edges = build_edges()
    validate(SOURCES, PROXIES, edges)
    write_csv(HERE / "source_registry.csv", SOURCE_FIELDS, SOURCES)
    write_csv(HERE / "proxy_evidence.csv", PROXY_FIELDS, PROXIES)
    write_csv(HERE / "dag_edge_evidence.csv", DAG_FIELDS, edges)
    write_proxy_tex(PROXIES)
    write_edge_tex(edges, "MIMIC-III", "dag_edge_rows_mimic.tex")
    write_edge_tex(edges, "PhysioNet 2012", "dag_edge_rows_physionet.tex")
    print(f"source_registry.csv: {len(SOURCES)} rows")
    print("proxy_evidence.csv: 19 rows (9 MIMIC-III, 10 PhysioNet 2012)")
    print("dag_edge_evidence.csv: 102 rows (57 MIMIC-III, 45 PhysioNet 2012)")


if __name__ == "__main__":
    main()
