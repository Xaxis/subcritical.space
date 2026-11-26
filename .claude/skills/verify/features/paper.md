# Paper

`tools/paper.py` flattens paper/*.md for Paperwright: ledger links become their text, and the
cited sources become `build/subcritical.bib` with their identifiers.

<!-- covers: cli:paper -->

## How to check it

```sh
make paper && head -5 build/subcritical-paper.md && python3 tools/paper.py --ids
```

Expect: both files written; `--ids` prints one identifier per cited source. Until paper/ has
sections, the paper is empty and the count is 0.
