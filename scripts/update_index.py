#!/usr/bin/env python3
"""根据会话记录的 frontmatter 更新 Docs/progress/index.md。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


START = "<!-- sessions:start -->"
END = "<!-- sessions:end -->"


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def session_rows(progress_root: Path, limit: int) -> list[str]:
    sessions_root = progress_root / "sessions"
    rows: list[tuple[str, str]] = []
    for path in sessions_root.rglob("*.md"):
        meta = parse_frontmatter(path)
        date = meta.get("date", "")
        title = meta.get("title") or path.stem
        task_type = meta.get("task_type", "")
        status = meta.get("status", "")
        agent = meta.get("ai_agent", "")
        device = meta.get("device", "")
        rel = path.relative_to(progress_root).as_posix()
        row = f"| {date} | [{title}]({rel}) | {task_type} | {status} | {agent} | {device} |"
        rows.append((date, row))
    rows.sort(key=lambda item: item[0], reverse=True)
    return [row for _, row in rows[:limit]]


def default_index() -> str:
    return (
        "# 项目进度索引\n\n"
        "## 最新记录\n\n"
        f"{START}\n"
        "| 日期 | 记录 | 类型 | 状态 | 代理 | 机器 |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        f"{END}\n"
    )


def update_index(progress_root: Path, limit: int) -> Path:
    index_path = progress_root / "index.md"
    progress_root.mkdir(parents=True, exist_ok=True)
    if index_path.exists():
        text = index_path.read_text(encoding="utf-8")
    else:
        text = default_index()

    rows = session_rows(progress_root, limit)
    table = "\n".join(
        [
            START,
            "| 日期 | 记录 | 类型 | 状态 | 代理 | 机器 |",
            "| --- | --- | --- | --- | --- | --- |",
            *rows,
            END,
        ]
    )

    if START in text and END in text:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), flags=re.DOTALL)
        text = pattern.sub(table, text)
    else:
        text = text.rstrip() + "\n\n## 最新记录\n\n" + table + "\n"

    index_path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    return index_path


def resolve_progress_root(project_root: Path, progress_root: str) -> Path:
    candidate = Path(progress_root)
    if candidate.is_absolute():
        return candidate
    return project_root / candidate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="目标项目根目录。")
    parser.add_argument("--progress-root", default="Docs/progress", help="进度根目录。默认：Docs/progress")
    parser.add_argument("--limit", type=int, default=50, help="最新记录最多列出多少条。默认：50")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    project_root = Path(args.project_root).resolve()
    progress_root = resolve_progress_root(project_root, args.progress_root)
    index_path = update_index(progress_root, args.limit)
    print(index_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
