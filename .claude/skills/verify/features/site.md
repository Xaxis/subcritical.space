# Site

subcritical.space (until registered, https://subcritical.vercel.app): the Next.js site in `site/`,
rendered at build time from `research/` and `data/`, deployed by `tools/site/deploy.sh`.

<!-- covers: page:/, page:/research, page:/research/[slug], page:/notes/[slug], page:/numbers, page:/sources, api:GET /apple-icon, api:GET /manifest.webmanifest, api:GET /opengraph-image, api:GET /robots.txt, api:GET /sitemap.xml -->

## Sub-features

- `/`: the memo read as structure (`site/lib/memo.ts`): perspectives and mechanisms, definitions,
  pathways, protocol planks; three figures (`site/components/figures/`): the loop gain (D2), the
  line (D4) and the detection bound, which starts from the ledger's inputs; the plan's progress,
  read from which files exist (`site/lib/progress.ts`).
- `/research`, `/research/[slug]`: every `research/*.md` except the ledger; `/notes/[slug]` the
  survey notes. Ledger links render the model's value as `a.num`, citations `[@key]` link to
  `/sources#key`, links between research files go to their pages (`site/lib/text.ts`).
- `/numbers`: `data/numbers.json`, each entry anchored by id. `/sources`: `research/sources.toml`.
- Share card, home-screen icon, manifest, robots and sitemap; the sitemap lists every page and is
  what `tools/site/shots.ts` checks.

## How to check it

```sh
pnpm lint && pnpm typecheck && pnpm test          # test/content.test.ts: memo parse, links, port
cd site && ~/.claude/claude-core/bin/heavy npx next build && (npx next start -p 4527 &) && cd ..
~/.claude/claude-core/bin/heavy node tools/site/shots.ts --url http://localhost:4527
~/.claude/claude-core/bin/heavy node tools/site/interact.ts --url http://localhost:4527
```

Expect: tests pass (5); the build lists every page as static; shots.ts prints `"ok":true` with
each sitemap page at 200 and `/no-such-page` at 404, and writes shots to `out/site-shots/` (look at
the ones you changed, both themes, both widths); interact.ts prints its `ok` lines and exits 0.
Stop the server you started afterwards.

Live: `~/.claude/claude-core/bin/heavy tools/site/deploy.sh` (or `--check` for an existing
deploy) runs all of the above against the production address and ends `site ok: <sha> is live`.
