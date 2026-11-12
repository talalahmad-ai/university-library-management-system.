# Assignment 1 quality review

**Scope:** Phase 1 / Assignment 1 only. **Prepared:** 12 November 2026.  
**Result:** Local artifacts pass 26 checks; GitHub publishing and assigned Issues remain Blocked. Assignment 1 is not fully complete for submission.

## Local verification

The [validator output](evidence/validation-output.txt) records the actual run of `python scripts/validate_package.py`. The checks cover the required files, all 16 unique WBS leaves, an acyclic dependency network, every finish-to-start edge, inclusive calendar durations, the confirmed student on every task, task/role/person totals, the 15% reserve, one-person daily capacity, the independent 32-day longest path, RACI ownership, 12 scored risks, 16 distinct task Issue definitions, diagrams.net XML hierarchy, workbook sheets/formulas/cached results, PDF bounds, image decoding, local document links, tracked folders and preservation of the original commit.

Base effort is **112 h** (Lead 30, Analyst 37.5, Designer 44.5, all belonging to Talal). A1/A2/A3/A4 totals are 34/31/18/29 h. The unallocated 15% reserve is 16.8 h, giving a 128.8 h estimate envelope. No role is counted as another person. Combined planned daily demand does not exceed the assumed six-hour limit, including concurrent UML/UI work.

The 11-page planning PDF was opened, rendered and visually reviewed, including portrait/landscape transitions, the contents page, tables, charts and risk responses. All extracted text stays inside page bounds. Standalone vector chart PDFs and full-resolution PNGs are supplied for readable viewing. The nine-sheet XLSX was opened programmatically in both formula and cached-value modes; totals agree with independent calculations. This does not claim an Excel application screenshot or formal standards certification.

Seven genuine screenshots were decoded and visually reviewed: four actual public GitHub page/README captures and three local CSV renderings. The WBS and Gantt are genuine generated planning exports. The [capture manifest](evidence/capture-manifest.json) records their sources and times. Source attachment hashes are in [source-hashes.json](evidence/source-hashes.json).

The task-creation helper was exercised in its read-only dry-run mode and found zero existing matching Issues. It prepared 16 would-create definitions without mutating the repository. Live creation could not be tested successfully because the GitHub integration denied it; no successful assignments are claimed.

## Actual remote verification and limitations

The exact trailing-dot repository was inspected before changes. It contains one original README and commit `d6eb076`; its history remains an ancestor of all local work. Although metadata reports Write permission and Talal is an eligible assignee, Issue creation/label writes returned HTTP 403 through the connector and CLI, including retries after the user reported a permission update. A normal Git push and the connector Git-data write API also returned 403.

The [actual remote snapshot](evidence/remote-verification.json) and real screenshots show **one original remote commit, zero new preparation commits published and zero live Issues**. Current screenshots therefore do not satisfy the submitted-folder, new remote history or assigned-Issue evidence requirements. See [publish failure](evidence/publish-access-failure.json) and [Issue failure](evidence/issue-access-failure.json). No alternate repository, forced push, fabricated screenshot or impersonated student commit was used.

## Remaining interventions

1. Restore effective **Contents and Issues write access** for the connected GitHub app on the exact repository, or use an authorized CLI account to publish the included Git bundle and run the Issue-creation helper. Re-verify and capture the final real remote tree, commits and assigned Issues.
2. Supply official submission dates and confirm Talal's availability; every current date is proposed and every official deadline remains null.
3. Resolve the existing repository's literal final period against the PDF's requested name without silently renaming it.
4. Talal reviews and understands the prepared plan. Role allocation and estimates are not evidence that he performed the preparation.

The [compliance matrix](compliance-matrix.md) uses only Verified, Pending and Blocked. Assignments 2–4 are scheduled but not executed; no SRS, UML, Figma prototype or human usability results are presented as completed. Stop at this Phase 1 handover until the user supplies the next instruction.
