# Project Progress Memory Logger

### 让 AI Agent 记录项目里真正发生过的事

<p>
  <img src="https://img.shields.io/badge/Codex-412991?style=flat-square&logo=openai&logoColor=white" alt="Codex">
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square" alt="OpenCode">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

`project-progress-memory-logger` 是一个 AI Agent Skill，用于在 AI 辅助完成项目任务后，在当前项目内生成 `Docs/progress/` 进度记录。记录内容包括用户需求、文件变更、运行命令、测试结果、关键决策、未完成事项和下一步。

它适用于 Codex、Claude Code、Cursor、OpenCode、OpenClaw，以及其他能加载 `SKILL.md` 的 AI 编程助手。

仓库地址：[renquan87/Project-Progress-Memory-Logger](https://github.com/renquan87/Project-Progress-Memory-Logger)

## 功能

AI Agent 可以推进任务，但跨会话接手时常缺少项目现场：README 可能过期，决策分散在聊天里，命令和测试结果没有固定位置保存。

这个 Skill 提供一个项目内进度记录流程，让下一次接手的 AI Agent 能快速看到：

- 用户提出的需求；
- Agent 对任务范围的理解；
- 仓库中发生的文件变更；
- 执行过的命令和工具；
- 通过或跳过的测试检查；
- 已做出的决策；
- 仍未完成的事项；
- 下一次接手时优先阅读的文件和优先执行的动作。

## 输出结构

默认写入目标项目：

```text
Docs/progress/
├── index.md
├── project_memory.md
├── sessions/
├── decisions.md
├── todos.md
└── environment.md
```

`sessions/` 保存单次任务记录。其他文件保存长期项目记忆、决策、待办和环境信息。

默认记录保持简洁；任务复杂或用户要求完整交接时，可以写更详细的交接记录。

## 安装

```bash
npx skills add renquan87/Project-Progress-Memory-Logger
```

安装后，在一次项目任务结束时让 Agent 记录进展。

## 触发示例

项目任务结束，或用户说出这些话时使用：

```text
记录一下
保存上下文
写入项目日志
更新项目记忆
收尾
交接
```

英文触发词如 `record this`、`save context`、`write project log` 也可以使用。

适合代码修改、调试、文档、实验、部署、调研记录和计划收尾。

## 反馈

使用过程中如果有建议、遇到问题，或觉得哪里不好用，欢迎到 [GitHub Issues](https://github.com/renquan87/Project-Progress-Memory-Logger/issues) 提交。

## 仓库结构

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

## 许可证

MIT
