#!/usr/bin/env python3
"""Rewrite every ledger link's text to the model's value, so no document types a number by hand.

A ledger link is [any text](numbers.md#id) in research/, or [any text](../research/numbers.md#id)
in paper/. With --check, change nothing and exit 1 if any link is stale or names no number.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[([^\]]*)\]\(((?:\.\./research/)?numbers\.md)#([a-z0-9-]+)\)")
DOCS = ["research", "paper"]


def documents() -> list[Path]:
    files = []
    for folder in DOCS:
        for path in sorted((ROOT / folder).rglob("*.md")):
            if path.name == "numbers.md" or "notes" in path.parts or "sources" in path.parts:
                continue
            files.append(path)
    return files


def sync(check: bool) -> int:
    numbers = json.loads((ROOT / "data" / "numbers.json").read_text())
    stale, unknown = [], []
    for path in documents():
        text = path.read_text()

        def replace(m: re.Match) -> str:
            key = m.group(3)
            if key not in numbers:
                unknown.append(f"{path.relative_to(ROOT)}: {key}")
                return m.group(0)
            shown = numbers[key]["display"]
            if m.group(1) != shown:
                stale.append(f"{path.relative_to(ROOT)}: {key}: {m.group(1)!r} -> {shown!r}")
            return f"[{shown}]({m.group(2)}#{key})"

        new = LINK.sub(replace, text)
        if new != text and not check:
            path.write_text(new)
    for line in unknown:
        print(f"unknown number: {line}", file=sys.stderr)
    if check:
        for line in stale:
            print(f"stale: {line}", file=sys.stderr)
        return 1 if (stale or unknown) else 0
    if stale:
        print(f"sync: rewrote {len(stale)} link{'s' if len(stale) != 1 else ''}")
    return 1 if unknown else 0


if __name__ == "__main__":
    sys.exit(sync("--check" in sys.argv))
