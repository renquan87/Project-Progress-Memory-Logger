---
title: "{{TITLE}}"
date: "{{TIMESTAMP}}"
project: "{{PROJECT_NAME}}"
project_root: "{{PROJECT_ROOT}}"
operator: "{{OPERATOR}}"
ai_agent: "{{AI_AGENT}}"
device: "{{DEVICE}}"
task_type: "{{TASK_TYPE}}"
status: "{{STATUS}}"
branch: "{{GIT_BRANCH}}"
commit: "{{GIT_COMMIT}}"
git_dirty: "{{GIT_DIRTY}}"
session_id: "{{SESSION_ID}}"
---

# {{TITLE}}

## 1. Task Overview

- **Task type:** {{TASK_TYPE}}
- **Status:** {{STATUS}}
- **Project:** {{PROJECT_NAME}}
- **Device / environment:** {{DEVICE}}
- **Related files or artifacts:** TBD

## 2. Original User Request

Record the user's request as faithfully as possible. Preserve important constraints, paths, filenames, expected outputs, and acceptance criteria.

> TBD

## 3. Agent Understanding

Describe how the AI agent interpreted the task, including scope, constraints, assumptions, and what should be avoided.

- TBD

## 4. Known Project Context And New Context

### Existing Context Used

- TBD

### New Context Learned This Session

- TBD

## 5. Execution Plan

1. TBD

## 6. Execution Timeline

| Time | Step | Evidence / Notes |
| --- | --- | --- |
| {{TIMESTAMP}} | Session started | TBD |

## 7. Tool Calls

| Tool | Purpose | Result |
| --- | --- | --- |
| TBD | TBD | TBD |

## 8. Commands Run

| Command | Working Directory | Result | Notes |
| --- | --- | --- | --- |
| `TBD` | `{{PROJECT_ROOT}}` | TBD | TBD |

Summarize long outputs instead of pasting noisy logs. Include exact error messages only when they are needed for future debugging.

## 9. Files And Code Changes

| Path | Change Type | Why It Changed | Important Notes |
| --- | --- | --- | --- |
| TBD | created / modified / deleted | TBD | TBD |

## 10. Key Implementation Notes

Describe the important design or code changes at the level a future maintainer needs.

- TBD

## 11. Tests, Validation, And Results

| Check | Command / Method | Result | Evidence |
| --- | --- | --- | --- |
| TBD | TBD | TBD | TBD |

Record skipped checks and the reason.

## 12. Problems Encountered And Fixes

| Problem | Cause / Diagnosis | Fix | Remaining Risk |
| --- | --- | --- | --- |
| TBD | TBD | TBD | TBD |

## 13. Decisions And Tradeoffs

| Decision | Reason | Alternatives Considered | Impact | Status |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | proposed / accepted / reversed |

## 14. Outputs Produced

- TBD

## 15. Unfinished Items

| Item | Priority | Blocker / Dependency | Owner | Status |
| --- | --- | --- | --- | --- |
| TBD | P0 / P1 / P2 | TBD | TBD | open |

## 16. Next Steps

1. TBD

## 17. Cross-Device Collaboration Notes

| Device / Environment | Role | Paths / Artifacts | Sync Status | Notes |
| --- | --- | --- | --- | --- |
| {{DEVICE}} | current task environment | `{{PROJECT_ROOT}}` | TBD | TBD |

## 18. Sensitive Information Handling

- Raw secrets, tokens, passwords, cookies, private keys, and credentials were not recorded.
- Redactions applied: TBD
- Sensitive paths or private names that future agents should know exist without seeing the raw value: TBD

## 19. Future AI Recovery Summary

Read this section first in the next session.

- Current state: TBD
- Most important files: TBD
- Commands already run: TBD
- First next action: TBD

## 20. Completeness Checklist

- [ ] Original user request is captured.
- [ ] Agent understanding and scope are captured.
- [ ] Commands, tools, and outputs are summarized.
- [ ] Files changed and reasons are listed.
- [ ] Tests or skipped validation are recorded.
- [ ] Decisions, todos, and unresolved risks are recorded.
- [ ] Cross-device notes are recorded when relevant.
- [ ] Secrets and sensitive content are redacted.
- [ ] Future AI recovery summary is actionable.
