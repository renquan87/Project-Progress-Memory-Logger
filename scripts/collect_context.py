#!/usr/bin/env python3
"""收集可安全记录的项目、Git 和环境上下文，输出 JSON。"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import platform
import subprocess
from pathlib import Path
from typing import Any


def run_command(command: list[str], cwd: Path, timeout: int = 8) -> dict[str, Any]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError:
        return {"available": False, "returncode": None, "stdout": "", "stderr": "command-not-found"}
    except subprocess.TimeoutExpired:
        return {"available": False, "returncode": None, "stdout": "", "stderr": "timeout"}
    return {
        "available": True,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def git_text(project_root: Path, args: list[str]) -> str | None:
    result = run_command(["git", *args], project_root)
    if not result["available"] or result["returncode"] != 0:
        return None
    return result["stdout"]


def collect_git(project_root: Path) -> dict[str, Any]:
    root = git_text(project_root, ["rev-parse", "--show-toplevel"])
    if root is None:
        return {"available": False}
    status_short = git_text(project_root, ["status", "--short"]) or ""
    changed_files = []
    untracked_files = []
    for line in status_short.splitlines():
        if not line:
            continue
        path = line[3:] if len(line) > 3 else line
        changed_files.append(path)
        if line.startswith("??"):
            untracked_files.append(path)
    return {
        "available": True,
        "root": root,
        "branch": git_text(project_root, ["branch", "--show-current"]) or "detached-or-unknown",
        "commit": git_text(project_root, ["rev-parse", "--short", "HEAD"]) or "unknown",
        "dirty": bool(status_short),
        "status_short": status_short.splitlines(),
        "changed_files": changed_files,
        "untracked_files": untracked_files,
        "diff_stat": (git_text(project_root, ["diff", "--stat"]) or "").splitlines(),
        "last_commit_subject": git_text(project_root, ["log", "-1", "--pretty=%s"]) or "unknown",
    }


def collect_gpu(project_root: Path) -> dict[str, Any]:
    result = run_command(
        ["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
        project_root,
        timeout=5,
    )
    if not result["available"] or result["returncode"] != 0:
        return {"nvidia_smi_available": False}
    return {
        "nvidia_smi_available": True,
        "gpus": [line.strip() for line in result["stdout"].splitlines() if line.strip()],
    }


def collect(project_root: Path) -> dict[str, Any]:
    now = dt.datetime.now().astimezone()
    safe_env_names = [
        "SHELL",
        "TERM",
        "VIRTUAL_ENV",
        "CONDA_DEFAULT_ENV",
        "CUDA_VISIBLE_DEVICES",
        "PYTHONPATH",
    ]
    safe_env = {name: os.environ.get(name, "") for name in safe_env_names if os.environ.get(name)}
    return {
        "timestamp": now.isoformat(timespec="seconds"),
        "project_root": str(project_root.resolve()),
        "cwd": os.getcwd(),
        "hostname": platform.node(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "timezone": now.tzname(),
        "git": collect_git(project_root),
        "environment": safe_env,
        "gpu": collect_gpu(project_root),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="目标项目根目录。")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    project_root = Path(args.project_root)
    if not project_root.exists() or not project_root.is_dir():
        raise SystemExit(f"项目根目录不是目录：{project_root}")
    print(json.dumps(collect(project_root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
