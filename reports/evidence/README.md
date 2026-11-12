# Assignment 1 evidence index

All screenshots are genuine captures. GitHub screenshots show the actual public remote, which still has only its initial README/commit because writes are blocked. Local CSV renderings and generated charts document the prepared plan; they are explicitly distinguished from GitHub evidence. No new remote commit or assigned Issue is claimed.

| Requirement / observation | Evidence | Status / interpretation |
|---|---|---|
| Existing repository inspected before changes | [Baseline record](baseline-inspection.json), [original README](baseline-readme.md) | Verified |
| Actual repository homepage | [GitHub homepage](github-repository.png) | Verified capture of baseline; prepared folders/files are not published |
| Actual remote README | [GitHub README](github-readme.png) | Verified capture of the original short README, not the prepared README |
| Actual remote commit history | [GitHub commits](github-commits.png), [remote verification](remote-verification.json) | One original remote commit; three-new-commit remote requirement Blocked |
| Actual Issues list | [GitHub Issues](github-issues.png), [Issue map](../issue-map.md) | Zero live Issues; assigned task Issues and individual-Issue screenshots Blocked |
| Integration Issue/label writes | [Failure record](issue-access-failure.json) | HTTP 403, including retry after reported permission change |
| Publishing and Git data API writes | [Failure record](publish-access-failure.json) | HTTP 403; zero new commits published |
| Dated Gantt and gates | [Gantt PNG](../gantt-chart.png), [vector PDF](../gantt-chart.pdf), [schedule](../project-schedule.csv) | Verified local proposed plan |
| WBS hierarchy | [WBS PNG](../wbs-diagram.png), [vector PDF](../wbs-diagram.pdf), [editable diagrams.net](../wbs.drawio) | Verified local artifact |
| Actual named responsibility matrix | [RACI browser rendering](local-raci.png), [CSV](../responsibility-matrix.csv) | Verified local artifact; Talal A/R on every package |
| Task/person effort | [Effort browser rendering](local-effort.png), [CSV](../effort-estimates.csv) | Verified local artifact; base 112 h |
| Risk assessment | [Risk browser rendering](local-risks.png), [CSV](../risk-register.csv) | Verified local artifact; 12 scored risks |
| File format and planning validation | [QA report](../quality-review.md), [validation output](validation-output.txt) | Verified local checks; does not certify external completion |

The [capture manifest](capture-manifest.json) records source URLs/files, UTC capture times and capture type. Screenshots use actual Chromium renderings; no browser interface or GitHub activity was drawn. All screenshot files were opened/decoded and visually reviewed. Dates in planning documents are proposed, not official deadlines. The [compliance matrix](../compliance-matrix.md) records the remaining gates.

After effective write access is available: publish the bundled commits, create the 16 assigned task Issues, verify the real remote tree/history/assignees, capture the final GitHub pages and at least one individual assigned Issue, update this index and make a genuine follow-up commit.
