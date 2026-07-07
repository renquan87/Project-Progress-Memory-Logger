# Maintenance Guide

Use this reference before finalizing a progress record and when the progress system becomes large.

## Update Policy

| File | Update When |
| --- | --- |
| `sessions/` | Every recorded task, but keep the record concise by default. |
| `index.md` | Every new session log, one line only. |
| `project_memory.md` | Durable project background, current state, constraints, or read-first notes changed. |
| `decisions.md` | A technical, research, process, or direction decision affects future work. |
| `todos.md` | A cross-session task is opened, changed, blocked, completed, or dropped. |
| `environment.md` | A device, path, dataset, checkpoint, deployment target, or runtime changes. |

## Anti-Bloat Strategy

- Keep `project_memory.md` short and current.
- Keep session logs short too. A normal task should not need a 20-section report.
- Keep `index.md` as links and one-line descriptions.
- Archive or summarize old sessions by milestone when the session count grows.
- Prefer tables for ongoing todos and decisions.
- Avoid duplicating the same command output in multiple files.
- Do not let the progress note become longer than the actual code or documentation change unless the task was mainly analysis.

## Completeness Checklist

Before reporting completion to the user, verify:

- The original user request is captured.
- Key files and artifacts are listed.
- Commands and tool calls are summarized with results.
- Tests, validation, and skipped checks are recorded.
- Errors and fixes are recorded when relevant.
- Decisions, todos, and environment files are updated only when they affect future work.
- Sensitive content is redacted.
- The next step is concrete.
- The user has also been told in chat what changed; the progress note is not the only report.

## Periodic Stage Summary

Create a stage summary when one of these happens:

- A milestone is completed.
- A paper, release, experiment batch, or deployment phase ends.
- More than 20 session logs accumulate in one phase.
- The project direction changes substantially.

Stage summaries should link to source sessions rather than copying them.
