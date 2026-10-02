# GitHub 接入记录

以下早期记录保留当时原文；其中“未生效”“尚待确认”“没有实际合并”等仅适用于对应历史阶段，不代表当前状态。最新核对见文末“合并后状态核对”。

## 历史阶段一：初建与套餐限制

日期：2026-10-02
仓库：gy9037/project-collaboration-standards，初建 private=true；经用户明确回复“公开吧”，现 private=false。

用户在确认现有 GitHub 授权与私有仓库建议后回复“可以”，据此创建私有仓库；GitHub auto_init 创建 README 起点，未将 V1.0 文件直接 push 到 main。正式内容在任务分支通过 PR 导入。

已核实本机授权有效。API 请求仓库 rulesets 返回 HTTP 403：Upgrade to GitHub Pro or make this repository public to enable this feature。未更改可见性、购买套餐或配置绕过权限。用户需决定后续方案；目前 main 保护未生效，严格执行分支/PR/用户确认行为规则但不将其冒充平台保护。

已具备：本地规范及审查文件、根核心文件、Issue/PR 模板、静态验证入口。导入任务尚待用户确认及保护限制处理，接入验收未完成。

## 历史阶段二：公开与保护配置（合并前）

用户确认：本会话“公开吧”。公开前检查仓库工作树和提交，未发现真实凭据；删除输入清单中的本机绝对路径，导入提交采用 GitHub 隐私邮箱。规范正文与审查结论未变。仅改写本协调者创建的未合并任务提交，未改写 main。

main 保护 PUT 配置成功并回读：PR 必须、管理员适用、禁止 force push、禁止删除、要求线性历史。当前无 CI 状态检查；审批 review 数量为 0，单人仓库不要求自己审批自己的 PR。用户对当前版本的明确合并确认仍由执行规则和 PR 确认卡保存，未将其声称为 GitHub 自动识别聊天的门禁。

平台配置读取已验证；没有用直接 push main 的破坏性试验验证，没有实际合并 PR，完整接入验收仍未完成。原套餐阻塞解除，当前等待用户合并确认。

## 合并后状态核对

核对日期：2026-10-02。维护任务：[Issue #3](https://github.com/gy9037/project-collaboration-standards/issues/3)。本节为只读核对，不重新执行历史合并或修改平台配置。

- [PR #2](https://github.com/gy9037/project-collaboration-standards/pull/2) 状态为 MERGED，合并时间为 `2026-10-02T03:41:45Z`（北京时间 11:41:45），mergeCommit 为 `a0ef723d0700123b18ecb6a5878a8f8a4de2faf4`，与本次核对的 main SHA 一致。
- PR #2 正文保存用户对 head `6b761df9ea88fcec9a04b3167400097e5d3aebb0` 的明确合并确认；[Issue #1](https://github.com/gy9037/project-collaboration-standards/issues/1) 已 CLOSED，正文记录已 Squash Merge。
- Issue #1 正文另记录合并后 59 个文件的 Git blob 校验通过。这是导入任务的历史验证记录，本次未重做该项校验。
- 仓库可见性为 PUBLIC。main protection API 回读显示 PR required、`enforce_admins=true`、`required_linear_history=true`、`allow_force_pushes=false`、`allow_deletions=false`、`required_approving_review_count=0`，未配置 required status checks。配置回读不等于阻断行为测试，用户确认仍依赖执行规则与 PR 记录，不是平台自动识别聊天批准。
- 本维护任务开始时，本地分支为 `gy9037/orca-onboarding`，HEAD 与上述 main SHA 一致，工作区干净，无无关改动；随后从该提交创建任务分支 `docs/3-sync-adoption-status`。

核对命令与接口（均为只读）：

```sh
gh pr view 2 --repo gy9037/project-collaboration-standards --json state,mergedAt,mergeCommit,body,url
gh issue view 1 --repo gy9037/project-collaboration-standards --json state,body,url
gh repo view gy9037/project-collaboration-standards --json visibility
gh api repos/gy9037/project-collaboration-standards/commits/main --jq .sha
gh api repos/gy9037/project-collaboration-standards/branches/main/protection
git status --short --branch
git rev-parse HEAD
```

证据入口：[合并提交](https://github.com/gy9037/project-collaboration-standards/commit/a0ef723d0700123b18ecb6a5878a8f8a4de2faf4) · [main 保护 API](https://api.github.com/repos/gy9037/project-collaboration-standards/branches/main/protection)（需相应读取权限，返回实时配置）。

验证边界：初始导入已完成真实的用户确认后 PR 合并；配置已回读核对。未进行直接 push main 被阻断的破坏性测试，尚无试点项目接入验收证据，也未验证全部使用场景，不宣称整个接入验收完成。Issue #3 本维护任务只推进至 PR 等待用户确认，不执行合并；后续实时进度以该 Issue 及关联 PR 为准。
