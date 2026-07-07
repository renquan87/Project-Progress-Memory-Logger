# Project Progress Memory Logger

### 让 AI Agent 把项目里真正发生过的事记下来

**[🇺🇸 English](README.md)** | **🇨🇳 中文**

<p>
  <img src="https://img.shields.io/badge/Codex-412991?style=flat-square&logo=openai&logoColor=white" alt="Codex">
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square" alt="OpenCode">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square" alt="OpenClaw">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

`project-progress-memory-logger` 是一个 AI Agent Skill。它会在项目的 `Docs/progress/` 目录里用简短记录保存任务中真正重要的事：用户需求、文件变更、运行命令、测试结果、决策、未解决问题和下一步。

它适用于 Codex、Claude Code、Cursor、OpenCode、OpenClaw，以及其他能加载 `SKILL.md` 的 AI 编程助手。

仓库地址：[renquan87/Project-Progress-Memory-Logger](https://github.com/renquan87/Project-Progress-Memory-Logger)

## 它解决什么问题

AI Agent 可以推进任务，但项目记忆经常在会话之间断掉。下一次接手时，Agent 看到的是过期 README、缺失上下文、零散决策和不完整命令记录。

这个 skill 给 Agent 加了一道收尾动作：任务结束前，把项目记录写清楚，但不要写成流水账或长篇报告。

它会记录：

- 用户提出了什么需求
- Agent 如何理解任务
- 仓库里改了哪些内容
- 用过哪些命令和工具
- 哪些测试或检查通过
- 做过哪些决策
- 还有哪些事项未完成
- 下一次 AI 接手时先读什么

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

`sessions/` 里是一事一记的简短记录。其他文件负责保存长期项目记忆，保持短、清楚、方便扫读。

默认 session 记录只保留 6 类信息：用户要求、改了什么、命令与验证、结果、决策与风险、下一步。只有用户明确要求完整 handoff，或任务确实复杂到需要交接，才写详细记录。

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
更新记忆
收尾
```

英文触发词如 `record this`、`save context`、`write project log` 也可以使用。

适合代码、调试、文档、实验、部署、调研记录和计划收尾。

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
