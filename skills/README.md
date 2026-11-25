# Skills

本目录是 skill 正本。规范只写原则和底线，具体做法在这里；规范 V2.0 第 10 条触发表决定什么场景用哪个 skill。skill 与规范冲突时以规范为准。

## 列表与触发场景

| 场景 | skill |
|---|---|
| 有新想法、判断是否值得立项 | [collab-idea](collab-idea/SKILL.md) |
| 新建项目、把已有仓库接入本规范、项目升级规范版本、迁移平台 | [collab-project-setup](collab-project-setup/SKILL.md) |
| 新建或补全 Issue | [collab-issue](collab-issue/SKILL.md) |
| 安排执行者、并行推进多个 Issue | [collab-assignment](collab-assignment/SKILL.md) |
| 任务交付后验收 | [collab-verification](collab-verification/SKILL.md) |
| PR 准备合并 | [collab-merge](collab-merge/SKILL.md) |
| 换执行者、换模型、暂停、额度将尽，或接手进行中的任务 | [collab-handoff](collab-handoff/SKILL.md) |
| 做出影响未来判断的决定 | [collab-decision](collab-decision/SKILL.md) |
| 发现流程问题、整理反馈、修改规范或 skill、发布新版本 | [collab-standard-maintenance](collab-standard-maintenance/SKILL.md) |
| 要把某项工作做成自动化 | [collab-automation](collab-automation/SKILL.md) |

## 安装

单独 clone 一份本仓库，只用于同步：停在 main，只执行 `git pull`，不在里面修改。在这个 clone 根目录把 `skills/<name>` 链接到所用工具的 skill 目录，例如：

```sh
for d in skills/collab-*; do ln -sfn "$PWD/$d" ~/.config/opencode/skills/; done   # OpenCode
for d in skills/collab-*; do ln -sfn "$PWD/$d" ~/.claude/skills/; done            # Claude Code
for d in skills/collab-*; do ln -sfn "$PWD/$d" ~/.agents/skills/; done            # 其他读取 ~/.agents/skills 的工具
```

skill 合并后在该 clone 执行 `git pull`。复制安装的，每次 skill 合并后重新复制，并核对与 main 一致。

## 修改

不在链接目标（同步用 clone）里改 skill。修改在另一个工作副本的任务分支进行，经 PR 合并后再同步。

兼容性：skill 必须兼容所有在用的规范版本。某步骤只适用于特定版本时，在 skill 内注明版本；无法兼容的修改随新规范版本发布。

修改 skill 走规范第 9 条：改变步骤或判定条件等同修改规范，按第 5 条第二档由用户确认合并；只改措辞的按第 5 条正常判档。流程见 [collab-standard-maintenance](collab-standard-maintenance/SKILL.md)。
