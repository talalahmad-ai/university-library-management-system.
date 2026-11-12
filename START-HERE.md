# Assignment 1 handover

**Student / owner:** Talal Ahmad (`talalahmad-ai`)  
**Actual repository:** <https://github.com/talalahmad-ai/university-library-management-system.>  
**Scope:** Phase 1 only. Do not treat the future A2–A4 plan as completed coursework.

## Read and review

1. Read [README](README.md) and the [planning report PDF](reports/assignment-1-plan.pdf).
2. Review the [editable workbook](reports/assignment-1-planning.xlsx), [charter](reports/project-charter.md), [WBS](reports/wbs.md), [schedule](reports/project-schedule.md), [RACI/effort](reports/responsibility-matrix.md) and [risk register](reports/risk-register.md).
3. Check the [compliance matrix](reports/compliance-matrix.md), [quality review](reports/quality-review.md) and [evidence index](reports/evidence/README.md). These distinguish verified artifacts from blocked live Issues and unconfirmed dates.

## Interventions before submission or Phase 2

- **Contents and Issues access:** Git push was denied with 403; the connector's Git data write API, Issue creation and CLI label creation also returned `403: Resource not accessible by integration`. Issue/label retries after the user reported a permission update still failed. Repository Write metadata alone did not resolve this. The owner should check that the connected GitHub app is installed/authorized for this exact repository and has effective Contents and Issues read/write permission. Accept any pending permission update and reconnect if needed. If the required permissions are not offered or the session remains restricted, use an authorized CLI account on your own computer. Do not send tokens in chat.
- **Official dates and availability:** Supply the official A1–A4 submission deadlines. Current targets are proposed, and six hours/day including weekends is a capacity assumption for Talal to confirm.
- **Literal repository name:** The existing name has a final period; the PDF requests `university-library-management-system` without it. Have the instructor accept that difference or have the owner rename the existing repository. Renaming preserves history but requires updating origin, links, the planning source, scripts and final screenshots. No rename or replacement repository has been performed.

## Publish the preserved Git history first

No prepared changes are currently published. The handover archive includes `phase-1-history.bundle`, containing the original commit and genuine sequential Codex preparation commits. Use it to preserve the actual history rather than uploading a flat snapshot as a single commit:

```bash
gh auth login --hostname github.com --git-protocol https --web
git clone phase-1-history.bundle university-library-management-system.
cd university-library-management-system.
git remote set-url origin https://github.com/talalahmad-ai/university-library-management-system..git
git fetch origin
git merge-base --is-ancestor origin/main HEAD
git push -u origin main
```

The double period before `git` is intentional: one period belongs to the repository name and the other starts `.git`. Run from the directory containing the extracted bundle. The ancestor check must succeed. If the owner or a teammate has added new work, reconcile on a branch before pushing; never force-push. If branch protection has changed, publish a review branch and follow the repository's review rules. A flat source snapshot is also included for inspection, but it is not a substitute for the bundled commits.

## Create the 16 assigned Issues without duplicates

All 16 [drafts](.github/issue-drafts/) name Talal and include proposed dates, dependencies, estimates, deliverables and acceptance criteria. Draft files are not live Issues.

On your own computer, install Git/GitHub CLI if missing, then authenticate an authorized account:

```bash
gh auth status
python3 scripts/sync_github_issues.py
python3 scripts/sync_github_issues.py --apply
```

The first script call is read-only. `--apply` creates missing phase labels, four milestones with **no official due dates**, and missing Issues assigned to `talalahmad-ai`. It matches existing WBS prefixes before creation and stops on duplicates. Re-running does not create another Issue for an already matched package. It does not alter existing Issue bodies, accounts, collaborators or the repository name. If labels/milestones/Issue creation fails with 403, use an account/connection with Issues write permission; do not keep retrying a restricted credential.

Verify actual remote state:

```bash
gh issue list --repo talalahmad-ai/university-library-management-system. --state all --limit 100 --json number,title,assignees,labels,milestone,url
git fetch origin
git log origin/main --oneline
python3 scripts/verify_remote.py --strict
```

There should be one matching Issue for each of the 16 WBS leaf IDs, assigned to `talalahmad-ai`. Review all labels and milestone links. Creating future-phase tracking Issues is part of A1 planning; it does not authorize executing A2–A4.

## Capture the remaining real evidence

Open the actual repository Issues list and at least one individual assigned Issue. Save readable screenshots under `reports/evidence/`, record URLs/time, update [issue map](reports/issue-map.md), evidence index and compliance matrix, and make a genuine follow-up commit. Never recreate a GitHub page locally as evidence.

The capture script can capture public GitHub pages and local artifact renderings after the files/Issues are ready:

```bash
python3 scripts/verify_remote.py
python3 scripts/capture_evidence.py
python3 scripts/validate_package.py
git status
```

## Regenerate planning artifacts

Python dependencies are listed in [scripts/requirements.txt](scripts/requirements.txt). Edit `reports/planning-data.json`, then run `bash scripts/rebuild.sh`. Reconcile workbook review edits into that JSON before rebuilding. Keep all official deadlines distinct from proposed dates. A generated chart or report is not evidence of student participation or actual time spent.

## Permanent ownership and history

The repository already belongs to `talalahmad-ai`; Talal has permanent owner control. No ownership transfer is required. `Hamza-Khaalid` is the preparation helper, not an additional student. Codex preparation commits preserve the initial owner commit and current timestamps. Do not change their authors to imply student work. Talal should review the artifacts and make genuine subsequent contributions under his own account as he develops the coursework.

The final `reports/evidence/remote-verification.json` records the verified published commit list and actual Issue count at capture time. The [QA report](reports/quality-review.md) explains the remaining gates.
