# Stage 4.3 Evidence Report

## 16.1 Git State

- Branch: `main`.
- Stage 4.2 commit verified: `c9f6b12 step 4.2` is the current `HEAD` and changed `prompt.txt`, Chapter 6, Stage 4.2 logs, and `thesis-writing/thesis/main.pdf`.
- Initial status: the worktree already contained unrelated modifications in root documentation and router files, the nested `causal-irregular-time-series` gitlink, requirement files, tests, important-md copies, literature catalog, validation config, and `tmp_verify_router.py`.
- Final status after Stage 4.3 cleanup is expected to include the same unrelated changes plus Stage 4.3 edits to `thesis-writing/thesis/chapters/05_proxy_state_construction.tex`, `thesis-writing/logs/unresolved_placeholders.md`, `thesis-writing/logs/deferred_fixes.md`, generated `thesis-writing/thesis/main.pdf`, and this new report. A newly observed untracked `thesis-writing/prompts-and-documents/` directory is outside Stage 4.3 scope.
- Stage 4.3 files changed: Chapter 5 source, placeholder log, deferred-fix log, Stage 4.3 evidence report, and generated thesis PDF.
- No commit or push was performed.

## 16.2 Baseline Build

- Command sequence: `cd thesis-writing/thesis && latexmk -C && latexmk -xelatex main.tex && test -f main.pdf && pdfinfo main.pdf`.
- Return status: `0`.
- Baseline PDF path: `thesis-writing/thesis/main.pdf`.
- Baseline page count: `44`.
- Baseline warnings: final log scan found no fatal LaTeX errors, unresolved citations, unresolved references, duplicate-label warnings, Biber errors, emergency stops, or fatal errors. Nonfatal layout warnings were present, mainly underfull boxes in existing tables and an overfull bibliography line.

## 16.3 Files Inspected

- Thesis and logs: `prompt.txt`, `thesis-writing/thesis/main.tex`, Chapter 5 skeleton/source, Chapter 6 source for cross-reference style, `unresolved_placeholders.md`, `deferred_fixes.md`, and previous Stage 4 reports.
- Planning: `thesis_story.md`, `thesis_outline.md`, `chapter_evidence_map.md`, `terminology_and_notation.md`, `citation_plan.md`, `table_plan.md`, `figure_plan.md`, `writing_order.md`, and `stage4_prompt_queue.md`.
- Audit: `repository_map.md`, `evidence_inventory.md`, `experiment_inventory.csv`, `claim_evidence_ledger.csv`, `terminology_map.md`, `unresolved_questions.md`, and `figure_table_inventory.md`.
- Literature: `literature/README.md`, `literature/metadata/catalog.csv`, and `literature/metadata/references.bib`.
- Active PhysioNet tagging: `causal-irregular-time-series/src/tagging_latent_variables_physionet.py` and `configs/physionet-global-variables.csv`.
- Active MIMIC tagging: `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py` and `configs/mimic-global-variables.csv`.
- Legacy taggers: `src/draft/tagging_latent_variables_physionet_old.py`, `src/draft/tagging_latent_variables_mimiciii_old.py`, `src/draft/clinically_sufficient_tagging_latent_variables.py`, and `src/draft/optimize_latent_thresholds.py`.
- Prediction normalization: `STraTS/src/main.py`, `STraTS/src/dataset.py`, `STraTS/AGENTS.md`, `router.py`, and `split_predicted_latent_tags.py`.
- Majority voting: `causal-irregular-time-series/src/majority_vote_latents.py`.
- Orchestration: `causal-irregular-time-series/main.py`, mortality prediction, matching, and CATE consumers.
- Rule artifacts: PhysioNet and MIMIC tag CSVs under `final-results/trees/`.
- Validation artifacts: MIMIC `latent_tags_with_features.csv`, `prevalence.csv`, `mortality_by_tag.csv`, `cooccurrence_phi.csv`, and `validation_summary.json`.
- Tree artifacts: PhysioNet and MIMIC tree pickles and rendered PNG directories were located but not inserted as figures.

## 16.4 Active-Implementation Decision

- Active PhysioNet tagger: `causal-irregular-time-series/src/tagging_latent_variables_physionet.py`.
- Active MIMIC tagger: `causal-irregular-time-series/src/tagging_latent_variables_mimiciii.py`.
- Legacy files: the `src/draft/*old.py` taggers, the draft clinically sufficient tagger, and draft threshold optimizer were classified as legacy because they live under `src/draft/`, use older non-`LAT_*` schemas, or optimize older/simple rule sets rather than the configured active columns.
- Evidence: active config files expose the same `LAT_*` orders as the current active source; archived tag CSV headers match those active orders.
- Artifact match: PhysioNet tag CSV has `ts_id` plus 11 active PhysioNet columns; MIMIC tag CSV has `ts_id` plus 10 active MIMIC columns. This verifies schema agreement, not producing command, source commit, input hash, or threshold-mode provenance.

## 16.5 PhysioNet Rule Matrix

All rows use the active PhysioNet tagger. Record summaries are min, max, mean, first, and last over the processed record unless a helper column is already present. Missing numeric values do not fire comparisons.

| column | construct | source features | time or record summary | threshold logic | missingness behavior | clinical citation | implementation evidence | artifact evidence | validation limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `LAT_CHRONIC_BASELINE_RISK` | Baseline vulnerability | Age, BMI from height/weight, albumin, ICU type | First values and albumin min | Score >=2 across age >=75, BMI <18.5 or >=40, albumin <3.0, ICU type 1 or 3 | Missing terms do not add points | Broad phenotyping only | Active PhysioNet tagger decision helper | Header present in PhysioNet tag CSV | Exact chronic-risk clauses need citation/review |
| `LAT_GLOBAL_SEVERITY` | Multi-domain acute severity | Hemodynamic, respiratory, neurologic, renal, hepatic/coag, metabolic, cardiac summaries | Record summaries and helper flags | >=3 abnormal domains, or >=2 plus critical marker such as lactate >=4, pH <7.20, ventilation, GCS <=8, or MAP <60 | Missing domains do not count | Sepsis-3 and SOFA broad grounding | Active helper combines domain evidence | Header present and binary | Not a complete SOFA score |
| `LAT_SHOCK` | Circulatory shock or instability | MAP, SBP, lactate, HR, urine helper, pH, bicarbonate | Record summaries and optional urine helpers | >=2 abnormal clauses, or low MAP with lactate >=4 | Missing values do not fire; urine only if helper exists | Sepsis-3 broad grounding | Active shock rule | Header present and binary | No vasopressor requirement in PhysioNet rule |
| `LAT_RESPIRATORY_FAILURE` | Hypoxemia, ventilatory failure, support | Mechanical ventilation, PF, SaO2, PaO2, RR, PaCO2, pH | Record summaries; PF used or approximated | >=2 abnormal clauses, or ventilation with PF <300 | Missing oxygenation values do not fire | Respiratory phenotyping and Berlin ARDS context | Active respiratory rule | Header present and binary | Not adjudicated ARDS |
| `LAT_RENAL_DYSFUNCTION` | Renal dysfunction | Creatinine, BUN, urine helper, potassium, bicarbonate | First/max creatinine and record summaries | >=2 abnormal clauses; creatinine >=3.5 sufficient | Missing values do not fire; urine helper availability uncertain | KDIGO broad grounding | Active renal rule | Header present and binary | Not full KDIGO staging |
| `LAT_HEPATIC_DYSFUNCTION` | Hepatic injury/reserve | Bilirubin, AST, ALT, ALP, albumin, platelets | Record summaries | Weighted score >=2; bilirubin >=2 counts twice | Missing values do not fire | SOFA for bilirubin only | Active hepatic rule | Header present and binary | Transaminase, ALP, albumin clauses need citation |
| `LAT_COAG_HEME_DYSFUNCTION` | Hematologic/coagulation stress | Platelets, hematocrit, WBC, platelet change | Record summaries and first-to-min drop | Score >=2; platelets <100 counts twice | Missing values do not fire | ISTH DIC and SOFA broad grounding | Active coag/heme rule | Header present and binary | Not complete DIC score |
| `LAT_INFLAMMATION_SEPSIS_BURDEN` | Inflammation or sepsis-like burden | Temperature, WBC, HR, RR, PaCO2, lactate, platelets | Record summaries | Score >=3; temperature or WBC can anchor lactate stress at score >=2 | Missing values do not fire | Sepsis-3 broad grounding | Active inflammation rule | Header present and binary | Not formal Sepsis-3 diagnosis |
| `LAT_NEUROLOGIC_DYSFUNCTION` | Depressed consciousness or neuro/metabolic stress | GCS, sodium, glucose, PaCO2, SaO2, pH | Record summaries | Score >=2; GCS <=12 counts twice | Missing values do not fire | SOFA neurologic context | Active neurologic rule | Header present and binary | Sedation ambiguity not reviewed |
| `LAT_CARDIAC_INJURY_STRAIN` | Cardiac injury or strain | Troponin I/T, ICU type, HR, MAP, SBP, lactate | Record summaries | Score >=2; troponin evidence counts twice | Missing values do not fire | Citation gap | Active cardiac rule | Header present and binary | Cardiac thresholds project-specific |
| `LAT_METABOLIC_DERANGEMENT` | Acid-base/electrolyte/glucose derangement | pH, bicarbonate, lactate, sodium, potassium, magnesium, glucose, PaCO2 | Record summaries | Score >=2, or critical pH/lactate/potassium sufficient | Missing values do not fire | Citation gap | Active metabolic rule | Header present and binary | Exact thresholds need citation/review |

## 16.6 MIMIC Rule Matrix

The active MIMIC tagger supports exactly one of three input modes per run: precomputed summary CSV, canonical processed pickle, or raw concept CSVs. In canonical-pickle mode it aliases `MBP` to MAP, `PCO2` to PaCO2, `PO2` to PaO2, `O2 Saturation` to SpO2, `Creatinine Blood` to creatinine, and `Bilirubin (Total)` to bilirubin; reconstructs GCS total from components; and derives urine summaries when weight is available. Missing numeric values do not fire comparisons; helper flags fire only when positive/truthy.

| column | construct | source features | time or record summary | threshold logic | clinical citation | implementation evidence | artifact evidence | cross-dataset correspondence | validation limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `LAT_CHRONIC_BURDEN` | Chronic burden/vulnerability | Age, comorbidity, Elixhauser, chronic helpers, malignancy/immunosuppression, admission type | One row per stay summaries/helpers | Score >=2 across chronic-burden clauses | Broad phenotyping only | Active MIMIC chronic rule | Header present and binary | Related to PhysioNet chronic baseline risk, not identical | Input-mode and citation provenance incomplete |
| `LAT_INFLAMMATION_SEPSIS` | Inflammation/infection/sepsis-like burden | Temperature, WBC, lactate, culture and antibiotic helpers | Summaries/helpers | Score >=2 with infection/inflammation anchoring | Sepsis-3 broad grounding | Active MIMIC inflammation rule | Header present and binary | Related to PhysioNet inflammation burden, shorter name and different helpers | Not formal Sepsis-3 diagnosis |
| `LAT_GLOBAL_SEVERITY` | Multi-domain acute severity | Circulatory, respiratory, neurologic, renal, metabolic, inflammatory, hepatic/coag domains | Summaries/helpers | >=3 abnormal domains | Sepsis-3 and SOFA broad grounding | Active MIMIC severity rule | Header present and binary | Similar high-level role, different features | Not complete SOFA |
| `LAT_SHOCK` | Shock/hemodynamic instability | MAP, SBP, hypotension helper, vasopressors, lactate, urine, pH, base excess | Summaries/helpers; urine 24h or 6h when available | Score >=2, or vasopressor plus hypoperfusion/acidosis/hypotension | Sepsis-3 broad grounding | Active MIMIC shock rule | Header present and binary | Richer than PhysioNet due vasopressor/context helpers | Source-specific proxy |
| `LAT_RESPIRATORY_FAILURE` | Respiratory failure/support | SpO2, PF, FiO2, ventilation, RR, PaCO2, pH | Summaries/helpers | Score >=2 or support plus hypoxemia/oxygenation/ventilatory failure | Respiratory phenotyping and Berlin ARDS context | Active MIMIC respiratory rule | Header present and binary | Similar label to PhysioNet with richer support helpers | Not adjudicated ARDS |
| `LAT_RENAL_DYSFUNCTION` | Renal dysfunction | Creatinine, BUN, urine, potassium, bicarbonate, dialysis/CRRT | Summaries/helpers | Score >=2 or dialysis/CRRT present | KDIGO broad grounding | Active MIMIC renal rule | Header present and binary | Similar concept with dialysis helper | Not full KDIGO staging |
| `LAT_HEPATIC_COAG_DYSFUNCTION` | Combined hepatic/coag dysfunction | Bilirubin, AST/ALT, platelets, INR/PT/PTT, albumin | Summaries/helpers | Score >=2 across hepatic/coag clauses | SOFA and ISTH DIC broad grounding | Active combined rule | Header present and binary | Combines PhysioNet hepatic and coag/heme constructs | Combined construct needs review |
| `LAT_NEUROLOGIC_DYSFUNCTION` | Neurologic dysfunction with sedation caveat | GCS, components, RASS, pupil/focal helper, sedation/intubation helper | Summaries/helpers | Score >=2; GCS <=8 counts twice; sedation point alone insufficient | SOFA neurologic context | Active neurologic rule | Header present and binary | Similar label, richer MIMIC context | Sedation ambiguity remains |
| `LAT_METABOLIC_DERANGEMENT` | Acid-base/electrolyte/glucose derangement | pH, bicarbonate, base excess, lactate, potassium, sodium, glucose | Summaries | Score >=2 across metabolic clauses | Citation gap | Active metabolic rule | Header present and binary | Similar name to PhysioNet with different thresholds/features | Exact thresholds need citation |
| `LAT_CARDIAC_STRAIN` | Cardiac strain/injury | Troponin flags/values, CK-MB, arrhythmia, HR, hypotension, cardiac unit/surgery | Summaries/helpers | Score >=2 and requires biomarker or rhythm evidence | Citation gap | Active cardiac rule | Header present and binary | Related to PhysioNet cardiac injury/strain, not identical | Exact thresholds need citation |

## 16.7 Clinical Citation-Coverage Matrix

| dataset | proxy-state column | clinical construct | implemented measurements/rules | candidate citation | alignment | limitations | citation status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PhysioNet | `LAT_CHRONIC_BASELINE_RISK` | Baseline vulnerability | Age, BMI, albumin, ICU type score | `banda_2018_electronic_phenotyping` | Broad phenotyping only | Exact clauses are project-specific | CITATION GAP |
| PhysioNet | `LAT_GLOBAL_SEVERITY` | Acute organ severity | Multi-domain abnormality score | `singer_2016_sepsis3`, `vincent_et_al_1996_sofa` | Broadly aligned | Not complete SOFA; `vincent` local PDF missing | CITATION EXISTS BUT LOCAL PDF MISSING |
| PhysioNet | `LAT_SHOCK` | Shock/instability | MAP/SBP/lactate/HR/acidosis/urine score | `singer_2016_sepsis3` | Partially aligned | No vasopressor clause | PARTIALLY ALIGNED |
| PhysioNet | `LAT_RESPIRATORY_FAILURE` | Respiratory failure | Oxygenation, ventilation, RR, PaCO2/pH | `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping`, `ranieri_et_al_2012_berlin_ards` | Broadly aligned | Not adjudicated ARDS; `ranieri` local PDF missing | CITATION EXISTS BUT LOCAL PDF MISSING |
| PhysioNet | `LAT_RENAL_DYSFUNCTION` | Renal dysfunction | Creatinine/BUN/urine/potassium/bicarb | `kdigo_2012_acute_kidney_injury` | Broadly aligned | Not full KDIGO staging | SUPPORTED FOR BROAD CLINICAL GROUNDING |
| PhysioNet | `LAT_HEPATIC_DYSFUNCTION` | Hepatic dysfunction | Bilirubin plus AST/ALT/ALP/albumin/platelets | `vincent_et_al_1996_sofa` | Partial | Non-bilirubin clauses need support; local PDF missing | CITATION EXISTS BUT LOCAL PDF MISSING |
| PhysioNet | `LAT_COAG_HEME_DYSFUNCTION` | Coag/heme stress | Platelets, HCT, WBC, platelet drop | `taylor_et_al_2001_isth_dic`, `vincent_et_al_1996_sofa` | Broad/partial | Not complete DIC score; `vincent` PDF missing | PARTIALLY ALIGNED |
| PhysioNet | `LAT_INFLAMMATION_SEPSIS_BURDEN` | Inflammation/sepsis burden | Temperature, WBC, HR, RR, PaCO2, lactate, platelets | `singer_2016_sepsis3` | Partial | Not formal Sepsis-3 | PARTIALLY ALIGNED |
| PhysioNet | `LAT_NEUROLOGIC_DYSFUNCTION` | Neurologic dysfunction | GCS plus metabolic/respiratory stress | `vincent_et_al_1996_sofa` | Broad | Sedation not adjudicated; local PDF missing | CITATION EXISTS BUT LOCAL PDF MISSING |
| PhysioNet | `LAT_CARDIAC_INJURY_STRAIN` | Cardiac strain/injury | Troponin, ICU type, HR, MAP/SBP, lactate | none in current corpus | None | Cardiac thresholds project-specific | CITATION GAP |
| PhysioNet | `LAT_METABOLIC_DERANGEMENT` | Metabolic derangement | Acid-base, lactate, electrolytes, glucose | none in current corpus | None | Exact thresholds project-specific | CITATION GAP |
| MIMIC | `LAT_CHRONIC_BURDEN` | Chronic burden | Age, comorbidity, Elixhauser, chronic helpers, admission type | `banda_2018_electronic_phenotyping` | Broad phenotyping only | Exact construct project-specific | CITATION GAP |
| MIMIC | `LAT_INFLAMMATION_SEPSIS` | Inflammation/infection burden | Temperature, WBC, lactate, culture/antibiotic evidence | `singer_2016_sepsis3` | Partial | Not formal Sepsis-3 | PARTIALLY ALIGNED |
| MIMIC | `LAT_GLOBAL_SEVERITY` | Acute severity | Multi-domain abnormality score | `singer_2016_sepsis3`, `vincent_et_al_1996_sofa` | Broad | Not complete SOFA; `vincent` PDF missing | CITATION EXISTS BUT LOCAL PDF MISSING |
| MIMIC | `LAT_SHOCK` | Shock | Vasopressors, hypotension, lactate, urine, acidosis | `singer_2016_sepsis3` | Partially aligned | Source-specific proxy | PARTIALLY ALIGNED |
| MIMIC | `LAT_RESPIRATORY_FAILURE` | Respiratory failure | SpO2, PF, FiO2, support, RR, PaCO2/pH | `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping`, `ranieri_et_al_2012_berlin_ards` | Broad | Not adjudicated ARDS; `ranieri` PDF missing | CITATION EXISTS BUT LOCAL PDF MISSING |
| MIMIC | `LAT_RENAL_DYSFUNCTION` | Renal dysfunction | Creatinine, BUN, urine, K, bicarb, dialysis/CRRT | `kdigo_2012_acute_kidney_injury` | Broad | Not full KDIGO staging | SUPPORTED FOR BROAD CLINICAL GROUNDING |
| MIMIC | `LAT_HEPATIC_COAG_DYSFUNCTION` | Combined hepatic/coag | Bilirubin, AST/ALT, platelets, INR/PT/PTT, albumin | `vincent_et_al_1996_sofa`, `taylor_et_al_2001_isth_dic` | Partial | Combined construct needs review; `vincent` PDF missing | CLINICAL REVIEW REQUIRED |
| MIMIC | `LAT_NEUROLOGIC_DYSFUNCTION` | Neurologic dysfunction | GCS, RASS, pupil/focal, sedation/intubation | `vincent_et_al_1996_sofa` | Broad | Sedation ambiguity; local PDF missing | CITATION EXISTS BUT LOCAL PDF MISSING |
| MIMIC | `LAT_METABOLIC_DERANGEMENT` | Metabolic derangement | pH, bicarb, base excess, lactate, electrolytes, glucose | none in current corpus | None | Exact thresholds project-specific | CITATION GAP |
| MIMIC | `LAT_CARDIAC_STRAIN` | Cardiac strain/injury | Troponin, CK-MB, arrhythmia, HR, hypotension, context | none in current corpus | None | Exact thresholds project-specific | CITATION GAP |

## 16.8 Artifact-Schema Audit

Audit row counts are recorded here only and were not inserted into Chapter 5.

| artifact | granularity | key columns/schema | binary validation | duplicate-ID status | row count | provenance status |
| --- | --- | --- | --- | --- | ---: | --- |
| PhysioNet proxy tags | one `ts_id` row | `ts_id` plus 11 active PhysioNet `LAT_*` columns | all latent columns binary | 0 duplicate `ts_id` | 11988 | schema matches active source; command/hash/threshold mode unknown |
| MIMIC proxy tags | one `ts_id` row | `ts_id` plus 10 active MIMIC `LAT_*` columns | all latent columns binary | 0 duplicate `ts_id` | 44812 | schema matches active source; input mode/command/hash unknown |
| MIMIC tags with features | one `ts_id` row | `ts_id`, 83 feature-like columns, 10 tag columns | full table not binary because features included | 0 duplicate `ts_id` | 44812 | diagnostic trace present; producing command unknown |
| MIMIC prevalence | one latent row | `latent`, `n_positive`, `prevalence` | not applicable | not applicable | 10 | descriptive, not validation |
| MIMIC mortality by tag | one latent row | `latent`, tag counts, mortality by tag, risk ratio | not applicable | not applicable | 10 | unadjusted association, not causal |
| MIMIC co-occurrence | latent-by-latent matrix | index column plus 10 latent columns | not applicable | not applicable | 10 | pairwise association only |
| MIMIC validation summary | JSON summary | `n_stays`, `available_latents`, prevalence, mortality, sanity checks, notes | not applicable | not applicable | `n_stays=44812` | sanity/provenance incomplete; not clinical adjudication |
| Majority-vote tags | one shared `ts_id` row | `ts_id` plus dataset-specific active latent columns | all majority outputs binary | 0 duplicate `ts_id` | MIMIC 26845, PhysioNet 7993 | run summaries present; voter manifests absent |

Additional audit hashes: PhysioNet tag CSV `dc884602eee4c9f2`; MIMIC tag CSV `c56183201b0b9088`; MIMIC feature table `fa22059187def7b8`; MIMIC validation JSON `66ed479a5e7fabf9`; MIMIC majority outputs share `bf512547fa5b29ba`; PhysioNet majority outputs share `69bdde166c0a388c`.

## 16.9 Majority-Vote Contract

- Voter discovery: non-hidden `.csv` files in the supplied voter directory, sorted by path string.
- Required schema: every voter contains `ts_id` and at least one non-id latent column.
- Binary validation: all non-`ts_id` columns must contain only binary values; probability columns entering unsplit would fail validation.
- ID alignment: duplicate normalized `ts_id` values are rejected; rows are aligned on the intersection of IDs shared by all voters.
- Latent alignment: the first voter defines column order; later voters must have the same latent-column set and are reordered to the reference.
- Vote threshold: source uses `2 * ones_count >= n_voters`, equivalent to `sum_m Z_ik^(m) >= ceil(M/2)`.
- Tie handling: even-voter ties map to `1`.
- Output schema: `ts_id` followed by reference latent columns.
- Run-summary linkage: all 12 inspected `run_summary.json` files report overall `success`, majority-vote stage `success`, and absolute `latent_tags_dir` paths under `/truenas/home/kenzikob/causal-irregular-time-series/latent-tags-{dataset}`.
- Provenance limitation: actual voter file lists, hashes, checkpoint/source links, row counts per voter, and exact export split manifests are not archived locally.

## 16.10 Citations Used

- `banda_2018_electronic_phenotyping`: general EHR phenotyping and broad context for rule-derived constructs.
- `ratner_et_al_2020_snorkel`: weak-label/aggregation context only; the chapter states that this project does not implement the Snorkel generative label model.
- `singer_2016_sepsis3`: broad sepsis, shock/lactate, and organ-dysfunction context; not used to claim formal Sepsis-3 diagnosis.
- `vincent_et_al_1996_sofa`: broad SOFA organ-dysfunction context; local PDF gap retained where relevant.
- `kdigo_2012_acute_kidney_injury`: renal dysfunction concepts; not full KDIGO staging.
- `ranieri_et_al_2012_berlin_ards`: respiratory/oxygenation grounding; local PDF gap retained and not used to claim adjudicated ARDS.
- `taylor_et_al_2001_isth_dic`: coagulation/DIC context; not used to claim complete DIC scoring.
- `essay_mosier_subbian_2020_acute_respiratory_failure_phenotyping`: respiratory-failure phenotyping context.
- Citation validation: all inserted keys exist in `references.bib`; no missing citation keys were found.

## 16.11 Placeholders

- Generic Chapter 5 placeholders resolved: broad `[STAGE 4 DRAFT REQUIRED]`, generic `[VALIDATION REQUIRED]`, and generic `[TABLE REQUIRED]` placeholders in C5.1-C5.4 were removed or replaced with precise evidence gates.
- Precise placeholders retained/new:
  - `[SUPERVISOR DECISION REQUIRED: approve proxy state as the primary thesis term and review construct-level clinical wording]`
  - `[VALIDATION REQUIRED: identify whether the archived PhysioNet proxy-state CSV used default or externally optimized thresholds and record the threshold-file provenance]`
  - `[CITATION REQUIRED: clinical grounding for PhysioNet chronic baseline-risk BMI, albumin, and ICU-type clauses]`
  - `[CITATION REQUIRED: clinical grounding for hepatic transaminase, alkaline phosphatase, and albumin clauses in proxy-state rules]`
  - `[CITATION REQUIRED: clinical grounding for cardiac injury or strain proxy thresholds]`
  - `[CITATION REQUIRED: clinical grounding for metabolic, electrolyte, and acid-base proxy thresholds]`
  - `[VALIDATION REQUIRED: verify the provenance and active-rule correspondence of the planned proxy-state decision-tree figures]`
  - `[VALIDATION REQUIRED: identify the MIMIC tagger input mode, source artifact hash, producing command, and source commit for the archived tag CSV]`
  - `[CITATION REQUIRED: clinical grounding for MIMIC chronic burden rule clauses]`
  - `[CITATION REQUIRED: clinical grounding for MIMIC metabolic, electrolyte, and acid-base proxy thresholds]`
  - `[CITATION REQUIRED: clinical grounding for MIMIC cardiac strain proxy thresholds]`
  - `[VALIDATION REQUIRED: create a per-run majority-vote voter manifest listing every binary voter CSV, source predictive model, export split, checkpoint hash, input-artifact hash, row count, latent ordering, and majority-vote output hash]`
- Expected resolution stage: advisor/citation review, result-manifest preparation, predictive/causal manifest preparation, and later figure/appendix pass.

## 16.12 Deferred Fixes

- Previously known issues confirmed: `DF-4.1-002`, `DF-4.2-002`, `DF-4.2-003`, and `DF-4.2-004` remain open because prediction export and voter provenance still lack complete manifests.
- Issues resolved through evidence only: none of the prior deferred fixes were closed by Stage 4.3; they were only narrowed or referenced.
- New Stage 4.3 items added:
  - `DF-4.3-001` PhysioNet proxy provenance.
  - `DF-4.3-002` PhysioNet tree serialization/provenance.
  - `DF-4.3-003` MIMIC proxy provenance.
  - `DF-4.3-004` clinical citation coverage.
  - `DF-4.3-005` clinical/chart-review validation.
  - `DF-4.3-006` majority-vote voter manifests.
  - `DF-4.3-007` majority-vote tie-to-one convention.
  - `DF-4.3-008` PhysioNet urine-clause availability.

## 16.13 Final Build

- Command sequence:

```bash
cd thesis-writing/thesis
latexmk -C
latexmk -xelatex main.tex
test -f main.pdf
pdfinfo main.pdf
```

- Return status: `0`.
- PDF path: `thesis-writing/thesis/main.pdf`.
- Final page count: `53`.
- Citation status: final `main.log` and `main.blg` scan found no `Citation ... undefined`, `There were undefined references`, or `Biber error` messages.
- Reference status: final scan found no `Reference ... undefined` messages.
- Duplicate-label status: final scan found no `multiply defined` messages.
- Fatal errors: none found; no `LaTeX Error`, `Undefined control sequence`, `Emergency stop`, or `Fatal error`.
- Nonfatal warnings: final `main.log` contains 22 overfull and 255 underfull box warnings. The largest final overfull box is 35.5364 pt in a dense Chapter 5 proxy-definition table; one pre-existing bibliography overfull remains. These warnings do not prevent PDF generation.

## 16.14 Readiness

READY WITH NON-BLOCKING WARNINGS.

Stage 4.3 drafted all four Chapter 5 sections, documented the active PhysioNet and MIMIC proxy-state rules, separated rule-derived, predicted, and majority-vote proxy states, kept citation and provenance gaps visible, and produced a successful clean PDF build. Stage 4.4 should not start until a separate prompt requests it.
