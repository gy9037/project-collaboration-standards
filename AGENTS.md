# 规范仓库执行规则

Standard Version: v1.0
规范源：https://github.com/gy9037/project-collaboration-standards

开始任务先读 PROJECT.md、此文件、README.md 与当前 Issue/PR，检查分支和提交状态。首次接手读取 standards/versions/v1.0/STANDARD.md；维护正式规范时另读 standards/AGENTS.md 与 MAINTAINER.md。

任务在分支执行，提交前检查 diff、凭据和无关文件；验证入口为 `python3 tools/verify_package.py`，非代码验收同时核对内容和可操作性。需追踪任务建立 Issue。通过 PR 进入 main，默认 Squash Merge，合并当前版本前必须取得用户确认。

关键规则变动或用户要求触发独立审查；按需交接写在当前 Issue。证据可确定的事实源失配予以同步，否则交用户判断。中央规范升级不自动修改旧项目。

main 平台保护暂因私有仓库套餐限制无法启用。此风险不授予直接 push、强推或自动合并权限。升级套餐、改为公开或采用其他方案需用户决定。

Overrides：无。

合并 main、生产部署、重要删除、账号/密钥/权限修改、重大依赖升级、实际费用、对外正式发布或发送，需要用户确认。
