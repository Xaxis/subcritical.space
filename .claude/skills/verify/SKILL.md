---
name: verify
description: Verify Subcritical (a research repository: a Python model that computes every published number, a docs sync that writes those numbers into the Markdown, a check that every citation resolves, a paper build for Paperwright, experiments under tools/exp/, and the Next.js site in site/ deployed to Vercel). Has the feature map, the static checks and a proven recipe for each feature. Use to prove a change in this repo works, to find where a feature lives, or to see what a change could break.
---

# Verify Subcritical

`FM=~/.claude/claude-core/bin/featuremap`

- **Where does a feature live?** `features.json` (`id`, `entry`, `reach`), then `features/<area>.md`.
- **What did my change touch?** `$FM affected`. A change to `data/inputs.toml` or
  `model/subcritical.py` reaches every document that links a number: run `make model docs check`.
- **Keeping it current:** when you add, rename, move or remove a feature (an experiment under
  `tools/exp/` is one), run `$FM generate --write`, update the matching `features/<area>.md`, and
  confirm `$FM check` exits 0, in the same commit.

## Static checks

| Check | Command | Proves | Baseline |
|---|---|---|---|
| check | `make check` | no em dash in any tracked file; the model reproduces data/numbers.json and research/numbers.md; every ledger link shows the model's value; every `[@key]` names a source with a type and an identifier; every sourced input's source exists | passes, under 1 s |
| lint | `pnpm lint` | Biome over site/ and tools/ | passes |
| typecheck | `pnpm typecheck` | the site's TypeScript | passes |
| test | `pnpm test` | site/test/content.test.ts: the memo parses, links and citations resolve, the detection port matches the model | 5 pass |
| build | `heavy pnpm build` | every page builds static | passes |

Known pre-existing failures: none.

## Launch

The model and checks run with Python 3.11 or later and the standard library. The site: `pnpm
install`, then in site/ `heavy npx next build` and `npx next start -p 4527` (this project's port).
See `features/site.md` for the browser checks and the deploy. The paper is published in
Paperwright through its connector (`.mcp.json`).
