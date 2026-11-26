"""The ledger: every number Subcritical publishes, with its value, unit, basis and where it comes from.

Inputs live in data/inputs.toml. Each one says what kind of number it is:
  measured    an independent measurement, with a source and a date
  vendor      a claim by an interested party (a company about itself), with a source
  spec        fixed by a protocol specification (a BIP, a consensus rule)
  design      a choice this design makes, stated as a choice
  assumption  a number we picked where no source fixes it, stated as an assumption
  modelled    the output of someone else's published model, with its source

Derived quantities are defined in model/subcritical.py as functions of other quantities. The ledger
evaluates them in order, records the inputs each one read, and renders the results.
"""

from __future__ import annotations

import json
import math
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent
BASES = {"measured", "vendor", "spec", "design", "assumption", "modelled", "derived"}


@dataclass
class Quantity:
    id: str
    value: float
    unit: str
    basis: str
    fmt: str = ",.0f"
    label: str = ""
    source: str = ""
    date: str = ""
    note: str = ""
    formula: str = ""
    inputs: list[str] = field(default_factory=list)
    defined_in: str = ""

    def display(self) -> str:
        return render(self.value, self.fmt, self.unit)


def render(value: float, fmt: str, unit: str) -> str:
    if fmt == "%":
        text = f"{value * 100:.0f}%"
    elif fmt.endswith("%"):
        text = f"{value * 100:{fmt[:-1]}f}%"
    elif fmt == "sig2":
        text = sig(value, 2)
    elif fmt == "sig3":
        text = sig(value, 3)
    else:
        text = format(value, fmt)
    if unit in ("", "%"):
        return text
    if unit.startswith("/"):
        return f"{text}{unit}"
    return f"{text} {unit}"


def sig(value: float, digits: int) -> str:
    """Round to significant digits and group thousands, without scientific notation."""
    if value == 0:
        return "0"
    exp = math.floor(math.log10(abs(value)))
    decimals = max(digits - 1 - exp, 0)
    rounded = round(value, decimals - 0) if decimals else round(value, -(exp - digits + 1))
    if decimals:
        return f"{rounded:,.{decimals}f}"
    return f"{int(rounded):,}"


class Ledger:
    def __init__(self, inputs_path: Path = ROOT / "data" / "inputs.toml", overrides: dict | None = None):
        self.q: dict[str, Quantity] = {}
        self.order: list[str] = []
        self._reading: list[str] | None = None
        raw = tomllib.loads(inputs_path.read_text())
        lines = inputs_path.read_text().splitlines()
        for key, spec in raw.items():
            basis = spec["basis"]
            if basis not in BASES - {"derived"}:
                raise ValueError(f"input {key}: basis {basis!r} is not one of {sorted(BASES)}")
            if basis in ("measured", "vendor", "spec", "modelled") and not spec.get("source"):
                raise ValueError(f"input {key}: a {basis} number needs a source")
            line = next((i + 1 for i, l in enumerate(lines) if l.strip() == f"[{key}]"), 0)
            value = float(spec["value"])
            if overrides and key in overrides:
                value = float(overrides.pop(key))
            self._add(
                Quantity(
                    id=key,
                    value=value,
                    unit=spec.get("unit", ""),
                    basis=basis,
                    fmt=spec.get("fmt", ",.0f"),
                    label=spec.get("label", ""),
                    source=spec.get("source", ""),
                    date=spec.get("date", ""),
                    note=spec.get("note", ""),
                    defined_in=f"data/inputs.toml#L{line}",
                )
            )
        if overrides:
            raise KeyError(f"--set names inputs that do not exist: {sorted(overrides)}")

    def _add(self, quantity: Quantity) -> None:
        if quantity.id in self.q:
            raise KeyError(f"{quantity.id} is defined twice")
        self.q[quantity.id] = quantity
        self.order.append(quantity.id)

    def __getitem__(self, key: str) -> float:
        if key not in self.q:
            raise KeyError(f"{key} is read before it is defined")
        if self._reading is not None and key not in self._reading:
            self._reading.append(key)
        return self.q[key].value

    def derive(
        self,
        id: str,
        fn: Callable[["Ledger"], float],
        formula: str,
        unit: str = "",
        fmt: str = ",.0f",
        label: str = "",
        note: str = "",
        defined_in: str = "",
    ) -> float:
        self._reading = []
        value = float(fn(self))
        read, self._reading = self._reading, None
        if not math.isfinite(value):
            raise ValueError(f"{id} is not finite")
        self._add(
            Quantity(
                id=id,
                value=value,
                unit=unit,
                basis="derived",
                fmt=fmt,
                label=label,
                note=note,
                formula=formula,
                inputs=read,
                defined_in=defined_in,
            )
        )
        return value

    def to_json(self) -> dict:
        out = {}
        for key in self.order:
            q = self.q[key]
            out[key] = {
                "value": q.value,
                "display": q.display(),
                "unit": q.unit,
                "basis": q.basis,
                "label": q.label,
                "formula": q.formula,
                "inputs": q.inputs,
                "source": q.source,
                "date": q.date,
                "note": q.note,
                "defined_in": q.defined_in,
            }
        return out

    def to_markdown(self) -> str:
        head = [
            "# The ledger",
            "",
            "Every number Subcritical publishes, generated by `make model` from `data/inputs.toml` and",
            "`model/subcritical.py`. Do not edit this file by hand. Documents link here as",
            "`[text](numbers.md#id)` and `make docs` rewrites the link text to the value below.",
            "",
            "Basis: **measured** (independent measurement), **vendor** (a claim by an interested party),",
            "**spec** (fixed by a protocol rule), **design** (a choice this design makes), **assumption**",
            "(a number we picked where no source fixes it), **modelled** (the output of a published model),",
            "**derived** (computed from the others).",
            "",
        ]
        body = []
        for key in self.order:
            q = self.q[key]
            body.append(f'<a id="{key}"></a>')
            body.append(f"### {key}")
            body.append("")
            body.append(f"**{q.display()}**{': ' + q.label if q.label else ''}")
            body.append("")
            body.append(f"- basis: {q.basis}")
            if q.formula:
                body.append(f"- formula: `{q.formula}`")
                body.append("- inputs: " + ", ".join(f"[{i}](#{i})" for i in q.inputs))
            if q.source:
                body.append(f"- source: [@{q.source}]" + (f", {q.date}" if q.date else ""))
            if q.note:
                body.append(f"- note: {q.note}")
            body.append(f"- defined in: `{q.defined_in}`")
            body.append("")
        return "\n".join(head + body)


def write_outputs(ledger: Ledger) -> None:
    (ROOT / "data" / "numbers.json").write_text(json.dumps(ledger.to_json(), indent=2) + "\n")
    (ROOT / "research" / "numbers.md").write_text(ledger.to_markdown())
