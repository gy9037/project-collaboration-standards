# 可迁移项目协作系统 V1.0

本文件包提供三个可分别建立 Git 仓库的目录：`standards/`、`idea-lab/`、`project-template/`。这是可落地的文件模板包，尚未连接远端或配置真实平台保护规则。

1. 阅读 [正式规范](standards/versions/v1.0/STANDARD.md)。
2. 想法探索使用 [Idea Lab](idea-lab/README.md)。
3. 正式立项复制 [项目模板](project-template/README.md) 并填写三个核心文件。
4. 按 [接入清单](standards/ADOPTION.md) 建立远端、Issue 与 PR 流程。
5. 需要决策、研究、交接等内容时，再从 [可选模板](optional-templates/README.md) 复制对应文件。

规范版本锁定在项目内 `.standards/v1.0/STANDARD.md`；中央新版本不会自动改变现有项目。`baseline/` 保留已确认 RC1；`audit/` 保存独立审查、修订与复核证据。

本次发布仅交付本地文件包，没有部署、合并 main、对外发送或创建定时自动化。

## 发布证据

[发布说明](RELEASE-NOTES.md) · [独立初审](audit/BLACKBOX-REVIEW.md) · [独立复核](audit/BLACKBOX-RECHECK.md) · [修订记录](audit/REVISIONS.md) · [验证记录](audit/VERIFICATION.md) · [文件校验清单](MANIFEST.sha256)

[补充独立盲审](audit/BLIND-REVIEW.md) · [盲审修订复核](audit/BLIND-RECHECK.md) · [盲审输入校验记录](audit/BLIND-INPUT-MANIFEST.json)

## 当前 GitHub 仓库

本仓库公开（用户已确认）：[gy9037/project-collaboration-standards](https://github.com/gy9037/project-collaboration-standards)。当前状态见 [PROJECT.md](PROJECT.md)，执行规则见 [AGENTS.md](AGENTS.md)。文件包历史的“未初始化 Git”描述针对交付时快照；实际接入进度以 PROJECT.md 与 [GitHub 接入记录](audit/GITHUB-ADOPTION.md) 为准。
