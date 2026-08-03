# Stage 5.4 — Institutional, Ethics, Governance, and Administrative Compliance Audit

## 22.1 Repository baseline

- Verified head: `ad52c76a31e3e06bd44b36e6ce68f47ce84558f8` (`step 5.3`).
- Verified immediate parent: `f71c9bab70c8fb6347c7692236cd2cfd03e84fa1` (`step 5.2`).
- Branch: `main`.
- `ad52c76` exists, has the expected message, and has `f71c9ba` as its immediate parent.
- Stage 5.3 added the reproducibility package and provenance ledgers. Its diff changes no thesis PNG, checked result source, result generator, research-code directory, or literature source. Its three reader-facing thesis changes are narrow provenance clarifications in the appendix, Chapter 6, and Chapter 9.
- The five external assistant figure decisions are recorded in `stage_5_3_external_figure_decision.{md,csv}` as transcribed external decisions, explicitly not Codex approval. The record also states that those decisions do not supply clinical, ethics, causal-identification, or statistical-significance approval.

The complete initial worktree was preserved. It contained the following pre-existing modifications before Stage 5.4 edits:

```text
 M README.md
 M SCRIPTS.md
 m causal-irregular-time-series
 M fix_preprocessor.py
 M prompt.txt
 M requirements-full.txt
 M requirements-router.txt
 M requirements.txt
 M router.py
 M runs/validate_demo/config/physionet_resolved_config.csv
 M tests/test_router.py
 M thesis-writing/important-md-copies/clinicause_root_project_overview.md
 M thesis-writing/important-md-copies/clinicause_root_router_usage.md
 M thesis-writing/important-md-copies/strats_project_overview.md
 M thesis-writing/literature/metadata/catalog.csv
 M thesis-writing/logs/stage_5_2_appendix_audit.csv
 M thesis-writing/logs/stage_5_2_figure_validation.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-edges.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-MIMIC-nodes.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-edges.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-DAG-PHYSIONET-nodes.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT-summary.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-MIMIC-CATE.csv
 M thesis-writing/logs/stage_5_2_figure_values/F-RESULT-PHYSIONET-CATE.csv
 M thesis-writing/logs/stage_5_2_reproducibility_artifact_audit.csv
 M thesis-writing/logs/stage_5_2_table_audit.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-analysis-populations.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-forest-mimic.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-linear-comparison.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-matching-support.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-pfn-comparison.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-predictive-performance.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-robustness-summary.csv
 M thesis-writing/results/checked_cate_candidates.csv
 M thesis-writing/results/checked_cohort_candidates.csv
 M thesis-writing/results/checked_figure_candidates.csv
 M thesis-writing/results/checked_heterogeneity_candidates.csv
 M thesis-writing/results/checked_matching_failures.csv
 M thesis-writing/results/checked_matching_results.csv
 M thesis-writing/results/checked_mortality_prediction.csv
 M thesis-writing/results/checked_permutation_candidates.csv
 M thesis-writing/results/checked_predictive_exports.csv
 M thesis-writing/results/checked_predictive_metrics.csv
 M thesis-writing/results/checked_proxy_cooccurrence.csv
 M thesis-writing/results/checked_proxy_mortality_association.csv
 M thesis-writing/results/checked_proxy_prevalence.csv
 M thesis-writing/results/checked_sensitivity_candidates.csv
 M thesis-writing/results/results_manifest.csv
 M tmp_verify_router.py
```

These were not reset, cleaned, staged, amended, or otherwise modified by this stage.

## 22.2 Institutional sources

The local institutional authority inspected was `thesis-writing/general-instructions.pdf` (3 PDF pages; the root-level `general-instructions.pdf` is absent). Pages 9-11 of the source PDF record the relevant graduate-thesis rules; its printed PDF page 10 contains technical items 1-14 and printed PDF page 11 contains items 15-20 and the Hebrew-default sequence. The local files inspected in full or at the required locations were:

- `thesis-writing/planning/bgu_requirements_map.md`
- `thesis-writing/thesis/main.tex`
- `thesis-writing/thesis/frontmatter/`
- `thesis-writing/thesis/appendices/appendices.tex`
- `thesis-writing/logs/unresolved_placeholders.md`
- `thesis-writing/logs/deferred_fixes.md`

The local PDF is authoritative for the stated technical requirements and the Hebrew-default rule. It refers to a faculty forms system but does not supply current forms, an exact current English-thesis title/approval-page sequence, author identity, departmental authorization, approval identifiers, consent/waiver text, data-use terms, or governance determinations. No such fact was invented.

## 22.3 Institutional compliance

`stage_5_4_institutional_compliance.csv` contains 34 auditable rows:

| status | count |
| --- | ---: |
| COMPLIANT | 19 |
| COMPLIANT_WITH_QUALIFICATION | 4 |
| EXTERNALLY_GATED | 9 |
| NOT_APPLICABLE | 1 |
| SOURCE_AMBIGUOUS | 1 |

Locally compliant items include A4 size, 2 cm margins, 1.5 spacing, top-centered page numbers, Roman front matter, Arabic body, hierarchical numbering, independent figure/table counters, abstracts, keyword count, TOC depth, nomenclature, lists, appendix/bibliography order, and no rendered raw administrative placeholder.

The official title/approval forms, English-language authorization, official metadata, exact English-thesis sequence, and institutional determination wording remain external gates. The thesis does not pretend that omitted official pages are complete.

## 22.4 Formatting

- Page size: A4 (`595.28 x 841.89 pt`).
- Margins: 2 cm configured; nominal text block is 170 mm by 257 mm.
- Spacing: `\onehalfspacing`.
- Numbering: Roman front matter and Arabic body; all sampled normal and chapter-opening pages have top-centered numbers.
- TOC: rendered through subsection depth.
- Figures/tables: separately numbered and separately listed.
- Nomenclature: populated abbreviations and notation/symbol lists render before the lists.
- Bibliography: rendered after Appendix A with zero undefined citations, zero Biber errors, and one non-fatal biblatex Hebrew-language dummy-definition warning.
- Sequence: current rendered sequence is Hebrew abstract, English abstract, keywords, TOC, abbreviations, notation/symbols, lists, chapters, appendix, bibliography. It is `LOCALLY_SUPPORTED_WITH_ENGLISH_THESIS_QUALIFICATION`; final title/approval pages and their exact position require current faculty-form confirmation.

The final log records 48 overfull and 1,157 underfull box warnings. The rendered abstract, keyword, TOC, list, Chapter 4, Chapter 9, Chapter 11, Chapter 12, appendix, and bibliography samples showed no clipping. These logged layout diagnostics are retained for the dedicated Stage 5.5 hardening pass; they do not contradict a locally checkable BGU minimum in the inspected render.

## 22.5 Abstracts and keywords

- English abstract: 347 source-text tokens; Hebrew abstract: 306 source-text tokens. Both are below 500.
- Both abstracts have four corresponding paragraphs, no citations, and no footnotes. The prior equivalence ledger remains `stage_5_1_abstract_equivalence.csv`.
- English and Hebrew keyword blocks each contain 15 aligned phrases.
- Hebrew text and embedded Latin terms render correctly. Stage 5.4 isolated embedded Latin terms with `\textenglish{}`; no factual abstract content changed.
- The abstracts are pages i and ii; keyword blocks render on page iii.

## 22.6 Ethics and governance

`stage_5_4_ethics_governance_audit.csv` contains 20 material claims:

| support status | count |
| --- | ---: |
| SUPPORTED | 4 |
| SUPPORTED_WITH_QUALIFICATION | 4 |
| NEGATIVE_BOUNDARY_SUPPORTED | 12 |

No project-specific IRB/ethics approval number, exemption, consent procedure, waiver, data-use agreement, governance approval, clinical validation, chart review, fairness validation, privacy-risk measurement, qualified DAG approval, or clinical deployment authorization is claimed. The thesis appropriately distinguishes dataset context and access conditions from project-level institutional approval.

One reader-facing repair was made in Chapter 11:

| path | old wording | new wording | evidence | reason |
| --- | --- | --- | --- | --- |
| `thesis-writing/thesis/chapters/11_discussion.tex` | No institutional approval number, consent procedure, ethics-board decision, or data-use agreement is inferred here. | The repository does not establish the project-specific institutional approval, consent or waiver procedure, data-use agreement, or governance determination. These facts must be supplied from authoritative institutional records and must not be inferred from dataset access, de-identification, or repository contents. | No authoritative project record is present; local task requires this boundary. | Make the no-inference boundary complete and explicit without asserting absence of oversight. |

## 22.7 Dataset-specific ethics

### MIMIC-III

The thesis describes MIMIC-III as a deidentified controlled-access critical-care database and cites the approved Johnson et al. dataset reference for its qualified-researcher/training/data-use-agreement context. This is a dataset-level description only. No local project credentialing record, project institutional approval, consent/waiver determination, governance record, or project data-use agreement is available. The remaining gap is authoritative project documentation.

### PhysioNet 2012

The thesis describes PhysioNet 2012 as a mortality-prediction challenge dataset and cites the approved Silva et al. challenge reference. The repository establishes neither a project access record nor an institutional approval, consent/waiver, data-use, or governance determination. The remaining gap is authoritative project and dataset-governance documentation, if applicable.

## 22.8 Privacy scan

The scan covered thesis source and the immutable Stage 5.3 reproducibility package. No credential, token, password, API key, email, raw patient-level value, or explicit patient-identifier column was found in the scanned scope. No protected patient data were copied into any Stage 5.4 log.

Two historical absolute paths with a username remain in an internal, immutable provenance CSV. They are redacted in the privacy ledger, are not reader-facing, and are retained only because they document historical lineage. Chapter 9's reader-facing storage-root path was replaced with the non-identifying phrase “machine-specific storage path.”

## 22.9 Administrative metadata

`stage_5_4_administrative_inputs.csv` enumerates 22 inputs. Resolved technical metadata is limited to a provisional English working title that is not ratified or rendered. All official identity, title, department, faculty, degree, supervisor, date, committee, authorization, ethics, consent, agreement, governance, and form data remain intentionally unresolved rather than inferred. Acknowledgements remain omitted pending author-approved text.

## 22.10 Official-form and authorization gates

- Current faculty title-page form: not available locally.
- Current faculty approval-page form: not available locally.
- English-thesis authorization: not documented locally.
- Exact current English-thesis sequence: not established by the supplied Hebrew-default instructions.
- Official identity/degree/department/supervisor/date/committee values: not documented locally.
- Ethics, consent/waiver, data-use, privacy, and governance wording: not documented locally.

The provisional title/approval pages were intentionally removed from the compiled PDF. The centralized macros remain non-rendered source placeholders only; no blank page or raw requirement marker is presented as a completed official page.

## 22.11 Thesis repairs

| path | old wording | new wording | evidence | reason |
| --- | --- | --- | --- | --- |
| `thesis-writing/thesis/main.tex` | Provisional title and approval pages rendered administrative-gate text. | Their input is disabled with a source comment explaining the missing authoritative inputs. | Current forms and metadata are absent; task placeholder policy. | Remove reader-facing drafting gates and avoid a false submission-ready appearance. |
| `thesis-writing/thesis/chapters/09_experimental_design.tex` | Named a machine-specific storage root. | Uses “a machine-specific storage path.” | Privacy scan. | Remove unnecessary reader-facing infrastructure detail. |
| `thesis-writing/thesis/chapters/11_discussion.tex` | Incomplete no-inference sentence. | Explicit project-specific institutional-evidence boundary. | Ethics/governance audit. | Distinguish repository evidence from institutional records. |
| `thesis-writing/thesis/frontmatter/abstract_secondary.tex` | Embedded Latin terms relied on mixed-direction defaults. | Embedded Latin terms use `\textenglish{}`. | Rendered Hebrew inspection. | Preserve reliable RTL/LTR rendering without altering claims. |
| `thesis-writing/thesis/frontmatter/keywords.tex` | Final Latin keyword phrase relied on mixed-direction defaults. | Final Latin phrase uses `\textenglish{}`. | Rendered Hebrew inspection. | Preserve readable aligned bilingual keyword rendering. |

## 22.12 Submission inputs

The detailed checklist is `stage_5_4_submission_inputs_required.md`. It separates required items from the author, supervisor/department, institution/data-governance authority, and qualified clinical reviewer, and records why each is needed, insertion point, provider, acceptable evidence, status, and blocking effect.

## 22.13 Files changed

Stage 5.4 changed only these allowed paths:

- `thesis-writing/thesis/main.tex`
- `thesis-writing/thesis/chapters/09_experimental_design.tex`
- `thesis-writing/thesis/chapters/11_discussion.tex`
- `thesis-writing/thesis/frontmatter/abstract_secondary.tex`
- `thesis-writing/thesis/frontmatter/keywords.tex`
- `thesis-writing/thesis/main.pdf`
- `thesis-writing/logs/stage_5_4_institutional_compliance.csv`
- `thesis-writing/logs/stage_5_4_ethics_governance_audit.csv`
- `thesis-writing/logs/stage_5_4_privacy_scan.csv`
- `thesis-writing/logs/stage_5_4_administrative_inputs.csv`
- `thesis-writing/logs/stage_5_4_format_validation.csv`
- `thesis-writing/logs/stage_5_4_submission_inputs_required.md`
- `thesis-writing/logs/stage_5_4_evidence_report.md`

## 22.14 Protected-file validation

The initial protected baseline contained 160 files, including 21 thesis `.tex` files that were separately hashed before edits. The final protected-evidence comparison covers 139 immutable evidence/code/literature/reproducibility/figure paths and is byte-identical: 139 of 139 unchanged. The remaining 21 baseline entries are thesis source files; only the five allowed Stage 5.4 `.tex` repairs changed.

All five thesis PNG figures are byte-identical:

| figure | SHA-256 |
| --- | --- |
| `mimic_causal_dag.png` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` |
| `physionet_causal_dag.png` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` |
| `results_mimic_forest_original_cate_ranking.png` | `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969` |
| `results_original_three_estimator_direction_agreement.png` | `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` |
| `results_physionet_forest_original_cate_ranking.png` | `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87` |

Checked CSVs, result records, result generators, literature, the entire Stage 5.3 reproducibility package, causal source, and STrATS source are unchanged from the initial Stage 5.4 hash baseline.

## 22.15 Final build and render

Build command: `latexmk -C && latexmk -xelatex main.tex` in `thesis-writing/thesis`.

- PDF exists: yes.
- Page count: 109.
- PDF SHA-256: `ba69edf130121c347a4d4573ec3d2120374afb8f12ca56273c3c5f9a07d6e389`.
- Undefined citations: 0.
- Undefined references: 0.
- Duplicate labels: 0.
- Biber errors/warnings: 0/0.
- Missing glyphs: 0.
- Bidi errors: 0.
- Fatal errors: 0.
- `xdvipdfmx` warnings: 0.
- Overfull/underfull boxes: 48/1,157, logged for Stage 5.5 layout hardening; no clipping observed in inspected required pages.

Rendered inspection covered the intentionally omitted title/approval pages; both abstracts; both keyword blocks; TOC; nomenclature; lists; Chapter 4; Chapter 9; Chapter 11; Chapter 12; Appendix A; and bibliography transition.

## 22.16 Remaining gates

Only external inputs remain: current faculty forms and exact sequence; departmental English-thesis authorization; official title/identity/department/faculty/degree/supervisor/date/committee values; authoritative ethics/approval/exemption/consent/waiver/data-use/governance/privacy wording; and qualified clinical review records. These are tracked precisely and are not represented as repository findings.

## 22.17 Readiness decision

READY FOR STAGE 5.5 WITH NON-BLOCKING ADMINISTRATIVE GATES
