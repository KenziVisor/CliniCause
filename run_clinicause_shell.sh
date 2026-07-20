#!/usr/bin/env bash

# Run the complete CliniCause pipeline directly on the host machine.
# This script may be launched from any working directory.
#
# Requirements:
#   - Place this file in the CliniCause repository root, next to router.py.
#   - Activate the desired Python environment before running this script.
#   - Ensure the active environment contains all project dependencies.
#
# Example:
#   bash run_clinicause.sh
#
# Optional one-run overrides:
#   DATASET=mimic RUN_ID=my_mimic_run bash run_clinicause.sh

set -euo pipefail

# ==============================================================================
# USER CONFIGURATION — edit values in this section when needed.
# Do not add machine-specific absolute repository paths: the repository root is
# detected automatically from this script's location.
# ==============================================================================

# Allowed values: physionet, mimic, both
DATASET="${DATASET:-both}"

# Output directory, relative to the CliniCause repository root unless absolute.
OUTPUT_ROOT="${OUTPUT_ROOT:-runs}"

# Raw-data locations, relative to the CliniCause repository root unless absolute.
PHYSIONET_RAW_DATA_PATH="${PHYSIONET_RAW_DATA_PATH:-data/physionet2012}"
MIMIC_RAW_DATA_PATH="${MIMIC_RAW_DATA_PATH:-data/mimiciii}"

# Pipeline configuration.
STAGES="${STAGES:-all}"
STRATS_MAX_CONCURRENT="${STRATS_MAX_CONCURRENT:-1}"

# Python executable from the environment activated by the user.
PYTHON_BIN="${PYTHON_BIN:-python}"

# Optional run identifier. Leave empty to generate one automatically.
RUN_ID="${RUN_ID:-${CLINICAUSE_RUN_ID:-}}"

# ==============================================================================
# IMPLEMENTATION — normally do not edit below this line.
# ==============================================================================

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

OUTPUT_ROOT_PATH="$(resolve_from_project_root "${OUTPUT_ROOT}")"
PHYSIONET_RAW_DATA_PATH="$(resolve_from_project_root "${PHYSIONET_RAW_DATA_PATH}")"
MIMIC_RAW_DATA_PATH="$(resolve_from_project_root "${MIMIC_RAW_DATA_PATH}")"

case "${DATASET}" in
  physionet|mimic|both) ;;
  *)
    echo "Error: DATASET must be physionet, mimic, or both; received: ${DATASET}" >&2
    exit 2
    ;;
esac

if [[ -z "${RUN_ID}" ]]; then
  RUN_ID="all_${DATASET}_$(date -u +%Y%m%dT%H%M%SZ)_$$"
fi

if [[ ! -f "${ROUTER_PATH}" ]]; then
  echo "Error: router.py was not found at ${ROUTER_PATH}." >&2
  echo "Place this script in the CliniCause repository root." >&2
  exit 1
fi

if [[ ! -d "${THESIS_REPO_ROOT}" ]]; then
  echo "Error: thesis repository was not found at ${THESIS_REPO_ROOT}." >&2
  exit 1
fi

if [[ ! -d "${STRATS_REPO_ROOT}" ]]; then
  echo "Error: STraTS repository was not found at ${STRATS_REPO_ROOT}." >&2
  exit 1
fi

if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  echo "Error: Python executable '${PYTHON_BIN}' was not found." >&2
  echo "Activate the intended environment before running this script." >&2
  exit 1
fi

mkdir -p "${OUTPUT_ROOT_PATH}" "${PROJECT_ROOT}/logs"

printf '%s\n' \
  "Starting complete CliniCause run" \
  "Host: $(hostname)" \
  "Dataset: ${DATASET}" \
  "Project root: ${PROJECT_ROOT}" \
  "Output root: ${OUTPUT_ROOT_PATH}" \
  "Run ID: ${RUN_ID}" \
  "Python: $(command -v "${PYTHON_BIN}")"
"${PYTHON_BIN}" --version
date -u

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

echo "Complete CliniCause run finished successfully"
date -u
