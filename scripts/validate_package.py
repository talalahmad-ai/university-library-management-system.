#!/usr/bin/env python3
"""Validate Assignment 1 artifacts and planning math; report remote blockers separately."""
import csv
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date,timedelta
from pathlib import Path
from xml.etree import ElementTree

import fitz
import openpyxl
from PIL import Image

ROOT=Path(__file__).resolve().parents[1];R=ROOT/'reports'
D=json.loads((R/'planning-data.json').read_text());T=D['tasks'];ids={t['id'] for t in T}
checks=[]
def check(ok,message):
    checks.append((bool(ok),message))
    print(('PASS ' if ok else 'FAIL ')+message)
def rows(name):
    with (R/name).open(newline='') as f:return list(csv.DictReader(f))

needed=['README.md','START-HERE.md','requirements/README.md','diagrams/README.md','ui-prototype/README.md',
        'reports/project-charter.md','reports/wbs.md','reports/wbs.csv','reports/wbs.drawio','reports/wbs-diagram.png','reports/wbs-diagram.pdf',
        'reports/project-schedule.md','reports/project-schedule.csv','reports/gantt-chart.png','reports/gantt-chart.pdf',
        'reports/responsibility-matrix.md','reports/responsibility-matrix.csv','reports/effort-estimates.csv','reports/risk-register.md','reports/risk-register.csv',
        'reports/assignment-1-plan.pdf','reports/assignment-1-planning.xlsx','reports/compliance-matrix.md','reports/quality-review.md','reports/evidence/README.md',
        '.github/issue-plan.json','reports/issue-map.md']
check(all((ROOT/p).is_file() and (ROOT/p).stat().st_size>0 for p in needed),'Required editable documents and exports exist')
check(len(ids)==len(T)==16,'16 unique leaf work packages')
lookup={t['id']:t for t in T};visited=set();active=set()
def visit(i):
    if i in active:raise ValueError('Dependency cycle at '+i)
    if i in visited:return
    active.add(i)
    for p in lookup[i]['depends']:visit(p)
    active.remove(i);visited.add(i)
try:
    for i in ids:visit(i)
    graph_ok=True
except (ValueError,KeyError):graph_ok=False
check(graph_ok,'Dependency graph exists and is acyclic')
fs_ok=all(date.fromisoformat(lookup[p]['end'])<date.fromisoformat(t['start']) for t in T for p in t['depends'])
check(fs_ok,'Every finish-to-start dependency has valid date ordering')
schedule=rows('project-schedule.csv')
check({r['WBS ID'] for r in schedule}==ids and len(schedule)==16,'Schedule covers each WBS leaf once')
check(all(int(r['Calendar days'])==(date.fromisoformat(r['End'])-date.fromisoformat(r['Start'])).days+1 for r in schedule),'Inclusive calendar durations match actual dates')
check(all('Talal Ahmad' in r['Assigned student'] and 'talalahmad-ai' in r['Assigned student'] for r in schedule),'Every task has the confirmed actual student')
alloc=rows('effort-estimates.csv');base=[r for r in alloc if r['WBS ID'] in ids]
check(len(base)==16 and all(abs(sum(float(r[c]) for c in ['Lead role h','Analyst role h','Designer role h'])-float(r['Talal total person-hours']))<1e-8 for r in base),'Role-to-person effort reconciles for every task')
check(abs(sum(float(r['Talal total person-hours']) for r in base)-112)<1e-8,'Base person effort = 112 h; no role double counting')
check(abs(D['contingency_hours']-112*.15)<1e-8,'15% unallocated reserve = 16.8 h; envelope = 128.8 h')
load=defaultdict(float)
for t in T:
    start,end=map(date.fromisoformat,[t['start'],t['end']]);length=(end-start).days+1
    for j in range(length):load[start+timedelta(j)]+=sum(t['hours'])/length
check(max(load.values())<=D['capacity_hours_per_day']+1e-8 and abs(sum(load.values())-112)<1e-8,'Combined one-student workload <= 6 h/day and daily allocations sum to 112 h')
earliest={}
def ef(i):
    if i not in earliest:
        t=lookup[i];earliest[i]=max([ef(p) for p in t['depends']]+[0])+(date.fromisoformat(t['end'])-date.fromisoformat(t['start'])).days+1
    return earliest[i]
check(max(ef(i) for i in ids)==32,'Independent longest dependency path = 32 calendar days')
raci=rows('responsibility-matrix.csv')
check(len(raci)==16 and {r['WBS ID'] for r in raci}==ids and all(r['RACI']=='A/R' and 'Talal Ahmad' in r['Named student'] for r in raci),'Exactly one named accountable/responsible student per package')
risk=rows('risk-register.csv')
check(len(risk)>=8 and len({r['ID'] for r in risk})==len(risk) and all(int(r['Score'])==int(r['Likelihood (1–5)'])*int(r['Impact (1–5)']) and r['Mitigation'] and r['Contingency'] and r['Owner'] for r in risk),'12 risk scores, owners, mitigations and contingencies are complete')
plan=json.loads((ROOT/'.github/issue-plan.json').read_text())
check({r['id'] for r in plan}==ids and len(plan)==16 and all(r['assignees']==['talalahmad-ai'] and (ROOT/r['body_file']).is_file() for r in plan),'One real-ready assigned Issue definition per major work package (drafts only)')
tree=ElementTree.parse(R/'wbs.drawio');cell_ids={x.attrib.get('id') for x in tree.findall('.//mxCell')}
check(ids<=cell_ids and {'project','p1','p2','p3','p4'}<=cell_ids,'Editable diagrams.net WBS XML contains hierarchy and every leaf')
wb=openpyxl.load_workbook(R/'assignment-1-planning.xlsx',data_only=True)
fw=openpyxl.load_workbook(R/'assignment-1-planning.xlsx',data_only=False)
check(set(['Overview','Schedule','Milestones','WBS','RACI','Effort','Risks','Gantt','Capacity'])<=set(wb.sheetnames),'XLSX opens with nine planning sheets')
check(wb['Schedule']['M22'].value==112 and wb['Effort']['F22'].value==112 and abs(wb['Effort']['F24'].value-16.8)<1e-8 and abs(wb['Effort']['F25'].value-128.8)<1e-8,'Cached spreadsheet totals agree with independently calculated totals')
check(all(wb['Schedule'].cell(r,15).value=='OK' for r in range(6,22)) and all(wb['Capacity'].cell(r,4).value=='OK' for r in range(6,38)),'Spreadsheet dependency and capacity checks have correct cached results')
check(all(str(fw['Effort'].cell(r,6).value).startswith('=SUM(') for r in range(6,22)) and all(str(fw['Risks'].cell(r,5).value).startswith('=') for r in range(6,18)),'Effort totals and risk scores remain editable formulas')
pdfs=[];bounds_ok=True
for name in ['assignment-1-plan.pdf','gantt-chart.pdf','wbs-diagram.pdf']:
    doc=fitz.open(R/name);pdfs.append((name,len(doc)))
    for page in doc:
        for b in page.get_text('blocks'):
            if b[0]<-1 or b[1]<-1 or b[2]>page.rect.width+1 or b[3]>page.rect.height+1:bounds_ok=False
check(all(pages>0 for _,pages in pdfs) and bounds_ok,'All PDFs open; extracted text blocks remain inside page bounds')
image_ok=True
for f in list(R.glob('*.png'))+list((R/'evidence').glob('*.png')):
    try:
        with Image.open(f) as im:im.verify()
    except Exception:image_ok=False
check(image_ok,'All exported charts and captured screenshots decode successfully')
broken=[]
for f in ROOT.rglob('*.md'):
    if '.git' in f.parts:continue
    for m in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',f.read_text()):
        target=m.group(1).split('#')[0]
        if not target or '://' in target or target.startswith('mailto:'):continue
        if not (f.parent/target).resolve().exists():broken.append((str(f.relative_to(ROOT)),target))
check(not broken,'All local Markdown links and embedded images resolve')
if broken:print('Broken links:',broken)
tracked=subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines()
check(all(any(p.startswith(folder+'/') for p in tracked) for folder in ['requirements','diagrams','ui-prototype','reports']),'All four required folders contain Git-tracked files')
ancestor=subprocess.run(['git','merge-base','--is-ancestor','d6eb07659dd092780801050675d9dbc30f8495ca','HEAD'],cwd=ROOT).returncode==0
check(ancestor,'Original remote commit remains an ancestor; no rewritten history')
statuses=[]
if (R/'compliance-matrix.csv').exists():statuses=[r['Status'] for r in rows('compliance-matrix.csv')]
check(bool(statuses) and all(x in ['Verified','Pending','Blocked'] for x in statuses),'Compliance statuses use only Verified, Pending and Blocked')
failures=sum(not ok for ok,_ in checks)
print(f'\nLocal checks: {len(checks)-failures}/{len(checks)} passed.')
print('Submission gate: review Pending/Blocked rows in compliance-matrix.md. Local checks do not prove live Issues or official deadline confirmation.')
sys.exit(1 if failures else 0)
