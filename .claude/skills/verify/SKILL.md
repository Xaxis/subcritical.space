---
name: verify
description: Verify Detent (a research repository: a Python model that computes every published number, a docs sync that writes those numbers into the Markdown, a check that every citation resolves, a paper build for Paperwright, and experiments under tools/exp/). Has the feature map, the static checks and a proven recipe for each feature. Use to prove a change in this repo works, to find where a feature lives, or to see what a change could break.
---

# Verify Detent

`FM=~/.claude/claude-core/bin/featuremap`

- **Where does a feature live?** `features.json` (`id`, `entry`, `reach`), then `features/<area>.md`.
- **What did my change touch?** `$FM affected`. A change to `data/inputs.toml` or
  `model/detent.py` reaches every document that links a number: run `make model docs check`.
- **Keeping it current:** when you add, rename, move or remove a feature (an experiment under
  `tools/exp/` is one), run `$FM generate --write`, update the matching `features/<area>.md`, and
  confirm `$FM check` exits 0, in the same commit.

## Static checks

| Check | Command | Proves | Baseline |
|---|---|---|---|
| check | `make check` | no em dash in any tracked file; the model reproduces data/numbers.json and research/numbers.md; every ledger link shows the model's value; every `[@key]` names a source with a type and an identifier; every sourced input's source exists | passes, under 1 s |

Known pre-existing failures: none.

## Launch

Nothing to launch: no server, no site. The model and checks run with Python 3.11 or later and the
standard library. The paper is published in Paperwright through its connector (`.mcp.json`).
