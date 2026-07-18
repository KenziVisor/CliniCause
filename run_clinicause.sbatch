#!/bin/bash
#SBATCH --job-name=clinicause-all
#SBATCH --output=/truenas/home/kenzikob/CliniCause/logs/clinicause_all_%j.out
#SBATCH --error=/truenas/home/kenzikob/CliniCause/logs/clinicause_all_%j.err
#SBATCH --time=24:00:00
#SBATCH --partition=shared
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=29G

set -euo pipefail

# -------- Paths --------
IMAGE=/truenas/sif_images/pytorch_cuda12.6_ngc_conda_vscode.sif
PROJECT_ROOT=/truenas/home/kenzikob/CliniCause
CONDA_ENV=/truenas/home/kenzikob/conda/envs/clinicause

# -------- Run config --------
DATASET=${DATASET:?Submit with DATASET=physionet, DATASET=mimic, or DATASET=both}
OUTPUT_ROOT=${OUTPUT_ROOT:-runs}
RUN_ID=${CLINICAUSE_RUN_ID:-all_${DATASET}_${SLURM_JOB_ID}}
STAGES=all

case "${DATASET}" in
  physionet|mimic|both) ;;
  *)
    echo "DATASET must be physionet, mimic, or both; received: ${DATASET}" >&2
    exit 2
    ;;
esac

mkdir -p "${PROJECT_ROOT}/logs"
mkdir -p "${PROJECT_ROOT}/${OUTPUT_ROOT}"

echo "Submitting complete CliniCause job"
echo "Job ID: ${SLURM_JOB_ID}"
echo "Dataset: ${DATASET}"
echo "Project root: ${PROJECT_ROOT}"
echo "Run ID: ${RUN_ID}"
date -u

/usr/bin/apptainer exec --nv \
  --bind "${PROJECT_ROOT}:/workspace" \
  --env "CC_DATASET=${DATASET}" \
  --env "CC_RUN_ID=${RUN_ID}" \
  --env "CC_OUTPUT_ROOT=${OUTPUT_ROOT}" \
  --env "CC_CONDA_ENV=${CONDA_ENV}" \
  --env "CC_STAGES=${STAGES}" \
  "${IMAGE}" \
  bash -lc '
    set -euo pipefail

    cd /workspace

    source /opt/conda/etc/profile.d/conda.sh
    conda activate "${CC_CONDA_ENV}"

    echo "Inside container"
    echo "Host: $(hostname)"
    echo "Python: $(which python)"
    python --version
    echo "CliniCause commit: $(git rev-parse HEAD)"
    echo "STraTS commit: $(git -C STraTS rev-parse HEAD)"
    echo "Causal commit: $(git -C causal-irregular-time-series rev-parse HEAD)"
    nvidia-smi || true

    python router.py \
      --dataset "${CC_DATASET}" \
      --run-id "${CC_RUN_ID}" \
      --output-root "${CC_OUTPUT_ROOT}" \
      --thesis-repo-root ./causal-irregular-time-series \
      --strats-repo-root ./STraTS \
      --physionet-raw-data-path /workspace/data/physionet2012 \
      --mimic-raw-data-path /workspace/data/mimiciii \
      --stages "${CC_STAGES}" \
      --strats-max-concurrent 1
  '

echo "Complete CliniCause job finished successfully"
date -u
