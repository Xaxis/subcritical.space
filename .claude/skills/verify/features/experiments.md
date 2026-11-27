# Experiments

The experiments in `tools/exp/`, numbered in `research/04-claims.md`. Each fetches real data into
`tools/exp/cache/` through `tools/exp/lib.py`, is deterministic given its seed, and writes
`data/results/<name>.json`; `make model` loads each result's `numbers` into the ledger with basis
`experiment` (`model/ledger.py`, `_load_results`). The contract is `tools/exp/README.md`.

<!-- covers: cli:e02-time-horizons, cli:e05-detection, cli:e08-footprint-floor, cli:e24-response-latency -->

## Sub-features

- e02-time-horizons (E2): refits METR's frontier time-horizon trend from its published YAML: the
  50% and 80% doubling times, an interval from resampling models within their published intervals,
  the 50%-to-80% horizon ratio and whether it is stable, shrinking or growing, the latest frontier
  horizon, and our refit over METR's figure.
- e05-detection (E5): C3's Monte Carlo of detection time per evader path, with channels that share
  a trust anchor merged, against the memo's product; and a survival fit of the covert-programme
  discovery rate over the case table `tools/exp/data/e05_detection.csv`. Reads ledger inputs by id.
- e08-footprint-floor (E8): chips, energy and power for a run from the ledger's monitored budget to
  1e27 FLOP, year by year, a Monte Carlo over the uncertain inputs, each facility channel's margin
  and the year the floor crosses below it. Ledger inputs only; nothing fetched.
- e24-response-latency (E24): the time from a confirmed finding to a response in the arms-control
  record, case by case from `tools/exp/data/e24_response_latency.csv`, by response type.
- A case table's sources not yet listed sit in `tools/exp/data/<name>.sources.toml`, merged by
  `tools/sources_from_notes.py --write`.

## How to check it

```sh
uv venv .venv && uv pip install --python .venv/bin/python -r tools/exp/requirements.txt  # once
.venv/bin/python tools/exp/e02_time_horizons.py && cp data/results/e02_time_horizons.json /tmp/h.json
.venv/bin/python tools/exp/e02_time_horizons.py && cmp data/results/e02_time_horizons.json /tmp/h.json && echo identical
python3 model/subcritical.py --only e2-refit-over-metr
```

For any experiment, the same rerun-and-compare, without the network for E5, E8 and E24:

```sh
for e in e05_detection e08_footprint_floor e24_response_latency; do
  cp data/results/$e.json /tmp/$e.json && .venv/bin/python tools/exp/$e.py && cmp data/results/$e.json /tmp/$e.json && echo "$e identical"
done
```

Expect: `wrote data/results/e02_time_horizons.json (12 numbers)` both times and `identical` (deterministic);
the ledger shows `e2-refit-over-metr` at 1.00 (the refit reproduces METR's published doubling
time) with basis experiment. A results file naming a script that does not exist makes the model
fail. E5, E8 and E24 print `identical` (about 15 s, 3 s and 15 s on one core).
