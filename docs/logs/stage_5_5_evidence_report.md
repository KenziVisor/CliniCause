# Stage 5.5 evidence report

## 28.1 Repository baseline

- Head: `3e29da1d8c6b91ddc00d44b9637218ed0047e6a6`, message `step 5.4`.
- Parent: `ad52c76a31e3e06bd44b36e6ce68f47ce84558f8`, message `step 5.3`.
- Branch: `main`.
- Stage 5.4 verification: its seven new submission/compliance records, five allowed thesis `.tex` changes, and `main.pdf` are present; it did not change figures, results, research code, literature, or the Stage 5.3 reproducibility package.  Its readiness decision is `READY FOR STAGE 5.5 WITH NON-BLOCKING ADMINISTRATIVE GATES`.
- Initial root worktree: 51 pre-existing status records, including the user-controlled `prompt.txt`, root documentation/scripts/requirements/router/test changes, checked-result CSV changes, Stage 5.2 audit-table changes, a literature catalog change, and an existing `runs/` configuration change.  They were recorded and preserved; none was reset, cleaned, staged, amended, committed, pushed, fetched, or normalized.
- Nested worktrees: `causal-irregular-time-series` was already dirty, with `src/preprocess_mimic_iii_large.py` modified; `STraTS` was clean.  Neither repository was modified or executed.

## 28.2 No-research-execution confirmation

Only document/static inspection commands were used: `git`, `sed`, `rg`, `sha256sum`, `latexmk`, `pdfinfo`, `qpdf --check`, `pdftotext`, `pdftoppm`, `montage`, `chktex`, `aspell`, and a temporary standard-library parser restricted to TeX/PDF build artefacts.

No project source code, research module, pipeline, notebook, test suite, figure generator, data loader, patient-level record, or project package was run or imported.

## 28.3 Protected baseline

The initial baseline recorded recursive SHA-256 state for 63 protected path records containing 396 files, plus every thesis `.tex` source.  The five frozen figures have these final, unchanged SHA-256 hashes:

| figure | SHA-256 |
| --- | --- |
| `mimic_causal_dag.png` | `79fa7209166d24a9056753ef785865eb87995b2a363c1b3b5a2bff657fe204d8` |
| `physionet_causal_dag.png` | `67d545d696b480136ee9ed58604d2cd56b406832e7b48d5a67b946f4837be7c2` |
| `results_mimic_forest_original_cate_ranking.png` | `e87b0d768ee3e1f11835d8fc7beb324c0b7a72e6ddc374c0872610cd1242b969` |
| `results_original_three_estimator_direction_agreement.png` | `0f2b89b3fce68b965c79387287f7651e635d91cf4e8232e079acc4cb640b59ea` |
| `results_physionet_forest_original_cate_ranking.png` | `1a64ad1dac16fae862ae886b1f3d19d878c3043cccc3d32b22ae2472bb854c87` |

## 28.4 Baseline build

The baseline build succeeded with 109 A4 pages, PDF SHA-256 `ebaab95d7399e430e7bcf85bf9a50bafeefc037e58791a8110b958d64dbf0306`, and a clean `qpdf --check`.  It had 48 overfull and 1,157 underfull boxes, with zero unresolved citations/references, duplicate labels, Biber errors, missing glyphs, bidi errors, fatal errors, and final-log `xdvipdfmx` warnings.

## 28.5 Frozen-content snapshot

`stage_5_5_frozen_content_snapshot.csv` contains 2,064 reader-facing records: 918 integers, 388 decimals, one fraction, 133 citation-key occurrences, 110 labels, 58 references, five figure files, five figure captions, eight table captions, 106 headings, and 332 table-source lines.  Its post-edit comparison is byte-for-value unchanged for all tracked content.

## 28.6 Copy editing

All reader-facing TeX sources were inspected in full, along with static spelling/LaTeX diagnostics.  No materially distinct edit met all required conditions (unchanged scientific meaning, numbers, citations, causal strength, and clinical strength).  The intentionally header-only `stage_5_5_copy_edit_ledger.csv` records zero edits.  This avoids cosmetic churn in already accurate prose and protects frozen tables, captions, and interpretations.

## 28.7 Terminology and notation

The terminology audit covers 25 canonical terms, including proxy-state vocabulary, cohorts, datasets, model names, DAG/DAGs, CATE language, matching language, and directional-concordance language.  Contextual plurals, code names, and grammatical hyphenation variants were retained; no semantic conflation was found and no repair was required.  The nomenclature and notation entries remain consistent with their uses.

## 28.8 Causal and clinical boundaries

The consistency audit contains 884 substantive reader-facing occurrences of the requested causal/clinical terms.  Every occurrence retains the established boundary: assumption-conditional observational interpretation; proxy state not diagnosis; matching not CATE; agreement not correctness; no unsupported significance, clinical recommendation, deployment, fairness-validation, or project-specific ethics/governance claim.  No claim was strengthened or weakened.

## 28.9 Cross-references

All 58 `\ref`, `\pageref`, and `\autoref` occurrences were audited against 110 unique labels.  Every target exists and resolved in the build; no label relationship, display context, capitalization, or spacing repair was required.  Undefined references and duplicate labels are both zero.

## 28.10 Layout warnings

| class | count | disposition |
| --- | ---: | --- |
| `MATERIAL_RENDERED_DEFECT` | 0 | None found. |
| `MINOR_READABILITY_DEFECT` | 0 | None found. |
| `BENIGN_TEX_DIAGNOSTIC` | 2 families | 48 overfull boxes and 25 clean-conversion duplicate-longtable-destination messages; no rendered intrusion or broken link. |
| `LONGTABLE_OR_JUSTIFICATION_ARTIFACT` | 1 family | 1,157 underfull boxes in narrow longtable cells/justified prose; rendered output is readable. |
| `UNRESOLVED` | 0 | None. |

No blanket `\sloppy`, `\emergencystretch`, margin, font-size, or line-spacing suppression was added.  Existing scoped difficult-table settings were retained.

## 28.11 Full-PDF visual review

All 109 pages were rendered after the final build and recorded one per row in `stage_5_5_full_pdf_review.csv`.  The review found no clipping, overlap, margin intrusion, detached caption, malformed table, unintended blank page, bad header/footer, or RTL/LTR failure.  The five figures were inspected only for layout; their approved scientific content was not re-evaluated.  Official title and approval pages remain deliberately absent.

## 28.12 Bilingual front matter

Both abstracts remain below 500 words, factually equivalent, free of citations/footnotes, and numerically unchanged.  English and Hebrew keyword lists each contain 15 aligned concepts.  The rendered Hebrew abstract and keyword block retain stable mixed-direction handling; no unofficial Hebrew title was created.

## 28.13 Administrative gates

The current PDF remains a polished advisor-ready draft, not a submission-ready thesis.  Required authoritative inputs remain: current official forms and sequence, English-thesis authorization, official metadata, ethics/governance/consent/data-use wording, and clinical-review records.  No value or statement was inferred or inserted.

## 28.14 Files changed

- `thesis-writing/thesis/main.pdf` (permitted regenerated build output only)
- `thesis-writing/logs/stage_5_5_frozen_content_snapshot.csv`
- `thesis-writing/logs/stage_5_5_copy_edit_ledger.csv`
- `thesis-writing/logs/stage_5_5_terminology_audit.csv`
- `thesis-writing/logs/stage_5_5_consistency_audit.csv`
- `thesis-writing/logs/stage_5_5_cross_reference_audit.csv`
- `thesis-writing/logs/stage_5_5_layout_warning_ledger.csv`
- `thesis-writing/logs/stage_5_5_full_pdf_review.csv`
- `thesis-writing/logs/stage_5_5_release_handoff.md`
- `thesis-writing/logs/stage_5_5_evidence_report.md`

No thesis `.tex`, bibliography, figure, result, reproducibility, literature, audit, planning, prior-stage log, code, generator, test, or user-controlled prompt file was changed.

## 28.15 Frozen-content comparison

- Changed numerical tokens: 0.
- Citation-key additions/removals: 0/0.
- Changed labels: 0.
- Changed figure captions: 0.
- Changed table values: 0.
- Changed figure files: 0.

## 28.16 Protected-file validation

The protected-path comparison reports 63 of 63 path records unchanged (396 recursive files), including all checked CSVs, result records, reproducibility and literature packages, research repositories, prior-stage logs, generators, and figures.  The permitted regenerated PDF is reported separately above; it is not a protected source or evidence record.

## 28.17 Final build

- Page count: 109.
- PDF SHA-256: `7f747606dac9fcf773f9ac9317bc64b2f930efa5628a109f39ddb160b792988a`.
- Final up-to-date `latexmk -xelatex main.tex` check: exit 0.
- Final log: 48 overfull, 1,157 underfull, 0 unresolved citations, 0 unresolved references, 0 duplicate labels, 0 Biber errors/warnings, 0 missing glyphs, 0 bidi errors, 0 fatal errors, and 0 `xdvipdfmx` warnings.
- `qpdf --check`: no syntax or stream-encoding error.
- Complete rendered-page inspection: pass.

## 28.18 Release handoff

`stage_5_5_release_handoff.md` carries forward the authoritative submission-input checklist, exact future insertion locations, and the Final Release Audit requirements.  The exact next action is to obtain the listed authoritative inputs; do not begin insertion or release packaging until they are supplied.

## 28.19 Readiness decision

READY FOR FINAL RELEASE PREPARATION WITH EXTERNAL SUBMISSION INPUTS PENDING
