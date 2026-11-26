# Docs

The ledger links in research/ and paper/ and the repository check.

<!-- covers: cli:sync, cli:check -->

## Sub-features

- sync: `make docs` rewrites each `[text](numbers.md#id)` to the model's value; `--check` only reports.
- check: `make check` runs every promise in `tools/check.py`'s docstring.

## How to check it

```sh
make docs && make check; echo "exit $?"
sed -i 's/\[[^]]*\](numbers.md#miss-prob-one-channel)/[stale](numbers.md#miss-prob-one-channel)/' research/00-memo.md
python3 tools/sync.py --check; echo "exit $? (expect 1)"; make docs && git diff --stat research/00-memo.md
```

Expect: the first exits 0; the stale link makes `--check` exit 1, and `make docs` restores it (no diff).
