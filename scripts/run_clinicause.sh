#!/usr/bin/env bash

# Run CliniCause directly in the caller's active Python environment.
#
# Complete pipeline:
#   STAGES=all bash run_clinicause.sh
# Dataset construction through majority vote:
#   STAGES=dataset-extraction bash run_clinicause.sh

set -euo pipefail

DATASET="${DATASET:-both}"
OUTPUT_ROOT="${OUTPUT_ROOT:-runs}"
PHYSIONET_RAW_DATA_PATH="${PHYSIONET_RAW_DATA_PATH:-data/physionet2012}"
MIMIC_RAW_DATA_PATH="${MIMIC_RAW_DATA_PATH:-data/mimiciii}"
STAGES="${STAGES:-all}"
STRATS_MAX_CONCURRENT="${STRATS_MAX_CONCURRENT:-1}"
PYTHON_BIN="${PYTHON_BIN:-python}"
RUN_ID="${RUN_ID:-${CLINICAUSE_RUN_ID:-}}"

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
PROJECT_ROOT="${SCRIPT_DIR}"
THESIS_REPO_ROOT="${PROJECT_ROOT}/causal-irregular-time-series"
STRATS_REPO_ROOT="${PROJECT_ROOT}/STraTS"
ROUTER_PATH="${PROJECT_ROOT}/router.py"

resolve_from_project_root() {
  local path="$1"
  if [[ "${path}" = /* ]]; then
    printf '%s\n' "${path}"
  else
    printf '%s\n' "${PROJECT_ROOT}/${path}"
  fi
}

case "${DATASET}" in
  physionet|mimic|both) ;;
  *)
    echo "Error: DATASET must be physionet, mimic, or both; received: ${DATASET}" >&2
    exit 2
    ;;
esac

if [[ -z "${RUN_ID}" ]]; then
  RUN_ID="${STAGES}_${DATASET}_$(date -u +%Y%m%dT%H%M%SZ)_$$"
fi

if [[ ! -f "${ROUTER_PATH}" || ! -d "${THESIS_REPO_ROOT}" || ! -d "${STRATS_REPO_ROOT}" ]]; then
  echo "Error: run_clinicause.sh must remain in the CliniCause repository root." >&2
  exit 1
fi
if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  echo "Error: Python executable '${PYTHON_BIN}' was not found." >&2
  exit 1
fi

OUTPUT_ROOT_PATH="$(resolve_from_project_root "${OUTPUT_ROOT}")"
PHYSIONET_RAW_DATA_PATH="$(resolve_from_project_root "${PHYSIONET_RAW_DATA_PATH}")"
MIMIC_RAW_DATA_PATH="$(resolve_from_project_root "${MIMIC_RAW_DATA_PATH}")"

printf '%s\n' \
  "Starting CliniCause run" \
  "Dataset: ${DATASET}" \
  "Stage selector: ${STAGES}" \
  "Output root: ${OUTPUT_ROOT_PATH}" \
  "Run ID: ${RUN_ID}"

cd "${PROJECT_ROOT}"
"${PYTHON_BIN}" "${ROUTER_PATH}" \
  --dataset "${DATASET}" \
  --run-id "${RUN_ID}" \
  --output-root "${OUTPUT_ROOT_PATH}" \
  --thesis-repo-root "${THESIS_REPO_ROOT}" \
  --strats-repo-root "${STRATS_REPO_ROOT}" \
  --physionet-raw-data-path "${PHYSIONET_RAW_DATA_PATH}" \
  --mimic-raw-data-path "${MIMIC_RAW_DATA_PATH}" \
  --stages "${STAGES}" \
  --strats-max-concurrent "${STRATS_MAX_CONCURRENT}"

echo "CliniCause run finished successfully"
