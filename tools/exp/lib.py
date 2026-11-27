"""What every experiment shares: fetching real data into the cache with its checksum, a seeded
random generator, and writing results the ledger reads. Standard library only, so every experiment
can import it; an experiment that needs more lists it in tools/exp/requirements.txt.

  from lib import Results, fetch, rng

  res = Results("E2", "horizons", seed=1)
  path = fetch(URL, "metr/benchmark_results.yaml", res, what="METR's time-horizon results")
  ...
  res.number("e2-doubling-days", 129.4, unit="days", fmt=",.0f", label="...", note="...")
  res.detail("fit", {...})
  res.write()

Results are written with sorted keys and no timestamp, so a rerun with the same data and seed
writes the same file, and `git diff` shows only what changed.
"""

from __future__ import annotations

import hashlib
import inspect
import json
import random
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CACHE = ROOT / "tools" / "exp" / "cache"
RESULTS = ROOT / "data" / "results"
AGENT = "research-fetch/1.0 (python-urllib)"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def rng(seed: int) -> random.Random:
    """The experiment's only source of randomness."""
    return random.Random(seed)


class Results:
    def __init__(self, experiment: str, name: str, seed: int):
        caller = Path(inspect.stack()[1].filename).resolve()
        self.out = {
            "experiment": experiment,
            "name": name,
            "script": caller.relative_to(ROOT).as_posix(),
            "seed": seed,
            "data": [],
            "numbers": {},
            "details": {},
        }
        self.prefix = experiment.lower() + "-"

    def data(self, what: str, url: str, path: Path) -> None:
        """Record a data file the result depends on: where it came from and exactly which bytes."""
        entry = {"what": what, "url": url, "sha256": sha256(path)}
        if entry not in self.out["data"]:
            self.out["data"].append(entry)

    def number(
        self, id: str, value: float, unit: str = "", fmt: str = "sig3", label: str = "", note: str = ""
    ) -> None:
        """A number for the ledger. Its id starts with the experiment's code (e2-...)."""
        if not id.startswith(self.prefix):
            raise ValueError(f"{id}: an experiment's numbers start with {self.prefix!r}")
        if id in self.out["numbers"]:
            raise ValueError(f"{id} is recorded twice")
        value = float(value)
        if value != value or value in (float("inf"), float("-inf")):
            raise ValueError(f"{id} is not finite")
        self.out["numbers"][id] = {"value": value, "unit": unit, "fmt": fmt, "label": label, "note": note}

    def detail(self, key: str, value) -> None:
        """Anything else worth keeping (fits, tables, per-item results), not read by the ledger."""
        self.out["details"][key] = value

    def write(self) -> Path:
        RESULTS.mkdir(parents=True, exist_ok=True)
        path = RESULTS / f"{self.out['name']}.json"
        path.write_text(json.dumps(self.out, indent=2, sort_keys=True) + "\n")
        print(f"wrote {path.relative_to(ROOT)} ({len(self.out['numbers'])} numbers)")
        return path


def fetch(url: str, name: str, res: Results | None = None, what: str = "", sha: str = "") -> Path:
    """Download url into tools/exp/cache/<name> once, and reuse it after. With `sha`, refuse bytes
    that differ (a source that changed under us). With `res`, record the file in the results."""
    path = CACHE / name
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": AGENT})
        with urllib.request.urlopen(req, timeout=120) as r:
            tmp = path.with_suffix(path.suffix + ".part")
            tmp.write_bytes(r.read())
            tmp.rename(path)
    got = sha256(path)
    if sha and got != sha:
        raise ValueError(f"{name}: sha256 {got} is not the expected {sha}; the source changed")
    if res is not None:
        res.data(what or name, url, path)
    return path
