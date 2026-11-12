#!/usr/bin/env python3
"""Generate editable Assignment 1 tables from planning-data.json. No network or Git mutations."""
import csv
import json
from datetime import date
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
DATA = json.loads((REPORTS / 'planning-data.json').read_text())
TASKS = DATA['tasks']
OWNER = f"{DATA['student']['name']} (@{DATA['student']['github']})"

def effort(t):
    return sum(t['hours'])

def duration(t):
    return (date.fromisoformat(t['end']) - date.fromisoformat(t['start'])).days + 1

def csvfile(name, headers, rows):
    with (REPORTS / name).open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(headers); w.writerows(rows)

def table(headers, rows):
    def clean(x):
        return str(x).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(map(clean, headers)) + ' |',
                     '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                    ['| ' + ' | '.join(map(clean, row)) + ' |' for row in rows])

def build_tables():
    rows = [[t['id'], t['phase'], t['name'], t['start'], t['end'], duration(t),
             ', '.join(t['depends']) or '—', OWNER, t['role'], effort(t),
             'Proposed; not official'] for t in TASKS]
    headers = ['WBS ID', 'Phase', 'Activity', 'Start', 'End', 'Calendar days',
               'FS predecessors', 'Assigned student', 'Functional lead role', 'Person-hours', 'Date status']
    csvfile('project-schedule.csv', headers, rows)
    schedule = '# Project schedule and Gantt\n\n'
    schedule += '**All dates are proposed, not official deadlines.** Prepared 12 November 2026. '
    schedule += 'This is a forward plan, not a record of work actually performed on those dates. '
    schedule += 'The Phase 1 preparation occurred earlier than its proposed coursework gate.\n\n'
    schedule += '![Proposed Gantt](gantt-chart.png)\n\n'
    schedule += table(headers[:7] + ['Hours'], [r[:7] + [r[9]] for r in rows])
    schedule += f'\n\nEvery task is assigned to **{OWNER}**. Functional roles are shown in the [CSV](project-schedule.csv), '
    schedule += '[RACI/effort table](responsibility-matrix.md) and [editable workbook](assignment-1-planning.xlsx).\n\n'
    schedule += '## Milestones and submission deadlines\n\n'
    schedule += table(['Gate', 'Phase', 'Proposed readiness / submission target', 'Depends on', 'Official deadline'],
                      [[m['id'], m['phase'], m['date'], ', '.join(m['depends']), 'Not supplied'] for m in DATA['milestones']])
    schedule += '\n\n## Scheduling rules and feasibility\n\n'
    schedule += '- Durations use inclusive calendar days, including weekends. A milestone is a zero-effort end-of-day gate.\n'
    schedule += '- Every dependency is finish-to-start: the successor starts strictly after the predecessor\'s end date. The dependency graph must be acyclic.\n'
    schedule += '- Concurrent tasks 3.1 and 4.1 use the same student. Daily load adds the effort/duration of all active packages across all roles; the maximum base load is six hours/day.\n'
    schedule += '- Working-day availability is unconfirmed. A six-hour daily capacity is an estimate; replan if Talal has less time or does not work weekends.\n'
    schedule += '- Total base effort is 112 hours. The unallocated 15% reserve is 16.8 hours; it is not hidden in task estimates and does not establish calendar float.\n'
    schedule += '- The calculated critical dependency chain is 1.1 → 1.3 → 1.4 → 1.5 → 1.6 → 1.7 → 2.1 → 2.2 → 2.3 → 3.1 → 3.2 → 4.2 → 4.3 → 4.4 (32 calendar days). Task 1.2 has four days of float; 4.1 has two.\n'
    schedule += '- All later phases are planned only. No student execution, stakeholder consultation or usability participation is claimed by this schedule.\n\n'
    schedule += 'Edit [planning-data.json](planning-data.json), regenerate with the two build scripts and rerun validation. The workbook can be edited for review; reconcile accepted edits back into the JSON before regenerating.\n'
    (REPORTS / 'project-schedule.md').write_text(schedule)

    wbs_rows = [[t['id'], t['name'], t['deliverable'], t['acceptance']] for t in TASKS]
    csvfile('wbs.csv', ['WBS ID', 'Work package', 'Deliverable', 'Acceptance evidence'], wbs_rows)
    wbs = '# Work Breakdown Structure\n\n'
    wbs += 'The project root is 0.0; Assignment 1–4 branches are 1.0–4.0. The 16 numbered leaf packages are the only effort-bearing items; summary branches and milestones are not double-counted.\n\n'
    wbs += '![WBS](wbs-diagram.png)\n\n'
    wbs += '| Branch | Planned outcome | Execution status |\n|---|---|---|\n'
    wbs += '| 1.0 Assignment 1 | Project initiation, repository, planning and GitHub evidence | Phase 1 execution |\n'
    wbs += '| 2.0 Assignment 2 | Stakeholder needs and requirements/SRS baseline | Future plan only |\n'
    wbs += '| 3.0 Assignment 3 | Four UML views and explanations | Future plan only |\n'
    wbs += '| 4.0 Assignment 4 | Clickable UI, real usability review and final submission | Future plan only |\n\n'
    wbs += table(['ID', 'Package', 'Deliverable', 'Acceptance evidence'], wbs_rows)
    wbs += '\n\nEditable sources: [CSV dictionary](wbs.csv), [diagrams.net file](wbs.drawio), '
    wbs += '[planning source](planning-data.json) and [workbook WBS sheet](assignment-1-planning.xlsx). '
    wbs += 'Visual exports: [PNG](wbs-diagram.png) / [PDF](wbs-diagram.pdf). '
    wbs += 'Every leaf ID has a schedule row, effort row, accountable student and Issue definition.\n'
    (REPORTS / 'wbs.md').write_text(wbs)

    raci_rows = [[t['id'], t['name'], OWNER, 'A/R', t['role']] for t in TASKS]
    csvfile('responsibility-matrix.csv', ['WBS ID', 'Work package', 'Named student', 'RACI', 'Functional lead role'], raci_rows)
    effort_rows = [[t['id'], t['name'], *t['hours'], effort(t), OWNER] for t in TASKS]
    totals = [sum(t['hours'][i] for t in TASKS) for i in range(3)]
    csvfile('effort-estimates.csv', ['WBS ID', 'Task', 'Lead role h', 'Analyst role h', 'Designer role h', 'Talal total person-hours', 'Student'],
            effort_rows + [['TOTAL', 'Base estimate', *totals, sum(totals), OWNER], ['RESERVE', 'Unallocated 15%', '', '', '', DATA['contingency_hours'], OWNER], ['ENVELOPE', 'Base + reserve', '', '', '', sum(totals) + DATA['contingency_hours'], OWNER]])
    raci = '# Responsibility assignment and effort\n\n'
    raci += f'**Confirmed student:** {OWNER}. One student holds Lead, Analyst and Designer roles. '
    raci += 'These are functional roles, not three people. The user supplied the identity; these allocations are the proposed work plan, not a claim of completed student effort.\n\n'
    raci += '**R** performs the work; **A** owns its acceptance; **C** provides two-way consultation; **I** receives updates. '
    raci += 'For a one-student team, A/R on every package is appropriate. Each row contains exactly one accountable person. '
    raci += 'No additional confirmed team member exists to list as C or I. Librarian/instructor/peer consultations may be sought later; their participation is not invented. '
    raci += '`Hamza-Khaalid` is the preparation helper and is not assigned assessed student work.\n\n'
    raci += table(['ID', 'Work package', 'Student', 'RACI', 'Lead role'], raci_rows)
    raci += '\n\n## Task and person-hour allocation\n\n'
    raci += table(['ID', 'Lead h', 'Analyst h', 'Designer h', 'Talal total h'],
                  [[t['id'], *t['hours'], effort(t)] for t in TASKS] + [['TOTAL', *totals, sum(totals)]])
    raci += '\n\nAll 112 base person-hours are assigned to Talal; role hours sum to the same 112 hours, not three times that figure. '
    raci += 'A1 uses 34 h; A2 31 h; A3 18 h; A4 29 h. A 15% unallocated estimate reserve adds 16.8 h, giving a 128.8 h planning envelope. '
    raci += 'Hours include drafting, self-review, export checks and basic revision; they exclude production software. '
    raci += 'Reserve usage requires replanning; it is not actual time spent.\n\n'
    raci += 'Estimate basis: small academic analysis/design packages, one named student and reusable tools. '
    raci += 'Average task effort is distributed across inclusive calendar duration for capacity checks; this is a planning approximation. '
    raci += 'Confirm availability and compare actuals with estimates at each gate; reassess a >20% variance. '
    raci += 'The [CSV](effort-estimates.csv) and workbook contain editable task/person allocations and calculated totals.\n'
    (REPORTS / 'responsibility-matrix.md').write_text(raci)

    risk_rows = [[r['id'],r['risk'],r['likelihood'],r['impact'],r['likelihood']*r['impact'],
                  'High' if r['likelihood']*r['impact']>=15 else 'Medium' if r['likelihood']*r['impact']>=6 else 'Low',
                  OWNER,r['role'],r['trigger'],r['mitigation'],r['contingency']] for r in DATA['risks']]
    risk_headers = ['ID','Risk','Likelihood (1–5)','Impact (1–5)','Score','Priority','Owner','Monitoring role','Trigger','Mitigation','Contingency']
    csvfile('risk-register.csv',risk_headers,risk_rows)
    risk = '# Risk register\n\n**Owner for every risk:** ' + OWNER + '. Functional roles identify the monitoring perspective.\n\n'
    risk += '## Scoring and review\n\nLikelihood: 1 rare, 2 unlikely, 3 possible, 4 likely, 5 almost certain. '
    risk += 'Impact: 1 negligible rework, 2 minor rework, 3 material task delay, 4 phase-gate threat, 5 inability to meet a mandatory submission element. '
    risk += 'Score = likelihood × impact; 1–5 Low, 6–14 Medium, 15–25 High. These are qualitative planning judgments, not measured probabilities. '
    risk += 'Review High risks at each work session and all risks at phase gates or when a trigger occurs. Talal owns mitigation and contingency decisions.\n\n'
    risk += '**High priority:** R01 (16, ambiguous policies) and R05 (16, official deadlines unknown). '
    risk += 'The original URL access problem was resolved by the corrected trailing-dot URL; R03 monitors recurrence. '
    risk += 'The literal repository-name mismatch is a current open decision tracked by R12.\n\n'
    for r in DATA['risks']:
        score=r['likelihood']*r['impact']
        risk += f"## {r['id']} — {r['risk']}\n\n"
        risk += f"Likelihood **{r['likelihood']}** · Impact **{r['impact']}** · Score **{score}** · " + ('High' if score>=15 else 'Medium' if score>=6 else 'Low') + f" · Monitoring role: {r['role']}\n\n"
        risk += f"- Trigger: {r['trigger']}.\n- Mitigation: {r['mitigation']}\n- Contingency: {r['contingency']}\n\n"
    risk += 'Editable [CSV](risk-register.csv) / [workbook](assignment-1-planning.xlsx). No risk is asserted to have been accepted by the instructor.\n'
    (REPORTS / 'risk-register.md').write_text(risk)

def build_drawio():
    mx = Element('mxfile', host='app.diagrams.net', version='24.7.17')
    diagram = SubElement(mx,'diagram',id='wbs',name='Assignment 1 WBS')
    model=SubElement(diagram,'mxGraphModel',dx='1600',dy='1400',grid='1',gridSize='10',page='1',pageWidth='1600',pageHeight='1400')
    root=SubElement(model,'root'); SubElement(root,'mxCell',id='0'); SubElement(root,'mxCell',id='1',parent='0')
    def box(i,label,x,y,w,h,color='#E8EFF7'):
        cell=SubElement(root,'mxCell',id=i,value=label,style=f'rounded=1;whiteSpace=wrap;html=0;fillColor={color};strokeColor=#24435F;fontSize=16;',vertex='1',parent='1')
        SubElement(cell,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
    def edge(a,b):
        c=SubElement(root,'mxCell',id=f'e-{a}-{b}',style='edgeStyle=orthogonalEdgeStyle;endArrow=none;strokeColor=#728197;',edge='1',parent='1',source=a,target=b)
        SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
    box('project','0.0 University Library Management System\nCoursework planning / design',500,20,580,80,'#C9E2F2')
    names=['1.0 Assignment 1\nPlanning and GitHub','2.0 Assignment 2\nRequirements and SRS','3.0 Assignment 3\nUML models','4.0 Assignment 4\nPrototype and review']
    for phase in range(1,5):
        x=20+(phase-1)*395; pid=f'p{phase}'
        box(pid,names[phase-1],x,160,360,70); edge('project',pid)
        group=[t for t in TASKS if t['phase']==f'A{phase}']
        for j,t in enumerate(group):
            box(t['id'],t['id']+' '+t['name'],x+20,280+j*130,330,100)
            edge(pid,t['id'])
    ElementTree(mx).write(REPORTS/'wbs.drawio',encoding='utf-8',xml_declaration=True)

if __name__=='__main__':
    build_tables(); build_drawio()
    print(f'Generated tables, WBS source, RACI, schedule and {len(DATA["risks"])} risks for {len(TASKS)} work packages; base effort {sum(map(effort,TASKS)):g} h.')
