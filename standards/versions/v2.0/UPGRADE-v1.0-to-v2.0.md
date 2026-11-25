# 从 V1.0 升级到 V2.0

## 主要变化

1. 规范从 37 条精简为 10 条，执行细节改为 skill，见 V2.0 第 10 条触发表。
2. 合并分两档，满足条件的 PR 由 AI 自行合并（第 5 条）。
3. 用户审批清单只剩 4 项，重大依赖升级、合并不再列入（第 6 条）。
4. main 保护改为执行端拦截，不再要求平台分支保护（`collab-project-setup`）。

## 条款对照

| V1.0 | V2.0 去向 |
|---|---|
| 1 核心原则 | 正文开头；第 1 条事实源。第 6 点（自动化）→ `collab-automation` |
| 2 系统组成 | 删除 |
| 3 Idea Lab、35 Idea Lab 结构 | `collab-idea` |
| 4 项目类型、5 生命周期 | `collab-project-setup` |
| 6 核心文件 | 第 2 条 |
| 7 分类事实源 | 第 1 条 |
| 8 Issue 管理 | 第 3 条（最小信息）；类型、状态、标签 → `collab-issue` |
| 9 任务规模 | `collab-issue` |
| 10 Git 与分支 | 第 4 条；命名等细节 → `collab-merge` |
| 11 Commit | 第 8 条（及时提交）；提交规范 → `collab-merge` |
| 12 PR | `collab-merge` |
| 13 用户合并确认卡 | 第 5 条（分档）；卡片与送达 → `collab-merge` |
| 14 main 保护 | 删除；执行端拦截 → `collab-project-setup` |
| 15 协作模型、16 路由、17 并行冲突 | `collab-assignment` |
| 18 Critical Areas | 第 2 条（定义）；识别清单 → `collab-project-setup`；用于第 5 条分档 |
| 19 独立审查 | `collab-verification` |
| 20 AI 权限 | 第 6 条（只列审批事项） |
| 21 任务交接、22 中断恢复 | 第 8 条；细节 → `collab-handoff` |
| 23 验证 | `collab-verification` |
| 24 Decision Record | `collab-decision` |
| 25 全局规范仓库、26 规范升级 | 第 9 条；升级步骤 → `collab-project-setup` |
| 27–30 流程反馈、维护者、蒸馏、归档 | `collab-standard-maintenance` |
| 31 敏感信息 | 第 7 条 |
| 32 大文件、33 平台迁移、34 项目结构 | `collab-project-setup` |
| 36 V1 暂不做 | 删除；自动化 → `collab-automation` |
| 37 总体链路 | 删除，由触发表代替 |

## 项目升级步骤

按 `collab-project-setup` 的「升级到新规范版本」执行。要点：

1. 用户确认升级。
2. 复制 `standards/versions/v2.0/STANDARD.md` 到项目 `.standards/v2.0/STANDARD.md`，保留旧快照。
3. 更新 AGENTS.md：`Standard Version: v2.0`、锁定路径；删除 V1.0 的场景指引，改为指向第 10 条触发表；保留 Overrides 并检查是否仍需要。
4. 在 PROJECT.md 登记 Critical Areas（第 5 条分档依赖它；未登记但拿不准是否涉及的，按涉及处理，走第二档）。识别清单和默认条目见 `collab-project-setup`。
5. 安装执行端 main 拦截。
6. 在 AGENTS.md 登记第二档确认卡的送达渠道。
7. 走 PR 合并。升级 PR 修改了执行规则，属于第二档。

## 影响评估

结论分三档，与 `collab-standard-maintenance` E 节一致：

| 结论 | 项目情况 |
|---|---|
| 无需处理 | 已归档或暂停；或差异不影响该项目 |
| 建议升级 | 正在使用 V1.0，有待合并 PR 积压或审批经常卡住；V1.0 继续执行没有风险 |
| 必须升级 | 继续执行 V1.0 会导致数据丢失、安全、权限问题，或与平台现状冲突（例如 V1.0 要求的平台分支保护在该仓库无法开启，main 实际无保护） |

V1.0 不再新增修订。
