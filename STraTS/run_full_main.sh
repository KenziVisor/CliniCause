#!/bin/bash

set -euo pipefail

SCRIPT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON:-python}"
TRAIN_FRAC="${STRATS_TRAIN_FRAC:-0.5}"
MODEL_RUN="${STRATS_MODEL_RUN:-1o10}"
PIPELINE_RUN_ID="${CLINICAUSE_RUN_ID-standalone}"
CONFIG_FINGERPRINT="${STRATS_CONFIG_FINGERPRINT-legacy-standalone}"
SEED_MODULUS=2147483647

scope="${DATASET_SCOPE-both}"
run_physionet=0
run_mimic=0
case "$scope" in
  physionet)
    run_physionet=1
    ;;
  mimic)
    run_mimic=1
    ;;
  both|physionet,mimic|mimic,physionet)
    run_physionet=1
    run_mimic=1
    ;;
  "")
    echo "DATASET_SCOPE must not be empty" >&2
    exit 2
    ;;
  *)
    echo "Unknown DATASET_SCOPE '$scope'; expected physionet, mimic, both, physionet,mimic, or mimic,physionet" >&2
    exit 2
    ;;
esac

if [[ -z "$PIPELINE_RUN_ID" ]]; then
  echo "CLINICAUSE_RUN_ID must not be empty" >&2
  exit 2
fi
if [[ -z "$CONFIG_FINGERPRINT" ]]; then
  echo "STRATS_CONFIG_FINGERPRINT must not be empty" >&2
  exit 2
fi
if [[ ! "$MODEL_RUN" =~ ^[1-9][0-9]*o[1-9][0-9]*$ ]]; then
  echo "STRATS_MODEL_RUN must have form <run>o<total>" >&2
  exit 2
fi

BASE_SEED_RAW="${STRATS_BASE_SEED-2023}"
if [[ ! "$BASE_SEED_RAW" =~ ^[0-9]+$ ]]; then
  echo "STRATS_BASE_SEED must be an integer in [0, $SEED_MODULUS)" >&2
  exit 2
fi
BASE_SEED=$((10#$BASE_SEED_RAW))
if (( BASE_SEED < 0 || BASE_SEED >= SEED_MODULUS )); then
  echo "STRATS_BASE_SEED must be an integer in [0, $SEED_MODULUS)" >&2
  exit 2
fi

derive_seed() {
  local seed="$1"
  local offset="$2"
  printf '%s\n' "$(( (seed + offset) % SEED_MODULUS ))"
}

if [[ -v STRATS_INPUT_ROOT ]]; then
  if [[ -z "$STRATS_INPUT_ROOT" ]]; then
    echo "STRATS_INPUT_ROOT must not be empty when set" >&2
    exit 2
  fi
  INPUT_ROOT="$STRATS_INPUT_ROOT"
else
  INPUT_ROOT="$SCRIPT_ROOT/data"
fi
if [[ -v STRATS_OUTPUT_ROOT ]]; then
  if [[ -z "$STRATS_OUTPUT_ROOT" ]]; then
    echo "STRATS_OUTPUT_ROOT must not be empty when set" >&2
    exit 2
  fi
  OUTPUT_BASE="$STRATS_OUTPUT_ROOT"
  explicit_output_root=1
else
  OUTPUT_BASE="$SCRIPT_ROOT/outputs"
  explicit_output_root=0
fi

if (( run_physionet == 1 && run_mimic == 1 )); then
  PHYSIONET_OUTPUT_ROOT="$OUTPUT_BASE/physionet"
  MIMIC_OUTPUT_ROOT="$OUTPUT_BASE/mimic"
elif (( run_physionet == 1 )); then
  if (( explicit_output_root == 1 )); then
    PHYSIONET_OUTPUT_ROOT="$OUTPUT_BASE"
  else
    PHYSIONET_OUTPUT_ROOT="$OUTPUT_BASE/physionet_2012"
  fi
else
  if (( explicit_output_root == 1 )); then
    MIMIC_OUTPUT_ROOT="$OUTPUT_BASE"
  else
    MIMIC_OUTPUT_ROOT="$OUTPUT_BASE/mimic_iii"
  fi
fi

PHYSIONET_DATASET_SEED="$(derive_seed "$BASE_SEED" 100000)"
MIMIC_DATASET_SEED="$(derive_seed "$BASE_SEED" 200000)"
PHYSIONET_STRATS_SEED="$(derive_seed "$PHYSIONET_DATASET_SEED" 1)"
PHYSIONET_GRU_SEED="$(derive_seed "$PHYSIONET_DATASET_SEED" 3)"
PHYSIONET_GRUD_SEED="$(derive_seed "$PHYSIONET_DATASET_SEED" 4)"
PHYSIONET_TCN_SEED="$(derive_seed "$PHYSIONET_DATASET_SEED" 5)"
PHYSIONET_SAND_SEED="$(derive_seed "$PHYSIONET_DATASET_SEED" 6)"
MIMIC_STRATS_SEED="$(derive_seed "$MIMIC_DATASET_SEED" 1)"
MIMIC_GRU_SEED="$(derive_seed "$MIMIC_DATASET_SEED" 3)"
MIMIC_GRUD_SEED="$(derive_seed "$MIMIC_DATASET_SEED" 4)"
MIMIC_TCN_SEED="$(derive_seed "$MIMIC_DATASET_SEED" 5)"
MIMIC_SAND_SEED="$(derive_seed "$MIMIC_DATASET_SEED" 6)"

run_model() {
  local model_seed="$1"
  shift
  "$PYTHON_BIN" "$SCRIPT_ROOT/src/main.py" \
    --dataset "$CURRENT_DATASET" \
    --processed_data_path "$CURRENT_PROCESSED_DATA" \
    --latent_csv_path "$CURRENT_LABELS" \
    --train_frac "$TRAIN_FRAC" \
    --run "$MODEL_RUN" \
    --pipeline_run_id "$PIPELINE_RUN_ID" \
    --config_fingerprint "$CONFIG_FINGERPRINT" \
    --base_seed "$BASE_SEED" \
    --dataset_seed "$CURRENT_DATASET_SEED" \
    --seed "$model_seed" \
    "$@"
}

run_physionet_pipeline() {
  CURRENT_DATASET="physionet_2012"
  CURRENT_PROCESSED_DATA="$INPUT_ROOT/processed/physionet_2012.pkl"
  CURRENT_LABELS="$INPUT_ROOT/physionet_latent_tags.csv"
  CURRENT_DATASET_SEED="$PHYSIONET_DATASET_SEED"
  local models="$PHYSIONET_OUTPUT_ROOT/models"
  local predictions="$PHYSIONET_OUTPUT_ROOT/predictions"

  run_model "$PHYSIONET_STRATS_SEED" \
    --pretrain 1 --model_type strats --hid_dim 64 --num_layers 2 --num_heads 16 \
    --dropout 0.2 --attention_dropout 0.2 --lr 5e-4 \
    --output_dir "$models/strats_pretrain" --max_epochs 100

  run_model "$PHYSIONET_STRATS_SEED" \
    --model_type strats --hid_dim 64 --num_layers 2 --num_heads 16 \
    --dropout 0.2 --attention_dropout 0.2 --lr 5e-5 \
    --init_ckpt_path "$models/strats_pretrain/checkpoint_best.bin" \
    --output_dir "$models/strats"

  run_model "$PHYSIONET_GRU_SEED" \
    --model_type gru --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --output_dir "$models/gru"
  run_model "$PHYSIONET_GRUD_SEED" \
    --model_type grud --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --output_dir "$models/grud"
  run_model "$PHYSIONET_TCN_SEED" \
    --model_type tcn --num_layers 6 --hid_dim 64 --kernel_size 4 \
    --dropout 0.2 --lr 5e-4 --output_dir "$models/tcn"
  run_model "$PHYSIONET_SAND_SEED" \
    --model_type sand --num_layers 4 --r 24 --M 12 --hid_dim 64 \
    --dropout 0.2 --lr 5e-4 --output_dir "$models/sand"

  run_model "$PHYSIONET_STRATS_SEED" \
    --model_type strats --hid_dim 64 --num_layers 2 --num_heads 16 \
    --dropout 0.2 --attention_dropout 0.2 --lr 5e-5 \
    --restore_ckpt_path "$models/strats/checkpoint_best.bin" \
    --output_dir "$models/strats" --save_pred_csv_path "$predictions/strats.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$PHYSIONET_GRU_SEED" \
    --model_type gru --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/gru/checkpoint_best.bin" \
    --output_dir "$models/gru" --save_pred_csv_path "$predictions/gru.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$PHYSIONET_GRUD_SEED" \
    --model_type grud --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/grud/checkpoint_best.bin" \
    --output_dir "$models/grud" --save_pred_csv_path "$predictions/grud.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$PHYSIONET_TCN_SEED" \
    --model_type tcn --num_layers 6 --hid_dim 64 --kernel_size 4 \
    --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/tcn/checkpoint_best.bin" \
    --output_dir "$models/tcn" --save_pred_csv_path "$predictions/tcn.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$PHYSIONET_SAND_SEED" \
    --model_type sand --num_layers 4 --r 24 --M 12 --hid_dim 64 \
    --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/sand/checkpoint_best.bin" \
    --output_dir "$models/sand" --save_pred_csv_path "$predictions/sand.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
}

run_mimic_pipeline() {
  CURRENT_DATASET="mimic_iii"
  CURRENT_PROCESSED_DATA="$INPUT_ROOT/processed/mimic_iii.pkl"
  CURRENT_LABELS="$INPUT_ROOT/mimic_latent_tags.csv"
  CURRENT_DATASET_SEED="$MIMIC_DATASET_SEED"
  local models="$MIMIC_OUTPUT_ROOT/models"
  local predictions="$MIMIC_OUTPUT_ROOT/predictions"

  run_model "$MIMIC_STRATS_SEED" \
    --pretrain 1 --model_type strats --hid_dim 64 --num_layers 2 --num_heads 16 \
    --dropout 0.2 --attention_dropout 0.2 --lr 5e-4 \
    --output_dir "$models/strats_pretrain" --max_epochs 30

  run_model "$MIMIC_STRATS_SEED" \
    --model_type strats --hid_dim 64 --num_layers 2 --num_heads 16 \
    --dropout 0.2 --attention_dropout 0.2 --lr 5e-5 \
    --init_ckpt_path "$models/strats_pretrain/checkpoint_best.bin" \
    --output_dir "$models/strats"

  run_model "$MIMIC_GRU_SEED" \
    --model_type gru --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --output_dir "$models/gru"
  run_model "$MIMIC_GRUD_SEED" \
    --model_type grud --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --output_dir "$models/grud"
  run_model "$MIMIC_TCN_SEED" \
    --model_type tcn --num_layers 4 --hid_dim 128 --kernel_size 4 \
    --dropout 0.2 --lr 5e-4 --output_dir "$models/tcn"
  run_model "$MIMIC_SAND_SEED" \
    --model_type sand --num_layers 4 --r 24 --M 12 --hid_dim 64 \
    --dropout 0.2 --lr 5e-4 --output_dir "$models/sand"

  run_model "$MIMIC_STRATS_SEED" \
    --model_type strats --hid_dim 64 --num_layers 2 --num_heads 16 \
    --dropout 0.2 --attention_dropout 0.2 --lr 5e-5 \
    --restore_ckpt_path "$models/strats/checkpoint_best.bin" \
    --output_dir "$models/strats" --save_pred_csv_path "$predictions/strats.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$MIMIC_GRU_SEED" \
    --model_type gru --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/gru/checkpoint_best.bin" \
    --output_dir "$models/gru" --save_pred_csv_path "$predictions/gru.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$MIMIC_GRUD_SEED" \
    --model_type grud --hid_dim 64 --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/grud/checkpoint_best.bin" \
    --output_dir "$models/grud" --save_pred_csv_path "$predictions/grud.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$MIMIC_TCN_SEED" \
    --model_type tcn --num_layers 4 --hid_dim 128 --kernel_size 4 \
    --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/tcn/checkpoint_best.bin" \
    --output_dir "$models/tcn" --save_pred_csv_path "$predictions/tcn.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
  run_model "$MIMIC_SAND_SEED" \
    --model_type sand --num_layers 4 --r 24 --M 12 --hid_dim 64 \
    --dropout 0.2 --lr 5e-4 \
    --restore_ckpt_path "$models/sand/checkpoint_best.bin" \
    --output_dir "$models/sand" --save_pred_csv_path "$predictions/sand.csv" \
    --predict_split all --max_epochs 0 --validate_after 0
}

cd "$SCRIPT_ROOT/src"
if (( run_physionet == 1 )); then
  run_physionet_pipeline
fi
if (( run_mimic == 1 )); then
  run_mimic_pipeline
fi
