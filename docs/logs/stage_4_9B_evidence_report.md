# Stage 4.9B Evidence Report — Literature, Citation, and Cross-Chapter Consistency Audit

## 24.1 Git state

Verified `7ef3d97 step 4.9A` on branch `main`; its immediate predecessor is `4fa3f4f step 4.8`.  `stage_4_9A_evidence_report.md` exists and concludes **READY WITH NON-BLOCKING WARNINGS**.

The initial worktree already contained unrelated user changes, including root code, result, requirement, prompt, documentation, nested-repository, and catalog paths.  They were preserved.  Stage 4.9B changed only the following allowed files:

- `thesis-writing/thesis/chapters/02_background_related_work.tex`
- `thesis-writing/thesis/chapters/05_proxy_state_construction.tex`
- `thesis-writing/thesis/chapters/11_discussion.tex`
- `thesis-writing/logs/deferred_fixes.md`
- `thesis-writing/logs/unresolved_placeholders.md`
- `thesis-writing/logs/stage_4_9B_citation_usage.csv`
- `thesis-writing/logs/stage_4_9B_claim_citation_matrix.csv`
- `thesis-writing/logs/stage_4_9B_proxy_rule_citation_matrix.csv`
- this report
- `thesis-writing/thesis/main.pdf` from the clean build.

No literature PDF, bibliography, catalog, checksum, result, figure, source-code, configuration, planning, audit, Chapter 10, or Chapter 12 file was modified.  No commit, push, experiment, result regeneration, or web research occurred.

## 24.2 Baseline build

From `thesis-writing/thesis`, ran `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf`.  Baseline returned status 0 and produced `thesis-writing/thesis/main.pdf` with 119 pages.  Biber, citations, references, and labels resolved; there were no fatal errors.  The non-fatal layout baseline was 99 overfull and 1,149 underfull boxes.

## 24.3 Corpus integrity

The canonical catalog contains 40 entries: 35 core and 5 optional.  Thirty-eight local PDFs are available (29 `present`, 9 `downloaded`), while `vincent_et_al_1996_sofa` and `ranieri_et_al_2012_berlin_ards` remain `missing`.  All 38 entries in `checksums.sha256` passed `sha256sum -c`.

All cited available-PDF paths exist.  There are zero duplicate BibTeX keys, zero duplicate catalog keys, zero duplicate nonempty DOI values, and zero duplicate nonempty titles.  Catalog and BibTeX keys reconcile, titles/authors/years/DOIs/source roles had no obvious mismatch, and Biber compiled the cited entries cleanly.  Classification: **NO_ISSUE**; the two missing PDFs are the documented **NON_BLOCKING_METADATA_WARNING**.

## 24.4 Whole-thesis citation inventory

The programmatic Chapters 1–11 scan supports `cite`, `textcite`, `parencite`, and `autocite`, including comma-separated keys.

| Measure | Result |
| --- | ---: |
| Citation commands | 91 |
| Citation-key uses | 133 |
| Unique cited keys | 34 |
| Core keys used | 34 |
| Optional keys used | 0 |
| Cited missing-PDF keys | 2 |
| Undefined bibliography keys | 0 |
| Keys without catalog rows | 0 |
| Duplicate bibliography/catalog keys | 0 / 0 |
| Uncited corpus entries | 6 |

| Chapter | Unique cited keys |
| --- | ---: |
| 1 | 16 |
| 2 | 34 |
| 3 | 3 |
| 4 | 3 |
| 5 | 8 |
| 6 | 5 |
| 7 | 11 |
| 8 | 5 |
| 9 | 0 |
| 10 | 0 |
| 11 | 18 |

The uncited entries are expected reserves: `shukla2019interpolation` is the historical excluded-model source; `vanderweele_ding_2017_evalue`, `ding_vanderweele_2016_sensitivity_without_assumptions`, `robins_hernan_brumback_2000_msm`, `shukla_marlin_2018_irregular_clinical_timeseries`, and `kent_steyerberg_vanklaveren_2018_personalized_ebm_hte` are optional sources.  No citation was added merely to reduce this count.  The complete context-level inventory is `stage_4_9B_citation_usage.csv`.

## 24.5 Source-role findings

The claim matrix records every material cited sentence or shared citation sentence.  Dataset papers support dataset/challenge/benchmark context only; they are not used as evidence for local preprocessing, cohort construction, splits, or artifact lineage.  Primary model and causal-method papers support canonical concepts only; Chapters 6–8 retain local contracts, adaptations, graph logic, estimator settings, exports, and limitations.  The EconML and DoWhy papers are explicitly software-context citations, not theoretical substitutes.  Reviews frame fields, limitations, and ICU/EHR challenges rather than local execution evidence.

Clinical sources provide conceptual grounding only where Chapter 5 contains local proxy rules.  The text and matrix distinguish project-specific rule thresholds from complete clinical definitions.  No citation was found to validate the project DAG, local nuisance models, local CATEs, positivity, proxy-state clinical validity, or clinical actionability.  The narrow repairs were: (1) reduce Chapter 2 CausalPFN prose to the approved exploratory-only sentence; (2) remove LLM expertise terminology; and (3) replace duplicate reader-facing citation markers with explicit project-specific wording and log tracking.

## 24.6 Cross-chapter overlap

### Chapter 1 versus Chapter 2

The shared themes are irregular sampling, informative measurement, proxy states, prediction-versus-causality, DAG assumptions, and the integration gap.  Paragraph-level semantic review found justified role separation: Chapter 1 motivates the problem, objective, questions, contribution hierarchy, findings preview, and roadmap; Chapter 2 supplies dataset/model/phenotyping/causal literature synthesis and limitations.  No broad shortening was warranted.  Remaining overlap is necessary transition context.

### Chapter 2 versus Chapter 6


### Chapter 2 versus Chapter 7

Chapter 2 retains target-trial, intervention-definition, DAG/backdoor, DML, forest/GRF, HTE, and limitation concepts.  Chapter 7 retains the dataset-specific project graph, graph transformations, adjustment logic, matching, estimator configuration, saved fields, and source-code boundary.  Literature is not presented as validation of the local DAG or estimates.  No repair needed.

### Chapter 2 versus Chapter 8

Chapter 2 retains overlap, sensitivity, and general diagnostic workflow concepts.  Chapter 8 retains local diagnostics, robustness stages, fallback/reconstructed output qualification, and estimator-specific gaps.  DoWhy is not represented as a complete refuter suite; overlap literature is not represented as proof of positivity.  No repair needed.

## 24.7 CausalPFN

CausalPFN appears only in its bounded project role.  Chapter 2 now contains one approved exploratory statement and no citation, architecture, training, peer-equivalence, or theoretical claim.  Chapter 7 describes repository implementation separately from literature positioning.  Chapters 9–11 retain completed intended CATE execution, intentionally skipped sensitivity/permutation stages, incomplete diagnostics, and positive but bounded directional agreement.  Chapter 10 remains unchanged and is the numerical authority.  The primary method-source gap remains `DF-4.7-003`; final status: **CONSISTENT, EXPLORATORY, NON-BLOCKING GAP RETAINED**.

## 24.8 Proxy-rule citation coverage

`stage_4_9B_proxy_rule_citation_matrix.csv` records both datasets for respiratory, renal, hepatic, coagulation/hematologic, shock/hemodynamic, sepsis-related, global-severity, chronic-baseline, cardiac, and metabolic families.  Respiratory phenotyping has general support; renal, coagulation, shock, and sepsis families have conceptual clinical grounding; hepatic and global-severity families remain bounded by missing SOFA PDF use; and chronic-baseline, cardiac, and metabolic families have no approved exact clinical source.  Every exact threshold remains unsupported as a complete clinical definition, every family requires clinical review, and all allowed wording is explicitly “project-specific proxy,” “clinically informed by,” or “draws on concepts from.”

The Chapter 5 reader-facing markers for chronic-baseline, hepatic, cardiac, and metabolic citation gaps were consolidated into one project-specific statement and tracking logs.  This is a presentation repair, not a resolution of the evidence gaps.

## 24.9 Missing PDFs

`vincent_et_al_1996_sofa` is cited once in Chapter 2 and seven times in Chapter 5; `ranieri_et_al_2012_berlin_ards` is cited once in Chapter 2 and twice in Chapter 5.  All uses are bounded: Chapter 2 uses authoritative terminology/conceptual grounding and expressly disclaims detailed implementation reliance; Chapter 5 identifies source-code rules as local, labels them incomplete/project-specific, and does not claim complete SOFA or Berlin ARDS implementation.  No PDF was downloaded.

## 24.10 Optional-source decisions

| Optional key | Decision |
| --- | --- |
| `vanderweele_ding_2017_evalue` | RETAIN_UNCITED_OPTIONAL; it must not replace implemented robustness-value/OVB references. |
| `ding_vanderweele_2016_sensitivity_without_assumptions` | REDUNDANT_WITH_CORE_SOURCE. |
| `robins_hernan_brumback_2000_msm` | RISK_OF_IMPLEMENTATION_CONFUSION; longitudinal MSMs are not implemented. |
| `shukla_marlin_2018_irregular_clinical_timeseries` | OUT_OF_SCOPE; historical excluded-model workshop source. |
| `kent_steyerberg_vanklaveren_2018_personalized_ebm_hte` | REDUNDANT_WITH_CORE_SOURCE. |

## 24.11 LLM literature decision

Chapters 1, 2, 5, 7, and 11 were checked.  **NO FORMAL LLM-ASSISTED-DESIGN LITERATURE ADDED IN THE CURRENT THESIS; PROVENANCE-ONLY FRAMING RETAINED PENDING SEPARATE AUTHOR APPROVAL.**  The prose consistently states that prompts contributed candidate proxy-state and DAG design provenance; source code defines implemented rules and graphs; no LLM was an executed estimator or pipeline component; it did not learn/discover a DAG from data; and its output was not clinical validation.  The prompt-run and human-review manifest remains open.

## 24.12 InterpNet


## 24.13 Reader-facing placeholders

Generic drafting markers are absent.  The four Chapter 5 citation-gap markers and the Chapter 11 CausalPFN citation marker were moved to explicit prose plus the tracking logs because each underlying issue is already stated and tracked.  Precise remaining supervisor, clinical-review, provenance, validation, ethics, and administrative gates remain where reader-facing qualification is necessary.  Final-submission blockers continue to include clinical review, the CausalPFN source, prompt/human-review manifest, missing PDFs, and supervisor related-work approval.

## 24.14 Result protection

Confirmed: **0 Chapter 10 changes; 0 numerical-result changes; 0 hierarchy changes; 0 selected-figure changes.**  CausalForestDML remains primary, LinearDML secondary, CausalPFN exploratory, original cohorts primary, and outcome-downsampled analyses robustness-only.

## 24.15 Final build

After repairs, ran `latexmk -C`, `latexmk -xelatex main.tex`, `test -f main.pdf`, and `pdfinfo main.pdf`.  Return status was 0.  Output is `thesis-writing/thesis/main.pdf`, 119 pages, SHA-256 `1ca37f382a369410e339f005febee21db0da0fccd065447c9de415be657dcb6d`.  There are 0 unresolved citations, 0 unresolved references, 0 duplicate labels, 0 Biber warnings, and 0 fatal errors.  Layout warnings remain 99 overfull and 1,149 underfull boxes; they are non-fatal pre-existing/table-layout warnings.  The exclusion scan and the prohibited LLM-phrase scan both return zero matches.

## 24.16 Readiness

**READY WITH NON-BLOCKING WARNINGS**

The thesis can proceed to Stage 4.10A.  External gates remain: verified primary CausalPFN source; exact clinical support and clinical review for project-specific proxy rules; SOFA and Berlin ARDS PDFs; prompt-run/human-review manifest; and final supervisor related-work approval.
