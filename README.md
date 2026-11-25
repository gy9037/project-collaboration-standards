# 可迁移项目协作系统 V2.0

本仓库公开（用户已确认）：[gy9037/project-collaboration-standards](https://github.com/gy9037/project-collaboration-standards)。项目状态见 [PROJECT.md](PROJECT.md)，执行规则见 [AGENTS.md](AGENTS.md)，实时任务进度见仓库 [Issues](https://github.com/gy9037/project-collaboration-standards/issues) / [PRs](https://github.com/gy9037/project-collaboration-standards/pulls)。

V2.0 把规范精简为 10 条原则和底线，执行细节改为 skill，由规范第 10 条触发表指向。决定原因见 [DR-001](standards/decisions/DR-001-精简规范并将执行细节改为skill.md)，从 V1.0 升级见 [升级说明](standards/versions/v2.0/UPGRADE-v1.0-to-v2.0.md)。

## 使用

1. 阅读 [正式规范 V2.0](standards/versions/v2.0/STANDARD.md)，重点是第 10 条触发表。
2. 按触发表使用 [skills](skills/README.md)：想法用 collab-idea，立项和接入用 collab-project-setup，依此类推。
3. 想法探索使用 [Idea Lab](idea-lab/README.md)。
4. 正式立项复制 [项目模板](project-template/README.md)，填写三个核心文件。
5. 需要决策、研究、交接等内容时，从 [可选模板](optional-templates/README.md) 复制对应文件。

规范版本锁定在项目内 `.standards/<版本>/STANDARD.md`；中央新版本不会自动改变现有项目，升级需用户确认。

## V1.0 历史

[V1.0 正文](standards/versions/v1.0/STANDARD.md)（37 节）原文保留，不再修订。V1.0 导入 [PR #2](https://github.com/gy9037/project-collaboration-standards/pull/2) 于 2026-10-02 经用户确认后 Squash Merge，[Issue #1](https://github.com/gy9037/project-collaboration-standards/issues/1) 已关闭；状态同步见 [Issue #3](https://github.com/gy9037/project-collaboration-standards/issues/3) · [PR #4](https://github.com/gy9037/project-collaboration-standards/pull/4)。`baseline/` 保留已确认 RC1；`audit/` 保存独立审查、修订与复核证据，其中「未初始化 Git」等描述针对当时的交付快照。main 保护配置见 [GitHub 接入记录](audit/GITHUB-ADOPTION.md)。

## 发布证据

[发布说明](RELEASE-NOTES.md) · [文件校验清单](MANIFEST.sha256)

V1.0：[独立初审](audit/BLACKBOX-REVIEW.md) · [独立复核](audit/BLACKBOX-RECHECK.md) · [修订记录](audit/REVISIONS.md) · [验证记录](audit/VERIFICATION.md) · [补充独立盲审](audit/BLIND-REVIEW.md) · [盲审修订复核](audit/BLIND-RECHECK.md) · [盲审输入校验记录](audit/BLIND-INPUT-MANIFEST.json)
