from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"


def run_script(name: str, *args: str, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *args],
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


class ScriptWorkflowTests(unittest.TestCase):
    def test_progress_tree_session_index_context_and_redaction(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)

            init_result = run_script("init_progress.py", str(project))
            self.assertIn("已初始化进度树", init_result.stdout)
            self.assertTrue((project / "Docs/progress/index.md").exists())
            self.assertTrue((project / "Docs/progress/project_memory.md").exists())

            session_result = run_script(
                "new_session.py",
                str(project),
                "--task-type",
                "code-change",
                "--title",
                "开发检查会话",
                "--agent",
                "Codex",
                "--device",
                "test-device",
                "--operator",
                "tester",
                "--status",
                "completed",
            )
            session_path = Path(session_result.stdout.strip())
            self.assertTrue(session_path.exists())
            self.assertEqual(session_path.parent, project / "Docs/progress/sessions")
            self.assertIn("开发检查会话", session_path.read_text(encoding="utf-8"))

            update_result = run_script("update_index.py", str(project))
            self.assertTrue(Path(update_result.stdout.strip()).exists())
            index_text = (project / "Docs/progress/index.md").read_text(encoding="utf-8")
            self.assertIn("开发检查会话", index_text)
            self.assertIn("code-change", index_text)

            context_result = run_script("collect_context.py", str(project))
            context = json.loads(context_result.stdout)
            self.assertEqual(context["project_root"], str(project.resolve()))
            self.assertIn("platform", context)
            self.assertIn("git", context)

            redacted_result = run_script(
                "redact_text.py",
                input_text=(
                    "api_key=abc123\n"
                    "Authorization: Bearer secret-token-1234567890\n"
                    "password=hunter2\n"
                    "https://user:pass@example.com/path\n"
                ),
            )
            redacted = redacted_result.stdout
            self.assertIn("api_key=<REDACTED_SECRET>", redacted)
            self.assertIn("Bearer <REDACTED_TOKEN>", redacted)
            self.assertIn("password=<REDACTED_SECRET>", redacted)
            self.assertIn("https://<REDACTED_CREDENTIALS>@example.com/path", redacted)


if __name__ == "__main__":
    unittest.main()
