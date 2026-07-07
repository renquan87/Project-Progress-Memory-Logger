# 项目进度记忆

让 AI 代理用中文、短记录保存项目进度。

`project-progress-memory-logger` 是一个 AI 代理技能。它的作用不是写长篇复盘，而是在项目的 `Docs/progress/` 里保存下一次继续工作真正需要的信息。

仓库地址：`https://github.com/renquan87/Project-Progress-Memory-Logger`

## 解决什么问题

新开对话时，AI 经常不知道上次做了什么、文件改到哪里、下一步该做什么。这个技能只解决这件事：

- 已经做了什么；
- 关键文件在哪里；
- 跑过什么命令/测试；
- 产物和结果在哪里；
- 下一步先做什么；
- 有什么风险或限制。

## 默认输出

```text
Docs/progress/
  index.md
  project_memory.md
  sessions/
  decisions.md
  todos.md
  environment.md
```

## 默认记录格式

普通会话记录只写六段：

1. 用户要求；
2. 改了什么；
3. 命令与验证；
4. 结果；
5. 决策与风险；
6. 下一步。

默认 20-60 行。只有用户明确要求完整交接，或任务确实复杂，才写长记录。

## 安装

```bash
npx skills add renquan87/Project-Progress-Memory-Logger
```

## 触发示例

```text
记录一下
保存上下文
更新项目记忆
写项目日志
收尾
交接
```

## 设计原则

- 中文优先；
- 短记录优先；
- 不写思考过程；
- 不写聊天流水账；
- 不把一次性冒烟测试写成正式结论；
- 不用项目记忆替代对用户的实时汇报。

## 许可证

MIT
