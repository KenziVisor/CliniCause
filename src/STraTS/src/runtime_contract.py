"""Pure seed and model-configuration contracts for STraTS invocations."""

from __future__ import annotations

import hashlib
import json
import math
import re
from typing import Any


SEED_MODULUS = 2_147_483_647
DATASET_SEED_OFFSETS = {
    "physionet_2012": 100_000,
    "mimic_iii": 200_000,
}
MODEL_SEED_OFFSETS = {
    "strats": 1,
    "istrats": 2,
    "gru": 3,
    "grud": 4,
    "tcn": 5,
    "sand": 6,
    "interpnet": 7,
}
MODEL_CONFIG_FIELDS = (
    "model_type",
    "hid_dim",
    "num_layers",
    "num_heads",
    "dropout",
    "attention_dropout",
    "kernel_size",
    "r",
    "M",
    "max_obs",
    "max_timesteps",
    "hours_look_ahead",
    "ref_points",
    "train_frac",
    "run",
)
TRAINING_CONFIG_FIELDS = (
    "max_epochs",
    "max_steps",
    "patience",
    "lr",
    "train_batch_size",
    "gradient_accumulation_steps",
    "eval_batch_size",
    "validate_after",
    "validate_every",
)


def validate_base_seed(seed: int) -> int:
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError(f"Seed must be an integer, got {seed!r}.")
    if seed < 0 or seed >= SEED_MODULUS:
        raise ValueError(f"Seed must be in [0, {SEED_MODULUS}), got {seed!r}.")
    return seed


def _offset_seed(seed: int, offset: int) -> int:
    return (validate_base_seed(seed) + int(offset)) % SEED_MODULUS


def derive_dataset_seed(base_seed: int, dataset: str) -> int:
    try:
        offset = DATASET_SEED_OFFSETS[dataset]
    except KeyError as exc:
        raise ValueError(f"Unsupported dataset for seed derivation: {dataset!r}") from exc
    return _offset_seed(base_seed, offset)


def derive_model_seed(base_seed: int, dataset: str, model: str) -> int:
    dataset_seed = derive_dataset_seed(base_seed, dataset)
    try:
        offset = MODEL_SEED_OFFSETS[model]
    except KeyError as exc:
        raise ValueError(f"Unsupported model for seed derivation: {model!r}") from exc
    return _offset_seed(dataset_seed, offset)


def parse_model_run(run_spec: str) -> tuple[int, int]:
    match = re.fullmatch(r"([1-9]\d*)o([1-9]\d*)", str(run_spec))
    if match is None:
        raise ValueError(f"Invalid model run specification {run_spec!r}; expected <run>o<total>.")
    run, total = map(int, match.groups())
    if run > total:
        raise ValueError(
            f"Invalid model run specification {run_spec!r}; require run <= total."
        )
    return run, total


def derive_effective_seed(model_seed: int, run_spec: str) -> int:
    run, _ = parse_model_run(run_spec)
    return _offset_seed(model_seed, run)


def model_config_from_args(args: Any, architecture_mode: str) -> dict[str, Any]:
    if architecture_mode not in {"pretrain", "finetune", "scratch"}:
        raise ValueError(f"Unsupported architecture mode: {architecture_mode!r}")
    config = {
        field: getattr(args, field)
        for field in MODEL_CONFIG_FIELDS
        if hasattr(args, field)
    }
    config["architecture_mode"] = architecture_mode
    return config


def training_config_from_args(args: Any) -> dict[str, Any]:
    """Capture the effective optimizer and training schedule for provenance."""

    return {
        field: getattr(args, field)
        for field in TRAINING_CONFIG_FIELDS
        if hasattr(args, field)
    }


def validate_training_config(config: dict[str, Any]) -> dict[str, Any]:
    expected = set(TRAINING_CONFIG_FIELDS)
    actual = set(config)
    if actual != expected:
        raise ValueError(
            "Training configuration fields mismatch: "
            f"missing={sorted(expected - actual)} extra={sorted(actual - expected)}"
        )
    integer_fields = expected - {"lr"}
    for field in integer_fields:
        value = config[field]
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"Training configuration {field} must be an integer.")
    if config["max_epochs"] < 0 or config["max_steps"] < 0:
        raise ValueError("Training epoch/step limits must be nonnegative.")
    for field in (
        "patience",
        "train_batch_size",
        "gradient_accumulation_steps",
        "eval_batch_size",
        "validate_every",
    ):
        if config[field] <= 0:
            raise ValueError(f"Training configuration {field} must be positive.")
    lr = config["lr"]
    if isinstance(lr, bool) or not isinstance(lr, (int, float)):
        raise ValueError("Training configuration lr must be numeric.")
    if not math.isfinite(float(lr)) or float(lr) <= 0:
        raise ValueError("Training configuration lr must be finite and positive.")
    return dict(config)


def scientific_config_fingerprint(
    model_config: dict[str, Any],
    training_config: dict[str, Any],
) -> str:
    payload = json.dumps(
        {
            "model_config": model_config,
            "training_config": training_config,
        },
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
