#!/usr/bin/env python3
"""Apply the Stage 4.6A-R author decisions without changing checked values."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "thesis-writing" / "results"
LOGS = ROOT / "thesis-writing" / "logs"
FIGURES = ROOT / "thesis-writing" / "figures-options"
PPTX = ROOT / "thesis-writing" / "prompts-and-documents" / "true_final_thesis_engineering_seminar_unified_redesign.pptx"

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def png_size(path: Path) -> tuple[int, int]:
    raw = path.read_bytes()[:24]
    assert raw[:8] == b"\x89PNG\r\n\x1a\n", path
    return int.from_bytes(raw[16:20], "big"), int.from_bytes(raw[20:24], "big")

def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv(path: Path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

def add_or_update_selection(filename: str, selector):
    path = OUT / filename
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    if "selection_status" not in fields:
        fields.append("selection_status")
    protected = [dict(row) for row in rows]
    for row in rows:
        row["selection_status"] = selector(row)
    # This repair may only add selection metadata; every pre-existing cell must remain exact.
    for before, after in zip(protected, rows, strict=True):
        assert all(before[k] == after[k] for k in before if k != "selection_status"), filename
    write_csv(path, fields, rows)
    return rows

def add_constant_metadata(filename: str, column: str, value: str):
    path = OUT / filename
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    if column not in fields:
        fields.append(column)
    for row in rows:
        row[column] = value
    write_csv(path, fields, rows)

def main():
    cate_path = OUT / "checked_cate_candidates.csv"
    cate_rows = read_csv(cate_path)
    original = [r for r in cate_rows if r["sampling_condition"] == "original"]
    direction = {}
    for row in original:
        direction.setdefault((row["dataset"], row["treatment"]), []).append(float(row["mean_cate"]))
    assert len(direction) == 19
    concordant = {key: values for key, values in direction.items() if len({x > 0 for x in values}) == 1}
    assert len(concordant) == 18
    assert len([key for key in direction if key[0] == "mimic"]) == 9
    assert len([key for key in concordant if key[0] == "mimic"]) == 9
    assert len([key for key in direction if key[0] == "physionet"]) == 10
    assert len([key for key in concordant if key[0] == "physionet"]) == 9
    shock = direction[("physionet", "LAT_SHOCK")]
    assert sum(x < 0 for x in shock) == 2 and sum(x > 0 for x in shock) == 1

    # Freeze all checked-table selection labels; no source, numerical, row-order, or row-count field changes occur.
    add_or_update_selection("checked_predictive_metrics.csv", lambda r: (
        "EXCLUDED_FROM_THESIS_PIPELINE" if r.get("model") == "interpnet" else
        "PRIMARY_MAIN_TEXT" if r.get("metric_split") == "test" else "SUPPORTING_APPENDIX"))
    add_or_update_selection("checked_predictive_exports.csv", lambda r: "SUPPORTING_APPENDIX")
    add_or_update_selection("checked_cate_candidates.csv", lambda r: (
        "ROBUSTNESS_APPENDIX" if r["sampling_condition"] == "outcome-downsampled" else
        "PRIMARY_MAIN_TEXT" if r["estimator"] == "CausalForestDML" else
        "SECONDARY_MAIN_TEXT" if r["estimator"] == "LinearDML" else
        "EXPLORATORY_MAIN_TEXT" if r["estimator"] == "CausalPFN" else "UNSELECTED"))
    add_constant_metadata("checked_cate_candidates.csv", "normalized_cate_selection_status", "OMIT_FROM_CHAPTER_10_MAIN_TEXT")
    # The existing checked matching table is deliberately cross-run-consistent,
    # not one row per estimator.  Keep its 30 rows intact and make its composite
    # original-run hierarchy explicit rather than inventing estimator rows.
    add_or_update_selection("checked_matching_results.csv", lambda r: (
        "ROBUSTNESS_APPENDIX" if r["sampling_condition"] == "outcome-downsampled" else
        "SUPPORTING_MAIN_TEXT[CausalForestDML];SECONDARY_APPENDIX[LinearDML];EXPLORATORY_APPENDIX[CausalPFN]"))
    add_or_update_selection("checked_matching_failures.csv", lambda r: "ROBUSTNESS_APPENDIX" if r["sampling_condition"] == "outcome-downsampled" else "SUPPORTING_APPENDIX")
    add_or_update_selection("checked_sensitivity_candidates.csv", lambda r: (
        "NOT_APPLICABLE" if r["estimator"] == "CausalPFN" else
        "ROBUSTNESS_APPENDIX" if r["sampling_condition"] == "outcome-downsampled" else "SUPPORTING_APPENDIX"))
    add_or_update_selection("checked_permutation_candidates.csv", lambda r: (
        "NOT_APPLICABLE" if r["estimator"] == "CausalPFN" else
        "ROBUSTNESS_APPENDIX" if r["sampling_condition"] == "outcome-downsampled" else "SUPPORTING_APPENDIX"))
    for name in ("checked_proxy_prevalence.csv", "checked_proxy_cooccurrence.csv", "checked_proxy_mortality_association.csv", "checked_mortality_prediction.csv"):
        add_or_update_selection(name, lambda r: "SUPPORTING_APPENDIX")

    # Existing candidate rows are retained and the 16 new optional figures are appended.
    fig_path = OUT / "checked_figure_candidates.csv"
    with fig_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); fig_fields = list(reader.fieldnames or []); fig_rows = list(reader)
    fig_rows = [row for row in fig_rows if not row.get("figure_id", "").startswith("OPTION-")]
    figure_map = {
        "mimic_non_downsampled_cate_ranking.png": ("MAIN_RESULTS", "BLOCKED_VALUE_CONFLICT", "checked_cate_candidates.csv", "BLOCKED_VALUE_CONFLICT", "All nine exposures are shown, but displayed labels equal the two-DML average rather than the image-labelled median across all three estimators."),
        "physionet_non_downsampled_cate_ranking.png": ("MAIN_RESULTS", "BLOCKED_VALUE_CONFLICT", "checked_cate_candidates.csv", "BLOCKED_VALUE_CONFLICT", "All ten exposures are shown, but displayed labels equal the two-DML average rather than the image-labelled median across all three estimators."),
        "cross_model_direction_counts.png": ("MAIN_RESULTS", "BLOCKED_VALUE_CONFLICT", "checked_cate_candidates.csv", "BLOCKED_VALUE_CONFLICT", "Image visibly aggregates all sampling modes and does not present the required original-cohort 18-of-19 comparison."),
        "mimic_all_run_stability.png": ("APPENDIX", "SUPPORTING_APPENDIX", "checked_cate_candidates.csv", "VALIDATED_SOURCE_ROUNDED", "Separates original and outcome-downsampled bars; descriptive stability display."),
        "physionet_all_run_stability.png": ("APPENDIX", "SUPPORTING_APPENDIX", "checked_cate_candidates.csv", "VALIDATED_SOURCE_ROUNDED", "Separates original and outcome-downsampled bars; descriptive stability display."),
        "mortality_prediction_true_auroc_auprc.png": ("APPENDIX", "SUPPORTING_APPENDIX", "checked_mortality_prediction.csv", "VALIDATED_SOURCE_ROUNDED", "Test AUROC/AUPRC from archived proxy-state mortality-prediction text; predictive association only."),
        "permutation_null_check.png": ("APPENDIX", "SUPPORTING_APPENDIX", "checked_permutation_candidates.csv", "VALIDATED_SOURCE_ROUNDED", "Aggregate permutation sanity diagnostic; not identification proof."),
        "sensitivity_intervals.png": ("APPENDIX", "SUPPORTING_APPENDIX", "checked_sensitivity_candidates.csv", "VALIDATED_SOURCE_ROUNDED", "Interval display retains archived diagnostic source limitations; does not validate the DAG or eliminate confounding."),
        "shock_rule_tree.png": ("APPENDIX", "SUPPORTING_APPENDIX", "checked_proxy_prevalence.csv", "NOT_NUMERICAL_ILLUSTRATION", "One illustrative proxy-rule example, not clinical validation."),
        "icu_scattered_events.png": ("METHODS_BACKGROUND_LATER", "RETAIN_LATER_METHODS_BACKGROUND", "none", "NOT_NUMERICAL_ILLUSTRATION", "Do not insert during this repair."),
        "latent_state_tags.png": ("METHODS_BACKGROUND_LATER", "RETAIN_LATER_METHODS_BACKGROUND", "none", "NOT_NUMERICAL_ILLUSTRATION", "Do not insert during this repair."),
        "majority_vote_tag_cleaning.png": ("METHODS_BACKGROUND_LATER", "RETAIN_LATER_METHODS_BACKGROUND", "none", "NOT_NUMERICAL_ILLUSTRATION", "Do not insert during this repair."),
        "causal_dag_overview.png": ("EXCLUDED", "EXCLUDED_FROM_THESIS", "none", "NOT_SELECTED", "Redundant with verified dataset-specific DAGs."),
        "correlation_vs_causation.png": ("EXCLUDED", "EXCLUDED_FROM_THESIS", "none", "NOT_SELECTED", "Generic rather than project-specific."),
        "mortality_prediction_metrics.png": ("EXCLUDED", "EXCLUDED_FROM_THESIS", "checked_mortality_prediction.csv", "NOT_SELECTED", "Superseded by corrected AUROC/AUPRC figure."),
        "sensitivity_intervals_trimmed.png": ("EXCLUDED", "EXCLUDED_FROM_THESIS", "checked_sensitivity_candidates.csv", "NOT_SELECTED", "Truncated visual range risks selective emphasis."),
    }
    assert {p.name for p in FIGURES.glob("*.png")} == set(figure_map)
    for name, (role, selection, source, validation, note) in sorted(figure_map.items()):
        path = FIGURES / name; width, height = png_size(path)
        fig_rows.append({"figure_id": f"OPTION-{name.removesuffix('.png').upper()}", "dataset": "mimic" if name.startswith("mimic") else "physionet" if name.startswith("physionet") else "cross-dataset", "source_path": rel(path), "source_sha256": sha(path), "width": width, "height": height, "input_source": source, "source_status": "OPTIONAL_FIGURE_ARCHIVED", "selection_status": selection, "admission_status": "BLOCKED_VALUE_CONFLICT" if validation == "BLOCKED_VALUE_CONFLICT" else "ADMISSIBLE_WITH_QUALIFICATIONS" if role != "EXCLUDED" else "EXCLUDED_LEGACY", "caveat_codes": validation, "notes": f"role={role}; {note}"})
    write_csv(fig_path, fig_fields, fig_rows)

    # Append the optional-figure and seminar contextual-provenance rows to the manifest.
    manifest_path = OUT / "results_manifest.csv"
    with manifest_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); manifest_fields = list(reader.fieldnames or []); manifest_rows = list(reader)
    existing_paths = {r["relative_path"] for r in manifest_rows}
    existing_by_path = {r["relative_path"]: r for r in manifest_rows}
    next_id = max(int(r["artifact_id"].split("-")[-1]) for r in manifest_rows) + 1
    for name, (role, selection, source, validation, note) in sorted(figure_map.items()):
        path = FIGURES / name
        width, height = png_size(path)
        update = {"result_family": "optional_figure", "planned_chapter_section": "Chapter 10" if role == "MAIN_RESULTS" else "Appendix" if role == "APPENDIX" else "Methods/background later" if role.startswith("METHODS") else "Excluded", "pipeline": "thesis_figure_option", "artifact_role": role.lower(), "relative_path": rel(path), "file_type": "png", "file_size_bytes": path.stat().st_size, "sha256": sha(path), "image_width": width, "image_height": height, "producing_stage": "optional figure archive", "source_commit": "da200b7", "source_commit_status": "ARCHIVE_COMMIT_CONFIRMED", "input_provenance_status": "ARTIFACT_SUPPORTED", "execution_status": "archived", "artifact_status": "present", "admission_status": "BLOCKED_VALUE_CONFLICT" if validation == "BLOCKED_VALUE_CONFLICT" else "ADMISSIBLE_WITH_QUALIFICATIONS" if role != "EXCLUDED" else "EXCLUDED_LEGACY", "provenance_class": "ARTIFACT_SUPPORTED", "caveat_codes": validation, "human_decision_required": "False", "notes": f"selection_status={selection}; checked_source={source}; {note}"}
        if rel(path) not in existing_paths:
            update["artifact_id"] = f"ART-{next_id:05d}"
            manifest_rows.append(update)
            next_id += 1
        else:
            existing_by_path[rel(path)].update(update)
    if PPTX.exists() and rel(PPTX) not in existing_paths:
        manifest_rows.append({"artifact_id": f"ART-{next_id:05d}", "result_family": "contextual_figure_provenance", "planned_chapter_section": "", "pipeline": "seminar_context", "artifact_role": "contextual_only", "relative_path": rel(PPTX), "file_type": "pptx", "file_size_bytes": PPTX.stat().st_size, "sha256": sha(PPTX), "column_names_or_schema_signature": "PowerPoint; not used as numerical authority", "source_commit": "da200b7", "source_commit_status": "ARCHIVE_COMMIT_CONFIRMED", "input_provenance_status": "CONTEXTUAL_ONLY", "artifact_status": "present", "admission_status": "NOT_APPLICABLE", "provenance_class": "ARTIFACT_SUPPORTED", "caveat_codes": "NOT_NUMERICAL_AUTHORITY", "human_decision_required": "False", "notes": "Contextual seminar provenance only; checked CSVs govern numerical claims."})
    write_csv(manifest_path, manifest_fields, manifest_rows)

    figure_lines = ["# Optional-Figure Selection Register", "", "All PNGs were visually inspected and SHA-256 hashed. Checked CSVs, not the seminar presentation, remain the numerical authority.", "", "| File | SHA-256 | Dimensions | Type | Checked source | Validation | Author decision | Placement | Caption boundary / limitation |", "|---|---|---:|---|---|---|---|---|---|"]
    for name, (role, selection, source, validation, note) in sorted(figure_map.items()):
        path = FIGURES / name; width, height = png_size(path)
        boundary = ("Use mean model-estimated CATE over the analyzed sample; never normalized CATE." if "ranking" in name else "Use only with its recorded diagnostic/illustrative limitation.")
        figure_lines.append(f"| `{name}` | `{sha(path)}` | {width}×{height} | {role} | `{source}` | {validation} | {selection} | {role} | {boundary} {note} |")
    figure_lines += ["", "## Explicit validation notes", "", "- Both ranking figures use original-cohort rows and show every prespecified exposure, but their displayed labels equal the two-DML average rather than the image-labelled median across all three estimators. Both are **BLOCKED_VALUE_CONFLICT** and must not be inserted without a separately approved replacement.", "- The author-selected `cross_model_direction_counts.png` is **BLOCKED_VALUE_CONFLICT**: it visibly aggregates all sampling modes, whereas the approved statement is based only on original-cohort rows. It must not be inserted or used to support that statement without a separately approved replacement.", "- The checked original-cohort rows reproduce 18 of 19 directionally concordant dataset--exposure comparisons: MIMIC 9/9; PhysioNet 9/10; the exception is `LAT_SHOCK` (CausalForestDML and LinearDML negative, CausalPFN slightly positive).", "- `true_final_thesis_engineering_seminar_unified_redesign.pptx` is contextual provenance only and is not a numerical source."]
    (OUT / "figure_selection_register.md").write_text("\n".join(figure_lines) + "\n", encoding="utf-8")

    decisions = """# Stage 4.6A-R Results Decision Register

## Decision freeze

**AUTHOR DECISION RECORDED.** Supervisor ratification remains pending. These choices were not made from effect magnitude, direction, apparent significance, estimator agreement, or post-hoc clinical interest.

- Primary population: original causal-analysis cohorts. Outcome-downsampled analyses are robustness/sensitivity material only, belong in supplementary material, and are never pooled with original analyses.
- Estimator hierarchy: CausalForestDML primary; LinearDML secondary; CausalPFN exploratory and included after LinearDML.
- Exposure policy: report every prespecified dataset-specific proxy-state exposure from original-cohort runs.
- Required wording: **descriptive matched-pair outcome difference** and **mean model-estimated CATE over the analyzed sample**. Omit normalized CATE from Chapter 10.
- Cross-dataset policy: qualitative/aligned-concept comparison only; no pooling. Original causal-analysis populations are MIMIC 26,845 and PhysioNet 7,993 records (difference 18,852; MIMIC approximately 3.36 times larger). These are not raw cohort totals.

## Frozen Chapter 10 order

1. Analysis-population counts
2. Predictive performance
3. Primary CausalForestDML results
4. Matching and empirical support
5. LinearDML comparison
6. CausalPFN exploratory results
7. Cross-dataset comparison
8. Robustness and sensitivity

Downsampling is addressed only within the final robustness section.

## Estimator agreement

The three estimators agree in mean-effect direction for 18 of 19 dataset--exposure comparisons: MIMIC 9 of 9 and PhysioNet 9 of 10. The exception is PhysioNet `LAT_SHOCK`: CausalForestDML and LinearDML are negative and CausalPFN is slightly positive.

CausalPFN reproduced the prevailing direction in nearly every comparison, supporting its promise as a complementary estimator within this pipeline. This broad agreement is not complete agreement and does not establish estimator equivalence, superiority, causal validity, or interchangeable uncertainty quantification. CausalPFN lacks the archived downstream sensitivity and permutation diagnostics available for the DML estimators.

## InterpNet

**NOT PART OF THE THESIS PIPELINE — EXCLUDED FROM THESIS.** Stage 4.6B must ignore historical audit and literature references to InterpNet.

## Former decision records

DEC-RESULT-001 through DEC-RESULT-016 are superseded by this author decision freeze where applicable; their evidence limitations remain in the manifest, source packet, and deferred-fix register.
"""
    (OUT / "results_decision_register.md").write_text(decisions, encoding="utf-8")

    source_packet = """# Stage 4.6A-R Results Source Packet

This packet is for Stage 4.6B. Use the checked CSVs and this frozen hierarchy; do not use historical InterpNet references in audit or literature files.

## Frozen hierarchy and population boundary

- Primary original causal-analysis populations: MIMIC 26,845 records; PhysioNet 7,993 records; difference 18,852; MIMIC is approximately 3.36 times larger. These are original causal-analysis population counts, not raw cohort totals.
- Original and outcome-downsampled results must never be pooled. Downsampled material is robustness/supplementary only.
- CausalForestDML is primary, LinearDML secondary, and CausalPFN exploratory. Report every prespecified original-cohort proxy-state exposure.
- Use **descriptive matched-pair outcome difference** and **mean model-estimated CATE over the analyzed sample**. Do not use normalized CATE in Chapter 10.

## Approved Chapter 10 order

1. Analysis-population counts (`checked_cohort_candidates.csv`)
2. Predictive performance (`checked_predictive_metrics.csv`)
3. Primary CausalForestDML (`checked_cate_candidates.csv`)
4. Matching and empirical support (`checked_matching_results.csv`, `checked_matching_failures.csv`)
5. LinearDML comparison (`checked_cate_candidates.csv`)
6. CausalPFN exploratory results (`checked_cate_candidates.csv`)
7. Cross-dataset comparison (`checked_cate_candidates.csv`)
8. Robustness and sensitivity (`checked_sensitivity_candidates.csv`, `checked_permutation_candidates.csv`)

## Direction agreement

Original-cohort rows support 18 of 19 directionally concordant dataset--exposure comparisons (MIMIC 9/9; PhysioNet 9/10). PhysioNet `LAT_SHOCK` is the exception: CausalForestDML and LinearDML negative; CausalPFN slightly positive. This does not establish estimator equivalence, superiority, causal validity, or interchangeable uncertainty quantification. CausalPFN has no archived downstream sensitivity/permutation diagnostics.

## Figure gate

Use `figure_selection_register.md`. Both original-cohort ranking figures are blocked because their labels are two-DML averages rather than the image-labelled median across all three estimators. `cross_model_direction_counts.png` is also blocked because it aggregates both sampling modes and must not support the 18-of-19 statement. Appendix selections retain their stated diagnostic or illustrative boundaries.

## Persisting limitations

Missing numbered configs, ignored archive-copy history, missing producing commits, predictive split/checkpoint lineage, raw cohort totals, missing PhysioNet proxy tables, overlap diagnostics, proxy clinical validation, and LLM prompt-execution provenance remain open.
"""
    (OUT / "results_source_packet.md").write_text(source_packet, encoding="utf-8")

    manifest_md = """# Stage 4.6A-R Results Manifest

The package inventories 1,369 archived result artifacts plus the 16 optional PNGs and one contextual seminar presentation. All have repository-relative paths and SHA-256 entries in `results_checksums.sha256`.

## Author decision freeze

**AUTHOR DECISION RECORDED; supervisor ratification remains pending.** Original cohorts are primary; outcome-downsampled analyses are robustness/supplementary only and are never pooled. CausalForestDML is primary, LinearDML secondary, and CausalPFN exploratory. Every prespecified original-cohort dataset-specific exposure is reported. Normalized CATE is omitted from Chapter 10.

## Predictive scope

The thesis predictive comparison contains exactly STraTS, GRU, GRU-D, TCN, and SAnD. **InterpNet is not part of the thesis pipeline and is excluded from the thesis.** Historical audit/literature records are not source-packet instructions.

## Direction agreement

Original-cohort checked CATE rows yield 18/19 concordant dataset--exposure comparisons: MIMIC 9/9 and PhysioNet 9/10. PhysioNet `LAT_SHOCK` is the exception (CausalForestDML and LinearDML negative; CausalPFN slightly positive). This is bounded directional agreement only; it does not establish equivalence, superiority, causal validity, or interchangeable uncertainty quantification.

## Optional figures

`figure_selection_register.md` classifies all 16 PNGs. Both original-cohort ranking figures are blocked because their labels conflict with their stated three-estimator median scale. `cross_model_direction_counts.png` is blocked because it mixes sampling modes; no replacement was generated. The seminar PowerPoint is contextual provenance only, never numerical authority.

## Readiness

BLOCKED: ALL THREE AUTHOR-SELECTED MAIN NUMERICAL FIGURES HAVE SOURCE-VALUE OR SAMPLING CONFLICTS. SUPERVISOR RATIFICATION OF THE RESULTS HIERARCHY REMAINS PENDING.
"""
    (OUT / "results_manifest.md").write_text(manifest_md, encoding="utf-8")

    report = """# Stage 4.6A-R Repair Report

## Repository verification

- Verified `da200b7 adding figures` with parent `b4b1212 step 4.6A`.
- Confirmed the Stage 4.6A checked package exists, `thesis-writing/figures-options/` contains 16 PNGs, Chapter 10 remains undrafted, and the prior decision-freeze had not been applied.

## Author decisions recorded

- Original population primary; outcome-downsampled analyses robustness/supplementary only.
- CausalForestDML primary; LinearDML secondary; CausalPFN exploratory.
- All prespecified original-cohort exposures retained; no post-hoc exposure selection.
- Approved effect wording and normalized-CATE omission recorded.
- Cross-dataset comparison is qualitative/aligned only. Original causal-analysis populations: MIMIC 26,845; PhysioNet 7,993; difference 18,852; MIMIC approximately 3.36 times larger.

## CATE direction validation

- Directly reproduced original-cohort concordance: 18/19 overall, MIMIC 9/9, PhysioNet 9/10.
- PhysioNet `LAT_SHOCK` is the exception: CausalForestDML and LinearDML negative; CausalPFN slightly positive.
- CausalPFN remains exploratory, not failed; its missing archived downstream sensitivity/permutation diagnostics remain explicit.

## InterpNet removal

- Removed every InterpNet occurrence from thesis `.tex` files and removed it from the predictive model/experiment tables. The thesis predictive comparison now has exactly STraTS, GRU, GRU-D, TCN, and SAnD.

## Figure audit

- Inspected and hashed all 16 optional PNGs; see `figure_selection_register.md`.
- Both original-cohort ranking figures are `BLOCKED_VALUE_CONFLICT`: their labels equal two-DML averages rather than their stated three-estimator median scale, although all prespecified exposures are present.
- `cross_model_direction_counts.png` is `BLOCKED_VALUE_CONFLICT`: it visibly aggregates original and downsampled rows and does not support the required 18-of-19 original-cohort statement. No blocked figure was altered or replaced.

## Checked-table and checksum validation

- Added selection-status metadata only; no existing numerical field, source path/hash, row count, or row order was changed.
- Updated manifest/checksum coverage for the 16 PNGs and contextual seminar presentation.

## Build

- Ran `latexmk -C && latexmk -xelatex main.tex`; `main.pdf` was produced successfully (79 A4 pages). Existing citation and layout warnings remain non-blocking and are not treated as new evidence.

## Readiness

BLOCKED: ALL THREE AUTHOR-SELECTED MAIN NUMERICAL FIGURES HAVE SOURCE-VALUE OR SAMPLING CONFLICTS.

SUPERVISOR RATIFICATION OF THE RESULTS HIERARCHY REMAINS PENDING.
"""
    (LOGS / "stage_4_6A_repair_report.md").write_text(report, encoding="utf-8")

    # Regenerate checksums for all final manifest sources and all human-readable/checked outputs.
    manifest_rows = read_csv(manifest_path)
    source_paths = sorted({ROOT / r["relative_path"] for r in manifest_rows if r.get("relative_path")})
    assert all(p.is_file() for p in source_paths)
    generated = sorted(p for p in OUT.iterdir() if p.is_file() and p.name not in {"results_checksums.sha256", Path(__file__).name})
    generated += [LOGS / "stage_4_6A_evidence_report.md", LOGS / "stage_4_6A_repair_report.md"]
    with (OUT / "results_checksums.sha256").open("w", encoding="utf-8") as f:
        for path in sorted(set(generated + source_paths)):
            f.write(f"{sha(path)}  {rel(path)}\n")

if __name__ == "__main__":
    main()
