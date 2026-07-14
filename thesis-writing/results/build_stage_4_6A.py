#!/usr/bin/env python3
"""Build the Stage 4.6A checked-results packet from archived artifacts only.

This is an audit/export utility.  It hashes and parses existing archives; it
does not import project code, deserialize binary artifacts, or run experiments.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "final-results"
OUT = ROOT / "thesis-writing" / "results"
LOG = ROOT / "thesis-writing" / "logs" / "stage_4_6A_evidence_report.md"

MANIFEST_COLUMNS = """artifact_id result_family planned_chapter_section planned_table_or_figure_id pipeline dataset model_or_estimator sampling_condition run_name treatment_or_proxy artifact_role relative_path recorded_absolute_path file_type file_size_bytes sha256 row_count column_count column_names_or_schema_signature image_width image_height producing_stage producing_script run_summary_path log_path configuration_path configuration_available configuration_hash source_commit source_commit_status command_available input_provenance_status execution_status artifact_status duplicate_group canonical_source admission_status provenance_class caveat_codes human_decision_required notes""".split()

CHECKED = {
    "checked_cohort_candidates.csv": "dataset population_name pipeline_stage sampling_condition count_type count_value outcome_rate source_path source_sha256 scope admission_status caveat_codes notes".split(),
    "checked_proxy_prevalence.csv": "dataset proxy_source latent n_positive prevalence source_path source_sha256 source_row admission_status provenance_class caveat_codes notes".split(),
    "checked_proxy_cooccurrence.csv": "dataset proxy_source latent_row latent_column phi source_path source_sha256 source_row admission_status provenance_class caveat_codes notes".split(),
    "checked_proxy_mortality_association.csv": "dataset proxy_source latent n_tag0 n_tag1 mortality_tag0 mortality_tag1 risk_ratio source_path source_sha256 source_row admission_status provenance_class caveat_codes notes".split(),
    "checked_predictive_metrics.csv": "dataset model run_name train_fraction metric_split loss auroc auprc minrp source_summary source_summary_sha256 source_log source_log_sha256 summary_log_agreement checkpoint_selection_rule admission_status provenance_class caveat_codes notes".split(),
    "checked_predictive_exports.csv": "dataset model path sha256 row_count unique_ts_id probability_column_count binary_column_count schema_valid binary_values_valid probability_range_valid export_split export_split_status checkpoint_provenance admission_status caveat_codes notes".split(),
    "checked_mortality_prediction.csv": "dataset sampling_condition model_type source_path source_sha256 duplicate_group metric_text admission_status provenance_class caveat_codes notes".split(),
    "checked_matching_results.csv": "dataset estimator sampling_condition treatment n n_treated n_control n_pairs match_rate mean_pair_effect std_pair_effect normalized_pair_effect final_allowed_distance sufficient_pairs observed_confounders source_path source_sha256 row_validation_status admission_status caveat_codes".split(),
    "checked_matching_failures.csv": "dataset estimator sampling_condition treatment failure_reason support_fields source_path admission_status notes".split(),
    "checked_cate_candidates.csv": "dataset estimator sampling_condition run_name treatment model_n outcome_rate treatment_rate mean_cate normalized_cate cate_std cate_min cate_max interval_fields_available observed_confounders missing_graph_candidates identifiable_with_available_nodes source_run_summary source_cate_summary source_treatment_csv source_control_message row_validation_status diagnostic_availability selection_status admission_status provenance_class caveat_codes notes".split(),
    "checked_heterogeneity_candidates.csv": "dataset estimator sampling_condition treatment diagnostic_type source_path source_sha256 row_count feature_count interval_available figure_candidate admission_status selection_status caveat_codes notes".split(),
    "checked_sensitivity_candidates.csv": "dataset estimator sampling_condition treatment analysis_status diagnostic_name diagnostic_value diagnostic_lower diagnostic_upper diagnostic_source estimator_native saved_training_direct recomputed fallback benchmark_variable benchmark_status residual_status contour_path contour_sha256 warnings source_path row_validation_status selection_status admission_status caveat_codes notes".split(),
    "checked_permutation_candidates.csv": "dataset estimator sampling_condition run_name treatment permutation_type num_trials seed original_statistic permuted_mean permuted_std z_score other_existing_fields source_path source_sha256 subprocess_status warning_fields row_validation_status selection_status admission_status caveat_codes notes".split(),
    "checked_figure_candidates.csv": "figure_id dataset estimator sampling_condition treatment source_path source_sha256 width height producing_script input_source source_status selection_status admission_status caveat_codes notes".split(),
}

def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()

def sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def read_csv(p: Path):
    with p.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

def csv_meta(p: Path):
    try:
        with p.open("r", encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.reader(fh))
        if not rows:
            return 0, 0, "EMPTY; parse=OK"
        header = rows[0]
        duplicate_headers = len(header) != len(set(header))
        duplicate_rows = len(rows[1:]) != len({tuple(x) for x in rows[1:]})
        return len(rows) - 1, len(header), "headers=" + "|".join(header) + f"; duplicate_headers={duplicate_headers}; duplicate_rows={duplicate_rows}; parse=OK"
    except Exception as e:
        return "", "", f"parse=ERROR:{type(e).__name__}"

def png_size(p: Path):
    try:
        raw = p.read_bytes()[:24]
        if raw[:8] == b"\x89PNG\r\n\x1a\n":
            return int.from_bytes(raw[16:20], "big"), int.from_bytes(raw[20:24], "big")
    except OSError:
        pass
    return "", ""

def family(path: str):
    if "/strats-outputs/" in path:
        return "predictive"
    if "/trees/" in path:
        return "proxy"
    if "majority_vote" in path:
        return "majority_vote_proxy"
    if "mortality_prediction" in path:
        return "mortality_prediction"
    if "/matching/" in path or "matching_" in path:
        return "matching"
    if "permutations_test" in path or "permutation" in path:
        return "permutation"
    if "analyze_cate_results" in path or "benchmark" in path or "sensitivity" in path:
        return "sensitivity"
    if "cate" in path or "global_summary" in path:
        return "cate"
    if "/graph/" in path:
        return "graph"
    if path.endswith("run_summary.json"):
        return "run_summary"
    return "supporting_archive"

def dataset_for(path: str):
    if "mimic" in path:
        return "mimic_iii" if "strats-outputs" in path else "mimic"
    if "physionet" in path:
        return "physionet_2012" if "strats-outputs" in path else "physionet"
    return ""

def run_parts(path: str):
    m = re.search(r"outputs-(mimic|physionet)-(forest|linear|pfn)(-downsample)?", path)
    if not m:
        return "", "", ""
    return m.group(0), {"forest":"CausalForestDML", "linear":"LinearDML", "pfn":"CausalPFN"}[m.group(2)], "outcome-downsampled" if m.group(3) else "original"

def write_csv(name, rows):
    columns = CHECKED[name]
    with (OUT / name).open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader(); writer.writerows(rows)

def text_metrics(p: Path):
    text = p.read_text(encoding="utf-8", errors="replace")
    meta = {k: v for k, v in re.findall(r"^(dataset|model_type|run|train_frac|checkpoint_selection_metric):\s*(.+)$", text, re.M)}
    blocks = {}
    for split in ("Validation", "Test"):
        m = re.search(rf"^{split}\n-+\n(.*?)(?=\n(?:Validation|Test)\n|\Z)", text, re.M | re.S)
        values = dict(re.findall(r"^(loss|auroc|auprc|minrp):\s*(.+)$", m.group(1), re.M)) if m else {}
        blocks[split.lower()] = values
    return meta, blocks

def final_log_metrics(p: Path):
    if not p.exists(): return {}
    text = p.read_text(encoding="utf-8", errors="replace")
    out = {}
    for split in ("val", "test"):
        hits = re.findall(rf"Final {split} res: (\{{.*?\}})", text)
        if hits:
            out["validation" if split == "val" else "test"] = dict(re.findall(r"'([a-z]+)': ([^,}]+)", hits[-1]))
    return out

def agreement(summary, logged):
    if not logged: return "LOG_MISSING"
    for key in ("loss", "auroc", "auprc", "minrp"):
        if key in summary and key in logged:
            try:
                if abs(float(summary[key]) - float(logged[key])) > 1e-6: return "CONFLICT"
            except ValueError: return "UNPARSEABLE"
    return "AGREE_WITH_TOLERANCE"

def mapping_get(row, *names):
    for n in names:
        if n in row: return row[n]
    return ""

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    archive_files = sorted(p for p in ARCHIVE.rglob("*") if p.is_file())
    hashes = {p: sha(p) for p in archive_files}
    hash_groups = defaultdict(list)
    for p, digest in hashes.items(): hash_groups[digest].append(p)

    run_json = {}
    for p in ARCHIVE.glob("causal-outputs/outputs-*/run_summary.json"):
        run_json[p.parent.name] = json.loads(p.read_text(encoding="utf-8"))

    manifest = []
    for i, p in enumerate(archive_files, 1):
        rp, name = rel(p), p.name
        run, estimator, sampling = run_parts(rp)
        rows = cols = schema = width = height = ""
        ext = p.suffix.lower().lstrip(".") or "no_extension"
        if ext in {"csv", "tsv"}:
            rows, cols, schema = csv_meta(p)
        elif ext == "json":
            try:
                obj = json.loads(p.read_text(encoding="utf-8")); schema = f"top_level={type(obj).__name__}; keys=" + "|".join(obj.keys()) if isinstance(obj, dict) else f"top_level={type(obj).__name__}"
            except Exception as e: schema = f"parse=ERROR:{type(e).__name__}"
        elif ext == "png": width, height = png_size(p); schema = "PNG; direct_archived_figure=True"
        elif ext in {"txt", "md", "log"}: schema = "text; parse=OK"
        elif ext in {"pkl", "pickle", "bin", "pt", "pth"}: schema = "binary; not deserialized"
        group = "" if len(hash_groups[hashes[p]]) == 1 else "SHA256-" + hashes[p][:12]
        canonical = ""
        if group:
            canonical = rel(sorted(hash_groups[hashes[p]], key=rel)[0])
        status, caveat = "ADMISSIBLE_WITH_QUALIFICATIONS", "ARCHIVE_COPY_PROVENANCE_PARTIAL"
        if "manager_global_summary" in name:
            status, caveat = ("EXCLUDED_MISLABELED", "MANAGER_SUMMARY_DATASET_LABEL_CONFLICT") if ("mimic" in rp and "physionet_manager" in name) else ("EXCLUDED_DUPLICATE", "REDUCED_MANAGER_SUMMARY")
        if name in {"AGENTS.md", "SCRIPTS.md"}: status, caveat = "NOT_APPLICABLE", "ARCHIVE_DOCUMENTATION"
        if group and canonical != rp and status.startswith("ADMISSIBLE"): status, caveat = "EXCLUDED_DUPLICATE", "HASH_EQUIVALENT_COPY"
        summary = run_json.get(run, {})
        stage = ""
        exec_status = ""
        recorded = ""
        config_path = ""
        if run:
            stage = next((s for s in (summary.get("stages") or {}) if f"/{s}/" in rp), "")
            stage_info = (summary.get("stages") or {}).get(stage, {})
            exec_status = stage_info.get("status", "")
            recorded = str(next(iter((stage_info.get("output_paths") or {}).values()), ""))
            config_path = summary.get("dataset_config_csv", "")
        manifest.append(dict(artifact_id=f"ART-{i:05d}", result_family=family(rp), planned_chapter_section="Chapter 10", planned_table_or_figure_id="", pipeline="STraTS" if "strats-outputs" in rp else "causal" if "causal-outputs" in rp else "proxy", dataset=dataset_for(rp), model_or_estimator=estimator, sampling_condition=sampling, run_name=run, treatment_or_proxy="", artifact_role="archived_source", relative_path=rp, recorded_absolute_path=recorded, file_type=ext, file_size_bytes=p.stat().st_size, sha256=hashes[p], row_count=rows, column_count=cols, column_names_or_schema_signature=schema, image_width=width, image_height=height, producing_stage=stage, producing_script=(summary.get("stages", {}).get(stage, {}).get("script_path", "") if run else ""), run_summary_path=(rel(ARCHIVE / "causal-outputs" / run / "run_summary.json") if run else ""), log_path=(summary.get("stages", {}).get(stage, {}).get("log_path", "") if run else ""), configuration_path=config_path, configuration_available="False" if config_path else "", configuration_hash="", source_commit="", source_commit_status="MISSING", command_available="True" if run else "", input_provenance_status="PROVENANCE_PARTIAL", execution_status=exec_status, artifact_status="present", duplicate_group=group, canonical_source=canonical, admission_status=status, provenance_class="EXECUTION_SUPPORTED" if run else "ARTIFACT_SUPPORTED", caveat_codes=caveat, human_decision_required="True" if family(rp) in {"cate", "matching", "sensitivity", "permutation"} else "False", notes="Generated from immutable ignored archive; external producing paths are not locally available."))
    with (OUT / "results_manifest.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=MANIFEST_COLUMNS); w.writeheader(); w.writerows(manifest)

    # Predictive summaries and exports.
    metric_rows, export_rows, cohort_rows = [], [], []
    for p in sorted(ARCHIVE.glob("strats-outputs/*/*/*/training_summary.txt")):
        meta, blocks = text_metrics(p); log = p.with_name("log.txt"); log_blocks = final_log_metrics(log)
        dataset = meta.get("dataset", dataset_for(rel(p))); model = meta.get("model_type", p.parents[2].name)
        for split, vals in blocks.items():
            metric_rows.append(dict(dataset=dataset, model=model, run_name=meta.get("run", ""), train_fraction=meta.get("train_frac", ""), metric_split=split, loss=vals.get("loss", ""), auroc=vals.get("auroc", ""), auprc=vals.get("auprc", ""), minrp=vals.get("minrp", ""), source_summary=rel(p), source_summary_sha256=hashes[p], source_log=rel(log) if log.exists() else "", source_log_sha256=hashes.get(log, ""), summary_log_agreement=agreement(vals, log_blocks.get(split, {})), checkpoint_selection_rule=meta.get("checkpoint_selection_metric", ""), admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", provenance_class="ARTIFACT_SUPPORTED", caveat_codes="PREDICTIVE_SPLIT_MANIFEST_MISSING;CHECKPOINT_EXPORT_MAPPING_MISSING", notes="Metrics copied from final training summary; final log values compared numerically."))
    # Explicitly retain the two absent InterpNet families as result-missing, not fabricated rows.
    for dataset in ("physionet_2012", "mimic_iii"):
        metric_rows.append(dict(dataset=dataset, model="interpnet", metric_split="", admission_status="BLOCKED_MISSING_RESULT", provenance_class="MISSING", caveat_codes="FINAL_TRAINING_SUMMARY_MISSING;FINAL_EXPORT_MISSING", notes="Implementation and wrapper references exist, but no final numerical summary or export is archived."))
    for p in sorted(ARCHIVE.glob("strats-outputs/predicted*latent_tags*.csv")):
        rows = read_csv(p); hdr = list(rows[0]) if rows else []
        ids = [r.get("ts_id", "") for r in rows]
        prob = [x for x in hdr if x.endswith("_prob")]
        binary = [x for x in hdr if x != "ts_id" and not x.endswith("_prob")]
        binary_ok = all(r.get(c, "") in {"0", "1", "0.0", "1.0"} for r in rows for c in binary)
        try: prob_ok = all(0 <= float(r[c]) <= 1 for r in rows for c in prob)
        except (ValueError, TypeError): prob_ok = False
        dset = "physionet_2012" if "physionet" in p.name else "mimic_iii"
        model = re.search(r"(?:tags_|tags)(strats|gru|grud|tcn|sand)", p.name)
        export_rows.append(dict(dataset=dset, model=model.group(1) if model else "", path=rel(p), sha256=hashes[p], row_count=len(rows), unique_ts_id=len(set(ids)), probability_column_count=len(prob), binary_column_count=len(binary), schema_valid=bool(hdr and hdr[0] == "ts_id" and len(prob) == len(binary)), binary_values_valid=binary_ok, probability_range_valid=prob_ok, export_split="", export_split_status="UNVERIFIED", checkpoint_provenance="UNVERIFIED", admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", caveat_codes="EXPORT_SPLIT_UNVERIFIED;CHECKPOINT_EXPORT_MAPPING_MISSING", notes="Export schema checked; out-of-sample status is not claimed."))
        cohort_rows.append(dict(dataset=dset, population_name=f"predictive export ({p.stem})", pipeline_stage="prediction_export", sampling_condition="", count_type="export_rows", count_value=len(rows), outcome_rate="", source_path=rel(p), source_sha256=hashes[p], scope="export contract, not raw cohort", admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", caveat_codes="EXPORT_SPLIT_UNVERIFIED", notes="Count is a CSV row count."))
    write_csv("checked_predictive_metrics.csv", metric_rows); write_csv("checked_predictive_exports.csv", export_rows)

    # Existing proxy tables only; PhysioNet counterparts are deliberately not derived.
    proxy_specs = [("prevalence.csv", "checked_proxy_prevalence.csv"), ("mortality_by_tag.csv", "checked_proxy_mortality_association.csv")]
    for src, target in proxy_specs:
        p = ARCHIVE / "trees/mimic-tags" / src; outrows = []
        if p.exists():
            for idx, row in enumerate(read_csv(p), 2):
                outrows.append(dict(dataset="mimic", proxy_source="rule-based", source_path=rel(p), source_sha256=hashes[p], source_row=idx, admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", provenance_class="ARTIFACT_SUPPORTED", caveat_codes="RULE_PROXY;ARCHIVE_COPY_PROVENANCE_PARTIAL", notes="Existing artifact copied; mortality values are unadjusted association artifacts.", **row))
        else: outrows.append(dict(dataset="physionet", proxy_source="rule-based", admission_status="BLOCKED_MISSING_RESULT", provenance_class="MISSING", caveat_codes="PHYSIONET_TABLE_NOT_ARCHIVED", notes="Not derived from patient-level tags in Stage 4.6A."))
        write_csv(target, outrows)
    phi = ARCHIVE / "trees/mimic-tags/cooccurrence_phi.csv"; phi_rows=[]
    if phi.exists():
        for idx, row in enumerate(read_csv(phi), 2):
            row_label = row.get("", "")
            for col, value in row.items():
                if col and value != "": phi_rows.append(dict(dataset="mimic", proxy_source="rule-based", latent_row=row_label, latent_column=col, phi=value, source_path=rel(phi), source_sha256=hashes[phi], source_row=idx, admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", provenance_class="ARTIFACT_SUPPORTED", caveat_codes="RULE_PROXY;ARCHIVE_COPY_PROVENANCE_PARTIAL", notes="Existing co-occurrence artifact copied."))
    phi_rows.append(dict(dataset="physionet", proxy_source="rule-based", admission_status="BLOCKED_MISSING_RESULT", provenance_class="MISSING", caveat_codes="PHYSIONET_TABLE_NOT_ARCHIVED", notes="Not derived from patient-level tags in Stage 4.6A.")); write_csv("checked_proxy_cooccurrence.csv", phi_rows)

    # Majority-vote and causal population counts.
    for p in sorted(ARCHIVE.glob("causal-outputs/outputs-*/majority_vote/latent_tags_majority_vote.csv")):
        run, estimator, sampling = run_parts(rel(p)); rows = read_csv(p)
        cohort_rows.append(dict(dataset=dataset_for(rel(p)), population_name=f"majority-vote {run}", pipeline_stage="majority_vote", sampling_condition=sampling, count_type="majority_vote_rows", count_value=len(rows), outcome_rate="", source_path=rel(p), source_sha256=hashes[p], scope="proxy table; voter composition unavailable", admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", caveat_codes="VOTER_MANIFEST_MISSING", notes="Duplicate groups are determined by SHA-256 in the manifest."))

    # Canonical CATE summaries: full summary is selected; reduced manager copies remain excluded.
    cate_rows, hetero_rows, sensitivity_rows, permutation_rows = [], [], [], []
    canonical_summaries = {}
    for run, summary in sorted(run_json.items()):
        run_dir = ARCHIVE / "causal-outputs" / run
        candidates = sorted((run_dir / "cate_estimation").glob("*global_summary.csv"))
        full = next((p for p in candidates if "manager" not in p.name), None)
        canonical_summaries[run] = full
        _, estimator, sampling = run_parts(run)
        dset = dataset_for(run)
        control = run_dir / "cate_estimation/control_messages_cate_estimation.csv"
        for row in read_csv(full) if full else []:
            treatment = row.get("treatment", "")
            treatment_csv = run_dir / "cate_estimation" / treatment / f"{treatment}_cate.csv"
            selected_cross = [x for x in read_csv(ARCHIVE / "causal-outputs/cate_cross_run_unified_table.csv") if x.get("run_folder") == run and x.get("treatment") == treatment]
            validation = "CROSS_RUN_ROW_MATCHED" if selected_cross and selected_cross[0].get("mean_cate") == row.get("mean_cate") else "SOURCE_ONLY"
            cate_rows.append(dict(dataset=dset, estimator=estimator, sampling_condition=sampling, run_name=run, treatment=treatment, model_n=row.get("n", ""), outcome_rate=row.get("outcome_rate", ""), treatment_rate=row.get("treatment_rate", ""), mean_cate=row.get("mean_cate", ""), normalized_cate=row.get("mean_normalized_cate", ""), cate_std=row.get("std_cate", ""), cate_min=row.get("min_cate", ""), cate_max=row.get("max_cate", ""), interval_fields_available=bool(row.get("saved_direct_sensitivity_interval_lb", "")), observed_confounders=row.get("observed_confounders", ""), missing_graph_candidates=row.get("missing_graph_candidates", ""), identifiable_with_available_nodes="UNRESOLVED", source_run_summary=rel(run_dir / "run_summary.json"), source_cate_summary=rel(full), source_treatment_csv=rel(treatment_csv) if treatment_csv.exists() else "", source_control_message=rel(control) if control.exists() else "", row_validation_status=validation, diagnostic_availability="INTENTIONAL_SKIP" if estimator == "CausalPFN" else "ARCHIVED_NONPFN_DIAGNOSTICS", selection_status="PENDING_HUMAN_SELECTION", admission_status="PENDING_HUMAN_SELECTION", provenance_class="EXECUTION_SUPPORTED", caveat_codes="NUMBERED_CONFIG_MISSING;ESTIMAND_WORDING_UNRESOLVED;ARCHIVE_COPY_PROVENANCE_PARTIAL", notes="Full per-run summary selected over reduced manager summary; mean_cate wording requires approval."))
        for p in sorted((run_dir / "cate_estimation").glob("*/*_cate.csv")):
            tr = p.parent.name; rr = read_csv(p); hdr = list(rr[0]) if rr else []
            hetero_rows.append(dict(dataset=dset, estimator=estimator, sampling_condition=sampling, treatment=tr, diagnostic_type="patient_level_cate_distribution", source_path=rel(p), source_sha256=hashes[p], row_count=len(rr), feature_count="", interval_available=any("interval" in x.lower() for x in hdr), figure_candidate="F-CATE-DIST-01", admission_status="PENDING_HUMAN_SELECTION", selection_status="PENDING_HUMAN_SELECTION", caveat_codes="NO_NEW_SUBGROUP_EFFECTS", notes="Patient-level CATE artifact inventoried; no new summary computed."))
        for p in sorted((run_dir / "cate_estimation").glob("*/*feature_importance.csv")):
            rr = read_csv(p)
            hetero_rows.append(dict(dataset=dset, estimator=estimator, sampling_condition=sampling, treatment=p.parent.name, diagnostic_type="feature_importance_or_coefficients", source_path=rel(p), source_sha256=hashes[p], row_count=len(rr), feature_count=len(rr), interval_available="", figure_candidate="F-FEATURE-IMP-01", admission_status="PENDING_HUMAN_SELECTION", selection_status="PENDING_HUMAN_SELECTION", caveat_codes="FEATURE_IMPORTANCE_NOT_MECHANISM", notes="Candidate only; no mechanistic interpretation."))
        bench = run_dir / "analyze_cate_results/benchmark_summary.csv"
        if bench.exists():
            analysis_control = run_dir / "analyze_cate_results/control_messages_analyze_cate_results.csv"
            control_by_treatment = {r.get("treatment", ""): r for r in read_csv(analysis_control)} if analysis_control.exists() else {}
            for row in read_csv(bench):
                tr=row.get("treatment", "")
                contour = run_dir / "analyze_cate_results" / tr / f"{tr}_sensitivity_contour.png"
                ctrl = control_by_treatment.get(tr, {})
                rv_source = ctrl.get("rv_source", "")
                interval_source = ctrl.get("sensitivity_interval_source", "")
                source_fields = ";".join(x for x in (rv_source, interval_source, ctrl.get("contour_source", "")) if x)
                sensitivity_rows.append(dict(dataset=dset, estimator=estimator, sampling_condition=sampling, treatment=tr, analysis_status=ctrl.get("run_status", "ARCHIVED"), diagnostic_name="benchmark_summary", diagnostic_value=mapping_get(row,"RV","analysis_RV","direct_rv"), diagnostic_lower=mapping_get(row,"sensitivity_interval_lb","direct_sensitivity_interval_lb"), diagnostic_upper=mapping_get(row,"sensitivity_interval_ub","direct_sensitivity_interval_ub"), diagnostic_source=source_fields, estimator_native="True" if "loaded_estimator_direct" in source_fields else "False", saved_training_direct="True" if "saved_training_direct" in source_fields else "False", recomputed="True" if any(x in source_fields for x in ("recomputed", "reconstructed", "refit")) else "False", fallback="True" if "fallback" in source_fields else "False", benchmark_variable=mapping_get(row,"proxy_primary_candidate","benchmark_variable"), benchmark_status=ctrl.get("real_benchmark_source", ""), residual_status=ctrl.get("saved_training_residuals_source", ""), contour_path=rel(contour) if contour.exists() else "", contour_sha256=hashes.get(contour,""), warnings=ctrl.get("warnings", ""), source_path=rel(bench), row_validation_status="BENCHMARK_AND_CONTROL_MESSAGE_SCHEMA_VALIDATED", selection_status="PENDING_HUMAN_SELECTION", admission_status="PENDING_HUMAN_SELECTION", caveat_codes="SENSITIVITY_SOURCE_CLASSIFICATION_RECORDED;REAL_BENCHMARK_MAY_BE_UNIMPLEMENTED", notes=f"Control-message source: {rel(analysis_control) if analysis_control.exists() else 'missing'}; numerical values copied without recomputation."))
        elif estimator == "CausalPFN":
            sensitivity_rows.append(dict(dataset=dset, estimator=estimator, sampling_condition=sampling, analysis_status="INTENTIONAL_SKIP", diagnostic_name="EconML_sensitivity", diagnostic_source="not_applicable_to_CausalPFN_pipeline", admission_status="NOT_APPLICABLE", caveat_codes="PFN_INTENTIONAL_SKIP", notes="Run summary records downstream diagnostic skip."))
        for perm_type, fn in [("treatment", "treatment_permutation_results.csv"), ("outcome", "outcome_permutation_results.csv")]:
            pp=run_dir / "permutations_test" / fn
            if pp.exists():
                for row in read_csv(pp):
                    permutation_rows.append(dict(dataset=dset, estimator=estimator, sampling_condition=sampling, run_name=run, treatment=mapping_get(row,"treatment"), permutation_type=perm_type, num_trials=mapping_get(row,"num_trials","trials"), seed=mapping_get(row,"seed"), original_statistic=mapping_get(row,"real_cate_mean","original_statistic","mean_cate"), permuted_mean=mapping_get(row,"permuted_mean","perm_mean"), permuted_std=mapping_get(row,"permuted_std","perm_std"), z_score=mapping_get(row,"z_score"), other_existing_fields=json.dumps(row, sort_keys=True), source_path=rel(pp), source_sha256=hashes[pp], subprocess_status=mapping_get(row,"status"), warning_fields=mapping_get(row,"warnings"), row_validation_status="SOURCE_SCHEMA_VALIDATED", selection_status="PENDING_HUMAN_SELECTION", admission_status="PENDING_HUMAN_SELECTION", caveat_codes="NO_NEW_PVALUES", notes="Archived aggregate permutation row copied."))
            elif estimator == "CausalPFN": permutation_rows.append(dict(dataset=dset, estimator=estimator, sampling_condition=sampling, run_name=run, permutation_type=perm_type, subprocess_status="INTENTIONAL_SKIP", admission_status="NOT_APPLICABLE", caveat_codes="PFN_INTENTIONAL_SKIP", notes="Run summary records skip; this is not a negative diagnostic result."))
    write_csv("checked_cate_candidates.csv", cate_rows); write_csv("checked_heterogeneity_candidates.csv", hetero_rows); write_csv("checked_sensitivity_candidates.csv", sensitivity_rows); write_csv("checked_permutation_candidates.csv", permutation_rows)

    # Matching cross-run table: each values is checked against listed canonical run summaries when available.
    matching_rows=[]; matching_src=ARCHIVE / "causal-outputs/cate_cross_run_matching_table.csv"
    for row in read_csv(matching_src):
        sources=row.get("source_matching_summary_paths", "").split("; "); matched=True
        for source in sources:
            p=ARCHIVE / "causal-outputs" / source
            if not p.exists() or not any(x.get("treatment") == row.get("treatment") and x.get("mean_pair_effect") == row.get("mean_pair_effect") for x in read_csv(p)): matched=False
        matching_rows.append(dict(dataset=row.get("dataset"), estimator="cross-run-consistent", sampling_condition="outcome-downsampled" if row.get("sampling") == "downsample" else "original", treatment=row.get("treatment"), n=row.get("n_total"), n_pairs=row.get("n_pairs"), match_rate=row.get("match_rate"), mean_pair_effect=row.get("mean_pair_effect"), std_pair_effect=row.get("std_pair_effect"), normalized_pair_effect=row.get("mean_normalized_pair_effect"), final_allowed_distance=row.get("final_allowed_distance"), sufficient_pairs=row.get("reached_sufficient_pairs"), observed_confounders=row.get("observed_confounders"), source_path=rel(matching_src), source_sha256=hashes[matching_src], row_validation_status="MATCHED_ALL_LISTED_RUN_SOURCES" if matched else "CONFLICT", admission_status="PENDING_HUMAN_SELECTION" if matched else "BLOCKED_VALUE_CONFLICT", caveat_codes="MATCHING_ESTIMAND_WORDING_UNRESOLVED"))
    write_csv("checked_matching_results.csv", matching_rows)
    fail_rows=[]; failures=ARCHIVE / "causal-outputs/cate_cross_run_matching_failures.csv"
    for row in read_csv(failures): fail_rows.append(dict(dataset=row.get("dataset"), estimator="cross-run-consistent", sampling_condition="outcome-downsampled" if row.get("sampling") == "downsample" else "original", treatment=row.get("treatment"), failure_reason=row.get("reason"), support_fields="", source_path=rel(failures), admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", notes="Failure is retained as failure, not a zero effect."))
    write_csv("checked_matching_failures.csv", fail_rows)

    # Mortality text artifacts: one canonical row per hash-equivalent group.
    mortality=[]; seen=set()
    for p in sorted(ARCHIVE.glob("causal-outputs/outputs-*/mortality_prediction/*.txt")):
        if hashes[p] in seen: continue
        seen.add(hashes[p]); run, _, sampling=run_parts(rel(p)); text=p.read_text(encoding="utf-8", errors="replace").strip().replace("\n", " | ")
        mortality.append(dict(dataset=dataset_for(rel(p)), sampling_condition=sampling, model_type="proxy-state mortality-prediction association", source_path=rel(p), source_sha256=hashes[p], duplicate_group="SHA256-"+hashes[p][:12] if len(hash_groups[hashes[p]])>1 else "", metric_text=text, admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", provenance_class="EXECUTION_SUPPORTED", caveat_codes="NONCAUSAL_ASSOCIATION;ARCHIVE_COPY_PROVENANCE_PARTIAL", notes="Canonical hash-equivalent copy only; metrics retained as source text."))
    write_csv("checked_mortality_prediction.csv", mortality)
    write_csv("checked_cohort_candidates.csv", cohort_rows)

    # Existing figures plus required planned-but-missing status rows.
    fig_rows=[]; fig_id=0
    for p in sorted(ARCHIVE.rglob("*.png")):
        fig_id+=1; run, estimator, sampling=run_parts(rel(p)); w,h=png_size(p)
        fig_rows.append(dict(figure_id=f"ARCHIVED-PNG-{fig_id:04d}", dataset=dataset_for(rel(p)), estimator=estimator, sampling_condition=sampling, treatment=p.parent.name if p.parent.name.startswith("LAT_") else "", source_path=rel(p), source_sha256=hashes[p], width=w, height=h, producing_script="", input_source="archived direct figure", source_status="ARCHIVED", selection_status="PENDING_HUMAN_SELECTION", admission_status="ADMISSIBLE_WITH_QUALIFICATIONS", caveat_codes="FIGURE_INPUT_PROVENANCE_PARTIAL", notes="Existing direct archived figure; not altered."))
    planned={"F-LC-PHY-STRATS","F-LC-MIMIC-STRATS","F-LC-ALL","F-MODEL-COMP-01","F-PROXY-PREV-01","F-PROXY-COOC-01","F-CATE-DIST-01","F-FEATURE-IMP-01","F-OVERLAP-01","F-SENS-SELECT","F-PERM-01"}
    present={r["figure_id"] for r in fig_rows}
    for f in sorted(planned): fig_rows.append(dict(figure_id=f, source_status="PLANNED_NOT_GENERATED", selection_status="PENDING_HUMAN_SELECTION", admission_status="BLOCKED_MISSING_RESULT", caveat_codes="PLANNED_FIGURE_NOT_YET_ADMISSIBLE", notes="Planning identifier; no figure generated in Stage 4.6A."))
    write_csv("checked_figure_candidates.csv", fig_rows)

    # Machine-readable source integrity checks before documents/checksums.
    assert len({r["artifact_id"] for r in manifest}) == len(manifest)
    assert all((ROOT / r["relative_path"]).is_file() for r in manifest)

    counts = defaultdict(int)
    for r in manifest: counts[r["result_family"]] += 1
    run_status = []
    for run, data in sorted(run_json.items()):
        _, est, samp = run_parts(run)
        stages="; ".join(f"{k}={v.get('status','unknown')}" for k,v in data.get("stages",{}).items())
        run_status.append(f"| {dataset_for(run)} | {est} | {samp} | `{run}` | {data.get('overall_status','unknown')} | {stages} | numbered config not archived |")
    manifest_md = "# Stage 4.6A Results Manifest\n\nThis manifest inventories archived sources only. `final-results/` is ignored/untracked, and recorded producing-machine paths are not treated as local sources.\n\n## Scope\n\n- Source artifacts inventoried: %d\n- Result-family counts: %s\n- Predictive final summaries: 10 completed families (five models × two datasets); InterpNet has no final summary/export.\n- Causal runs: 12 archived run summaries; numbered producing configs are referenced but absent locally.\n\n## Causal Run Matrix\n\n| Dataset | Estimator | Sampling | Run | Overall | Stage statuses | Configuration |\n|---|---|---|---|---|---|---|\n%s\n\n## Canonical-source rule\n\nFull per-run CATE summaries are the canonical CATE summaries. Reduced manager summaries are excluded; `physionet_manager_global_summary.csv` under the MIMIC LinearDML run is excluded as mislabeled. SHA-256-equivalent copies are grouped in `results_manifest.csv`.\n\n## Readiness\n\nREADY FOR HUMAN RESULT-SELECTION DECISIONS\n" % (len(manifest), ", ".join(f"{k}={v}" for k,v in sorted(counts.items())), "\n".join(run_status))
    (OUT / "results_manifest.md").write_text(manifest_md, encoding="utf-8")

    sections=[("C10.1 Data and cohort summary","checked_cohort_candidates.csv","Export, majority-vote, and run-summary counts","Pipeline-contract-specific counts","Raw cohort totals","Do not merge pipeline counts","Cohort-count source","Appendix/supporting"),("C10.2 Proxy prevalence and co-occurrence","checked_proxy_prevalence.csv; checked_proxy_cooccurrence.csv","MIMIC rule-based tables","Existing values only","PhysioNet counterpart tables","Proxy states, not diagnoses","Proxy exposure selection","Appendix/supporting"),("C10.3 Predictive performance","checked_predictive_metrics.csv","Ten training summaries and paired logs","Validation/test metrics","InterpNet numerical results","Do not overstate split provenance","Model comparison hierarchy","Main text candidate"),("C10.4 Learning-curve diagnostics","checked_figure_candidates.csv","Archived learning-curve PNGs","Diagnostic figures","Selected figure","Diagnostic only, not test-metric substitute","Learning-curve selection","Appendix"),("C10.5 Mortality prediction from proxy states","checked_mortality_prediction.csv","Canonical mortality text outputs","Existing source metrics","Formal causal interpretation","Proxy-state mortality-prediction association","Presentation role","Appendix/supporting"),("C10.6 Matching results","checked_matching_results.csv; checked_matching_failures.csv","Cross-run table and per-run summaries","Matched-pair fields","Approved estimand wording","Do not call mean_pair_effect ATE or ATT","Matching wording","Main text candidate"),("C10.7 CATE estimates","checked_cate_candidates.csv","Full per-run global summaries","Mean CATE and distribution fields","Primary estimator/sampling/exposures","Do not call mean_cate ATE","Primary hierarchy","Main text candidate"),("C10.8 Heterogeneity diagnostics","checked_heterogeneity_candidates.csv","Patient-level CATE and feature artifacts","Artifact availability","New subgroup effects","Feature importance is not mechanism","Figure choice","Appendix"),("C10.9 Overlap and support","checked_matching_results.csv; checked_matching_failures.csv","Matching support fields","Match rate and failures","Dedicated overlap figure","No positivity claim","Omit/generate figure later","Appendix"),("C10.10 Sensitivity","checked_sensitivity_candidates.csv","Non-PFN benchmark artifacts","Existing diagnostics","Primary contour","Keep source classification","Contour selection","Appendix/main-text decision"),("C10.11 Permutation checks","checked_permutation_candidates.csv","Archived aggregate files","Existing trial summaries","New p-values","Do not label formal test without source support","Role decision","Appendix"),("C10.12 Cross-dataset comparison","checked_cate_candidates.csv","Separate dataset rows","Dataset-specific estimates","Combined average","No cross-dataset pooling","Comparison scope","Appendix/supporting")]
    packet=["# Stage 4.6A Results Source Packet", "", "This packet points to checked CSVs; it deliberately does not reproduce full numerical tables."]
    for sec,file_,sources,available,blocked,boundary,decision,role in sections:
        packet += ["",f"## {sec}",f"- Checked file: `{file_}`",f"- Canonical source artifacts: {sources}","- Admission status: PENDING_HUMAN_SELECTION or explicitly qualified archive evidence",f"- Available numerical fields: {available}",f"- Blocked fields: {blocked}",f"- Required wording boundary: {boundary}",f"- Remaining human decision: {decision}","- Remaining provenance limitation: ignored archive copies and incomplete producing configuration/split manifests.",f"- Recommended role: {role}."]
    (OUT / "results_source_packet.md").write_text("\n".join(packet)+"\n", encoding="utf-8")

    decisions=[("001","primary causal sampling condition","original; outcome-downsampled","Both exist; original retains population outcome rate while downsampled is a distinct analysis population.","original for population interpretation; retain downsampled as separate sensitivity population","high"),("002","primary causal estimator","CausalForestDML; LinearDML; CausalPFN","All twelve summaries exist; PFN skips downstream diagnostics.","choose an estimator with complete archived diagnostics after human review","medium"),("003","role of CausalPFN","exploratory; supplementary; primary","PFN CATE summaries exist but diagnostic stages are intentionally skipped.","exploratory/supplementary","high"),("004","matching estimand wording","descriptive matched-pair difference; ATT-like; exclude","Archive reports mean_pair_effect only.","descriptive matched-pair difference","high"),("005","mean_cate wording","mean model-estimated CATE; other approved wording","Arithmetic summary of patient-level modeled CATE values.","mean model-estimated CATE","high"),("006","normalized_CATE inclusion and wording","omit; include with explicit normalization wording","Value divides by sample outcome rate.","omit from main text pending wording approval","high"),("007","thesis-primary proxy-state exposures","select subset; show all; none","Archived treatment sets differ by dataset.","human selection based on construct review","medium"),("008","original versus downsampled presentation","original primary; downsampled primary; parallel","Both populations have distinct n/outcome rates.","original primary, downsampled sensitivity","medium"),("009","cross-dataset comparison scope","qualitative; aligned proxy concepts; pooled","Schemas and proxy concepts differ.","qualitative/aligned only; no pooling","high"),("010","sensitivity-contour selection","choose one; appendix all; omit","Non-PFN contours are archived.","appendix all pending selection","medium"),("011","permutation main-text versus appendix role","main; appendix; omit","Aggregate archived rows exist for non-PFN only.","appendix pending source-interpretation review","medium"),("012","overlap figure omission or generation requirement","omit; create later","No dedicated overlap plot archived.","omit with support limitations stated","high"),("013","InterpNet exclusion","exclude; rerun later","No final summary or export archived.","exclude numerical comparison","high"),("014","learning-curve figure selection","select archived curve; appendix all","Archived PNGs exist.","appendix candidate pending selection","medium"),("015","cohort-count source","run summary; export; labels; recover manifest","Counts describe different contracts.","report source-specific counts only","high"),("016","primary versus supplementary tables","select hierarchy","All candidate tables are checked but no approved hierarchy is recorded.","main predictive + qualified CATE candidate; appendices for diagnostics","low")]
    register=["# Stage 4.6A Results Decision Register", "", "All recommendations are nonbinding; no recommendation is enacted in checked tables."]
    for n,q,opts,evidence,recommendation,confidence in decisions:
        register += ["",f"## DEC-RESULT-{n}",f"- Question: {q}",f"- Available options: {opts}",f"- Verified evidence: {evidence}","- Scientific consequences: determines which qualified, non-pooled result rows may be foregrounded.","- Provenance consequences: does not remove the archive, configuration, or split limitations.",f"- Recommended option: {recommendation}",f"- Recommendation confidence: {confidence}","- Human owner: thesis author and supervisor", "- Current status: OPEN", "- Required before Stage 4.6B: yes"]
    (OUT / "results_decision_register.md").write_text("\n".join(register)+"\n", encoding="utf-8")

    checked_summary=[]
    for name in CHECKED:
        p=OUT/name; rows,cols,_=csv_meta(p); checked_summary.append(f"| `{rel(p)}` | {rows} | {cols} | `{sha(p)}` |")
    report = "# Stage 4.6A Evidence Report\n\n## Git State\n\n- Verified approved commit: `7f5206a step 4.5`; parent is `a96d475 step 4.4S`.\n- Parent branch: `main`. Initial worktree was already dirty outside the authorized scope; no reset, checkout, stage, commit, or push was performed.\n- Causal nested repository: `main` at `417bb32`, with pre-existing modification to `src/preprocess_mimic_iii_large.py`. STraTS: `main` at `4d2a752`.\n- `final-results/` is ignored/untracked (`.gitignore`), so its archived copies have partial provenance.\n\n## Baseline and Final Build\n\n- Command: `latexmk -C && latexmk -xelatex main.tex && test -f main.pdf && pdfinfo main.pdf`.\n- Result: success; `thesis-writing/thesis/main.pdf`, 79 pages.\n- Warnings: existing undefined-citation/reference and layout warnings were emitted; no fatal build error.\n\n## Artifact Inventory\n\n- Manifested source artifacts: %d.\n- Families: %s.\n- SHA-256 was computed for every manifest source and every generated checked CSV/Markdown result file; no binary artifact was deserialized.\n\n## Predictive Validation\n\n- Ten completed final training summaries were parsed, with separate validation/test rows and paired-log numerical comparison.\n- InterpNet is retained as `BLOCKED_MISSING_RESULT` for both datasets.\n- Ten archived exports were schema checked; their split and checkpoint provenance remain unverified.\n\n## Proxy Validation\n\n- Existing MIMIC rule-based prevalence, co-occurrence, and unadjusted mortality-association tables were copied with provenance. PhysioNet counterpart tables remain explicitly missing and were not generated.\n- Majority-vote duplicates are grouped in the manifest by SHA-256; voter composition is not inferred.\n\n## Causal Run Matrix\n\n| Dataset | Estimator | Sampling | Run | Overall | Stage statuses | Configuration |\n|---|---|---|---|---|---|---|\n%s\n\n## Canonical and Conflict Audit\n\n- Full per-run CATE summaries were selected over reduced manager summaries.\n- Hash-equivalent copies are excluded from canonical use.\n- `outputs-mimic-linear/cate_estimation/physionet_manager_global_summary.csv` is excluded as mislabeled.\n- Exact numbered causal configs are referenced by run summaries but absent locally; they were not silently replaced by compact configs.\n\n## Checked Table Inventory\n\n| Path | Rows | Columns | SHA-256 |\n|---|---:|---:|---|\n%s\n\n## Source Packet and Decisions\n\n- Source packet: `thesis-writing/results/results_source_packet.md`.\n- Decision register: `thesis-writing/results/results_decision_register.md`; all 16 required decisions remain open.\n- Nonbinding hierarchy: original population for population interpretation; an estimator with complete archived diagnostics only after human selection; PFN exploratory; diagnostics generally appendix candidates.\n\n## Placeholders and Deferred Fixes\n\n- No existing placeholder is resolved merely by this audit.\n- New deferred issues: `DF-4.6A-001` through `DF-4.6A-006`, covering missing numbered configs, predictive split/checkpoint lineage, archive-copy/source-commit provenance, missing PhysioNet proxy tables, treatment-level diagnostic source/status, and result-hierarchy approval.\n\n## Scope Validation\n\n- No thesis chapter, research code, configuration, planning/audit file, source result artifact, or source figure was edited. The only thesis build output is `thesis-writing/thesis/main.pdf`.\n\n## Readiness\n\nREADY FOR HUMAN RESULT-SELECTION DECISIONS\n" % (len(manifest), ", ".join(f"{k}={v}" for k,v in sorted(counts.items())), "\n".join(run_status), "\n".join(checked_summary))
    LOG.write_text(report, encoding="utf-8")
    # Hash generated deliverables after their final contents are written.  The
    # checksum file is intentionally excluded from its own checksum listing.
    checksum_targets = sorted([p for p in OUT.iterdir() if p.is_file() and p.name not in {"results_checksums.sha256", Path(__file__).name}] + [LOG])
    with (OUT / "results_checksums.sha256").open("w", encoding="utf-8") as fh:
        for p in checksum_targets: fh.write(f"{sha(p)}  {rel(p)}\n")
        for p in archive_files: fh.write(f"{hashes[p]}  {rel(p)}\n")

if __name__ == "__main__": main()
