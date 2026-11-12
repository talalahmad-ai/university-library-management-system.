# Assignment 1 handover

**Student / owner:** Talal Ahmad (`talalahmad-ai`)  
**Authorized collaborator / helper:** `Hamza-Khaalid`  
**Repository:** <https://github.com/talalahmad-ai/university-library-management-system.>  
**Scope:** Phase 1 / Assignment 1 only. Assignments 2–4 are planned work.

## What is available

- [README](README.md), [project charter](reports/project-charter.md) and [planning report](reports/assignment-1-plan.pdf).
- [Editable nine-sheet workbook](reports/assignment-1-planning.xlsx), [schedule](reports/project-schedule.md), [WBS](reports/wbs.md), [RACI/effort](reports/responsibility-matrix.md) and [12-risk register](reports/risk-register.md).
- [16 actual assigned Issues](reports/issue-map.md), each with phase labels, acceptance criteria and a milestone. All are assigned to Talal and remain open for his review.
- Genuine incremental commits, with the original owner commit `d6eb076` preserved and preparation commits attributed to Codex.
- [Evidence index](reports/evidence/README.md), [compliance matrix](reports/compliance-matrix.md) and [quality review](reports/quality-review.md).

The app access issue was resolved after installation of `chatgpt-codex-connector` under Talal's personal account. Normal Git push and real Issue creation succeeded. Earlier 403 logs and baseline captures are retained as historical evidence; they do not describe the final state.

## Your remaining confirmations

1. **Official dates and availability:** Supply official A1–A4 deadlines and confirm Talal's available hours. Current targets are proposed; the six-hour daily capacity includes weekends. Milestones have proposed dates in their descriptions and no official due dates.
2. **Literal repository name:** The existing name ends in a period, while the PDF requests the name without one. Confirm instructor acceptance or have the owner rename the existing repository. If renamed, update origin, planning-data.json, links and final evidence. No rename was performed.
3. **Student review:** Talal should understand and review the plan, estimates and A1 Issues. Assignments and estimated hours do not claim he performed this preparation. Close Issues when the actual acceptance criteria and student review are satisfied.

## Clone and inspect the published work

```bash
git clone https://github.com/talalahmad-ai/university-library-management-system..git
cd university-library-management-system.
git log --oneline
gh issue list --repo talalahmad-ai/university-library-management-system. --state all --limit 100 --json number,title,assignees,labels,milestone,url
```

The double period before `git` is intentional: the first belongs to the repository name and the second starts `.git`. Use your own authorized GitHub account for changes. Fetch before publishing, follow any review/protection rules and preserve existing work with normal non-forced pushes.

## Verify and maintain the plan

```bash
python3 scripts/validate_package.py
python3 scripts/verify_remote.py --strict --no-write
python3 scripts/sync_github_issues.py
git status
```

The Issue helper is read-only by default and should report all 16 packages as `EXISTS`. Its `--apply` option creates missing task Issues/phase metadata and stops on duplicate WBS prefixes; no rerun is needed for the current complete set. Official deadlines remain a separate confirmation gate.

To revise the plan, edit `reports/planning-data.json`, run `bash scripts/rebuild.sh`, review the diff and recheck dependencies, totals and availability. Reconcile accepted workbook edits into JSON before regeneration. Dependencies are listed in [scripts/requirements.txt](scripts/requirements.txt).

To refresh genuine evidence after changes:

```bash
python3 scripts/verify_remote.py --strict
python3 scripts/capture_evidence.py
python3 scripts/validate_package.py
```

Capture sources and times are recorded in the manifest. The remote snapshot necessarily precedes the commit storing it; the `--no-write` check validates current live state without replacing that record.

## Ownership and backup

Talal already has permanent owner control; no ownership transfer is needed. `Hamza-Khaalid` is a collaborator/helper, not an additional student. Keep Codex preparation authors and original timestamps intact. Talal can make genuine subsequent contributions through his own account.

The handover archive includes a complete `phase-1-history.bundle` backup and a source snapshot. Restore the bundled main branch with:

```bash
git clone --branch main phase-1-history.bundle restored-lms
```

GitHub is the current publication source. Refer to the evidence snapshot for captured commits and actual Issue assignments. Phase 2 has not started; report and resolve the remaining confirmations before requesting later-phase execution.
