# Hebrew Abstract Repair Report

## Status

The scientific verification gate failed before the approved replacement was applied. The approved Hebrew text assigns the values `19` and `18 of 19` to dataset-specific positive-effect counts, but the checked result packet assigns those values to cross-dataset estimator-direction agreement. In accordance with `prompt.txt`, `frontmatter/abstract_secondary.tex` was not edited and no post-replacement build was attempted.

## Baseline

- Branch: `main`
- Commit: `112f3d8` (`concistency imporvment`)
- Baseline history inspected: `git log -10 --oneline`
- Applicable instruction files: no `AGENTS.md` governs `thesis-writing/`; the discovered instruction files are scoped to other repository subtrees.
- Pre-existing dirty paths (59), recorded before any task edit:

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
 M thesis-writing/logs/stage_5_2_table_values/T-results-forest-physionet.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-linear-comparison.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-matching-support.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-pfn-comparison.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-predictive-performance.csv
 M thesis-writing/logs/stage_5_2_table_values/T-results-robustness-summary.csv
 M thesis-writing/logs/stage_5_5A_full_resolution_pdf_review.csv
 M thesis-writing/logs/stage_5_5A_overfull_localization.csv
 M thesis-writing/logs/stage_5_5_consistency_audit.csv
 M thesis-writing/logs/stage_5_5_cross_reference_audit.csv
 M thesis-writing/logs/stage_5_5_frozen_content_snapshot.csv
 M thesis-writing/logs/stage_5_5_full_pdf_review.csv
 M thesis-writing/logs/stage_5_5_layout_warning_ledger.csv
 M thesis-writing/logs/stage_5_5_terminology_audit.csv
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

## Files inspected

- `prompt.txt`
- `thesis-writing/thesis/README.md`
- `thesis-writing/thesis/main.tex`
- `thesis-writing/thesis/latexmkrc`
- `thesis-writing/thesis/frontmatter/administrative_metadata.tex`
- `thesis-writing/thesis/frontmatter/abstract_primary.tex`
- `thesis-writing/thesis/frontmatter/abstract_secondary.tex`
- `thesis-writing/thesis/chapters/03_problem_definition_study_design.tex`
- `thesis-writing/thesis/chapters/05_proxy_state_construction.tex`
- `thesis-writing/thesis/chapters/07_causal_methodology.tex`
- `thesis-writing/thesis/chapters/10_results.tex`
- `thesis-writing/logs/stage_5_1_abstract_equivalence.csv`
- `thesis-writing/logs/stage_5_1_rq_contribution_matrix.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT.csv`
- `thesis-writing/logs/stage_5_2_figure_values/F-RESULT-DIRECTION-AGREEMENT-summary.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-forest-mimic.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-forest-physionet.csv`
- `thesis-writing/logs/stage_5_2_table_values/T-results-linear-comparison.csv`
- `thesis-writing/logs/stage_5_5_terminology_audit.csv`
- `thesis-writing/logs/stage_5_5A_overfull_localization.csv`
- `thesis-writing/logs/llm_methodology_integration_evidence_report.md`
- `thesis-writing/results/checked_cate_candidates.csv`
- `thesis-writing/thesis/main.log`
- `thesis-writing/thesis/main.pdf`, especially PDF page 2 (logical page `i`)

## Files changed

- `thesis-writing/logs/hebrew_abstract_repair.md` (this new report)

The Hebrew abstract, English abstract, preamble, administrative metadata, chapters, checked result files, figures, bibliography, tables, and research code were not changed by this task.

## Scientific verification gate

### Exact conflict

The approved replacement says:

> In PhysioNet 2012 a positive direction was obtained in all 19 comparisons, and in MIMIC-III in 18 of 19.

The checked artifacts instead establish:

- MIMIC-III contains 9 original-cohort proxy-state comparisons, and the primary `CausalForestDML` estimate is positive for 9 of 9.
- PhysioNet 2012 contains 10 original-cohort proxy-state comparisons, and the primary `CausalForestDML` estimate is positive for 9 of 10; `LAT_SHOCK` is negative (`-0.013849200594340203`).
- `CausalForestDML` and `LinearDML` agree in direction in all 19 cross-dataset dataset--exposure comparisons.
- All three estimators (`CausalForestDML`, `LinearDML`, and exploratory `CausalPFN`) agree in direction in 18 of those 19 cross-dataset comparisons. The sole disagreement is PhysioNet `LAT_SHOCK`, for which the two DML estimates are negative and `CausalPFN` is positive.

Primary verification sources:

- `stage_5_1_abstract_equivalence.csv`, rows `AE07`--`AE11`: 9/9 MIMIC positive, 9/10 PhysioNet positive, 19/19 DML direction agreement, and 18/19 three-estimator direction agreement.
- `F-RESULT-DIRECTION-AGREEMENT.csv`: all 19 exact joined rows and signs, including the PhysioNet-shock exception.
- `F-RESULT-DIRECTION-AGREEMENT-summary.csv`: MIMIC concordant 9, PhysioNet concordant 9 and discordant 1, total concordant 18 of 19.
- `T-results-forest-mimic.csv` and `T-results-forest-physionet.csv`: checked primary means, including negative PhysioNet shock.
- `checked_cate_candidates.csv`: source-level exact original-cohort estimator values.
- `chapters/10_results.tex`, result prose and the direction-agreement figure caption, which use the same checked values.

The relevant current artifacts and their `HEAD` versions agree on these counts, so the conflict is not caused by the pre-existing dirty state of those paths.

### Supported wording

The checked evidence supports the following result wording already used by the English abstract:

> For the primary original-cohort CausalForestDML summaries, all nine MIMIC-III proxy-state summaries were positive; nine of ten PhysioNet summaries were positive, with shock negative. CausalForestDML and LinearDML agreed in direction in all 19 original-cohort dataset--exposure comparisons. All three estimators agreed in direction in 18 of 19 comparisons.

The approved Hebrew replacement may not be installed unchanged unless the author confirms a scientifically supported correction to its result paragraph.

### Language-model/DAG statement

The assisting-tool description is supported with the qualifications present in the approved text. `chapters/05_proxy_state_construction.tex` records dataset-specific prompt/run artifacts as candidate design proposals, and `chapters/07_causal_methodology.tex` states that graph structure was informed by LLM-assisted design elicitation while active source code remains implementation authority. `llm_methodology_integration_evidence_report.md` likewise describes the graphs as LLM-assisted and project-specified, not discovered from patient data or validated by the LLM. Expert review and complete accepted/rejected decision provenance remain incomplete.

### Additional Hebrew--English claim mismatch

The approved Hebrew body names six predictive families by adding `Interpolation-Prediction Networks`. The checked abstract-equivalence record and thesis describe five evaluated families: STraTS, GRU, GRU-D, TCN, and SAnD. The archived causal input is more specific than the approved wording: one rule-derived source plus predicted-label sources from GRU, GRU-D, STraTS, and TCN; SAnD is not one of the archived final voters. The approved Hebrew text also omits the English abstract's primary/secondary/exploratory estimator hierarchy. Therefore claim equivalence is not established even apart from the incorrect result counts.

## Baseline RTL, font, and overflow diagnosis

- Font/language stack: XeLaTeX, `fontspec`, and `polyglossia`; English is the main language, Hebrew is configured as the other language, and the project-approved Hebrew font is `FreeSerif` with `Script=Hebrew`.
- Bidi mechanism: the body is in `\begin{hebrew}...\end{hebrew}`, and Latin fragments use `\textenglish{...}`. This provides real RTL body direction and LTR Latin runs.
- Heading defect: `\chapter*{\texthebrew{תקציר}}` occurs before the Hebrew environment begins. It therefore uses the English/LTR chapter layout and appears at the left instead of being positioned as an RTL heading.
- Alignment defect: the Hebrew environment retains TeX's fully justified paragraph setting. The baseline is RTL but visually justified, rather than cleanly right aligned with a ragged left edge.
- Overflow cause: long `\textenglish{...}` fragments are directionally isolated and locally unbreakable. In the result paragraph, the mixed `MIMIC-III`/Hebrew/`CausalForestDML` line cannot be broken safely under full justification. XeLaTeX reports `Overfull \hbox (49.17816pt too wide)` at abstract lines 9--10.
- Bounding-box confirmation: on PDF page 2, normal text reaches `xMax=538.583 pt`, while the displaced `III` reaches `xMax=587.577 pt`, approximately 49 pt beyond the intended right text margin. The PDF extraction and 300-DPI render also show `MIMIC-` and `III` separated across visual lines.
- The font itself contains the needed Hebrew glyphs; no missing-Hebrew-glyph warning was found in the baseline log. The defect is heading direction, paragraph alignment, and mixed-direction line breaking, not absence of Hebrew font support.

The smallest likely repair, after content confirmation, is local to `abstract_secondary.tex`: place the heading in RTL context, use right alignment with a ragged left edge for the abstract only, and wrap every Latin token with the existing `\textenglish` mechanism while adding safe break opportunities only inside unusually long Latin identifiers. No thesis-wide font or language change is indicated by the baseline evidence.

## Build and visual validation

- Documented clean command: `latexmk -C && latexmk -xelatex main.tex`, run from `thesis-writing/thesis/`.
- Post-change build result: not run, because the mandatory content gate stopped the replacement before a buildable task change existed.
- Baseline PDF: 118 A4 pages; the Hebrew abstract is PDF page 2, logical Roman page `i`.
- Baseline render: PDF page 2 was rendered individually at 300 DPI (`2481 x 3508`) and inspected full-size.
- Baseline visual result: Hebrew glyphs are readable and the body runs RTL, but the heading is left-positioned, the body is fully justified, and the `MIMIC-III` result line has visible bidi/overflow corruption. The page number is present and no vertical clipping was observed.
- Adjacent pages: baseline PDF page 1 is the English title page and page 3 is the English abstract. No task edit changed ordering or pagination.
- Affected-page warning result: the baseline contains one material overfull box of 49.17816 pt at Hebrew abstract lines 9--10. No post-repair warning result exists while the content gate is unresolved.
- Unresolved references introduced by this task: none; no TeX source was changed.

## Word count

The approved plain-text Hebrew abstract contains 369 whitespace-delimited tokens. Method: extract the lines strictly between the approved-abstract markers in `prompt.txt` and sum each line's `NF` using `awk`. This is below the 500-word ceiling, but it is a count of the blocked proposed text, not of a compiled replacement.

## Unresolved issues

1. Author confirmation is required for scientifically supported result wording. The two approved dataset-specific counts cannot be retained as written.
2. Author confirmation is required for the predictive-family/voter-lineage mismatch (`Interpolation-Prediction Networks` and the exact majority-vote inputs).
3. The local RTL/alignment/line-breaking repair and all post-change build, warning, page-margin, clipping, adjacency, and equivalence checks remain pending until the content gate is resolved.

BLOCKED FOR CONTENT CONFIRMATION — the approved result paragraph mislabels cross-dataset estimator-agreement counts as dataset-specific positive-effect counts, and the approved model/voter description conflicts with the checked thesis lineage.
