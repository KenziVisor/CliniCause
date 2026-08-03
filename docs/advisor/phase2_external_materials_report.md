# Phase 2 — External materials located for the AAAI clinical-evidence supplement

## Purpose and evidence boundary

This report responds to the missing-material register in `aaai_clinical_evidence_materials_audit.md`.

External research can help with:

- lawful access to canonical papers and guidelines;
- complete titles, authors, DOI values, and stable publication pages;
- independent verification of broad clinical constructs, measurement criteria, mortality associations, and informative observation processes;
- identifying where an implemented rule is only partially supported.

External research cannot recover:

- which paper ChatGPT originally supplied for every final proxy or DAG edge;
- the accepted/rejected proposal history;
- exact prompt-to-code correspondence;
- the producing implementation/configuration and artifact hashes;
- a qualified clinician's review and sign-off.

Therefore, every source in this package must initially be labeled either `ORIGINAL-SOURCE CANDIDATE — ATTRIBUTION NOT YET PROVEN` or `NEW INDEPENDENT-VERIFICATION SOURCE`. It must not be labeled `originally supplied by ChatGPT` until the final prompt-export PDFs establish that provenance.

## Main result

Two papers that the audit reported as missing locally were located through their authoritative publication records:

1. Vincent et al. (1996), the original SOFA paper.
2. ARDS Definition Task Force (2012), the Berlin ARDS definition.

Both have authoritative DOI/publication pages. Automated retrieval of the publisher PDFs was blocked in the current environment, so the repository should record the official link and either obtain the PDF through normal browser/institutional access or retain an explicit `PDF_NOT_LOCALLY_AVAILABLE` status.

A broader verification set was also located for neurological dysfunction, cardiac injury/strain, metabolic/electrolyte derangement, chronic burden, EHR phenotyping, and informative missingness. These sources can support independent verification but cannot repair original ChatGPT provenance by themselves.

## Recommended repository directory

```text
thesis-writing/paper-aaai/clinical-evidence/
  README.md
  sources/
    original-candidates/
    independent-verification/
  metadata/
    source_manifest.csv
    source_access_log.csv
  provenance/
    original_chatgpt_source_manifest.csv
    proposal_selection_lineage.csv
  verification/
    proxy_evidence_verification.csv
    dag_edge_verification.csv
  implementation/
    mimic_proxy_implementation_spec.csv
    physionet_proxy_implementation_spec.csv
  review/
    clinical_review_record.md
```

Only create this structure after confirming that no canonical directory with the same role already exists.

## Sources located

### 1. Global severity and multi-organ dysfunction

**Vincent JL, Moreno R, Takala J, et al. The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure. Intensive Care Medicine. 1996;22:707–710.**

- DOI: `10.1007/BF01709751`
- Official page: `https://link.springer.com/article/10.1007/BF01709751`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/8844239/`
- Suggested filename: `vincent_1996_sofa.pdf`
- Access status: authoritative metadata and article page located; publisher PDF was not retrievable automatically.
- Can support: the concept of a multi-domain organ-dysfunction score and the original SOFA domains.
- Cannot support by itself: the exact CliniCause local score composition, score threshold, all substituted variables, or every DAG edge involving global severity.
- Missing IDs addressed: `M-PDF-01` partially; `M-PRX-05` partially; `M-PRX-07` partially.

### 2. Respiratory dysfunction

**ARDS Definition Task Force. Acute Respiratory Distress Syndrome: The Berlin Definition. JAMA. 2012;307(23):2526–2533.**

- DOI: `10.1001/jama.2012.5669`
- Official article page: `https://jamanetwork.com/journals/jama/fullarticle/1160659`
- Official PDF route: `https://jamanetwork.com/journals/jama/articlepdf/1160659/jsc120003_2526_2533.pdf`
- Suggested filename: `ards_definition_task_force_2012_berlin_definition.pdf`
- Access status: authoritative article and PDF routes located; automated PDF download was blocked.
- Can support: ARDS oxygenation categories based on PaO2/FiO2 under specified ventilatory conditions and the clinical meaning of severe hypoxemic respiratory failure.
- Cannot support by itself: the complete CliniCause respiratory proxy, including all SpO2, respiratory-rate, PaCO2, pH, ventilation, and scoring clauses.
- Missing IDs addressed: `M-PDF-01` partially; `M-PRX-05` partially; `M-PRX-07` partially.

**Essay P, Mosier J, Subbian V. Rule-Based Cohort Definitions for Acute Respiratory Failure: Electronic Phenotyping Algorithm. JMIR Medical Informatics. 2020;8(4):e18402.**

- DOI: `10.2196/18402`
- Full text: `https://medinform.jmir.org/2020/4/e18402/`
- PDF: `https://medinform.jmir.org/2020/4/e18402/PDF`
- Suggested filename: `essay_2020_respiratory_failure_phenotyping.pdf`
- Access status: open-access PDF.
- Can support: the legitimacy and limitations of rule-based EHR phenotyping for acute respiratory failure, particularly treatment/ventilation-oriented computable phenotypes.
- Cannot support: every exact CliniCause cutoff or all respiratory DAG directions.

### 3. Renal dysfunction

**Kidney Disease: Improving Global Outcomes Acute Kidney Injury Work Group. KDIGO Clinical Practice Guideline for Acute Kidney Injury. Kidney International Supplements. 2012;2:1–138.**

- Official PDF: `https://kdigo.org/wp-content/uploads/2016/10/KDIGO-2012-AKI-Guideline-English.pdf`
- Guideline page: `https://kdigo.org/guidelines/acute-kidney-injury/`
- Suggested filename: `kdigo_2012_aki_guideline.pdf`
- Access status: open official PDF.
- Can support: AKI definition and staging by serum-creatinine change and urine output, and the clinical significance of AKI.
- Cannot support: the full local composite with BUN, potassium, bicarbonate, dialysis sufficiency, or the CliniCause score threshold unless those clauses are verified separately.

### 4. Sepsis, inflammation, shock, and organ dysfunction

**Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801–810.**

- DOI: `10.1001/jama.2016.0287`
- PubMed Central: `https://pmc.ncbi.nlm.nih.gov/articles/PMC4968574/`
- Official JAMA PDF route: `https://jamanetwork.com/journals/jama/articlepdf/2492881/jsc160002.pdf`
- Suggested filename: `singer_2016_sepsis3.pdf`
- Access status: open full text through PubMed Central.
- Can support: sepsis as infection-related organ dysfunction; qSOFA criteria; septic-shock criteria involving vasopressor-dependent hypotension and lactate above 2 mmol/L; high mortality of septic shock.
- Cannot support: the exact CliniCause inflammation score, all shock clauses, or a total causal effect of every proxy.

### 5. Coagulation and hematologic dysfunction

**Taylor FB Jr, Toh CH, Hoots WK, Wada H, Levi M. Towards definition, clinical and laboratory criteria, and a scoring system for disseminated intravascular coagulation. Thrombosis and Haemostasis. 2001;86(5):1327–1330.**

- DOI: `10.1055/s-0037-1616068`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/11816725/`
- Suggested filename: `taylor_2001_isth_dic_score.pdf`
- Access status: authoritative metadata located; no reliable open publisher PDF was identified in this pass.
- Can support: the concept of overt-DIC scoring using coagulation laboratory domains.
- Cannot support: the exact MIMIC mixed hepatic/coagulation proxy, the PhysioNet platelet/HCT/WBC composite, or thresholds absent from the ISTH score.

### 6. Neurological dysfunction

**Teasdale G, Jennett B. Assessment of coma and impaired consciousness: a practical scale. The Lancet. 1974;2(7872):81–84.**

- DOI: `10.1016/S0140-6736(74)91639-0`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/4136544/`
- Suggested filename: `teasdale_jennett_1974_glasgow_coma_scale.pdf`
- Access status: authoritative metadata located; no lawful open full PDF was confirmed.
- Can support: the Glasgow Coma Scale as a structured assessment of impaired consciousness.
- Cannot support: all CliniCause neuro-proxy thresholds, RASS clauses, pupil/focal findings, electrolyte/gas additions, sedation exclusions, or causal edges to mortality.

### 7. Cardiac injury and strain

**Thygesen K, Alpert JS, Jaffe AS, et al. Fourth Universal Definition of Myocardial Infarction (2018). Circulation. 2018;138:e618–e651.**

- DOI: `10.1161/CIR.0000000000000617`
- Official page: `https://www.ahajournals.org/doi/10.1161/CIR.0000000000000617`
- Official PDF route: `https://www.ahajournals.org/doi/pdf/10.1161/CIR.0000000000000617`
- Suggested filename: `thygesen_2018_fourth_universal_definition_mi.pdf`
- Access status: free-access official page; automated PDF retrieval failed in the current environment.
- Can support: myocardial injury as cardiac troponin above an assay-specific 99th-percentile upper reference limit, and the distinction between myocardial injury and myocardial infarction.
- Important limitation: it weakens any claim that fixed troponin-I/T values are universally valid across assays. Exact local fallback thresholds require assay/context evidence.

**Zochios V, Valchanov K. Raised cardiac troponin in intensive care patients with sepsis, in the absence of angiographically documented coronary artery disease: a systematic review. Journal of the Intensive Care Society. 2015.**

- PubMed Central: `https://pmc.ncbi.nlm.nih.gov/articles/PMC5593290/`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/28979375/`
- Suggested filename: `zochios_valchanov_troponin_sepsis_review.pdf`
- Access status: open full text.
- Can support: troponin elevation in critical illness/sepsis, proposed non-coronary mechanisms, and association with adverse prognosis.
- Cannot support: a universal diagnostic cutoff, CK-MB sufficiency, ICU-type clauses, or every cardiac→shock/mortality edge.

### 8. Metabolic and electrolyte derangement

**Lee JW. Fluid and Electrolyte Disturbances in Critically Ill Patients. Electrolytes & Blood Pressure. 2010;8(2):72–81.**

- PubMed Central: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3043756/`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/21468200/`
- Suggested filename: `lee_2010_fluid_electrolyte_disturbances_icu.pdf`
- Access status: open full text.
- Can support: clinical importance of sodium, potassium, magnesium, fluid, and acid-base derangements in critical illness.
- Cannot support: the exact local multi-domain score or every threshold/sufficient condition.

Additional useful independent-verification studies include:

- Bouadma et al., dyskalemia at ICU admission: `https://pmc.ncbi.nlm.nih.gov/articles/PMC6921444/`
- Tongyoo et al., serum potassium and ICU outcomes: `https://pmc.ncbi.nlm.nih.gov/articles/PMC5972260/`
- Oude Lansink-Hartgring et al., dysnatremia and mortality: `https://pmc.ncbi.nlm.nih.gov/articles/PMC4794471/`
- Gunnerson et al., metabolic acidosis subtypes and mortality: PubMed `https://pubmed.ncbi.nlm.nih.gov/16507145/`

These are new verification sources, not evidence of original ChatGPT attribution.

### 9. Informative missingness and measurement intensity

**Sharafoddini A, Dubin JA, Maslove DM, Lee J. A New Insight Into Missing Data in Intensive Care Unit Patient Profiles: Observational Study. JMIR Medical Informatics. 2019;7(1):e11605.**

- DOI: `10.2196/11605`
- Full text: `https://medinform.jmir.org/2019/1/e11605/`
- PDF route: `https://medinform.jmir.org/2019/1/e11605/PDF`
- Suggested filename: `sharafoddini_2019_informative_missingness_icu.pdf`
- Access status: open access.
- Can support: the presence/absence of ICU laboratory measurements can be informative; missingness reflects patient state and clinician ordering processes; missingness indicators can predict mortality.
- Relevant DAG families: severity/context→measurement intensity; measurement intensity→availability/counts; ordering-process nodes→observed data.
- Cannot support: every dataset-specific directed edge or establish directionality in the final DAG without further argument.

**Sisk R, Sperrin M, Peek N, et al. Informative presence and observation in routine health data: a review of methodology for clinical risk prediction. Journal of the American Medical Informatics Association. 2021;28(1):155–166.**

- DOI: `10.1093/jamia/ocaa242`
- Open full text: `https://academic.oup.com/jamia/article/28/1/155/5961436`
- Suggested filename: `sisk_2021_informative_presence_observation.pdf`
- Access status: open access.
- Can support: measurement presence, timing, frequency, and intensity can carry information about patient health; sicker patients are often monitored more intensively.
- Cannot prove: the exact causal directions in each CliniCause graph.

### 10. General EHR phenotyping and chronic burden

**Banda JM, Seneviratne M, Hernandez-Boussard T, Shah NH. Advances in Electronic Phenotyping: From Rule-Based Definitions to Machine Learning Models. Annual Review of Biomedical Data Science. 2018;1:53–68.**

- DOI: `10.1146/annurev-biodatasci-080917-013315`
- PubMed Central: `https://pmc.ncbi.nlm.nih.gov/articles/PMC6583807/`
- Suggested filename: `banda_2018_ehr_phenotyping_review.pdf`
- Can support: rule-based and learned EHR phenotypes as explicit computable representations and the need for validation/portability.
- Cannot support: a specific CliniCause threshold or DAG edge.

**Elixhauser A, Steiner C, Harris DR, Coffey RM. Comorbidity measures for use with administrative data. Medical Care. 1998;36(1):8–27.**

- DOI: `10.1097/00005650-199801000-00004`
- PubMed: `https://pubmed.ncbi.nlm.nih.gov/9431328/`
- Suggested filename: `elixhauser_1998_comorbidity_measures.pdf`
- Can support: use of structured comorbidity measures derived from administrative data.
- Cannot support: the local rule `count ≥2` or `Elixhauser ≥5` without a source for that exact cutoff.

**Charlson ME, Pompei P, Ales KL, MacKenzie CR. A new method of classifying prognostic comorbidity in longitudinal studies: development and validation. Journal of Chronic Diseases. 1987;40(5):373–383.**

- PubMed: `https://pubmed.ncbi.nlm.nih.gov/3558716/`
- Suggested filename: `charlson_1987_comorbidity_index.pdf`
- Can support: prognostic comorbidity weighting and the idea of combining age/comorbidity burden.
- Cannot support: the exact CliniCause chronic-burden composition or thresholds.

**Vincent JL, Dubois MJ, Navickis RJ, Wilkes MM. Hypoalbuminemia in acute illness: is there a rationale for intervention? Annals of Surgery. 2003.**

- PubMed Central: `https://pmc.ncbi.nlm.nih.gov/articles/PMC1514323/`
- Suggested filename: `vincent_2003_hypoalbuminemia_acute_illness.pdf`
- Can support: low albumin as a marker associated with morbidity and mortality in acute illness.
- Cannot support: the exact albumin cutoff or the complete chronic-baseline rule.

## What can now be completed

The following missing items can be advanced using this source set:

- `M-PDF-01`: authoritative access routes for SOFA and Berlin are now known; local PDF acquisition still requires browser/institutional access or an explicit missing-PDF status.
- `M-PRX-05`: paper-specific support paraphrases can be drafted for broad proxy concepts.
- `M-PRX-06`: titles, authors, DOI values, and stable publication pages can be normalized for the sources above.
- `M-PRX-07`: independent verification can be recorded as `supports concept`, `partially supports`, or `does not support exact local rule`.
- `M-DAG-03`: papers on sepsis, organ dysfunction, mortality, informative observation, and treatment/measurement processes can support verification of some edge families. Verification still has to be recorded one edge at a time.

## What remains impossible from external research alone

The following items remain repository/human tasks:

- `M-PRX-01`, `M-PRX-02`, `M-PRX-03`: exact active implementation, source aliases/item IDs, producing threshold mode, and temporal provenance.
- `M-PRX-04`: original ChatGPT paper-to-proxy attribution.
- `M-DAG-01`: original ChatGPT paper mapped to each of 102 final edges.
- `M-DAG-02`: original edge-specific rationale where the export only provides family-level reasoning.
- `M-HIST-01`, `M-CONFLICT-01`: accepted/rejected/renamed/split/merged decision lineage.
- `M-HIST-02`: exact run metadata and export completeness.
- `M-REVIEW-01`: qualified clinician review.

## Recommended next action

1. Add the accompanying `phase2_source_manifest.csv` to the new evidence directory.
2. Obtain the SOFA and Berlin PDFs through normal authorized access; otherwise record the official URL and `PDF_NOT_LOCALLY_AVAILABLE`.
3. Copy or reference the already-present KDIGO, Sepsis-3, DIC, Banda, and Essay files rather than duplicating them without purpose.
4. Add the neurological, cardiac, metabolic, and missingness sources as `NEW INDEPENDENT-VERIFICATION SOURCE`.
5. Upload or provide the two final ChatGPT response PDFs and the exact proxy/DAG implementation specifications for the provenance-mapping step.
6. Do not begin final LaTeX generation until every proxy and edge row has explicit values for source provenance, verification status, and support conclusion—even where the correct value is `none supplied`, `not recoverable`, or `does not support exact rule`.
