---
name: project-progress-memory-logger
description: Use this skill when the user asks to record progress, save context, update project memory, write a project log, capture a handoff, or when a completed task changed project state worth remembering. It writes concise project-local Docs/progress notes: what changed, commands/tests, outputs, decisions, next steps, and any risks. Default to short localized records, not verbose process transcripts.
metadata:
  short-description: Log project progress after each task
---

# Project Progress Memory Logger

## Purpose

Use this skill to preserve durable, project-local memory after AI-assisted work. The record should let a future AI agent or human maintainer recover the task context quickly. It is not a transcript, not a full chain-of-thought log, and not a substitute for telling the user what happened in the conversation.

## Trigger Conditions

Use this skill when any of these are true:

- The user asks to record the task, write a project log, save context, update project memory, create a handoff, or says phrases such as "记录一下", "保存上下文", "写入项目日志", "更新项目记忆", or "收尾".
- A code, documentation, experiment, paper, planning, debugging, deployment, data, or environment task has been completed and produced state worth remembering.
- The task produced durable project state: code changes, commands/tests, experiment metrics, generated reports, decisions, todos, environment changes, or cross-device notes.
- The user wants the conversation to become long-term project memory.

Skip when the user explicitly says not to record, the interaction was a simple standalone Q&A with no project-state change, the record would add more noise than value, safe redaction is impossible, or no project root can be confirmed.

## Default Output System

Create or update this tree in the target project:

```text
Docs/progress/
  index.md
  project_memory.md
  sessions/
  decisions.md
  todos.md
  environment.md
```

Use `Docs/progress/` by default. If the user project uses another docs root, such as `docs/progress/`, adapt to that root and record the choice in `environment.md`.

## Language Selection

Choose the language for `Docs/progress/` records from the user's context instead of defaulting to English:

- Use the language of the user's current request for new session records and related updates.
- If the current request mixes languages, use the language that carries the task instructions, unless the user explicitly asks for another language.
- When updating an existing progress file, keep the existing file's language if the update is small; switch only when creating a new file or when the user context clearly asks for a different language.
- Keep frontmatter keys, file names, code identifiers, commands, paths, and quoted source text unchanged when they need to stay machine-readable or faithful to the source.
- Apply the same language choice consistently across `sessions/`, `index.md`, `project_memory.md`, `decisions.md`, `todos.md`, and `environment.md` updates for the same task.
- Section headings should also use the chosen language. For Chinese users, write Chinese headings by default.

## Brevity Rules

Default to a concise record. The usual session log should be 20-60 lines, not a full report.

- Do not write a step-by-step transcript.
- Do not include internal reasoning, "what I thought", or tool-call trivia.
- Do not duplicate long command output. Keep the command and the result.
- Do not update every progress file by habit. Update only files whose long-term facts changed.
- Use a detailed handoff only when the user asks for it, the task is complex, or another agent truly cannot continue without detail.
- Always tell the user in the chat what was changed, what was run, and where outputs are. Project memory is supplementary, not a replacement for real-time reporting.

## Standard Workflow

1. Decide whether the task needs a progress record and whether it should be brief or detailed. Use brief by default.
2. Confirm the project root. Prefer the Git root; otherwise use the user-specified directory or a directory containing project markers such as `README.md`, `AGENTS.md`, `CLAUDE.md`, `pyproject.toml`, `package.json`, or `Docs/`.
3. Inspect or initialize `Docs/progress/`. Use `scripts/init_progress.py` when available.
4. Collect only high-signal facts: user request, changed files, commands/tests and results, outputs, decisions, next steps, risks.
5. Redact secrets and sensitive information before writing. Follow `references/redaction-policy.md`.
6. Create one concise session record under `Docs/progress/sessions/` using `templates/session-log.md`.
7. Update `index.md`, `project_memory.md`, `decisions.md`, `todos.md`, or `environment.md` only when the current task changes durable facts in those files.
8. Run `scripts/update_index.py` when available, then do a quick anti-bloat check.
9. Tell the user in the chat which files were created or updated, what commands/tests ran, and which items remain open.

## What To Load When Needed

- `templates/session-log.md` for a concise single-task record.
- `templates/index.md`, `templates/project-memory.md`, `templates/decisions.md`, `templates/todos.md`, and `templates/environment.md` when initializing the progress tree.
- `references/field-guide.md` for field meanings and conditional sections.
- `references/redaction-policy.md` before writing commands, credentials-adjacent text, logs, or environment details.
- `references/cross-device-guide.md` for laptop/server/lab-machine workflows.
- `references/maintenance-guide.md` before finalizing and updating indexes.

## Quality Bar

A good progress record answers these questions without the original chat:

- What did the user ask for?
- What changed?
- What commands/tests ran and what happened?
- Where are the important outputs?
- What decisions or durable environment facts changed?
- What remains open and what should the next session do first?
