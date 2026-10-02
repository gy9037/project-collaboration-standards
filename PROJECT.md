# 项目协作规范：当前状态

项目类型：non-code
项目目标：维护可迁移、可交接的项目协作规范及模板。
第一阶段目标：V1.0 文件包入库，经用户确认后通过 PR 进入 main；配置可用的保护并验证首次真实任务链路。
当前阶段：接入准备 / 规划
最近更新时间：2026-10-02
来源：ChatGPT 项目“项目协作规范”中的已确认 RC1 及正式 V1.0 文件包。

## 当前重点

1. 初始导入 PR 与用户验收。
2. 核对已启用的 main 保护与保存用户确认记录。
3. 完成首次真实受控任务验收，之后逐步接入试点项目。

## 当前边界与约束

范围为规范、Idea Lab 和通用模板，不开发初始化脚本或未验证自动化。当前仓库公开（用户已确认）；维护者角色由本次协调 Agent 暂负责，后续执行不绑定模型；每周整理职责未建立定时任务。

当前待办：main 保护已配置并通过 API 回读核对；导入 PR 等待用户对当前版本确认。真实合并流程尚未执行，不宣称接入验收完成。

## Critical Areas

- standards/versions/：已发布规范版本及历史，规则变更须用户确认和新版本处理。
- project-template/AGENTS.md 及锁定快照：跨项目权限与执行规则。
- .github/、根 AGENTS.md：本仓库任务入口及合并约束。

## 入口与验证

- 正式规范：standards/versions/v1.0/STANDARD.md
- 使用入口：README.md
- 审查证据：audit/BLIND-REVIEW.md、audit/BLIND-RECHECK.md
- 接入证据：audit/GITHUB-ADOPTION.md
- 静态验证：python3 tools/verify_package.py
- Issue：https://github.com/gy9037/project-collaboration-standards/issues/1
- PR：https://github.com/gy9037/project-collaboration-standards/pull/2
- DR：暂无。

GitHub 已自动建立含 README 的空仓库起点；V1.0 正式内容通过任务分支与 PR 导入。暂无生产环境或部署。
