#!/usr/bin/env python3
"""Every check this repository promises, in one command (make check).

1. No em dash in any file git tracks or would add.
2. The model reproduces: data/numbers.json and research/numbers.md equal a fresh run.
3. Every ledger link in research/ and paper/ shows the model's value (tools/sync.py --check).
4. Every citation [@key] in research/ and paper/ names a source in research/sources.toml, and every
   source there has a type, a title, a year (or says it is undated) and an identifier (DOI, arXiv
   ID, ISBN or URL). research/sources.toml is edited by hand.
5. Every measured, vendor or spec input in data/inputs.toml names a source that exists.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
sys.path.insert(0, str(ROOT / "tools"))

TYPES = {
    "peer-reviewed",
    "preprint",
    "spec",
    "book",
    "official-docs",
    "legislation",
    "legal-scholarship",
    "vendor",
    "news",
    "essay",
    "code",
    "dataset",
    "report",
}
CITE_GROUP = re.compile(r"\[([^\[\]]*@[^\[\]]*)\]")
CITE_KEY = re.compile(r"(?<![\w.])@([A-Za-z][\w:-]*[\w])")
DOI = re.compile(r"^10\.\d{4,9}/\S+$")
ARXIV = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")

failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)
    print(f"FAIL {message}", file=sys.stderr)


def tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    skip = re.compile(r"\.(png|jpe?g|gif|webp|ico|pdf|woff2?|ttf)$", re.I)
    return [ROOT / f for f in out.splitlines() if f and not skip.search(f)]


def check_dashes() -> None:
    dash = chr(0x2014)
    count = 0
    for path in tracked_files():
        try:
            text = path.read_text()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if dash in line:
                count += 1
                print(f"{path.relative_to(ROOT)}:{i}: em dash: {line.strip()[:100]}", file=sys.stderr)
    if count:
        fail(f"no-em-dash: {count} em dash{'es' if count != 1 else ''}")
    else:
        print("ok   no em dashes")


def check_model() -> None:
    import subcritical

    ledger = subcritical.build()
    want_json = json.dumps(ledger.to_json(), indent=2) + "\n"
    want_md = ledger.to_markdown()
    have_json = (ROOT / "data" / "numbers.json").read_text()
    have_md = (ROOT / "research" / "numbers.md").read_text()
    if want_json != have_json or want_md != have_md:
        fail("model: data/numbers.json or research/numbers.md is stale; run make model")
    else:
        print(f"ok   model reproduces {len(ledger.order)} numbers")


def check_sync() -> None:
    import sync

    if sync.sync(check=True):
        fail("docs: ledger links are stale or unknown; run make docs")
    else:
        print("ok   every ledger link shows the model's value")


def load_sources() -> dict:
    path = ROOT / "research" / "sources.toml"
    data = tomllib.loads(path.read_text())
    return data.get("source", {})


def check_sources() -> None:
    sources = load_sources()
    bad = 0
    for key, s in sources.items():
        for need in ("type", "title"):
            if not s.get(need):
                fail(f"source {key}: no {need}")
                bad += 1
        if not s.get("year") and not s.get("undated"):
            fail(f"source {key}: no year (an undated page says so in `undated`)")
            bad += 1
        if s.get("type") and s["type"] not in TYPES:
            fail(f"source {key}: type {s['type']!r} is not one of {sorted(TYPES)}")
            bad += 1
        ids = [k for k in ("doi", "arxiv", "isbn", "url") if s.get(k)]
        if not ids:
            fail(f"source {key}: no identifier (doi, arxiv, isbn or url)")
            bad += 1
        if s.get("doi") and not DOI.match(s["doi"]):
            fail(f"source {key}: doi {s['doi']!r} is malformed")
            bad += 1
        if s.get("arxiv") and not ARXIV.match(s["arxiv"]):
            fail(f"source {key}: arxiv {s['arxiv']!r} is malformed")
            bad += 1
    cited: dict[str, list[str]] = {}
    for folder in ("research", "paper"):
        for path in sorted((ROOT / folder).rglob("*.md")):
            if "notes" in path.parts:
                continue
            for i, line in enumerate(path.read_text().splitlines(), 1):
                for group in CITE_GROUP.findall(line):
                    for key in CITE_KEY.findall(group):
                        cited.setdefault(key, []).append(f"{path.relative_to(ROOT)}:{i}")
    missing = {k: v for k, v in cited.items() if k not in sources}
    for key, where in sorted(missing.items()):
        fail(f"citation @{key} has no source ({where[0]})")
    if not bad and not missing:
        print(f"ok   {len(cited)} cited keys, {len(sources)} sources, all identified")


def check_inputs() -> None:
    sources = load_sources()
    raw = tomllib.loads((ROOT / "data" / "inputs.toml").read_text())
    missing = [k for k, v in raw.items() if v.get("source") and v["source"] not in sources]
    for key in missing:
        fail(f"input {key}: source {raw[key]['source']!r} is not in research/sources.toml")
    if not missing:
        print(f"ok   {len(raw)} inputs, every source exists")


def main() -> int:
    check_dashes()
    check_model()
    check_sync()
    check_sources()
    check_inputs()
    if failures:
        print(f"check: {len(failures)} failure{'s' if len(failures) != 1 else ''}", file=sys.stderr)
        return 1
    print("check: all passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
