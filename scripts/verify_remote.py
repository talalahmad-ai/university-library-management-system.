#!/usr/bin/env python3
"""Read actual GitHub state and record it. --strict fails if publishing/task tracking is incomplete."""
import argparse
import json
import subprocess
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];R=ROOT/'reports'
D=json.loads((R/'planning-data.json').read_text());REPO=D['repository']
def gh(path):
    p=subprocess.run(['gh','api',path],capture_output=True,text=True,check=True)
    return json.loads(p.stdout)
def collection(path):
    items=[];page=1
    while True:
        batch=gh(path+('&' if '?' in path else '?')+f'per_page=100&page={page}')
        items.extend(batch)
        if len(batch)<100:return items
        page+=1
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--strict',action='store_true');parser.add_argument('--no-write',action='store_true',help='Verify current state without replacing the saved snapshot');args=parser.parse_args()
try:
    repo=gh('repos/'+REPO);commits=collection('repos/'+REPO+'/commits');rawissues=collection('repos/'+REPO+'/issues?state=all')
    issues=[x for x in rawissues if 'pull_request' not in x];contents=gh('repos/'+REPO+'/contents/')
    milestones=collection('repos/'+REPO+'/milestones?state=all')
    issue_plan={x['id']:x for x in json.loads((ROOT/'.github/issue-plan.json').read_text())}
    milestone_checks=[]
    for m in D['milestones']:
        matches=[x for x in milestones if x['title']==m['phase']+' — '+m['name']]
        deadline=D['official_deadlines'][m['phase']]
        honest=len(matches)==1 and (matches[0]['due_on'] is None if deadline is None else bool(matches[0]['due_on']) and matches[0]['due_on'][:10]==deadline)
        milestone_checks.append({'phase':m['phase'],'count':len(matches),'official_deadline_honest':honest})
    local=git('rev-list','d6eb07659dd092780801050675d9dbc30f8495ca..HEAD').splitlines()
    remote_shas={c['sha'] for c in commits};published=[c for c in local if c in remote_shas]
    package_checks=[]
    for task in D['tasks']:
        found=[x for x in issues if x['title'].startswith('['+task['id']+'] ')]
        issue=found[0] if len(found)==1 else None
        package_checks.append({'wbs':task['id'],'issue_count':len(found),
                               'assigned_correctly':bool(issue) and [a['login'] for a in issue['assignees']]==['talalahmad-ai'],
                               'labels_correct':bool(issue) and set(issue_plan[task['id']]['labels'])<={a['name'] for a in issue['labels']},
                               'milestone_correct':bool(issue) and issue['milestone'] is not None and issue['milestone']['title'].startswith(task['phase']+' — '),
                               'acceptance_criteria_present':bool(issue) and task['acceptance'] in (issue['body'] or '')})
    folder_names={c['name'] for c in contents if c['type']=='dir'}
    tracked_ok={'requirements','diagrams','ui-prototype','reports'}<=folder_names
    remote_tree=gh('repos/'+REPO+'/git/trees/'+commits[0]['commit']['tree']['sha']+'?recursive=1')
    remote_blobs={x['path']:x['sha'] for x in remote_tree['tree'] if x['type']=='blob'}
    local_blobs={}
    for line in git('ls-tree','-r','HEAD').splitlines():
        meta,path=line.split('\t',1);local_blobs[path]=meta.split()[2]
    mismatches=[path for path,sha in local_blobs.items() if remote_blobs.get(path)!=sha]
    task_ok=all(all(x[k] for k in ['assigned_correctly','labels_correct','milestone_correct','acceptance_criteria_present']) for x in package_checks)
    original_ok='d6eb07659dd092780801050675d9dbc30f8495ca' in remote_shas
    ready=len(local)>=3 and len(published)==len(local) and tracked_ok and task_ok and all(x['official_deadline_honest'] for x in milestone_checks) and original_ok and not mismatches and not remote_tree.get('truncated',False)
    snapshot={'observed_at_utc':datetime.now(timezone.utc).isoformat(),'repository':REPO,
              'declared_permissions':repo.get('permissions'),'remote_head':commits[0]['sha'],'remote_commit_count':len(commits),
              'remote_commits':[{'sha':c['sha'],'message':c['commit']['message'],'author':c['commit']['author']['name'],'authored_at':c['commit']['author']['date'],'url':c['html_url']} for c in commits],
              'remote_root':[{'name':c['name'],'type':c['type'],'sha':c['sha'],'url':c['html_url']} for c in contents],
              'local_head_at_snapshot':git('rev-parse','HEAD'),'local_preparation_commits_at_snapshot':len(local),'new_preparation_commits_published':len(published),
              'issue_count':len(issues),'issues':[{'number':x['number'],'title':x['title'],'url':x['html_url'],'state':x['state'],'assignees':[a['login'] for a in x['assignees']],'labels':[a['name'] for a in x['labels']],'milestone':x['milestone']['title'] if x['milestone'] else None,'milestone_number':x['milestone']['number'] if x['milestone'] else None} for x in issues],
              'task_issue_checks':package_checks,'milestone_checks':milestone_checks,'original_history_preserved':original_ok,'committed_file_count_checked':len(local_blobs),'committed_file_mismatches':mismatches,'required_remote_folders_present':tracked_ok,'publishing_and_tracking_status':'Verified' if ready else 'Blocked',
              'note':'This is a real snapshot, not proof of later publication. Repository permission metadata does not prove effective write access. Official dates, name exception and student review remain separate gates. Snapshot necessarily precedes the commit that stores this record.'}
    if not args.no_write:(R/'evidence/remote-verification.json').write_text(json.dumps(snapshot,indent=2)+'\n')
    print(f"Remote: {len(commits)} commits; {len(published)} local preparation commits published; {len(issues)} Issues. Publishing/tracking: {snapshot['publishing_and_tracking_status']}.")
    print(f"Checked {len(local_blobs)} committed file hashes, original history, {len(package_checks)} task assignees/labels/milestones/criteria and {len(milestone_checks)} honest deadline records. File mismatches: {len(mismatches)}.")
    raise SystemExit(2 if args.strict and not ready else 0)
except subprocess.CalledProcessError as exc:
    print('Remote verification failed: '+(exc.stderr or str(exc)).strip());raise SystemExit(1)
