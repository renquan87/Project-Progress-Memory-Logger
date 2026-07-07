# Project Progress Memory Logger

### Let your AI agent remember what actually happened in the project

**🇺🇸 English** | **[🇨🇳 中文](README.zh-CN.md)**

<p>
  <img src="https://img.shields.io/badge/Codex-412991?style=flat-square&logo=openai&logoColor=white" alt="Codex">
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square" alt="OpenCode">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

`project-progress-memory-logger` is an AI Agent Skill that creates concise project-local `Docs/progress/` notes after an AI-assisted task. It records the user request, file changes, commands, tests, decisions, open questions, and next steps without turning routine work into a long transcript.

It is built for Codex, Claude Code, Cursor, OpenCode, OpenClaw, and other assistants that can load `SKILL.md`.

Repository: [renquan87/Project-Progress-Memory-Logger](https://github.com/renquan87/Project-Progress-Memory-Logger)

## What Problem It Solves

AI agents are good at moving a task forward, but project memory often falls apart between sessions. The next agent sees a stale README, missing context, half-remembered decisions, and no record of which commands were actually run.

This skill gives the agent a simple closing ritual: before the task ends, write the project record, but keep it short by default.

It records:

- what the user asked for
- what the agent understood
- what changed in the repo
- which commands and tools were used
- which tests or checks passed
- which decisions were made
- what remains unfinished
- what the next AI session should read first

## Output

By default, records go into the target project:

```text
Docs/progress/
├── index.md
├── project_memory.md
├── sessions/
├── decisions.md
├── todos.md
└── environment.md
```

`sessions/` stores one concise log per task. The other files keep the long-term project memory short and easy to scan.

The default session log keeps six sections: user request, what changed, commands and validation, result, decisions and risks, and next step. Use detailed handoffs only when the user asks for them or the task is complex enough to need them.

## Install

```bash
npx skills add renquan87/Project-Progress-Memory-Logger
```

After installation, ask the agent to record progress at the end of a task.

## Trigger Examples

The skill should run at the end of a real project task, or when the user says:

```text
record this
save context
write project log
update project memory
capture a handoff
```

It is useful after coding, debugging, documentation, experiments, deployment work, research notes, or planning sessions.

## Feedback

If you have suggestions, run into problems, or find parts of the skill awkward to use, please open an issue in [GitHub Issues](https://github.com/renquan87/Project-Progress-Memory-Logger/issues).

## Repository Layout

```text
.
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── SKILL.md
├── agents/
├── examples/
├── references/
├── scripts/
├── templates/
└── tests/
```

## License

MIT
