from pathlib import Path
import re,json,sys
r=Path(sys.argv[1] if len(sys.argv)>1 else '.'); errors=[]
for f in r.rglob('*.md'):
 if '.git' in f.parts: continue
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' not in target and not target.startswith('#') and not (f.parent/target.split('#')[0]).exists(): errors.append(f'{f}: {target}')
s=(r/'standards/versions/v1.0/STANDARD.md').read_text()
assert len(re.findall(r'^# \d+\.',s,re.M))==37
for p in ['project-template/.standards/v1.0/STANDARD.md','idea-lab/.standards/v1.0/STANDARD.md']: assert (r/p).read_text()==s
for kind in ['feature','bug','improvement','research','maintenance']:
 t=(r/f'project-template/.github/ISSUE_TEMPLATE/{kind}.md').read_text()
 for field in ['目标或问题','验收标准','关联对象','当前状态']: assert field in t
assert not errors,errors
print(json.dumps({'result':'PASS','markdown_links':'PASS','37_sections':'PASS','locked_snapshots':'PASS','issue_fields':'PASS','files':len([f for f in r.rglob('*') if f.is_file() and '.git' not in f.parts])},ensure_ascii=False))
