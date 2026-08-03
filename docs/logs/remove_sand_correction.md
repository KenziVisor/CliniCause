# Author correction: predictive-model scope

## Authoritative scope

- Learned prediction models: STraTS, GRU, GRU-D, and TCN.
- Aggregate: those four predicted-label sources plus one Rule-Based Trees source.
- The predictive-performance table therefore has eight dataset--model test rows.

## Removed-reference inventory

Removed model-specific prose, table rows, captions, nomenclature entry, literature record/citation, result rows, export/lineage rows, and audit/snapshot rows from:

- `prompt.txt`
- `thesis/frontmatter/abstract_primary.tex`, `thesis/frontmatter/abstract_secondary.tex`, and `thesis/frontmatter/nomenclature.tex`
- `thesis/chapters/01_introduction.tex`, `02_background_related_work.tex`, `05_proxy_state_construction.tex`, `06_predictive_modeling.tex`, `07_causal_methodology.tex`, `09_experimental_design.tex`, `10_results.tex`, `11_discussion.tex`, and `12_conclusions_future_work.tex`
- `literature/metadata/catalog.csv`, `literature/metadata/checksums.sha256`, and `literature/metadata/references.bib`
- `audit/claim_evidence_ledger.csv`, `evidence_inventory.md`, `experiment_inventory.csv`, `figure_table_inventory.md`, `repository_map.md`, and `stage_2_validation_report.md`
- `planning/chapter_evidence_map.md`, `citation_plan.md`, `table_plan.md`, `terminology_and_notation.md`, `thesis_outline.md`, and `thesis_story.md`
- `reproducibility/README.md`, `environment_lineage.csv`, `predictive_run_lineage.csv`, and `provenance_gaps.csv`
- `results/checked_cohort_candidates.csv`, `checked_figure_candidates.csv`, `checked_predictive_exports.csv`, `checked_predictive_metrics.csv`, `results_checksums.sha256`, `results_manifest.csv`, and `results_manifest.md`
- `logs/bilingual_abstract_equivalence.csv`, `stage_5_1_abstract_equivalence.csv`, `stage_5_1_master_claim_audit.csv`, `stage_5_1_numeric_audit.csv`, `stage_5_2_reproducibility_artifact_audit.csv`, `stage_5_2_table_values/T-results-predictive-performance.csv`, `stage_5_5_consistency_audit.csv`, `stage_5_5_frozen_content_snapshot.csv`, `stage_5_5_terminology_audit.csv`, and the associated current stage reports.

Historical planning, context, copied operational notes, and their audit records were also cleared of the obsolete model claim. Thesis-support generators `results/build_stage_4_6A.py` and `results/repair_stage_4_6A.py` now prevent the obsolete material from being reintroduced into result summaries.

While validating the corrected export inventory, the generator's prefix order was corrected so GRU-D exports retain their own model label rather than being grouped under GRU. No numerical value changed.

Raw archived artifacts and the research-model implementation were not edited.

## Validation

- Case-insensitive reader-facing search: pass; no obsolete model name or expansion remains outside excluded research implementation and raw-archive paths.
- Counts: 4 learned models; 8 predictive dataset--model test rows; 8 prediction exports; 8 predictive lineage rows; 5 aggregate sources (4 predicted + 1 Rule-Based Trees).
- English/Hebrew abstract equivalence: rechecked in `bilingual_abstract_equivalence.csv` and `stage_5_1_abstract_equivalence.csv`; both record the four learned models and five-source aggregate.
- Build: `latexmk -xelatex -interaction=nonstopmode main.tex` completed successfully, producing `thesis/main.pdf` (133 pages).
- Layout inspection: the Hebrew and English abstracts, Chapter 9 prediction design, and Chapter 10 predictive-performance table were rendered and visually inspected. No correction-introduced layout problem was found.

Existing unrelated LaTeX overfull-box and PDF object warnings remain outside this correction's scope.

## Status

READY FOR AUTHOR REVIEW
