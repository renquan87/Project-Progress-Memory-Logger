#!/usr/bin/env python3
"""Run validation checks for this skill repository."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], cwd: Path = REPO_ROOT) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def main() -> int:
    skill_file = REPO_ROOT / "SKILL.md"
    if not skill_file.exists():
        raise SystemExit("SKILL.md is missing from the repository root.")

    scripts = sorted((REPO_ROOT / "scripts").glob("*.py"))
    if scripts:
        run([sys.executable, "-m", "py_compile", *[str(path) for path in scripts]])

    run([sys.executable, "-m", "unittest", "discover", "-s", str(REPO_ROOT / "tests"), "-p", "test_*.py"])

    print("\nAll skill checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
