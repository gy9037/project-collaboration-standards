---
name: collab-project-setup
description: "新建正式项目、把已有仓库接入本规范、升级项目锁定的规范版本、迁移 Git 平台，含 main 保护的执行端拦截配置。当 Idea 已 Ready 要立项、已有仓库要接入规范、项目要升级规范版本或迁移平台时使用。"
---

# 项目接入与升级

## 用途

让一个项目满足规范第 2、4 条的底线：有三个核心文件、锁定规范版本、main 只能经 PR 进入，并用首个真实任务验证流程走得通。

## 触发场景

- Idea 已 Ready，要建正式项目（来自 collab-idea）。
- 已有仓库要接入本规范。
- 项目要升级到新规范版本。
- 项目迁移 Git 平台，或新增一个本地 clone / 执行环境。

不触发：想法未 Ready → collab-idea；项目内日常任务 → collab-issue。

## 步骤

### A. 新建或接入

1. **建仓库。** 新项目用 `gh repo create <owner>/<name> --private --add-readme`，由平台生成 main 的首个 commit，之后全部走 PR，不向 main 推送。公开仓库属于对外发布（规范第 6 条第 1 项），先取得用户审批。clone 后立即做 C 节，再做任何推送。
2. **建任务分支** `chore/setup-collab`，复制规范仓库 `project-template/` 的全部文件（含 `.github/`、`.standards/`）。已有仓库只补缺失文件，不覆盖已有内容。
3. **判断项目类型**，写入 PROJECT.md：
   - `code`：成果是软件、脚本、服务，要构建、测试或部署。
   - `non-code`：成果是研究、方案、设计、内容、运营等。
   - `hybrid`：两类工作长期都占重要部分。
4. **填三个核心文件**（规范第 2 条）：
   - PROJECT.md：目标、类型、第一阶段目标及验收条件、当前阶段（立项 / 规划 / 执行 / 验证 / 阶段交付 / 维护迭代 / Paused / Archived）、范围与暂不做、约束、Critical Areas、实际验证入口（code 写测试 / 构建命令，non-code 写交付物和验收方式）、来源 Idea 链接。
   - AGENTS.md：`Standard Version: <版本>`、规范源仓库 URL、锁定快照路径 `.standards/<版本>/STANDARD.md`、开工必读、验证入口、通知用户的渠道（第二档确认卡、合并通知、待决问题发到哪里）、Overrides（无则写「无」）。
   - README.md：项目是什么、怎么开始了解或使用。
   - Critical Areas：保留模板中的默认条目（AGENTS.md、PROJECT.md 的 Critical Areas 段、`.standards/`、main 拦截配置、已安装 skill、依赖清单/锁文件、构建与部署配置）。再按识别清单逐项判断：核心功能、关键数据、基础架构、核心依赖（含依赖清单/锁文件）、关键配置（含构建/部署/CI 配置）。识别不全的写「其余待识别」。
5. **最低完整性检查。** 逐条确认，缺一条就在 PROJECT.md 写明缺口和负责人，不开始执行：
   - 第一阶段目标可验收；边界和约束清楚；
   - 高风险依赖已验证或有验证计划；
   - 阻止开工的未知问题有人处理；
   - 首批任务明确（按 collab-issue 建好）。
6. **按需建目录。** 只建现在用得到的。`docs/decisions/` 等到第一个 DR 时再建。视频、数据集、大型设计文件放外部存储，在 PROJECT.md「外部资料」写位置、用途、对应版本或任务，必要时写校验值。
7. **建标签**（含义见 collab-issue）：
   ```sh
   for l in feature bug improvement research maintenance todo in-progress blocked review; do gh label create "$l" --force; done
   ```
8. **核对 main 保护**：C 节已覆盖每个 clone 和执行环境。
9. **提 PR。** 接入 PR 含项目目标、范围等用户取舍，按规范第 5 条第二档由用户确认后合并。
10. **首个真实任务验收。** 选一个范围明确、风险可控、有验收标准的真实任务，完整走 Issue → 分支 → 验证 → PR → 按第 5 条分档合并。另外按 C 节第 1 项的验证命令确认推送 main 被 hook 拒绝。两项都通过后，在接入 Issue 记录证据并写「接入验收完成」；未通过时记录问题和下一步，不宣称已完成。

### B. 升级规范版本

1. 用户确认要升级（规范第 9 条）后，建 Issue 和分支 `chore/standard-<新版本>`。
2. 对比新旧版本，在 Issue 列出：对本项目有影响的条款、AGENTS.md 要改的地方、每条 Override 是否仍成立、风险。
3. 复制新版 `STANDARD.md` 到 `.standards/<新版本>/`，旧快照保留不删。
4. 改 AGENTS.md：`Standard Version`、锁定路径、场景指引（v2.0 起改为指向规范第 10 条触发表）、删除已失效的 Overrides。
5. 补齐新版本要求但项目缺少的配置（例如 v1.0 → v2.0 要安装 C 节的 hook 和执行端拒绝规则）。
6. PR 写差异、风险、验证结果，按第二档由用户确认合并；合并后生效。

### C. main 保护（执行端拦截）

目标：拦住 AI 误操作推 main 和强推，不拦用户本人。不依赖平台分支保护（私有仓库免费账号开不了）。

**1. 每个本地 clone 安装 pre-push hook。** 保存为 `$(git rev-parse --git-common-dir)/hooks/pre-push` 并 `chmod +x`（同一 clone 的所有 worktree 共用）。项目用 husky 等工具自定义了 `core.hooksPath` 时，hook 文件位置不同：按 `git config core.hooksPath` 的实际路径安装，下面第 2 项拒绝编辑的路径也改成该路径。

```sh
#!/bin/sh
# collab pre-push：拒绝推送 main/master、拒绝非快进（强推）。用户本人绕过：COLLAB_ALLOW_PROTECTED_PUSH=1 git push ...
[ "${COLLAB_ALLOW_PROTECTED_PUSH:-}" = "1" ] && { echo "pre-push: 已按用户显式设置放行" >&2; exit 0; }
status=0
while read -r local_ref local_sha remote_ref remote_sha; do
  case "$remote_ref" in
    refs/heads/main|refs/heads/master)
      echo "pre-push: 拒绝推送到 ${remote_ref#refs/heads/}，改走任务分支和 PR。" >&2
      status=1; continue ;;
  esac
  case "$local_sha" in *[!0]*) ;; *) continue ;; esac   # 删除任务分支：放行
  case "$remote_sha" in *[!0]*) ;; *) continue ;; esac  # 新建远端分支：放行
  if ! git merge-base --is-ancestor "$remote_sha" "$local_sha" 2>/dev/null; then
    echo "pre-push: 拒绝对 $remote_ref 的非快进推送。先 fetch 并 merge，不用 rebase 后强推。" >&2
    status=1
  fi
done
exit $status
```

- 拦截：推到 main/master（含删除）、`--force`、`--force-with-lease`、`+refspec` 造成的非快进。放行：任务分支新建、快进、删除。
- 用户本人绕过：`COLLAB_ALLOW_PROTECTED_PUSH=1 git push ...`，单次生效。AI 不得自行设置该变量，也不得用 `--no-verify`。
- 平台上的合并（`gh pr merge`）不经过 hook，第 5 条第一档照常可用。
- 验证：构造一个领先 main 的提交再 dry-run 推送（HEAD 与远端 main 相同时 git 不调用 hook，直接推 HEAD 测不出来）：
  `git push --dry-run origin "$(git commit-tree HEAD^{tree} -p HEAD -m hook-test)":refs/heads/main`
  期望输出「拒绝推送到 main」且退出码非 0。

**2. Agent 执行环境配置拒绝规则。** hook 可被 `--no-verify`、改 hooksPath 绕过，执行环境要再拦一层。以 OpenCode 为例（V2 格式，最后匹配的规则生效，放在 `permissions` 数组末尾；V1 写在 `permission.bash` 下）：

```jsonc
{ "action": "shell", "resource": "git push * main", "effect": "deny" },
{ "action": "shell", "resource": "git push * main *", "effect": "deny" },
{ "action": "shell", "resource": "git push *:main", "effect": "deny" },
{ "action": "shell", "resource": "git push *:main *", "effect": "deny" },
{ "action": "shell", "resource": "git push *refs/heads/main*", "effect": "deny" },
{ "action": "shell", "resource": "gh pr merge *--admin*", "effect": "deny" },
{ "action": "shell", "resource": "git push *--force*", "effect": "deny" },
{ "action": "shell", "resource": "git push -f*", "effect": "deny" },
{ "action": "shell", "resource": "git push * -f*", "effect": "deny" },
{ "action": "shell", "resource": "git push *+*", "effect": "deny" },
{ "action": "shell", "resource": "git push *--no-verify*", "effect": "deny" },
{ "action": "shell", "resource": "*COLLAB_ALLOW_PROTECTED_PUSH*", "effect": "deny" },
{ "action": "shell", "resource": "*core.hooksPath*", "effect": "deny" },
{ "action": "edit", "resource": "*.git/hooks/*", "effect": "deny" }
```

master 分支的项目把 `main` 换成 `master` 再加一组。其他工具（Claude Code、Codex 等）按各自的权限配置写同等规则。规则按命令文本匹配，拦不住「在 main 上直接 `git push`」这类不带分支名的写法，hook 是主防线，两层都要装。配置后在执行环境里试跑 `git push --no-verify --dry-run origin HEAD:main`，确认被拒绝。

**3. 可选：平台分支保护。** 公开仓库或付费账号可额外开启。这是平台权限变更（规范第 6 条第 3 项），先取得用户审批：

```sh
gh api -X PUT repos/<owner>/<repo>/branches/main/protection --input - <<'EOF'
{"required_status_checks":null,"enforce_admins":true,
 "required_pull_request_reviews":{"required_approving_review_count":0},
 "restrictions":null,"allow_force_pushes":false,"allow_deletions":false,"required_linear_history":true}
EOF
```

已有 CI 检查时把 `required_status_checks` 改为 `{"strict":true,"contexts":["<检查名>"]}`。

### D. 迁移平台

迁移 Issue、PR、标签、任务状态、DR 关联、必要的评论和交接记录；不能迁的导出归档并在 PROJECT.md 写位置。新平台按 A 节第 7、8 步重建标签和保护。

## 示例

Idea「账单整理」已 Ready：`gh repo create me/bill-tidy --private --add-readme` → 分支 `chore/setup-collab` 复制模板，类型 code，验证入口 `pytest`，Overrides 无 → 完整性检查通过 → 建标签 → 安装 hook，构造领先提交 dry-run 推 main 被拒 → OpenCode 加拒绝规则 → 接入 PR 由用户确认合并 → 首个任务「解析 A 银行 CSV」按流程合并 → 接入 Issue 写「接入验收完成」，回填 Idea 的项目链接。

## 验收

- [ ] README.md、PROJECT.md、AGENTS.md 已填写，无模板占位符；项目类型、验证入口已写。
- [ ] AGENTS.md 有规范版本、源仓库 URL、锁定快照路径、通知用户的渠道和 Overrides；快照文件存在。
- [ ] 最低完整性检查每条有结论，缺口有负责人。
- [ ] 9 个标签（5 类型 + 4 状态）已建。
- [ ] Critical Areas 含默认条目，已按识别清单逐项判断。
- [ ] 每个 clone 的 hook 已装，构造领先提交的 dry-run 推送 main 被拒绝。
- [ ] 执行环境拒绝规则已配置并试跑被拒。
- [ ] 首个真实任务按流程完成，接入 Issue 有证据和「接入验收完成」。
- [ ] 升级时：新旧快照都在，差异和 Overrides 结论记在 Issue，经用户确认合并。
