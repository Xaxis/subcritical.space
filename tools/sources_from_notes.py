#!/usr/bin/env python3
"""Merge the sources each survey track lists into research/sources.toml, one entry per work.

Every note in research/notes/ ends with a fenced ```toml block of [source.KEY] tables, written by
the helper that opened each source. This reads those blocks, keeps only entries that pass the same
rules as tools/check.py (a known type, a title, a year or `undated`, a well-formed identifier), and
adds the new keys to research/sources.toml. An existing key is never overwritten: if a note gives
the same key different content, or two notes disagree, it is reported for a person to settle.

Tracks name the same work differently. Entries that share an identifier (check.identifiers: a DOI,
an arXiv ID however written, an ISBN or a URL) are folded into one: the key kept is the one with
the strongest identifier (DOI, then arXiv), then a key without hyphens whose year agrees with the
arXiv ID, then the longer key; the others become its `aliases`, so a note's [@alias] still
resolves. Missing fields are filled from the folded entries, and `found_in` lists every note.

A research document can hand over sources the same way: a closing "## Sources to add" section
holding one ```toml block. With --write its entries join the list and the section is removed from
the document, since the list is now where they live.

  python3 tools/sources_from_notes.py            report what would change, change nothing
  python3 tools/sources_from_notes.py --write    write research/sources.toml, sorted by key
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from check import ARXIV, DOI, TYPES, identifiers  # noqa: E402

BLOCK = re.compile(r"```toml\n(.*?)```", re.S)
HANDOVER = re.compile(r"\n## Sources to add\n.*?(?=\n## |\Z)", re.S)


def handover(text: str) -> tuple[list[str], str]:
    """A document's "## Sources to add" section: its toml blocks, and the text without it."""
    m = HANDOVER.search(text)
    if not m:
        return [], text
    return BLOCK.findall(m.group(0)), (text[: m.start()] + "\n" + text[m.end() :]).rstrip("\n") + "\n"
FIELDS = ["type", "title", "authors", "year", "undated", "doi", "arxiv", "isbn", "url", "opened"]
HEADER = """# Every source Subcritical cites, edited by hand. One [source.KEY] table each, with:
#   type   peer-reviewed | preprint | spec | book | official-docs | legislation |
#          legal-scholarship | vendor | news | essay | code | dataset | report
#   title, year (or undated = true), and at least one identifier: doi, arxiv, isbn or url.
# Prefer DOIs and arXiv IDs: Paperwright adds sources only by identifier.
# A source nobody opened is not cited. Add `opened = "YYYY-MM-DD"` when it was read.
# One entry per work: a second key for the same work goes in `aliases` (tools/sources_from_notes.py
# folds them), and research/ and paper/ cite the entry's own key.
"""


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
    if isinstance(v, list):
        return "[" + ", ".join(toml_value(x) for x in v) + "]"
    text = str(v).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def render(key: str, s: dict) -> str:
    lines = [f"[source.{key}]"]
    for f in [*FIELDS, "found_in", "aliases"]:
        if f in s and s[f] not in ("", None, []):
            lines.append(f"{f} = {toml_value(s[f])}")
    return "\n".join(lines)


def notes_of(s: dict) -> list[str]:
    f = s.get("found_in", "")
    return [x.strip() for x in f.split(",") if x.strip()] if isinstance(f, str) else list(f)


def rank(key: str, s: dict) -> tuple:
    """Higher is kept: a DOI, an arXiv ID, no hyphen, a year that agrees with the arXiv ID, length."""
    ax = re.match(r"(\d{2})\d{2}\.", s.get("arxiv", ""))
    agrees = not ax or s.get("year") == 2000 + int(ax.group(1))
    return (bool(s.get("doi")), bool(s.get("arxiv")), "-" not in key, agrees, len(key), key)


def fold(entries: dict[str, dict]) -> tuple[dict[str, dict], list[str]]:
    """One entry per work. Returns the entries and a line for each fold."""
    parent = {k: k for k in entries}

    def root(k: str) -> str:
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k

    first: dict[tuple[str, str], str] = {}
    for key, s in entries.items():
        for ident in sorted(identifiers(s)):
            if ident in first:
                parent[root(key)] = root(first[ident])
            else:
                first[ident] = key
    groups: dict[str, list[str]] = {}
    for key in entries:
        groups.setdefault(root(key), []).append(key)
    out: dict[str, dict] = {}
    log: list[str] = []
    for keys in groups.values():
        keep = max(keys, key=lambda k: rank(k, entries[k]))
        merged = dict(entries[keep])
        names = list(merged.get("aliases", []))
        found = notes_of(merged)
        for k in sorted(keys):
            if k == keep:
                continue
            other = entries[k]
            for f in FIELDS:
                if f not in merged and other.get(f) not in (None, ""):
                    merged[f] = other[f]
            names += [k, *other.get("aliases", [])]
            found += [n for n in notes_of(other) if n not in found]
        if len(keys) > 1:
            log.append(f"{keep} keeps {', '.join(sorted(k for k in keys if k != keep))}")
        if names:
            merged["aliases"] = sorted(set(names))
        if found:
            merged["found_in"] = ", ".join(found)
        out[keep] = merged
    return out, log


def main(argv: list[str]) -> int:
    path = ROOT / "research" / "sources.toml"
    have = tomllib.loads(path.read_text()).get("source", {})
    known = set(have) | {a for s in have.values() for a in s.get("aliases", [])}
    new: dict[str, tuple[dict, str]] = {}
    issues: list[str] = []
    docs = sorted((ROOT / "research").glob("*.md"))
    handovers = [d for d in docs if HANDOVER.search(d.read_text())]
    for note in sorted((ROOT / "research" / "notes").glob("*.md")) + handovers:
        rel = note.relative_to(ROOT).as_posix()
        text = note.read_text()
        blocks = handover(text)[0] if note in handovers else BLOCK.findall(text)
        if not blocks:
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
                    old = {k: v for k, v in have[key].items() if k not in ("opened", "found_in", "aliases")}
                    if old != {k: v for k, v in s.items() if k != "opened"}:
                        issues.append(f"{rel}: {key} is already in sources.toml with other content; kept the existing entry")
                    continue
                if key in known:
                    continue
                if key in new and new[key][0] != s:
                    issues.append(f"{rel}: {key} differs from the entry in {new[key][1]}; kept the first")
                    continue
                new.setdefault(key, (s, rel))
    for line in issues:
        print(f"note {line}", file=sys.stderr)
    entries = dict(have)
    for key, (s, note) in new.items():
        entries[key] = {**s, "found_in": note}
    folded, log = fold(entries)
    for line in log:
        print(f"fold {line}")
    print(
        f"{len(new)} new keys from {len({n for _, n in new.values()})} notes; "
        f"{len(entries) - len(folded)} folded as aliases; {len(folded)} sources ({len(have)} before)"
    )
    if "--write" in argv and (new or log):
        body = "\n\n".join(render(k, folded[k]) for k in sorted(folded))
        path.write_text(HEADER + "\n" + body + "\n")
        print(f"wrote {path.relative_to(ROOT)}")
    if "--write" in argv:
        for doc in handovers:
            doc.write_text(handover(doc.read_text())[1])
            print(f"moved the sources to add out of {doc.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
