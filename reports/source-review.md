# Source review and scope decision

**Review date:** 12 November 2026 (Asia/Karachi). **Execution scope:** Phase 1 / Assignment 1 only.

## Authority and use of the attachments

The user's current request authorizes inspection, Assignment 1 preparation, verification and genuine evidence. The attached PDF defines the assignment requirements. The pasted master instruction is supporting context; its request to complete four assignments is not the active execution scope. Later-phase deliverables are represented only as planned work in the WBS and schedule.

| Source | Observed content | Treatment |
|---|---|---|
| Uploaded README.md | Repository heading and “ASSIGNMENT 01” | Preserve as an input; insufficient as the project README |
| Assignment PDF, page 1 | Case scenario; Assignment 1 steps 1–10; submission items and 10+15 marks | Official Assignment 1 checklist |
| Assignment PDF, pages 1–2 | Assignments 2–4; groups of 1–3 students | Future scope and planning constraints only |
| Starter ZIP | 31 files, draft charter/WBS/Gantt/RACI/risks, nine issue drafts; no Git metadata | Inspected as a supplied repository snapshot, not as remote history |
| Pasted text.txt | Expanded quality expectations and intended remote URL | Supporting detail within Phase 1; no fabricated identities, history or evidence |

## Inspection findings

1. No repository checkout existed in the initial workspace. The ZIP has no `.git` metadata, team identities or actual Issue/commit evidence.
2. Starter team names/handles are placeholders. The user subsequently confirmed Talal Ahmad (`talalahmad-ai`); no other student was named. Dates from 13 November to 14 December 2026 are explicitly provisional. There are no official deadlines or university/department details.
3. Starter tasks overlap without machine-readable dependency definitions. The revised plan uses explicit finish-to-start dependencies and checks every edge.
4. Starter estimates give task totals but no allocation to each person/role. The revised plan allocates each task's hours to Talal, with a functional-role breakdown. It checks row totals, column totals and the combined daily workload for one person.
5. Starter risks have mitigations but no distinct contingency actions. The revised register adds triggers, responses and ownership status.
6. Git 2.52.0 and an authenticated `Hamza-Khaalid` preparation account are available. The URL in the attachments omitted the literal final period; access to that URL failed. The user corrected the name to `university-library-management-system.`. API/CLI checks then verified the public repository and Write access, and cloning succeeded. Its sole original file was README.md and its sole commit was `d6eb07659dd092780801050675d9dbc30f8495ca`. There were zero Issues, no repository rulesets and an unprotected main branch. `talalahmad-ai` is eligible as an assignee. See [baseline inspection](evidence/baseline-inspection.json).
7. Live Issue creation and label creation returned `403: Resource not accessible by integration`. Both failed again after the user reported a permission update. Repository contents Write permission and owner assignee eligibility do not establish Issues write permission; the live task/evidence requirement remains blocked.

## Unresolved facts

| Fact | Current evidence | Required intervention |
|---|---|---|
| Student and role plan | Talal Ahmad / `talalahmad-ai`, confirmed by user | One-student allocation; confirm availability when baselining |
| Final repository owner | `talalahmad-ai`, verified remotely | Owner already controls the repository; no transfer is needed |
| University / department | Not supplied | Supply if needed for the cover page |
| Official submission dates | Not supplied | Confirm each official deadline; rebaseline the proposed schedule |
| Repository spelling | Verified existing name ends in a period | Owner/instructor to resolve the literal-name difference; do not silently rename |
| Library policies | Scenario supplies no limits or penalties | Confirm during later requirements work |

The original commit is preserved. No replacement remote, collaborator changes, account-setting changes or later-phase implementation has been performed. Original README text is retained in [baseline-readme.md](evidence/baseline-readme.md) and in Git history.
