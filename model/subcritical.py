#!/usr/bin/env python3
"""Subcritical's model: every derived number in the research and the paper.

  python3 model/subcritical.py                 every number
  python3 model/subcritical.py --only ID       one number with its formula and inputs
  python3 model/subcritical.py --set ID=VALUE  rerun with an input changed (repeatable)
  python3 model/subcritical.py --json          every number as JSON
  python3 model/subcritical.py --write         write data/numbers.json and research/numbers.md

Inputs are in data/inputs.toml with their basis and source. This file only derives. Experiment
results under tools/exp/ enter the ledger here, so documents cite them as ledger links.

Sections so far: the detection bound (the memo's starting formula, research/00-memo.md).
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ledger import Ledger, write_outputs  # noqa: E402


def here() -> str:
    return f"model/subcritical.py#L{sys._getframe(1).f_lineno}"


def build(overrides: dict | None = None) -> Ledger:
    L = Ledger(overrides=dict(overrides or {}))

    # -----------------------------------------------------------------------------------------
    # The detection bound. A secret program that must run for T years before it reaches the line
    # is missed by inspections arriving as a Poisson process at rate lam a year, each catching it
    # with probability p, with probability exp(-lam * p * T). Placeholder parameters, all design
    # or assumption, until the verification survey replaces them with sourced ones.

    L.derive(
        "miss-prob-one-channel",
        lambda q: math.exp(-q["inspections-per-year"] * q["detect-prob-per-inspection"] * q["breakout-years"]),
        "exp(-inspections-per-year * detect-prob-per-inspection * breakout-years)",
        fmt="%",
        label="chance one inspection channel misses a secret program for its whole breakout time",
        defined_in=here(),
    )
    return L


def parse_overrides(argv: list[str]) -> dict:
    out = {}
    for i, arg in enumerate(argv):
        if arg == "--set":
            key, _, value = argv[i + 1].partition("=")
            out[key] = value
    return out


def main(argv: list[str]) -> int:
    ledger = build(parse_overrides(argv))
    if "--write" in argv:
        write_outputs(ledger)
        print(f"wrote data/numbers.json and research/numbers.md ({len(ledger.order)} numbers)")
        return 0
    if "--json" in argv:
        print(json.dumps(ledger.to_json(), indent=2))
        return 0
    if "--only" in argv:
        key = argv[argv.index("--only") + 1]
        q = ledger.q[key]
        print(f"{key} = {q.display()}  ({q.basis})")
        if q.formula:
            print(f"  formula: {q.formula}")
            for i in q.inputs:
                print(f"  {i} = {ledger.q[i].display()}")
        return 0
    for key in ledger.order:
        q = ledger.q[key]
        print(f"{key:40} {q.display():>24}  {q.basis}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
