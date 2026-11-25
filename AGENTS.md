# 规范仓库执行规则

Standard Version: v2.0
规范源：https://github.com/gy9037/project-collaboration-standards

开始任务先读 PROJECT.md、此文件、README.md 与当前 Issue/PR，检查分支和提交状态。首次接手读取 standards/versions/v2.0/STANDARD.md；场景匹配时按其第 10 条触发表读 `skills/` 下对应 skill。维护正式规范或 skill 时另读 standards/AGENTS.md。

任务在分支执行，提交前检查 diff、凭据和无关文件；验证入口为 `python3 tools/verify_package.py`，非代码验收同时核对内容和可操作性。通过 PR 进入 main，默认 Squash Merge，按规范第 5 条分档合并，档位依据 PROJECT.md 的 Critical Areas；修改正式规范或 skill 步骤按第 9 条走第二档。

通知用户的渠道：<待用户登记；登记前发到当前会话，并在 PR 保存一份>

仓库经用户确认改为公开，main 已启用 PR 必须、管理员适用、禁止强推和删除、线性历史保护。第二档的用户确认须保存于 PR；平台不识别聊天批准。

用户审批事项只有规范第 6 条四类；清单外的事自行处理，在 Issue / PR 记录并汇报。

Overrides：无。
