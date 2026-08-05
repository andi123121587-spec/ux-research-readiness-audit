#!/usr/bin/env python3
"""Validate V2.2 UXRA Markdown reports.

Checks:
- unique Issue IDs and severity counts;
- explicit summary counts match Issue registry;
- Root Cause IDs referenced by Issue rows are well formed;
- action-plan Issue references exist in the registry;
- reports that allow guarded exploration do not also select PAUSE_CORE_PROTOTYPING.
"""
from __future__ import annotations
import argparse, re, sys
from collections import Counter
from pathlib import Path

ISSUE_ID_RE = re.compile(r"\bUXRA-[A-Z]{3}-\d{3}\b")
ROOT_ID_RE = re.compile(r"\bRC-\d{3}\b")
SEVERITY_RE = re.compile(r"\b(BLOCKER|MAJOR|MINOR)\b")
TRIPLE_RE = re.compile(r"(?P<blocker>\d+)\s*BLOCKER\s*[/|,，]\s*(?P<major>\d+)\s*MAJOR\s*[/|,，]\s*(?P<minor>\d+)\s*MINOR", re.I)


def registry_rows(text: str):
    rows=[]
    in_registry=False
    for lineno,line in enumerate(text.splitlines(),1):
        if 'Issue 注册表' in line: in_registry=True
        elif in_registry and line.startswith('## ') and 'Issue 注册表' not in line: in_registry=False
        if not in_registry or not line.lstrip().startswith('|'): continue
        im=ISSUE_ID_RE.search(line); sm=SEVERITY_RE.search(line)
        if im and sm:
            rm=ROOT_ID_RE.search(line)
            rows.append((im.group(0), sm.group(1).upper(), rm.group(0) if rm else None, lineno))
    return rows


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('report',type=Path); a=ap.parse_args()
    text=a.report.read_text(encoding='utf-8')
    rows=registry_rows(text)
    if not rows:
        print('FAIL: 未在 Issue 注册表中找到 Issue 行。'); return 2
    ids=[r[0] for r in rows]; counts=Counter(r[1] for r in rows); errors=[]
    dup=sorted({x for x in ids if ids.count(x)>1})
    if dup: errors.append('重复 Issue ID: '+', '.join(dup))
    missing_root=[f'{i}@L{ln}' for i,_,rc,ln in rows if rc is None]
    if missing_root: errors.append('Issue 缺少 Root Cause ID: '+', '.join(missing_root))
    expected={k:counts.get(k,0) for k in ('BLOCKER','MAJOR','MINOR')}
    for m in TRIPLE_RE.finditer(text):
        found={'BLOCKER':int(m.group('blocker')),'MAJOR':int(m.group('major')),'MINOR':int(m.group('minor'))}
        if found!=expected: errors.append(f'统计串 `{m.group(0)}` 与注册表 {expected} 不一致')
    # action plan references: references after an action plan heading must exist
    action_text=text.split('行动计划',1)[1] if '行动计划' in text else ''
    dangling=sorted(set(ISSUE_ID_RE.findall(action_text))-set(ids))
    if dangling: errors.append('行动计划引用不存在的 Issue: '+', '.join(dangling))
    if '原型探索状态：`EXPLORE_WITH_GUARDRAILS`' in text and '原型探索状态：`PAUSE_CORE_PROTOTYPING`' in text:
        errors.append('报告同时选择 EXPLORE_WITH_GUARDRAILS 与 PAUSE_CORE_PROTOTYPING')
    total=sum(expected.values())
    print(f"Issue 注册表: {expected['BLOCKER']} BLOCKER / {expected['MAJOR']} MAJOR / {expected['MINOR']} MINOR (Total {total})")
    if errors:
        print('FAIL:'); [print('- '+e) for e in errors]; return 1
    print('PASS: Issue、Root Cause、统计与行动引用一致。'); return 0

if __name__=='__main__': sys.exit(main())
