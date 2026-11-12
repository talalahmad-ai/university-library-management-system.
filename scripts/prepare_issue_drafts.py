#!/usr/bin/env python3
"""Prepare task Issue definitions locally. Does not contact GitHub or create Issues."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'reports/planning-data.json').read_text())
folder=ROOT/'.github/issue-drafts';folder.mkdir(parents=True,exist_ok=True)
plan=[]
for t in data['tasks']:
    title=f"[{t['id']}] {t['name']}"
    phase='Assignment 1 preparation' if t['phase']=='A1' else 'Future phase — planning only; not executed in Phase 1'
    body=f"""## Work package {t['id']} · {t['phase']}

**Scope:** {phase}
**Assigned student:** Talal Ahmad (@talalahmad-ai), identity confirmed by the user.
**Functional lead role:** {t['role']}; all three roles belong to the same student.
**Proposed dates:** {t['start']} to {t['end']} (calendar days; official deadline unconfirmed).
**Estimated effort:** {sum(t['hours']):g} person-hours, assigned to Talal. This is an estimate, not actual time spent.
**Finish-to-start predecessors:** {', '.join(t['depends']) or 'None'}.

## Deliverable

{t['deliverable']}.

## Acceptance criteria

- [ ] {t['acceptance']}
- [ ] Related files, links and exports are reviewed and open correctly.
- [ ] Any remaining assumptions or blockers are recorded; no student contribution or human evidence is fabricated.

## Review context

The Assignment 1 planning package was prepared with Codex assistance through the authorized helper account. Issue assignment denotes planned student responsibility, not participation already performed. A1 artifacts should be reviewed by Talal; later-phase deliverables await separate authorization. See the repository's `reports/wbs.md`, `reports/project-schedule.md` and `reports/compliance-matrix.md`. Keep official deadlines distinct from proposed targets.
"""
    path=folder/f"{t['id'].replace('.','-')}.md";path.write_text('# '+title+'\n\n'+body)
    plan.append({'id':t['id'],'title':title,'body':body,'body_file':str(path.relative_to(ROOT)),
                 'assignees':['talalahmad-ai'],'labels':['documentation',f"assignment-{t['phase'][1]}"]+(['future-phase'] if t['phase']!='A1' else ['planning']),
                 'phase':t['phase']})
(ROOT/'.github/issue-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
print(f'Prepared {len(plan)} Issue drafts; no remote changes.')
