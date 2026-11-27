# Experiments

Each experiment is one script, `tools/exp/<name>.py`, numbered in `research/04-claims.md` (E1,
E2, ...), which is where the list and the claims each one serves are kept.

## The contract

- **Real data.** It fetches public data or models from a source it names, through `lib.fetch`,
  into `tools/exp/cache/` (ignored by git). The result records each file's URL and sha256, so a
  rerun on changed data is visible.
- **Deterministic.** All randomness comes from `lib.rng(seed)` (or a numpy generator seeded from
  it). The same data and seed write the same result file, byte for byte.
- **One result file.** `lib.Results(...).write()` writes `data/results/<name>.json`: the
  experiment's code, the script, the seed, the data it read, its `numbers` and any `details`.
- **Into the ledger.** `make model` loads every result file's `numbers` with basis `experiment`, so
  documents cite them as ledger links like any other number. Ids start with the experiment's code
  in lower case (`e2-...`). A derived number built on a result goes in the model as usual.
- **The box is shared.** CPU work runs as `heavy python3 tools/exp/<name>.py`,
  GPU work (the box's AMD card, ROCm) under `gpu`. One heavy job at a time.
- **Dependencies.** `lib.py` is standard library only. An experiment that needs more lists it in
  `tools/exp/requirements.txt` and runs in the ignored `.venv/`:

  ```sh
  uv venv .venv && uv pip install --python .venv/bin/python -r tools/exp/requirements.txt
  .venv/bin/python tools/exp/<name>.py
  ```

- **Honest output.** A result that refutes a claim is written and cited like one that supports it.
  A script that cannot reach its data fails; it never falls back to made-up numbers.
