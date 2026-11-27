# Docs

The ledger links in research/ and paper/ and the repository check.

<!-- covers: cli:sync, cli:check, cli:sources-from-notes -->

## Sub-features

- sync: `make docs` rewrites each `[text](numbers.md#id)` to the model's value; `--check` only reports.
  It leaves the survey notes and the verification reports as written: they are records.
- check: `make check` runs every promise in `tools/check.py`'s docstring, including that every
  experiment result is strict JSON and ran on the ledger's current inputs (an input removed or
  changed upstream fails it until the experiment is rerun).
- sources-from-notes: `python3 tools/sources_from_notes.py [--write]` adds the sources each survey
  note lists in its ```toml block to `research/sources.toml`, skipping any that fail the check's rules
  and never overwriting an existing key, and folds entries that name one work (a shared DOI, arXiv
  ID however written, ISBN or URL) into one key with the others as `aliases`. The site resolves an
  alias to its work; `make check` fails on two entries for one work, and on research, paper or an
  input naming an alias instead of the key.

## How to check it

```sh
make docs && make check; echo "exit $?"
sed -i 's/\[[^]]*\](numbers.md#miss-prob-one-channel)/[stale](numbers.md#miss-prob-one-channel)/' research/00-memo.md
python3 tools/sync.py --check; echo "exit $? (expect 1)"; make docs && git diff --stat research/00-memo.md
python3 tools/sources_from_notes.py; echo "exit $?"
cp data/results/e24_response_latency.json /tmp/e24.json
python3 -c "import json;p='data/results/e24_response_latency.json';d=json.load(open(p));k=next(iter(d['details']['ledger_inputs']));d['details']['ledger_inputs'][k]=-1;open(p,'w').write(json.dumps(d))"
python3 tools/check.py 2>&1 | grep results; cp /tmp/e24.json data/results/e24_response_latency.json
```

Expect: the first exits 0; the stale link makes `--check` exit 1, and `make docs` restores it (no
diff). The dry run of sources-from-notes exits 0 and reports `0 new keys` and `0 folded as aliases` once
every note is merged, listing any entry it skipped and why. The tampered result makes the check print
`ledger input ... ran at -1` and `FAIL results`; restoring the file clears it.
