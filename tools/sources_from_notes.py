#!/usr/bin/env python3
"""Merge the sources each survey track lists into research/sources.toml.

Every note in research/notes/ ends with a fenced ```toml block of [source.KEY] tables, written by
the helper that opened each source. This reads those blocks, keeps only entries that pass the same
rules as tools/check.py (a known type, a title, a year or `undated`, a well-formed identifier), and
appends the new keys to research/sources.toml. An existing key is never overwritten: if a note
gives the same key different content, or two notes disagree, it is reported for a person to settle.

  python3 tools/sources_from_notes.py            report what would be added, change nothing
  python3 tools/sources_from_notes.py --write    append the new sources
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from check import ARXIV, DOI, TYPES  # noqa: E402

BLOCK = re.compile(r"```toml\n(.*?)```", re.S)
FIELDS = ["type", "title", "authors", "year", "undated", "doi", "arxiv", "isbn", "url", "opened"]


def problems(s: dict) -> list[str]:
    out = []
    if s.get("type") not in TYPES:
        out.append(f"type {s.get('type')!r}")
    if not s.get("title"):
        out.append("no title")
    if not s.get("year") and not s.get("undated"):
        out.append("no year")
    if not any(s.get(k) for k in ("doi", "arxiv", "isbn", "url")):
        out.append("no identifier")
    if s.get("doi") and not DOI.match(s["doi"]):
        out.append(f"doi {s['doi']!r}")
    if s.get("arxiv") and not ARXIV.match(s["arxiv"]):
        out.append(f"arxiv {s['arxiv']!r}")
    return out


def toml_value(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    text = str(v).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def render(key: str, s: dict, note: str) -> str:
    lines = [f"[source.{key}]"]
    for f in FIELDS:
        if f in s and s[f] not in ("", None):
            lines.append(f"{f} = {toml_value(s[f])}")
    lines.append(f'found_in = "{note}"')
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    path = ROOT / "research" / "sources.toml"
    have = tomllib.loads(path.read_text()).get("source", {})
    new: dict[str, tuple[dict, str]] = {}
    issues: list[str] = []
    for note in sorted((ROOT / "research" / "notes").glob("*.md")):
        rel = note.relative_to(ROOT).as_posix()
        blocks = BLOCK.findall(note.read_text())
        if not blocks:
            issues.append(f"{rel}: no ```toml block of sources")
            continue
        for block in blocks:
            try:
                data = tomllib.loads(block).get("source", {})
            except tomllib.TOMLDecodeError as e:
                issues.append(f"{rel}: the toml block does not parse: {e}")
                continue
            for key, s in data.items():
                bad = problems(s)
                if bad:
                    issues.append(f"{rel}: {key} skipped ({', '.join(bad)})")
                    continue
                if key in have:
                    old = {k: v for k, v in have[key].items() if k not in ("opened", "found_in")}
                    if old != {k: v for k, v in s.items() if k != "opened"}:
                        issues.append(f"{rel}: {key} is already in sources.toml with other content; kept the existing entry")
                    continue
                if key in new and new[key][0] != s:
                    issues.append(f"{rel}: {key} differs from the entry in {new[key][1]}; kept the first")
                    continue
                new.setdefault(key, (s, rel))
    for line in issues:
        print(f"note {line}", file=sys.stderr)
    print(f"{len(new)} new sources from {len({n for _, n in new.values()})} notes ({len(have)} already listed)")
    if "--write" in argv and new:
        text = path.read_text().rstrip("\n") + "\n"
        for key, (s, note) in sorted(new.items()):
            text += "\n" + render(key, s, note) + "\n"
        path.write_text(text)
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
