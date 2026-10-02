# 可迁移项目协作系统 V1.0

## 当前 GitHub 仓库

本仓库公开（用户已确认）：[gy9037/project-collaboration-standards](https://github.com/gy9037/project-collaboration-standards)。V1.0 导入 [PR #2](https://github.com/gy9037/project-collaboration-standards/pull/2) 已于 2026-10-02 经用户确认后 Squash Merge，[Issue #1](https://github.com/gy9037/project-collaboration-standards/issues/1) 已关闭。main 保护配置已回读核对；尚无试点接入验收证据，不代表整个接入验收完成。

当前处于导入完成后维护 / 试点准备阶段。状态同步任务及关联 PR 见 [Issue #3](https://github.com/gy9037/project-collaboration-standards/issues/3)，本维护任务只推进至 PR 等待用户确认，不执行合并；实时进度以 Issue/PR 为准。项目状态见 [PROJECT.md](PROJECT.md)，执行规则见 [AGENTS.md](AGENTS.md)，证据与未验证项见 [GitHub 接入记录](audit/GITHUB-ADOPTION.md)。

## 文件包与使用

本文件包提供三个可分别建立 Git 仓库的目录：`standards/`、`idea-lab/`、`project-template/`。交付时快照尚未连接远端或配置真实平台保护规则；该历史描述不代表本仓库当前状态，也不代表使用模板的项目已完成接入。

1. 阅读 [正式规范](standards/versions/v1.0/STANDARD.md)。
2. 想法探索使用 [Idea Lab](idea-lab/README.md)。
3. 正式立项复制 [项目模板](project-template/README.md) 并填写三个核心文件。
4. 按 [接入清单](standards/ADOPTION.md) 建立远端、Issue 与 PR 流程。
5. 需要决策、研究、交接等内容时，再从 [可选模板](optional-templates/README.md) 复制对应文件。

规范版本锁定在项目内 `.standards/v1.0/STANDARD.md`；中央新版本不会自动改变现有项目。`baseline/` 保留已确认 RC1；`audit/` 保存独立审查、修订与复核证据。

原文件包交付时仅交付本地文件包，没有部署、合并 main、对外发送或创建定时自动化。历史材料中的“未初始化 Git”等描述均针对交付时快照；后续仓库接入与合并记录见上方当前状态入口。

## 发布证据

[发布说明](RELEASE-NOTES.md) · [独立初审](audit/BLACKBOX-REVIEW.md) · [独立复核](audit/BLACKBOX-RECHECK.md) · [修订记录](audit/REVISIONS.md) · [验证记录](audit/VERIFICATION.md) · [文件校验清单](MANIFEST.sha256)

[补充独立盲审](audit/BLIND-REVIEW.md) · [盲审修订复核](audit/BLIND-RECHECK.md) · [盲审输入校验记录](audit/BLIND-INPUT-MANIFEST.json)
