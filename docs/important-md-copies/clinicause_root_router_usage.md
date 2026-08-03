# Router usage

The unified router is implemented in [router.py](router.py). It orchestrates preprocessing, latent tagging, decision-tree plotting, STraTS preparation/execution, prediction normalization, and the thesis main pipeline.

## Requirements

- Python 3.9+
- The two repositories must be present:
  - [causal-irregular-time-series](causal-irregular-time-series)
  - [STraTS](STraTS)
- Raw dataset folders must be available on the machine where the router is executed.
- The router is intended to be run later on the remote server; it should not be executed locally unless the data is available.

## Minimal examples

### Validate configuration only

```bash
python router.py --dataset both --run-id demo_run --strats-repo-root ./STraTS --validate-only
```

### Dry run

```bash
python router.py --dataset both --run-id demo_run --strats-repo-root ./STraTS --stages all --dry-run
```

### Full run

```bash
python router.py \
  --dataset both \
  --run-id full_001 \
  --output-root runs \
  --thesis-repo-root ./causal-irregular-time-series \
  --strats-repo-root ./STraTS \
  --physionet-raw-data-path /path/to/physionet2012 \
  --mimic-raw-data-path /path/to/mimiciii \
  --stages all \
  --overwrite
```

## Important flags

- `--dataset {physionet,mimic,both}`
- `--run-id <name>`
- `--output-root <path>`
- `--thesis-repo-root <path>`
- `--strats-repo-root <path>`
- `--stages <comma-separated-list>`
- `--physionet-raw-data-path <path>`
- `--mimic-raw-data-path <path>`
- `--dry-run`
- `--validate-only`
- `--skip-existing`
- `--overwrite`
- `--run-strats {true,false}`
