#!/usr/bin/env python3
"""Run every check in tools/formal/ (research/05-formal.md) and report each one's result.

  python3 tools/formal/run_all.py

Exits 1 if any check finds a counterexample or fails its own self-test. The checks are light
(standard library, seconds to a minute each), but together take a few minutes on one core.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    checks = sorted(p for p in HERE.glob("*.py") if p.name not in ("run_all.py", "_lib.py"))
    failed = []
    for path in checks:
        proc = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, cwd=HERE)
        print(f"{'ok  ' if proc.returncode == 0 else 'FAIL'} {path.name}", flush=True)
        print(proc.stdout.rstrip() + ("\n" + proc.stderr.rstrip() if proc.returncode else ""), flush=True)
        if proc.returncode != 0:
            failed.append(path.name)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
