# CLAUDE.md: Subcritical

Subcritical (subcritical.space): an open research program, and the site that presents it, on a
protocol that prevents the development of artificial superintelligence while keeping useful AI
allowed and improving. About half the work defines what superintelligence is and the mechanisms
that form it (physical, computational, dynamical, cognitive, organisational), each measured; the
protocol is derived from those mechanisms. It rests on operational, testable definitions (what
superintelligence is, what approaching it is, where useful AI ends and the weapons-grade path
begins), an evidence-based ranking of which capabilities lead there, a verification design that
trusts no single party, and proofs and rerunnable experiments for each key property. The owner's
request is `00-BRIEF.md`; where the work stands is `.claude/handoffs/subcritical.md`. Read both
first.

## Rules that shape every change

- **Nothing invented.** Every number comes from `data/inputs.toml` or `data/inputs/*.toml` (one file
  per part of the work, so parallel writers never share one; each input says whether it is
  measured, a vendor claim, a spec value, a design choice or an assumption, and names its source)
  or is derived in `model/subcritical.py` or `model/parts/NN_name.py` (one module per part, like the
  inputs). Documents cite a number as a ledger link,
  `[any text](numbers.md#id)` in research/ or `[any text](../research/numbers.md#id)` in paper/, and
  `make docs` rewrites the link text to the model's value. Never type a model number by hand.
- **Every citation resolves.** Cite as `[@key]`; the key must be in `research/sources.toml` with a
  type and an identifier (DOI, arXiv ID, ISBN or URL). Prefer DOIs and arXiv IDs: Paperwright adds
  sources only by identifier. A source nobody opened is not cited.
- **Credit what exists.** Each idea is marked new, extends prior work, or prior work in
  `research/03-novelty.md`, with the closest prior work and the searches tried. "Not found" is a
  claim about our search, not about the world; say so.
- **Never overclaim.** The protocol is a design. Nothing in it has been deployed or tested against
  a real adversary, and the documents say so wherever it matters. A definition is only as good as
  the test that measures it.
- **Every contribution passes every level or is cut.** Each claimed contribution in
  `research/04-claims.md` has its result recorded in `research/07-verification.md` for each level:
  (1) an independent prior-art search by a helper that did not propose it, (2) a formal statement
  and proof, (3) working experiments on real data, (4) a red team that only tries to break it,
  (5) Paperwright's integrity, reviewer and editor desks, resolved by us, (6) a fresh reviewer who
  has not seen the work. A claim that fails a level is cut or downgraded, never argued around.
- **Experiments rerun from tools/.** Each experiment is `tools/exp/<name>.py`, deterministic given
  its seed, fetching real data or models into `tools/exp/cache/` (ignored) from a source it names,
  and writing its results to `data/results/<name>.json`. Results enter the ledger through
  `model/subcritical.py`, so documents cite them as ledger links like any other number.
- **Share the box.** CPU-heavy experiments run under `heavy`, GPU ones under `gpu` (the box's AMD
  GPU; browsers never). One heavy job at a time.
- **No em dashes** anywhere: research text, code, comments, commit messages. `make check` fails on one.
- **research/notes/ is raw research** from the survey tracks, kept as written. The research files
  and the paper cite sources through `research/sources.toml`, not through the notes.

## Commands

```sh
make model     # data/numbers.json and research/numbers.md from inputs and model
make docs      # rewrite every ledger link to the model's value
make check     # em dashes, model reproduces, docs synced, citations and sources identified
make paper     # build/subcritical-paper.md, the paper flattened for Paperwright
python3 model/subcritical.py --only ID        # one number, its formula and inputs
python3 model/subcritical.py --set ID=VALUE   # a variant

pnpm install                       # the site's workspace (Node 24, pnpm 10)
pnpm lint && pnpm typecheck && pnpm test
heavy pnpm build                   # the site, static
heavy tools/site/deploy.sh         # deploy HEAD to Vercel and prove it live
```

Gate before committing: `make model docs check` all exit 0, and for a site change `pnpm lint`,
`pnpm typecheck`, `pnpm test` and a build.

## Working here

- This repo is **public** and its site deploys through Vercel (team xaxis-projects), whose seat
  check reads the commit author. Commit as the owner, `Xaxis` with the personal address the global
  instructions give, as on corerope.space and phosphoros.space. The local pre-commit and pre-push
  hooks refuse any other author and block private project names, local paths and personal
  addresses in staged text. (The first commit, 51560a7, predates the site and is by the noreply
  address.)
- Notes that name the owner's private projects or local paths go in `.claude/handoffs/*.private.md`,
  which git ignores.
- The site is `site/` (pnpm workspace, Next.js 16, Biome, TypeScript), deployed as the Vercel
  project `subcritical` by `heavy tools/site/deploy.sh`, which uploads the committed tree (git
  archive of HEAD; pushing does not deploy) and proves it live: headers, build marker, assets,
  every sitemap page shot at 1440 and 390 px in both themes with axe (`tools/site/shots.ts`), and
  the figures and theme toggle driven in a browser (`tools/site/interact.ts`). Until the owner
  registers subcritical.space it serves https://subcritical.vercel.app, the `url` in
  `site/lib/site.ts`; switch that one line when the domain is live and rerun the deploy, which
  adds the domain once it has nameservers. The site reads `research/` and `data/` at build time
  and types no number: ledger links render the model's value, citations resolve through
  `research/sources.toml`. Port 4527 for the local server (`pnpm --filter @subcritical/site
  start` after a build). 3D, when added, follows corerope.space and phosphoros.space, with
  fallbacks without WebGL and under reduced motion.
- Python 3.11 or later. The model and checks use the standard library only; experiments that need
  more (a model runtime, numerical libraries) list it in `tools/exp/requirements.txt` and run in
  the ignored `.venv/`.
- Paperwright is reached through its MCP connector, registered in `.mcp.json`
  (`https://paperwright.diy/mcp`, OAuth). Sign in with `/mcp` if its tools are missing.
- `.claude/skills/verify/` says how to check each feature; update it in the same commit as a
  feature change.
- License: MIT for code (model/, tools/, root config), CC BY 4.0 for research/, paper/ and data/.
