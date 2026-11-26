# Model

Every derived number, computed from `data/inputs.toml` by `model/detent.py` through
`model/ledger.py`, with its formula, inputs, basis and the line that defines it.

<!-- covers: cli:model, job:make-model -->

## Sub-features

- all: `python3 model/detent.py` prints every number with its basis.
- only: `--only ID` prints one number, its formula, each input's value.
- set: `--set ID=VALUE` (repeatable) reruns with an input changed; an unknown ID is an error.
- json: `--json` prints the ledger as JSON.
- write: `--write` (= `make model`) writes `data/numbers.json` and `research/numbers.md`.

## How to check it

```sh
python3 model/detent.py --only miss-prob-one-channel; echo "exit $?"
python3 model/detent.py --set inspections-per-year=12 | grep miss-prob-one-channel
python3 model/detent.py --set no-such-input=1; echo "exit $? (expect a KeyError)"
make model && git diff --stat data/numbers.json research/numbers.md
```

Expect: the first prints 30% with its three inputs and exits 0; the second shows 3%; the third
fails naming the unknown input; the last shows no diff when inputs did not change.
