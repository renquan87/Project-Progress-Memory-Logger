#!/usr/bin/env python3
"""从文本中脱敏常见凭据。"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECRET_ASSIGNMENT = re.compile(
    r"(?i)\b(api[_-]?key|access[_-]?token|refresh[_-]?token|auth[_-]?token|secret|client[_-]?secret|password|passwd|pwd|cookie|set-cookie)\b"
    r"(\s*[:=]\s*)"
    r"([^\s'\";,\]\}]+)"
)
JSON_SECRET = re.compile(
    r'(?i)("(?:api[_-]?key|access[_-]?token|refresh[_-]?token|auth[_-]?token|secret|client[_-]?secret|password|passwd|pwd|cookie)"\s*:\s*)"([^"]*)"'
)
BEARER = re.compile(r"(?i)\b(Bearer)\s+[A-Za-z0-9._~+/=-]{10,}")
BASIC_AUTH = re.compile(r"(?i)\b(Basic)\s+[A-Za-z0-9+/=-]{10,}")
OPENAI_KEY = re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b")
GITHUB_TOKEN = re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}\b")
AWS_ACCESS_KEY = re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b")
PRIVATE_KEY_BLOCK = re.compile(
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----",
    flags=re.DOTALL,
)
URL_WITH_CREDENTIALS = re.compile(r"([a-zA-Z][a-zA-Z0-9+.-]*://)([^/\s:@]+):([^@\s/]+)@")


def redact(text: str) -> str:
    text = PRIVATE_KEY_BLOCK.sub("<REDACTED_PRIVATE_KEY_BLOCK>", text)
    text = SECRET_ASSIGNMENT.sub(lambda m: f"{m.group(1)}{m.group(2)}<REDACTED_SECRET>", text)
    text = JSON_SECRET.sub(lambda m: f'{m.group(1)}"<REDACTED_SECRET>"', text)
    text = BEARER.sub(r"\1 <REDACTED_TOKEN>", text)
    text = BASIC_AUTH.sub(r"\1 <REDACTED_TOKEN>", text)
    text = OPENAI_KEY.sub("<REDACTED_OPENAI_KEY>", text)
    text = GITHUB_TOKEN.sub("<REDACTED_GITHUB_TOKEN>", text)
    text = AWS_ACCESS_KEY.sub("<REDACTED_AWS_ACCESS_KEY>", text)
    text = URL_WITH_CREDENTIALS.sub(r"\1<REDACTED_CREDENTIALS>@", text)
    return text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="可选输入文件。不提供时读取标准输入。")
    parser.add_argument("-o", "--output", help="可选输出文件。不提供时写入标准输出。")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.input:
        text = Path(args.input).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()
    output = redact(text)
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
