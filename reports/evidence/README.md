# Assignment 1 evidence index

**Current result:** preserved development history and planning artifacts are published; 16 real task Issues are assigned to Talal with correct phase labels, milestones and acceptance criteria. The earlier access blocker is resolved.

All current screenshots are genuine Chromium captures. Five show actual public GitHub pages/elements; three are explicitly labelled local CSV renderings. Dates are proposed, not official. No student participation, interviews or human usability results are inferred.

| Requirement | Actual evidence | Status / interpretation |
|---|---|---|
| Repository homepage and required folders | [GitHub repository](github-repository.png), [remote tree/hash verification](remote-verification.json) | Verified; requirements, diagrams, ui-prototype and reports are tracked and published |
| Prepared README | [GitHub-rendered README](github-readme.png), [README source](../../README.md) | Verified |
| Meaningful remote commits | [GitHub history](github-commits.png), [remote commit list](remote-verification.json) | Verified; at least three genuine preparation commits and the original owner commit are preserved |
| One assigned Issue per major task | [Actual Issues list](github-issues.png), [live Issue map](../issue-map.md) | Verified; 16 unique WBS-linked Issues assigned to talalahmad-ai |
| Individual Issue showing assignment | [Actual A1 Issue #7](github-assigned-issue.png) | Verified; assignee, labels, milestone and acceptance criteria visible |
| Real milestones with honest dates | [Milestone records](tracking-configuration.json), [remote verification](remote-verification.json) | Verified; four real milestones, official due dates unset, proposed targets disclosed |
| Gantt and schedule | [Gantt PNG](../gantt-chart.png), [vector PDF](../gantt-chart.pdf), [schedule CSV](../project-schedule.csv), [workbook](../assignment-1-planning.xlsx) | Verified proposed plan |
| WBS | [PNG](../wbs-diagram.png), [vector PDF](../wbs-diagram.pdf), [editable diagrams.net source](../wbs.drawio), [dictionary](../wbs.csv) | Verified |
| Named responsibility matrix | [RACI rendering](local-raci.png), [CSV](../responsibility-matrix.csv) | Verified; Talal A/R on every work package |
| Task/person effort estimates | [Effort rendering](local-effort.png), [CSV](../effort-estimates.csv) | Verified; 112 base person-hours, one student |
| Likelihood/impact and mitigations | [Risk rendering](local-risks.png), [CSV](../risk-register.csv) | Verified; 12 risks with calculated scores and responses |
| Artifact and planning checks | [Actual validator output](validation-output.txt), [QA report](../quality-review.md) | Verified after final validation |
| Existing-task detection | [Read-only Issue helper output](issue-sync-dry-run.txt) | Verified; all 16 Issues recognized as existing, no duplicate creation proposed |
| Source provenance | [Attachment hashes](source-hashes.json), [source review](../source-review.md) | Verified; active user request distinguished from attached instructions |

The [capture manifest](capture-manifest.json) records sources, capture type and actual UTC times. All eight current images decode and were visually reviewed; GitHub responses were HTTP 200. Standalone WBS/Gantt exports and the 11-page report were also opened and reviewed.

## Historical baseline and access resolution

[Earlier genuine captures](baseline/README.md) preserve the blocked-session state before the owner app installation. [Initial repository inspection](baseline-inspection.json) and [original README](baseline-readme.md) record the pre-change repository. The [Issue failure](issue-access-failure.json) and [publishing failure](publish-access-failure.json) are historical observations; [access-resolution.json](access-resolution.json) records the effective installation and subsequent successful writes. These historical files are not the current submission screenshots.

The remote snapshot was taken before the evidence commit that stores it. It records an actual state, not a fabricated screenshot of its own future commit. Run `python scripts/verify_remote.py --strict --no-write` to check current live history, file hashes, all 16 assignments/labels/milestones/criteria and the four deadline records without changing the saved snapshot.

Remaining confirmations are listed in the [compliance matrix](../compliance-matrix.md): official deadlines, Talal's availability/plan review and the literal repository-name exception. Assignments 2–4 remain planned only.
