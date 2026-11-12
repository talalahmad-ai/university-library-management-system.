# Assignment 1 quality review

**Scope:** Phase 1 / Assignment 1 only. **Revision:** 1.1, 12 November 2026.  
**Result:** **26/26 local checks passed.** Publishing, task tracking and genuine evidence are Verified. Human confirmations remain Pending.

## Artifact and planning verification

The [actual validator output](evidence/validation-output.txt) records `python scripts/validate_package.py`. Its 26 checks cover required files, the 16 unique WBS leaves, dependency existence and acyclicity, every finish-to-start edge, inclusive calendar durations, actual student assignments, role/person-hour totals, reserve arithmetic, one-person capacity, the independent 32-day longest path, RACI ownership, 12 scored risks, 16 task definitions, diagrams.net XML, workbook sheets/formulas/cached values, PDF bounds, image decoding, local document links, tracked folders and preservation of the original commit.

Base effort is **112 h** (Lead 30, Analyst 37.5, Designer 44.5; all roles belong to Talal). A1/A2/A3/A4 totals are 34/31/18/29 h. Unallocated 15% estimate reserve is 16.8 h; the envelope is 128.8 h. Combined daily demand is at most the assumed six hours, including concurrent UML/UI work. These are estimates, not time actually spent.

The revised **11-page PDF** was opened, rendered and visually reviewed, including the contents, portrait/landscape transitions, tables, WBS/Gantt and risk responses. Extracted text stays within page bounds. Full-resolution PNG and standalone vector chart PDFs are provided. The nine-sheet XLSX opens in formula and cached-value modes; calculated totals agree with independent arithmetic. No Excel application screenshot or formal standards certification is claimed.

Eight current screenshots were decoded and visually reviewed: five actual public GitHub page/README/Issue captures and three labelled local CSV renderings. All GitHub capture responses were HTTP 200. The [manifest](evidence/capture-manifest.json) records sources and times. [Attachment hashes](evidence/source-hashes.json) preserve input provenance. Historical captures remain separately labelled under baseline.

## Live GitHub verification

The repository is Talal's personal repository; Hamza-Khaalid is an authorized collaborator. Initial app-mediated writes returned 403. Inspection identified the actual connector app and the missing owner installation. After the user installed it under Talal, normal non-forced Git push and Issue creation succeeded. The [resolution record](evidence/access-resolution.json) and historical errors preserve the actual sequence.

The [live verification snapshot](evidence/remote-verification.json) verifies the original owner commit, all published preparation commits, all four required folders and every committed file hash. It also independently checks all **16** unique Issues for Talal's assignment, expected labels, phase milestone and acceptance criteria, plus all **four** milestones for honest official-deadline status. No committed file mismatch was found at the recorded snapshot. Milestone descriptions disclose proposed dates; official due dates remain unset.

All 16 Issues remain open for student review. A2–A4 Issues are future work records; their creation does not claim execution. The [Issue map](issue-map.md) links every WBS leaf to its actual Issue. The [helper dry run](evidence/issue-sync-dry-run.txt) recognizes all 16 existing Issues and proposes no duplicate creation. The helper was not rerun in write mode to manufacture activity.

The snapshot and screenshots necessarily precede the commit storing them. The final live check uses `python scripts/verify_remote.py --strict --no-write` to verify current publication without changing the captured record. Git history is preserved, authors and timestamps are genuine, and no alternate repository or ownership transfer was used.

## Remaining confirmations before baselining / Phase 2

1. Supply official A1–A4 submission dates and confirm Talal's availability; all current dates remain proposed.
2. Confirm instructor acceptance of the repository's literal final period, or have its owner rename the existing repository and update links/origin/evidence.
3. Talal reviews and understands the plan and the A1 task acceptance criteria. Planned A/R allocation and estimates do not claim completed student work.

The [compliance matrix](compliance-matrix.md) distinguishes Verified evidence from Pending confirmations. The technical access blocker is resolved. Assignments 2–4 have not been executed; no SRS, UML, Figma prototype or real usability feedback is presented as complete. Stop at this Phase 1 handover until the user supplies the next instruction.
