#!/usr/bin/env python3
"""初始化项目内的 Docs/progress 进度记忆树。"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path


TEMPLATE_MAP = {
    "index.md": "index.md",
    "project-memory.md": "project_memory.md",
    "decisions.md": "decisions.md",
    "todos.md": "todos.md",
    "environment.md": "environment.md",
}


def now_local() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def render(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def safe_relative(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def resolve_progress_root(project_root: Path, progress_root: str) -> Path:
    candidate = Path(progress_root)
    if candidate.is_absolute():
        return candidate
    return project_root / candidate


def init_progress(project_root: Path, progress_root: str, force: bool = False) -> list[Path]:
    project_root = project_root.resolve()
    target_root = resolve_progress_root(project_root, progress_root)
    templates_dir = skill_root() / "templates"
    timestamp = now_local()
    values = {
        "PROJECT_NAME": project_root.name,
        "PROJECT_ROOT": str(project_root),
        "PROGRESS_ROOT": safe_relative(target_root, project_root),
        "TIMESTAMP": timestamp,
    }

    created: list[Path] = []
    target_root.mkdir(parents=True, exist_ok=True)
    sessions_dir = target_root / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    created.extend([target_root, sessions_dir])

    for template_name, output_name in TEMPLATE_MAP.items():
        template_path = templates_dir / template_name
        output_path = target_root / output_name
        if output_path.exists() and not force:
            continue
        content = render(template_path.read_text(encoding="utf-8"), values)
        output_path.write_text(content, encoding="utf-8", newline="\n")
        created.append(output_path)

    return created


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="目标项目根目录。")
    parser.add_argument(
        "--progress-root",
        default="Docs/progress",
        help="进度目录，可以是相对项目根目录的路径，也可以是绝对路径。默认：Docs/progress",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="覆盖已有核心进度文件。sessions 目录永不删除。",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    project_root = Path(args.project_root)
    if not project_root.exists():
        raise SystemExit(f"项目根目录不存在：{project_root}")
    if not project_root.is_dir():
        raise SystemExit(f"项目根目录不是目录：{project_root}")

    created = init_progress(project_root, args.progress_root, force=args.force)
    print("已初始化进度树：")
    for path in created:
        print(os.fspath(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
