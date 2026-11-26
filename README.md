# Detent

An open research program on one question: can there be a protocol that prevents the development
of artificial superintelligence while leaving useful AI free to keep improving?

A detent is the catch in a mechanism that lets it move freely up to a point and holds it there. In
a chronometer's detent escapement it releases the wheel one tooth at a time. In diplomacy, détente
is rivals agreeing to limits they can check. Detent asks for both: a precise, measurable line
between useful AI and the path to superintelligence, and a way for rivals to verify that nobody
crosses it without trusting one another.

## Status

**Just started (2026-11-26).** The candidate definitions and the protocol's shape are in
`research/00-memo.md`. They are candidates, not findings. Nothing here has been deployed or tested
against a real adversary. Each claimed contribution will be recorded with its result at every level
of checking (an independent prior-art search, a proof, experiments on real data, a red team, paper
review and a fresh reviewer), and anything that fails a level is cut or downgraded.

## Layout

```
00-BRIEF.md                the request this program answers
research/00-memo.md        the first memo: candidate definitions, the protocol's shape
research/notes/            the survey tracks, raw, with their sources
research/numbers.md        the ledger: every number, generated, never edited by hand
research/sources.toml      every source, with its identifier
data/inputs.toml           every input, with its basis (measured, vendor, spec, design, assumption)
model/                     the model that derives every other number
tools/                     docs sync, the repository check, the paper build; tools/exp/ the experiments
paper/                     the paper, in Markdown, built for Paperwright by tools/paper.py
```

## Reproduce

You need Python 3.11 or later.

```sh
make model                                   # every number, from inputs and model
make docs                                    # write those numbers into the documents
make check                                   # em dashes, reproducibility, sync, every citation
python3 model/detent.py --only miss-prob-one-channel
python3 model/detent.py --set inspections-per-year=12
```

## Licence

Code is MIT; text and data are CC BY 4.0. See [LICENSE](LICENSE).
