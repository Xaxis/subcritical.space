#!/usr/bin/env python3
"""Every check this repository promises, in one command (make check).

1. No em dash in any file git tracks or would add.
2. The model reproduces: data/numbers.json and research/numbers.md equal a fresh run.
3. Every ledger link in research/ and paper/ shows the model's value (tools/sync.py --check).
4. Every citation [@key] in research/ and paper/ names a source in research/sources.toml by its own
   key (not one of its `aliases`, so the paper never lists one work twice), every source there has
   a type, a title, a year (or says it is undated) and an identifier (DOI, arXiv ID, ISBN or URL),
   and no two sources name the same work by the same identifier. research/sources.toml is edited
   by hand and by tools/sources_from_notes.py, which folds a second key for a work into `aliases`.
5. Every input in data/inputs.toml and data/inputs/*.toml that names a source names one that exists,
   by its own key.
6. Every link from one research document to another names a file that exists, and every anchor
   (#...) names a heading in it, by the site's rule (site/lib/text.ts slugify: ids on ## and ###
   headings). The site turns each into a page link, so a miss is a dead link there.
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
# New-style IDs (2401.01234) and the old style before April 2007 (physics/0210005, math.PR/0301001).
ARXIV = re.compile(r"^(\d{4}\.\d{4,5}|[a-z-]+(\.[A-Z]{2})?/\d{7})(v\d+)?$")

ARXIV_URL = re.compile(
    r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})", re.I
)

failures: list[str] = []


def identifiers(s: dict) -> set[tuple[str, str]]:
    """What names this work, normalised so one paper given as a DOI, an arXiv ID or an arXiv URL
    is recognised as the same: arXiv IDs without version, DOIs and URLs in lower case, URLs without
    scheme, www or trailing slash."""
    out: set[tuple[str, str]] = set()
    if s.get("arxiv"):
        out.add(("arxiv", re.sub(r"v\d+$", "", s["arxiv"].lower())))
    if s.get("doi"):
        doi = s["doi"].lower()
        m = re.match(r"10\.48550/arxiv\.(.+)", doi)
        out.add(("arxiv", m.group(1)) if m else ("doi", doi))
    if s.get("isbn"):
        out.add(("isbn", re.sub(r"[^0-9x]", "", s["isbn"].lower())))
    if s.get("url"):
        m = ARXIV_URL.search(s["url"])
        if m:
            out.add(("arxiv", re.sub(r"v\d+$", "", m.group(1).lower())))
        else:
            out.add(("url", re.sub(r"^https?://(www\.)?", "", s["url"].lower()).rstrip("/")))
    return out


def aliases(sources: dict) -> dict[str, str]:
    """Each alias and the key it stands for."""
    return {a: key for key, s in sources.items() for a in s.get("aliases", [])}


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
    alias_of: dict[str, str] = {}
    for key, s in sources.items():
        for a in s.get("aliases", []):
            if a in sources or a in alias_of:
                fail(f"source {key}: alias {a!r} is already a key or another source's alias")
                bad += 1
            alias_of[a] = key
    named: dict[tuple[str, str], str] = {}
    for key, s in sources.items():
        # The same title in the same year is one work too, even under two URLs (a page and its PDF).
        title = ("title", f"{re.sub(r'[^a-z0-9]', '', s.get('title', '').lower())} {s.get('year')}")
        for ident in [*sorted(identifiers(s)), title]:
            if ident in named:
                how = (
                    "add one key to the other's `aliases` by hand"
                    if ident[0] == "title"
                    else "run tools/sources_from_notes.py --write to fold them"
                )
                fail(f"sources {named[ident]} and {key} are one work ({ident[0]} {ident[1]}); {how}")
                bad += 1
            else:
                named[ident] = key
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
        if key in alias_of:
            fail(f"citation @{key} is an alias: cite @{alias_of[key]} ({where[0]})")
        else:
            fail(f"citation @{key} has no source ({where[0]})")
    if not bad and not missing:
        print(f"ok   {len(cited)} cited keys, {len(sources)} sources, all identified")


def check_inputs() -> None:
    sources = load_sources()
    from ledger import input_files

    raw: dict = {}
    for path in input_files():
        raw.update(tomllib.loads(path.read_text()))
    alias_of = aliases(sources)
    missing = [k for k, v in raw.items() if v.get("source") and v["source"] not in sources]
    for key in missing:
        src = raw[key]["source"]
        if src in alias_of:
            fail(f"input {key}: source {src!r} is an alias: name {alias_of[src]!r}")
        else:
            fail(f"input {key}: source {src!r} is not in research/sources.toml")
    if not missing:
        print(f"ok   {len(raw)} inputs, every source exists")


DOC_LINK = re.compile(r"\]\((?:\.\./research/)?([0-9][0-9a-z-]*\.md)(?:#([^)]*))?\)")
SELF_LINK = re.compile(r"\]\(#([^)]+)\)")


def slugify(text: str) -> str:
    """The site's heading id (site/lib/text.ts slugify), kept identical."""
    text = text.lower()
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return re.sub(r"\s+", "-", text.strip())


def anchors(path: Path) -> set[str]:
    out, fenced = set(), False
    for line in path.read_text().splitlines():
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and re.match(r"#{2,3} ", line):
            out.add(slugify(line.lstrip("#").strip()))
    return out


def check_doc_links() -> None:
    bad = 0
    cache: dict[Path, set[str]] = {}
    for folder in ("research", "paper"):
        for path in sorted((ROOT / folder).rglob("*.md")):
            if "notes" in path.parts or path.name == "numbers.md":
                continue
            for i, line in enumerate(path.read_text().splitlines(), 1):
                links = [(t, a) for t, a in DOC_LINK.findall(line)]
                links += [(path.name if folder == "research" else "", a) for a in SELF_LINK.findall(line)]
                for target, anchor in links:
                    file = ROOT / "research" / target if target else path
                    if not file.exists():
                        fail(f"{path.relative_to(ROOT)}:{i}: links to research/{target}, which does not exist")
                        bad += 1
                        continue
                    if anchor and anchor not in cache.setdefault(file, anchors(file)):
                        fail(f"{path.relative_to(ROOT)}:{i}: research/{file.name} has no heading #{anchor}")
                        bad += 1
    if not bad:
        print("ok   every link between documents names a file and a heading that exist")


def main() -> int:
    check_dashes()
    check_model()
    check_sync()
    check_sources()
    check_inputs()
    check_doc_links()
    if failures:
        print(f"check: {len(failures)} failure{'s' if len(failures) != 1 else ''}", file=sys.stderr)
        return 1
    print("check: all passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
