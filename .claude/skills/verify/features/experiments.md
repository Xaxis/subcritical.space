# Experiments

The experiments in `tools/exp/`, numbered in `research/04-claims.md`. Each fetches real data into
`tools/exp/cache/` through `tools/exp/lib.py`, is deterministic given its seed, and writes
`data/results/<name>.json`; `make model` loads each result's `numbers` into the ledger with basis
`experiment` (`model/ledger.py`, `_load_results`). The contract is `tools/exp/README.md`.

<!-- covers: cli:e02-time-horizons -->

## Sub-features

- e02-time-horizons (E2): refits METR's frontier time-horizon trend from its published YAML: the
  50% and 80% doubling times, an interval from resampling models within their published intervals,
  the 50%-to-80% horizon ratio and whether it is stable, shrinking or growing, the latest frontier
  horizon, and our refit over METR's figure.

## How to check it

```sh
uv venv .venv && uv pip install --python .venv/bin/python -r tools/exp/requirements.txt  # once
.venv/bin/python tools/exp/e02_time_horizons.py && cp data/results/e02_time_horizons.json /tmp/h.json
.venv/bin/python tools/exp/e02_time_horizons.py && cmp data/results/e02_time_horizons.json /tmp/h.json && echo identical
python3 model/subcritical.py --only e2-refit-over-metr
```

Expect: `wrote data/results/e02_time_horizons.json (12 numbers)` both times and `identical` (deterministic);
the ledger shows `e2-refit-over-metr` at 1.00 (the refit reproduces METR's published doubling
time) with basis experiment. A results file naming a script that does not exist makes the model
fail.
