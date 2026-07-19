# CliniCause AAAI-27 structure and format notes

Status: P1/P3 design baseline, verified 2026-07-19.

Purpose: mechanical genre, format, page-budget, visual, and skeleton decisions. This is not scientific manuscript prose.

## 1. Binding submission facts

Current official sources:

- [AAAI-27 Main Technical Track call](https://aaai.org/conference/aaai/aaai-27/main-technical-track-call/)
- [AAAI-27 submission instructions](https://aaai.org/conference/aaai/aaai-27/submission-instructions/)
- [AAAI-27 supplementary-material instructions](https://aaai.org/conference/aaai/aaai-27/supplementary-material/)
- [AAAI-27 conference page and dates](https://aaai.org/conference/aaai/aaai-27/)
- [AAAI publication policies and guidelines](https://aaai.org/aaai-publications/aaai-publication-policies-guidelines/)

| Requirement | Operational decision |
|---|---|
| Main content | Maximum 7 pages |
| Total manuscript | Maximum 9 pages; pages after page 7 may contain references only |
| Paper size/layout | US letter, official AAAI two-column style |
| Review identity | Anonymous submission mode; no identifying author, affiliation, acknowledgment, URL, or PDF metadata |
| Checklist | Required, but uploaded separately in the designated field; do not append/input it into `paper.pdf` |
| Supplement timing | Submitted on the supplementary deadline stated by AAAI; current call says three days after the main-paper deadline |
| Supplement categories | Supplementary Document PDF, Media ZIP, and Code/Data ZIP |
| Self-containment | Main paper must stand alone; reviewers are not obliged to inspect supplementary material |
| Code/data evidence | Artifacts intended as review evidence must be available at submission; a promise to release after acceptance is not review evidence |
| Generative AI | Judicious use is allowed under the current call, humans remain fully responsible; use must comply with AAAI publication documentation rules |

`TODO-AAAI G-AAAI-01`: recheck all mutable official rules immediately before submission.

## 2. Author-kit contract

Inspected completely: anonymous and camera-ready `.tex` samples, rendered PDFs, reproducibility-checklist source/PDF, `aaai2027.sty`, `aaai2027.bst`, and kit bibliography.

### Required skeleton preamble

```tex
\documentclass[letterpaper]{article}
\usepackage[submission]{aaai2027}
\usepackage[hyphens]{url}
\usepackage{graphicx}
\urlstyle{rm}
\def\UrlFont{\rm}
\usepackage{natbib}
\usepackage{caption}
\frenchspacing
\pdfinfo{/TemplateVersion (2027.1)}
```

`booktabs` is added for planned tables. PDFLaTeX is the supported engine. The official `aaai2027` bibliography style is selected by the style file; the approved project bibliography is connected externally rather than copied.

### Formatting controls

- Keep the kit's margins, fonts, two-column layout, title spacing, footer behavior, and page-number suppression unchanged.
- Do not add `hyperref`, geometry/margin packages, alternate fonts, navigation packages, manual line spacing, negative vertical space, or forced page breaks.
- Place captions below both figures and tables, matching the kit.
- Design figure labels for 9-point readability; use 10-point table text unless a justified 9-point reduction is required.
- Keep references at least 9 point; the kit style controls this.
- Use a single main `paper.tex`; no checklist input is included in the manuscript.
- Before release, inspect the compiled PDF metadata and every rendered page for identity leakage, clipping, overflow, and visual density.

### Observed kit behavior

- Anonymous sample and camera-ready sample each render as 10-page, US-letter (`612 × 792 pt`) PDFs.
- Submission mode renders the official anonymous-review treatment and suppresses supplied author/affiliation information.
- The sample uses compact first-page framing, numbered sections, conventional result tables/figures, references in the same PDF, and no page numbers.
- The separate checklist sample renders as two pages; it is a questionnaire artifact, not part of the 7-page technical narrative.

## 3. AAAI genre sample

The examples were studied for structure and density only. Their claims and numbers are not evidence for CliniCause.

| Example | Structural observations | Transfer to CliniCause |
|---|---|---|
| [CUPCase: Clinically Uncommon Patient Cases and Diagnoses](https://ojs.aaai.org/index.php/AAAI/article/view/35050) ([PDF](https://ojs.aaai.org/index.php/AAAI/article/download/35050/37205)) | Resource construction appears before evaluation; the first pipeline figure makes the artifact legible; evaluation and error analyses validate the resource; limitations and availability are explicit near the end | Put the end-to-end resource/pipeline before detailed estimators; make Figure 1 the orientation anchor; consolidate limitations/release status |
| [A Practical Approach to Causal Inference over Time](https://ojs.aaai.org/index.php/AAAI/article/view/33626) ([PDF](https://ojs.aaai.org/index.php/AAAI/article/view/33626/35781)) | Problem and contribution are compressed on page 1; background is selective; method and causal assumptions precede experiments; limitations are short and explicit | Compress related work; reserve space for study design/identification and bounded limitations |
| [Towards Ultrasound-based Reliable Disease Diagnosis Using Causal Inference](https://ojs.aaai.org/index.php/AAAI/article/view/37267) ([PDF](https://ojs.aaai.org/index.php/AAAI/article/view/37267/41229)) | Contributions are enumerated early; methods precede a dense experimental section; ablation/parameter detail supports the main result while implementation detail moves to supplement | Use explicit contribution functions, result-led visuals, and move nonessential implementation detail to supplement |

Genre synthesis:

1. Page 1 must establish the clinical/technical problem, resource-level answer, scope, and contribution hierarchy.
2. The central resource/pipeline figure should explain the complete object before component details.
3. Related work should distinguish the gap and nearest families, not reproduce thesis-length history.
4. Results should be organized around a small number of checked claims, not around every archived file.
5. Each central claim needs an immediately visible table/figure or a precise checked source.
6. Limitations should be consolidated and specific: proxy validity, observational identification, partial validation coverage, lineage gaps, and release state.
7. Supplementary material may carry detail but cannot repair an unsupported or non-self-contained main-paper claim.

## 4. Locked paper architecture

The skeleton uses the following exact section hierarchy:

1. Introduction
2. Related Work
3. CliniCause Resource and Pipeline
   1. Source Cohorts and Preprocessing
   2. Proxy Construction
   3. Causal Estimation and Validation
4. Evaluation
   1. Experimental Setup
   2. Predictive Results
   3. Causal Results
5. Discussion and Limitations
6. Conclusion

### Section functions and evidence inputs

| Section | Required function | Primary evidence input | Primary gate |
|---|---|---|---|
| Abstract | Post-body summary of problem, resource, two-dataset scope, and bounded checked outcomes | Final paper body only | Human wording review; write last |
| Introduction | Problem, resource-level answer, contribution hierarchy, scope, non-deployment boundary | Thesis Chs. 1/3/11; evidence-map C01/C02/C23 | G-HUM-01 |
| Related Work | Irregular-time-series prediction, proxy labeling/weak supervision, longitudinal causal estimation, resource gap | Thesis Ch. 2; approved bibliography | G-EVD-01 for CausalPFN |
| Resource and Pipeline | Explain the end-to-end object and interfaces | Thesis Chs. 3–8; current code for current contract only | G-RUN-01 for test-pass wording |
| Source Cohorts | Define units, cohort flow, preprocessing, split boundary | Thesis Chs. 3–4; checked cohort/exports | G-EVD-02 for exact split lineage |
| Proxy Construction | Define one-rule/four-source construction and label semantics | Thesis Chs. 5–6; checked proxy/predictive files | Human terminology review |
| Causal Estimation and Validation | Estimand, exposure/outcome/confounder roles, three estimators, diagnostics | Thesis Chs. 7–8; checked CATE/validation files | G-EVD-01/G-EVD-02 |
| Evaluation Setup | Datasets, archived run selection, metrics, sampling conditions | Results packet/decision register/checked files | G-EVD-02 qualification |
| Predictive Results | Compact archived four-model comparison | Checked predictive metrics | No superiority/significance claim |
| Causal Results | 19-combination direction matrix, exception, sampling robustness | Checked CATE candidates | Observational/proxy qualification |
| Discussion and Limitations | What the resource enables, what evidence does not establish, lineage/release limits | Thesis Ch. 11; gate register | G-HUM-01/G-REL-01 |
| Conclusion | Resource-level outcome without new claims | Locked claims only | Human final review |

## 5. Seven-page budget

| Content | Target pages | Control decision |
|---|---:|---|
| Title + abstract + Introduction | 0.9 | No abstract until body is stable; compact contribution block |
| Related Work | 0.55 | Synthesis by gap, not paper-by-paper catalog |
| Resource and Pipeline | 2.05 | Figure 1 earns central space; equations/definitions only if indispensable |
| Evaluation setup | 0.65 | One compact setup paragraph/table context; lineage qualifications explicit |
| Predictive Results | 0.65 | Table 1 plus result-led interpretation |
| Causal Results | 1.35 | Figure 2 + Table 2; show concordance and the one exception |
| Discussion, Limitations, Conclusion | 0.85 | Consolidated, specific boundaries |
| Total technical content | 7.00 | Hard cap; references start after technical page 7 and total PDF stays ≤9 pages |

The skeleton is not expected to occupy this budget. The budget governs later prose/visual drafting.

## 6. Visual budget and source contract

| ID | Planned artifact | Intended location | Width | Evidence source | Main/supplement | Gate |
|---|---|---|---|---|---|---|
| Figure 1 | End-to-end CliniCause resource/pipeline: cohorts → preprocessing → rule/predictive proxy sources → aggregation → causal estimators → validation outputs | Start of Section 3 | Two columns | Thesis method chapters + repository interfaces; redraw as paper-native figure | Main | G-HUM-01 for final emphasis |
| Table 1 | Dataset scope plus archived predictive metrics for GRU, GRU-D, STraTS, and TCN | Predictive Results | Two columns | Checked cohort + predictive metrics files | Main | None; retain archived-run qualification |
| Figure 2 | Cross-estimator directional agreement across 19 dataset-exposure combinations, visibly marking PhysioNet shock | Causal Results | Two columns | `checked_cate_candidates.csv`; thesis agreement figure may guide design | Main | None; human visual choice |
| Table 2 | Compact CATE/concordance summary, including 19/19 DML, 18/19 all-three, 55/57 sampling agreement and named exceptions | Causal Results | Two columns | `checked_cate_candidates.csv` | Main | None; no clinical-effect interpretation |
| Supplement S1 | Cohort/preprocessing detail and mappings | Supplement | Flexible | Thesis Ch. 4 + checked cohort files | Supplement | G-EVD-02 where lineage-specific |
| Supplement S2 | Matching, sensitivity, permutation, heterogeneity detail | Supplement | Flexible | Checked validation files | Supplement | Clearly label skipped/failed/partial coverage |
| Supplement S3 | Current validation-contract inventory and reproducibility ledger | Supplement/checklist support | Flexible | Router/tests + reproducibility package | Supplement | G-RUN-01/G-EVD-02 |

Rules for future visual production:

- Recompute any plotted number from the checked CSV and preserve full-precision calculation inputs.
- Prefer direct labels and a colorblind-safe palette; the result must remain legible in grayscale.
- Use no screenshots of tables or code.
- Captions state what is encoded and the critical qualification, not unsupported interpretation.
- Every visual has a checked-data source and a regeneration path before it can be marked final.

## 7. Main-paper versus supplement boundary

Main paper must contain:

- the study unit and two-dataset scope;
- the one-rule/four-predictive-source proxy construction at an intelligible level;
- the estimand/exposure/outcome distinction and all three estimator roles;
- the archived predictive comparison needed to validate the proxy sources;
- 19/19 DML and 18/19 three-estimator directional results, including the PhysioNet-shock exception;
- enough robustness evidence to support bounded stability language;
- explicit limitations on proxy validity, observational identification, partial validation, provenance, and release status.

Supplement may contain:

- full feature/exposure mappings and implementation parameters;
- full-precision result matrices and extended plots;
- per-exposure matching, sensitivity, permutation, and heterogeneity records;
- environment and artifact lineages;
- validation-contract and test inventories;
- anonymous code/data package instructions.

Supplement cannot be used to hide the exception, basic identification assumptions, or any qualification necessary to interpret a headline claim.

## 8. Reproducibility-checklist preparation register

No answer is asserted here; the final checklist must be completed against the final paper and release package.

| Area | Planned evidence | Unresolved action |
|---|---|---|
| Scope/claims | Claim lock in `paper_evidence_map.md` | Authors ratify contribution hierarchy and every empirical qualification |
| Assumptions/limitations | Thesis Chs. 3, 7, 8, 11 | Map final text to exact assumptions and failure modes |
| Dataset documentation | Cohort/preprocessing chapters; checked cohort candidates | Supply anonymous access and preprocessing instructions |
| Code | Current nested repositories and router contracts | Create anonymous licensed submission package; execute tests |
| Hyperparameters/configuration | Thesis method chapters and available config records | Recover missing numbered configs or disclose exact gap |
| Runs/seeds | Checked files, run lineage, permutation seed record | Recover predictive split/checkpoint linkage and producing revisions where possible |
| Statistical reporting | Checked point estimates and deterministic directional counts | State absence of uncertainty/significance evidence where applicable |
| Compute | Environment lineage | Verify against producing runs; do not substitute current environment |
| Artifacts | Manifests/checksums/source packet | Package and verify anonymous supplement/release artifacts |
| Responsible use | Thesis discussion plus final human review | Confirm privacy, license, intended-use, risk, and generative-AI disclosures |

## 9. Skeleton rules

- Scientific prose remains as comments only; placeholders are visibly labeled.
- The abstract is deliberately empty until the complete technical body exists.
- Each intended claim location names its evidence-map claim IDs and any gate.
- Planned floats contain no fabricated result; they state their future source and role.
- The project bibliography is wired as `../literature/metadata/references`; no unverified citation is added.
- The checklist is explicitly excluded from `paper.pdf` and reserved for separate upload.
- A successful skeleton build establishes format/build readiness only, not scientific readiness or checklist completeness.

READY FOR STAGE P1 — AAAI GENRE AND FORMAT STUDIED

READY FOR STAGE P3 — AAAI SKELETON DESIGN LOCKED
