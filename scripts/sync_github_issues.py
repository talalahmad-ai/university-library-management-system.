#!/usr/bin/env python3
"""Dry-run by default. --apply creates missing labels/milestones/task Issues without duplicate titles.

Requires a GitHub connection with Issues read/write permission. Never changes accounts,
repository names, collaborator settings or existing Issue bodies. Uses no embedded secrets.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'reports/planning-data.json').read_text())
PLAN=json.loads((ROOT/'.github/issue-plan.json').read_text())
REPO=DATA['repository']

def gh(args,payload=None):
    result=subprocess.run(['gh',*args],input=json.dumps(payload) if payload is not None else None,
                          capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return json.loads(result.stdout) if result.stdout.strip() else None

def collection(path):
    items=[];page=1
    while True:
        separator='&' if '?' in path else '?'
        batch=gh(['api',f'{path}{separator}per_page=100&page={page}'])
        items.extend(batch)
        if len(batch)<100:return items
        page+=1

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    existing=collection(f'repos/{REPO}/issues')
    closed=collection(f'repos/{REPO}/issues?state=closed')
    issues=[i for i in existing+closed if 'pull_request' not in i]
    matched={}
    for item in PLAN:
        same=[i for i in issues if i['title'].startswith('['+item['id']+'] ')]
        if len(same)>1:raise RuntimeError('Duplicate WBS Issues found for '+item['id']+'; review manually.')
        if same:matched[item['id']]=same[0]
    for item in PLAN:
        print(('EXISTS' if item['id'] in matched else 'WOULD CREATE')+' '+item['title']+' → @talalahmad-ai')
    if not args.apply:
        print('Dry run only. Use --apply after Issues write access is available.');return
    gh(['api',f'repos/{REPO}/assignees/talalahmad-ai'])
    labels={x['name'] for x in collection(f'repos/{REPO}/labels')}
    for name,color in [('assignment-1','16648A'),('assignment-2','316D54'),('assignment-3','765295'),('assignment-4','B55B28'),('planning','2D6A85'),('future-phase','BDB5AA')]:
        if name not in labels:gh(['api','--method','POST',f'repos/{REPO}/labels','--input','-'],{'name':name,'color':color,'description':'Coursework task tracking; later phases planned only' if name=='future-phase' else 'University LMS planning'})
    milestones=gh(['api',f'repos/{REPO}/milestones?state=all&per_page=100']);phase_numbers={}
    for m in DATA['milestones']:
        title=m['phase']+' — '+m['name'];same=next((x for x in milestones if x['title']==title),None)
        if same is None:
            same=gh(['api','--method','POST',f'repos/{REPO}/milestones','--input','-'],{'title':title,'description':f"Proposed target {m['date']}; official deadline unconfirmed. Due date unset. Later phases planned only."})
        phase_numbers[m['phase']]=same['number']
    for item in PLAN:
        if item['id'] in matched:
            current=matched[item['id']]
            if 'talalahmad-ai' not in [a['login'] for a in current['assignees']]:
                gh(['api','--method','POST',f"repos/{REPO}/issues/{current['number']}/assignees",'--input','-'],{'assignees':['talalahmad-ai']})
            continue
        created=gh(['api','--method','POST',f'repos/{REPO}/issues','--input','-'],{'title':item['title'],'body':item['body'],'assignees':item['assignees'],'labels':item['labels'],'milestone':phase_numbers[item['phase']]})
        print('CREATED '+created['html_url'])
    print('Run the evidence/remote verification again; creation alone does not prove final assignment state.')

if __name__=='__main__':
    try:main()
    except (RuntimeError,subprocess.SubprocessError) as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr);sys.exit(1)
