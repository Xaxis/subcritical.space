# Subcritical

An open research program, and a site at subcritical.space, on one question: can there be a protocol
that prevents the development of artificial superintelligence while leaving useful AI free to keep
improving?

A subcritical reactor still makes useful power, but each generation of its chain reaction is
smaller than the last, so it cannot run away. Subcritical asks for the same of AI: systems that are
useful and keep getting better, held below the point where their improvement feeds on itself
faster than anyone can check it. The first half of the work defines what superintelligence is and
by what mechanisms it forms (physical, computational, dynamical, cognitive, organisational), each
measured. The second half is a protocol that limits those mechanisms, verified without trusting
any one party.

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
data/inputs.toml           every input, with its basis (measured, vendor, spec, design, assumption);
                           data/inputs/*.toml holds more, one file per part of the work
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
python3 model/subcritical.py --only miss-prob-one-channel
python3 model/subcritical.py --set inspections-per-year=12
```

## Licence

Code is MIT; text and data are CC BY 4.0. See [LICENSE](LICENSE).
