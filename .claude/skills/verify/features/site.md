# Site

subcritical.space: the Next.js site in `site/`,
rendered at build time from `research/` and `data/`, deployed by `tools/site/deploy.sh`.

<!-- covers: page:/, page:/paper, page:/research, page:/research/[slug], page:/notes/[slug], page:/verification/[slug], page:/experiments, page:/numbers, page:/sources, api:GET /apple-icon, api:GET /manifest.webmanifest, api:GET /opengraph-image, api:GET /robots.txt, api:GET /sitemap.xml -->

## Sub-features

- `/`: what the work is and what the tests found, in chapters. A hero on a dark stage (the
  `.on-dark` tokens, in both themes; its background is the colour the 3D stage renders empty space
  at, so the canvas has no edge) with the coupled loops in 3D (`Stage` with `step={1}`, a closer
  camera) and four counts computed at build time: claims that passed all six levels (from the
  record), experiments with results (the plan and `data/results/`), ledger numbers, sources. Then:
  the line (D4) and the loop gain (D2) with their figures, the coupled loops (Y3) in 3D at full
  width, the detection bound, which starts from the ledger's inputs and gives E5's fitted discovery
  rate as an upper bound, and, once `research/07-verification.md` exists, "What the tests found":
  `site/components/ClaimCards.tsx` groups the record's claims by standing, each card with its
  standing's detail, its L3 cell and a mark per level (word and shape, never colour alone), and the
  full grid (`VerificationGrid.tsx`) behind a disclosure. `site/lib/verification.ts` parses "## The
  record" (one row per claim, one column per level, each cell opening with a bold status from a
  fixed vocabulary; an unknown status fails the build). Then the pathways as
  `research/02-pathways.md` ranks them (`site/lib/pathways.ts`, columns found by name), and the
  plan's progress as cards, read from which files exist (`site/lib/progress.ts`: written is not
  verified). The memo's pre-survey candidates are no longer on the home page; `/research/memo`
  keeps them.
- `/paper`: every `paper/*.md` in order on one page (`paperSections` in `site/lib/docs.ts`; the part
  comes from the file's number: 1x Part I, 2x Part II, 3x Part III), each file's title an h2
  anchored by its file name, its own headings shifted down a level with ids prefixed by it
  (`Markdown shift idPrefix`, so sections that share a heading never share an id), with the
  draft's status stated in the lead. In the sitemap once `paper/` has a file.
- 3D: `site/components/three/` (from corerope.space): `Stage.tsx` loads three.js only near the
  screen, releases it far away, pauses off screen, offers a pause button, holds a still frame under
  reduced motion and says in words what it shows without WebGL; `kit.ts` the renderer and bloom;
  `scenes/loops.ts` five loops stepped by `site/lib/loops.ts` (x' = G x + u, spectral radius).
  Shaders must clamp every `pow()` and `sqrt()` base (a NaN blacks out the bloom on real GPUs and
  not on SwiftShader).
- `/research`: the paper first, then the documents as cards grouped by part (by file number), each
  with its lead as plain text (a card is one link) and a reading time, then the verification reports
  and the survey tracks. `/research/[slug]`: every `research/*.md` except the ledger; `/notes/[slug]`
  the survey notes. Reading pages keep prose at a measure and let tables take the whole column
  (`.page-main` is a size container; `.prose .table-wrap` is `100cqi` wide and scrolls). Ledger links render the model's value as `a.num`, citations `[@key]` link to
  `/sources#key`, links between research files go to their pages (`site/lib/text.ts`). A
  citation's label is the first author's surname or the organisation's name and the year
  (`citeLabel` in `site/lib/text.ts`; affiliations in brackets dropped; a test runs it over every
  source).
- `/verification/[slug]`: each report in `research/verification/` (the levels run by helpers who
  wrote none of the work), listed on `/research`. Its links one level up (`../04-claims.md`,
  `../numbers.md#id`) resolve like any document's, in the site (`docHref`, `ledgerId`) and in
  `tools/check.py`. A report is a record: `make docs` leaves its numbers as written, and the page
  shows them dotted (`Markdown asWritten`), each titled with what the ledger shows now.
- `/experiments`: the plan in `research/04-claims.md` "## Experiments", parsed by
  `site/lib/experiments.ts` (code, title, what it does, CPU or GPU, its script, what it serves). A
  map of every experiment by phase (filled: has results) links to its card. Each card shows, first,
  the L3 cell of each claim it serves (from the record, labelled as the claim's level 3 on all its
  experiments), then folds what it does and, once `data/results/<script>.json` exists, all its
  numbers through the ledger, its data with sha256 and its seed. Only in the sitemap once the
  claims file exists.
- `/numbers`: `data/numbers.json` as one folding group per file it comes from (inputs by part,
  derived by model part, results by experiment), a row per number (`details#id`: id, label, value;
  opened, its basis, formula, inputs, source, note and where it is defined). `LedgerFilter.tsx`
  (client) searches ids and labels, which unfolds the groups with a match, and filters by basis,
  which only thins rows; a link to `/numbers#id` opens that row and its group and scrolls to it.
  Without script every group still opens by hand. `/sources`: `research/sources.toml`.
- Share card, home-screen icon, manifest, robots and sitemap; the sitemap lists every page and is
  what `tools/site/shots.ts` checks.

## How to check it

```sh
pnpm lint && pnpm typecheck && pnpm test          # test/content.test.ts: memo parse, links, port, loops, ranking, plan, experiments, labels
cd site && ~/.claude/claude-core/bin/heavy npx next build && (npx next start -p 4527 &) && cd ..
~/.claude/claude-core/bin/heavy node tools/site/shots.ts --url http://localhost:4527
~/.claude/claude-core/bin/heavy node tools/site/interact.ts --url http://localhost:4527
```

Expect: tests pass (11, the last parsing the verification record); the build lists every page as static; shots.ts prints `"ok":true` with
each sitemap page at 200 and `/no-such-page` at 404, no scroller that overflows with an opaque
background of its own (it stalls the full-page capture under SwiftShader for a minute or more a
segment; `tools/lib/scrollers.ts` names it, and the fix is to colour the content, as `.table-wrap`
and `.prose pre` do), and writes shots to `out/site-shots/` (look at
the ones you changed, both themes, both widths); interact.ts prints its `ok` lines and exits 0 (among them the 3D stage
drawing, turning supercritical together at c = 0.1, the reduced-motion still frame and the words
shown without WebGL). For `/numbers`, in a browser: `/numbers#miss-prob-one-channel` opens that
row inside its open group, in view; typing `breakout` leaves only matching rows with their groups
open; switching a basis off thins the rows and leaves groups as they were; clearing folds them.
Stop the server you started afterwards.

Live: `~/.claude/claude-core/bin/heavy tools/site/deploy.sh` (or `--check` for an existing
deploy) runs all of the above against the production address and ends `site ok: <sha> is live`.
