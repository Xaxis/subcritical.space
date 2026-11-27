# Formal checks

`research/05-formal.md` states each claim's theorem and proves it. Every statement with numerical
content has a deterministic check in `tools/formal/<claim>.py` (standard library, seeded random
instances, edge cases), which exits 1 and prints the counterexample if the statement fails.
`tools/formal/run_all.py` runs them all. A counterexample means the statement is wrong: fix the
statement, never the check.

<!-- covers: cli:formal-checks -->

## Sub-features

- formal-checks: one check per claim with numerical content (c1 to c11, the runaway condition, the
  inspection-game equilibrium), sharing `tools/formal/_lib.py`.

## How to check it

```sh
heavy python3 tools/formal/run_all.py      # a few minutes on one core
```

Expect: an `ok` line for every check and exit 0. To see that a check can fail, break the statement
it tests in a scratch copy (for example flip the inequality in `c1_margin.py`'s condition) and run
that file: it must exit 1 with a counterexample.
