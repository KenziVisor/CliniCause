# Reproducibility and provenance package

This compact package indexes the repository's authoritative evidence without duplicating the 1,389-row result manifest. It distinguishes archived facts from current-source reproduction, defaults, inference, and absent records.

## Evidence classes

`EXACT_ARCHIVED_ARTIFACT`, `EXACT_ARCHIVED_METADATA`, `EXACT_GIT_HISTORY_RECOVERY`, `EXACT_HASH_IDENTICAL_COPY`, `RUN_SUMMARY_RECORDED`, `LOG_RECORDED`, `CURRENT_SOURCE_REPRODUCTION`, `CURRENT_SOURCE_ONLY`, `CURRENT_DEFAULT_ONLY`, `INTENDED_REQUIREMENTS_ONLY`, `PARTIAL_LINEAGE`, `INFERRED_CANDIDATE_NOT_PROOF`, `MISSING_LOCAL_ARTIFACT`, `EXTERNAL_RECORD_REQUIRED`, `LIKELY_IRRECOVERABLE`, and `NOT_APPLICABLE`.

`artifact_index.csv` points to the detailed result records. `causal_run_lineage.csv` contains the twelve archived causal families; `predictive_run_lineage.csv` contains the ten dataset--model families. `data_lineage.csv`, `environment_lineage.csv`, and `source_version_lineage.csv` record the boundary between historical evidence and current implementation. `archive_copy_lineage.csv` records hash-identical DAG copies without asserting direction. `provenance_gaps.csv` gives each remaining gap an owner and next action.

The package does not claim a complete clean-checkout rerun, exact historical rerun, complete raw-data lineage, complete checkpoint lineage, or complete producing-environment capture. `checksums.sha256` is generated after package creation and intentionally checks the other package files rather than itself.
