from pathlib import Path
import hashlib, json, re, sys

r = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
results, errors = {}, []

def check(name, problems):
    results[name] = 'PASS' if not problems else 'FAIL'
    errors.extend(f'{name}: {p}' for p in problems)

def sha(p):
    return hashlib.sha256((r / p).read_bytes()).hexdigest()

# Markdown 链接有效
bad = []
for f in r.rglob('*.md'):
    if '.git' in f.parts: continue
    for target in re.findall(r'\]\(([^)]+)\)', f.read_text()):
        if '://' not in target and not target.startswith('#') and not (f.parent / target.split('#')[0]).exists():
            bad.append(f'{f.relative_to(r)} -> {target}')
check('markdown_links', bad)

# v1.0 与 RC1 原文未改动（发布时的 SHA-256），v1.0 仍为 37 节
FROZEN = {
    'standards/versions/v1.0/STANDARD.md': '6c561dc8f7d07399c3115d75b2c39aa5c198a440040135b8db674e171c7a07a3',
    'baseline/V1.0-RC1.md': '9320a9e0eeb30f49ce6d5784f46e807f2515985a9c1b7a638bed5a6b18b8a7b5',
}
v1 = (r / 'standards/versions/v1.0/STANDARD.md').read_text()
p = [f'{k} 已改动' for k, v in FROZEN.items() if sha(k) != v]
n = len(re.findall(r'^# \d+\.', v1, re.M))
if n != 37: p.append(f'v1.0 节数 {n} != 37')
check('v1_frozen', p)

# v2.0 为 10 节
v2_path = 'standards/versions/v2.0/STANDARD.md'
v2 = (r / v2_path).read_text()
n = len(re.findall(r'^## \d+\.', v2, re.M))
check('v2_10_sections', [] if n == 10 else [f'v2.0 节数 {n} != 10'])

# 锁定快照与中央 v2.0 逐字节相同
snaps = ['project-template/.standards/v2.0/STANDARD.md', 'idea-lab/.standards/v2.0/STANDARD.md']
check('locked_snapshots', [s for s in snaps if not (r / s).exists() or (r / s).read_bytes() != (r / v2_path).read_bytes()])

# 触发表中的 skill 存在、frontmatter name 一致，且 skills/ 下没有表外 skill
table = v2.split('## 10.', 1)[1]
names = re.findall(r'^\|[^|\n]+\|\s*(collab-[a-z-]+)\s*\|\s*$', table, re.M)
p = [] if names else ['触发表未解析到 skill']
for name in names:
    f = r / 'skills' / name / 'SKILL.md'
    if not f.exists():
        p.append(f'{name}: 缺少 SKILL.md'); continue
    m = re.match(r'---\n(.*?)\n---\n', f.read_text(), re.S)
    fm_name = re.search(r'^name:\s*(\S+)\s*$', m.group(1), re.M) if m else None
    if not fm_name or fm_name.group(1) != name:
        p.append(f'{name}: frontmatter name 不一致')
extra = sorted({d.name for d in (r / 'skills').iterdir() if d.is_dir()} - set(names))
p += [f'{d}: 不在触发表中' for d in extra]
check('skill_trigger_table', p)

# 每个 SKILL.md 含必需章节
p = []
for f in sorted((r / 'skills').glob('*/SKILL.md')):
    t = f.read_text()
    p += [f'{f.parent.name}: 缺少 {h}' for h in ['## 触发场景', '## 步骤', '## 验收'] if not re.search(rf'^{h}\s*$', t, re.M)]
check('skill_sections', p)

# Issue 模板通用字段
p = []
for kind in ['feature', 'bug', 'improvement', 'research', 'maintenance']:
    t = (r / f'project-template/.github/ISSUE_TEMPLATE/{kind}.md').read_text()
    p += [f'{kind}: 缺少 {field}' for field in ['目标或问题', '验收标准', '关联对象', '当前状态'] if field not in t]
check('issue_fields', p)

out = {'result': 'PASS' if not errors else 'FAIL', **results, 'skills': len(names),
       'files': len([f for f in r.rglob('*') if f.is_file() and '.git' not in f.parts])}
if errors: out['errors'] = errors
print(json.dumps(out, ensure_ascii=False, indent=1))
sys.exit(1 if errors else 0)
