# Assignment 1 requirements-to-deliverables compliance

Source: instructor PDF, Assignment 1 (page 1), steps 1–10 and both submission groups (10 + 15 marks). Only Phase 1 was executed. **Verified** means the stated evidence was checked; **Pending** needs confirmation or final verification; **Blocked** identifies an unavailable dependency. Historical access errors are resolved.

| ID | Requirement | Evidence file | Verification method | Status | Remaining action |
| --- | --- | --- | --- | --- | --- |
| A1-01 | GitHub account exists | evidence/baseline-inspection.json | Authenticated helper and existing owner verified | Verified | None |
| A1-02 | Existing repository is accessible and retained | evidence/baseline-inspection.json | Authenticated API/CLI; real clone; original ancestor | Verified | None |
| A1-02a | Repository has literal name required by PDF | ../README.md | Compare PDF name to existing trailing-dot name | Pending | Owner/instructor to accept spelling or rename existing repository |
| A1-03a | README describes project, objectives and actual student | ../README.md | Content review; Talal confirmed by user | Verified | Student review of the prepared text |
| A1-03b | Scope, assumptions and constraints defined | project-charter.md | Scenario capability and boundary review | Verified | Confirm policy questions in Phase 2 |
| A1-04a | Dated Gantt and schedule with activities and gates | project-schedule.csv; gantt-chart.pdf; assignment-1-planning.xlsx | Dependency, duration, capacity and export checks | Verified | None for proposed plan |
| A1-04b | Official submission deadlines confirmed | planning-data.json | All four official_deadlines are null and labeled | Pending | Supply official A1–A4 deadlines and confirm availability |
| A1-05a | Named responsibility assignment matrix | responsibility-matrix.csv | Talal is the sole A/R on all 16 rows | Verified | Talal to review proposed responsibilities |
| A1-05b | Effort estimated per task and person | effort-estimates.csv; assignment-1-planning.xlsx | Independent row/column and total checks; base 112 h | Verified | Re-estimate when actual availability is known |
| A1-06 | Risks assessed with mitigations | risk-register.csv; risk-register.md | 12 risks; valid L×I; named owner; mitigation/contingency | Verified | Monitor high risks and open decisions |
| A1-07a | Required folders tracked locally | ../requirements/README.md; ../diagrams/README.md; ../ui-prototype/README.md; README.md | Git ls-files for all four top-level folders | Verified | None |
| A1-07b | Required folders visible remotely | evidence/remote-verification.json; issue-map.md; evidence/access-resolution.json | Successful normal Git push; live remote tree/history and all 16 assignees, phase labels, milestones and acceptance criteria checked | Verified | None |
| A1-08 | Git installed and actual remote cloned | evidence/baseline-inspection.json | Git 2.52.0 and clone/remote inspection | Verified | None |
| A1-09a | At least three genuine meaningful new commits | ../README.md | Local Git log; current timestamps; Codex authorship; original preserved | Verified | None locally |
| A1-09b | Commit history verified on remote | evidence/remote-verification.json; issue-map.md; evidence/access-resolution.json | Successful normal Git push; live remote tree/history and all 16 assignees, phase labels, milestones and acceptance criteria checked | Verified | None |
| A1-10a | Issue definition for every major work package | ../.github/issue-plan.json; issue-map.md | 16 unique WBS-linked drafts; actual assignee specified | Verified | Drafts alone do not meet live Issue requirement |
| A1-10b | Actual GitHub Issue per major task assigned to student | evidence/remote-verification.json; issue-map.md; evidence/access-resolution.json | Successful normal Git push; live remote tree/history and all 16 assignees, phase labels, milestones and acceptance criteria checked | Verified | None |
| SUB-01 | Exact existing repository URL supplied | ../README.md | Authenticated API and actual public GitHub page | Verified | Resolve literal-name exception |
| SUB-01b | Prepared README and planning files published | evidence/remote-verification.json | Original prepared files are published; revised status/report is being published | Pending | Verify updated committed file hashes after publication |
| SUB-02 | Genuine screenshots of assigned GitHub Issues | evidence/README.md; issue-map.md | Actual assigned Issues exist; refreshed screenshot capture follows publication | Pending | Capture real Issues list and individual assigned Issue |
| SUB-03 | Editable and exported WBS | wbs.drawio; wbs.csv; wbs-diagram.pdf; wbs-diagram.png | XML hierarchy parse, source-ID checks and visual export review | Verified | None |
| QA-01 | PDF/XLSX/images/links verified | quality-review.md | Prior 26/26 checks passed; updated exports and final screenshots require refresh | Pending | Record final local checks and visual review |
| QA-02 | Later-phase execution excluded | ../requirements/README.md; ../diagrams/README.md; ../ui-prototype/README.md | Folders contain boundary READMEs, not later-phase deliverables | Verified | Await user instruction after reporting Phase 1 blockers |
| PLAN-01 | Student confirms availability and reviews proposed plan | project-charter.md; responsibility-matrix.md; ../START-HERE.md | Confirmed identity and role assignment; six-hour daily availability and plan acceptance are unconfirmed | Pending | Talal reviews estimates, responsibilities and capacity before baselining |
