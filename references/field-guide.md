# Field Guide

This reference explains what to record in each progress document. Load it when a session record is ambiguous or when choosing which sections to update.

## Required Fields For Every Session

| Field | Meaning |
| --- | --- |
| `title` | Human-readable task title. |
| `date` | Local timestamp with timezone. |
| `project` | Project name or repository name. |
| `project_root` | Absolute or project-relative root path. |
| `operator` | Human operator or project owner when known. |
| `ai_agent` | Agent platform, such as Codex, Claude Code, Roo, or OpenCode. |
| `device` | Current machine alias, hostname, or role. |
| `task_type` | Category such as `code-change`, `docs`, `experiment`, `paper`, `debugging`, `deployment`, `planning`, or `handoff`. |
| `status` | `draft`, `completed`, `partial`, `blocked`, or `abandoned`. |
| `branch` / `commit` | Git context when available. Use `not-a-git-repo` when unavailable. |

## Required Narrative Sections

Every normal session log should stay concise and include only:

- user request;
- what changed;
- commands/tests and results;
- outputs or important paths;
- decisions/risks if any;
- next step.

Use the old long handoff style only when the user explicitly asks for a full handoff, the task is unusually complex, or a future agent cannot continue safely from the concise form.

## Conditional Sections By Task Type

| Task Type | Additional Fields To Include |
| --- | --- |
| `code-change` | Changed files, API behavior, tests, diff summary, compatibility concerns. |
| `docs` | Documents edited, audience, source material, unresolved factual checks. |
| `experiment` | Dataset, split, seed, hardware, command, checkpoint, metrics, result path, failed runs. |
| `paper` | Manuscript section, cited sources, figure/table status, reviewer or advisor feedback. |
| `debugging` | Symptom, reproduction steps, failing command, root cause, fix, regression test. |
| `deployment` | Target environment, config files, service names, health checks, rollback notes. |
| `planning` | Constraints, candidate directions, decisions deferred, questions for stakeholders. |
| `handoff` | Current state, next owner, first command to run, files to read first. |

## Status Values

- `draft`: created but not filled.
- `completed`: task finished and record checked.
- `partial`: useful progress, but the user task is not fully completed.
- `blocked`: task cannot proceed until an external dependency is resolved.
- `abandoned`: task intentionally stopped.

## Writing Rules

- Choose the writing language from the user's current context. For example, use Chinese for progress records when the user is working in Chinese.
- Apply the chosen language consistently across the session log and any related `index.md`, `project_memory.md`, `decisions.md`, `todos.md`, or `environment.md` updates for the same task.
- Translate section headings too. Do not leave English headings in a Chinese progress record unless they are machine-readable frontmatter keys or code identifiers.
- Keep frontmatter keys, commands, paths, code identifiers, and faithful quotes in their original form when translation would reduce accuracy or machine readability.
- Preserve concrete paths, filenames, commands, metrics, and decision context.
- Summarize large outputs instead of copying logs wholesale.
- Keep routine implementation details in the session log and durable facts in `project_memory.md`.
- Put long-term work items in `todos.md`.
- Put decisions that affect future direction in `decisions.md`.
- Put machine-specific facts in `environment.md`.
- Do not update `project_memory.md`, `decisions.md`, `todos.md`, or `environment.md` just to show activity. Update them only when durable facts changed.
