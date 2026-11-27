# Experiments

The experiments in `tools/exp/`, numbered in `research/04-claims.md`. Each fetches real data into
`tools/exp/cache/` through `tools/exp/lib.py`, is deterministic given its seed, and writes
`data/results/<name>.json`; `make model` loads each result's `numbers` into the ledger with basis
`experiment` (`model/ledger.py`, `_load_results`). The contract is `tools/exp/README.md`.

<!-- covers: cli:e01-capability-compute, cli:e02-time-horizons, cli:e04-loop-gain, cli:e05-detection, cli:e06-games, cli:e08-footprint-floor, cli:e09-returns, cli:e11-coupled-loops, cli:e24-response-latency, cli:e25-licence-log -->

## Sub-features

- e01-capability-compute (E1): Epoch's model data joined to the capability index; the compute share
  and algorithmic rate by sample (reported as not identified when samples disagree), drift per OOM,
  Ho et al.'s fit and bootstrap reproduced, out-of-sample forecasts, the GPQA expert verdicts.
- e02-time-horizons (E2): refits METR's frontier time-horizon trend from its published YAML: the
  50% and 80% doubling times, an interval from resampling models within their published intervals,
  the 50%-to-80% horizon ratio and whether it is stable, shrinking or growing, the latest frontier
  horizon, and our refit over METR's figure.
- e04-loop-gain (E4): (a) the NanoGPT speedrun record coded by source of gain; (c) coverage, bias,
  false alarms and misses of the loop-gain estimator and the r and K triggers at calibrated and
  favourable round noise, with strategic sandbaggers. About 3 minutes; run under heavy.
- e05-detection (E5): C3's Monte Carlo of detection time per evader path, with channels that share
  a trust anchor merged, against the memo's product; and a survival fit of the covert-programme
  discovery rate over the case table `tools/exp/data/e05_detection.csv`. Reads ledger inputs by id.
- e06-games (E6): the published race and coalition games reproduced from their papers' parameters
  (`tools/exp/data/e06_games.csv`), compliance-only disclosure tested, C7's conditions mapped,
  repeated play and staged accumulation. About 2.5 minutes; run under heavy.
- e08-footprint-floor (E8): chips, energy and power for a run from the ledger's monitored budget to
  1e27 FLOP, year by year, a Monte Carlo over the uncertain inputs, each facility channel's margin
  and the year the floor crosses below it. Ledger inputs only; nothing fetched.
- e09-returns (E9): returns to research refitted across domains from the authors' own data, with
  compute's share free; reports r and the fixed-compute gain K, and what is not identified.
- e11-coupled-loops (E11): Part I's coupled-loop graph from the ledger, which entries are measured,
  the row-sum floor, rho(U) and the smallest gate sets, the cross-party bound from capability-index
  growth. About 2 s.
- e24-response-latency (E24): the time from a confirmed finding to a response in the arms-control
  record, case by case from `tools/exp/data/e24_response_latency.csv`, by response type.
- e25-licence-log (E25): a header-chain verifier over Bitcoin's real headers; licence spans, the
  powered-time budget, the rate floor's false stops, forging costs under rules G and W. About 10 s
  once the headers are cached.
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
for e in e05_detection e08_footprint_floor e09_returns e11_coupled_loops e24_response_latency e25_licence_log; do
  cp data/results/$e.json /tmp/$e.json && .venv/bin/python tools/exp/$e.py && cmp data/results/$e.json /tmp/$e.json && echo "$e identical"
done
```

Expect: `wrote data/results/e02_time_horizons.json (12 numbers)` both times and `identical` (deterministic);
the ledger shows `e2-refit-over-metr` at 1.00 (the refit reproduces METR's published doubling
time) with basis experiment. A results file naming a script that does not exist makes the model
fail. Each prints `identical` (E9 about 20 s, E11 2 s, E25 10 s once cached). E1, E4 and E6 take
minutes: run each under `~/.claude/claude-core/bin/heavy` and compare the same way.
