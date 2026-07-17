#!/bin/bash
#SBATCH --job-name=clinicause
#SBATCH --output=/truenas/home/kenzikob/CliniCause/logs/clinicause_%j.out
#SBATCH --error=/truenas/home/kenzikob/CliniCause/logs/clinicause_%j.err
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
RUN_ID=slurm_${SLURM_JOB_ID}
OUTPUT_ROOT=runs
DATASET=both
STAGES=all

mkdir -p ${PROJECT_ROOT}/logs
mkdir -p ${PROJECT_ROOT}/${OUTPUT_ROOT}

echo "Submitting CliniCause job"
echo "Job ID: ${SLURM_JOB_ID}"
echo "Project root: ${PROJECT_ROOT}"
echo "Run ID: ${RUN_ID}"
date

/usr/bin/apptainer exec --nv \
  --bind ${PROJECT_ROOT}:/workspace \
  ${IMAGE} \
  bash -lc "
    set -euo pipefail

    cd /workspace

    source /opt/conda/etc/profile.d/conda.sh
    conda activate ${CONDA_ENV}

    echo 'Inside container'
    echo 'Host:' \$(hostname)
    echo 'Python:' \$(which python)
    python --version
    nvidia-smi || true

    python router.py \
      --dataset ${DATASET} \
      --run-id ${RUN_ID} \
      --output-root ${OUTPUT_ROOT} \
      --thesis-repo-root ./causal-irregular-time-series \
      --strats-repo-root ./STraTS \
      --physionet-raw-data-path /workspace/data/physionet2012 \
      --mimic-raw-data-path /workspace/data/mimiciii \
      --stages ${STAGES} \
      --overwrite
  "

echo "CliniCause finished successfully"
date
