#!/usr/bin/env python3
"""Create a new session log from templates/session-log.md."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
from pathlib import Path


def now_local() -> dt.datetime:
    return dt.datetime.now().astimezone()


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run_git(project_root: Path, args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=project_root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return "not-a-git-repo"
    if result.returncode != 0:
        return "not-a-git-repo"
    return result.stdout.strip() or "unknown"


def git_dirty(project_root: Path) -> str:
    status = run_git(project_root, ["status", "--short"])
    if status == "not-a-git-repo":
        return "not-a-git-repo"
    return "true" if status else "false"


def slugify(value: str, limit: int = 48) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-._")
    if not slug:
        slug = "session"
    return slug[:limit].strip("-._") or "session"


def render(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def resolve_progress_root(project_root: Path, progress_root: str) -> Path:
    candidate = Path(progress_root)
    if candidate.is_absolute():
        return candidate
    return project_root / candidate


def create_session(args: argparse.Namespace) -> Path:
    project_root = Path(args.project_root).resolve()
    progress_root = resolve_progress_root(project_root, args.progress_root)
    sessions_root = progress_root / "sessions"
    timestamp = now_local()
    session_id = timestamp.strftime("%Y%m%dT%H%M%S%z") + "__" + slugify(args.task_type, 24) + "__" + slugify(args.title, 36)
    session_dir = sessions_root / timestamp.strftime("%Y") / timestamp.strftime("%Y-%m")
    session_dir.mkdir(parents=True, exist_ok=True)
    output_path = session_dir / f"{session_id}.md"
    if output_path.exists():
        raise SystemExit(f"Session file already exists: {output_path}")

    branch = run_git(project_root, ["branch", "--show-current"])
    commit = run_git(project_root, ["rev-parse", "--short", "HEAD"])
    values = {
        "TITLE": args.title,
        "TIMESTAMP": timestamp.isoformat(timespec="seconds"),
        "PROJECT_NAME": project_root.name,
        "PROJECT_ROOT": str(project_root),
        "OPERATOR": args.operator,
        "AI_AGENT": args.agent,
        "DEVICE": args.device,
        "TASK_TYPE": args.task_type,
        "STATUS": args.status,
        "GIT_BRANCH": branch,
        "GIT_COMMIT": commit,
        "GIT_DIRTY": git_dirty(project_root),
        "SESSION_ID": session_id,
    }
    template_path = skill_root() / "templates" / "session-log.md"
    content = render(template_path.read_text(encoding="utf-8"), values)
    output_path.write_text(content, encoding="utf-8", newline="\n")
    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="Target project root.")
    parser.add_argument("--progress-root", default="Docs/progress", help="Progress root. Default: Docs/progress")
    parser.add_argument("--task-type", required=True, help="Task type, for example code-change, docs, experiment, planning.")
    parser.add_argument("--title", required=True, help="Human-readable session title.")
    parser.add_argument("--agent", default="unknown-agent", help="AI agent name.")
    parser.add_argument("--device", default=os.uname().nodename if hasattr(os, "uname") else "unknown-device", help="Device alias.")
    parser.add_argument("--operator", default="unknown-operator", help="Human operator or project owner.")
    parser.add_argument("--status", default="draft", choices=["draft", "completed", "partial", "blocked", "abandoned"], help="Initial session status.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    project_root = Path(args.project_root)
    if not project_root.exists() or not project_root.is_dir():
        raise SystemExit(f"Project root is not a directory: {project_root}")
    output_path = create_session(args)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
