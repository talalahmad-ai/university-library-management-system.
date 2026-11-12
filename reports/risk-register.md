# Risk register

**Owner for every risk:** Talal Ahmad (@talalahmad-ai). Functional roles identify the monitoring perspective.

## Scoring and review

Likelihood: 1 rare, 2 unlikely, 3 possible, 4 likely, 5 almost certain. Impact: 1 negligible rework, 2 minor rework, 3 material task delay, 4 phase-gate threat, 5 inability to meet a mandatory submission element. Score = likelihood × impact; 1–5 Low, 6–14 Medium, 15–25 High. These are qualitative planning judgments, not measured probabilities. Review High risks at each work session and all risks at phase gates or when a trigger occurs. Talal owns mitigation and contingency decisions.

**High priority:** R03 (25, effective write access failure), R01 (16, ambiguous policies) and R05 (16, official deadlines unknown). The original URL problem was resolved by the corrected trailing-dot URL. R03 is now a realized issue: Git push, Git data writes and Issue creation return HTTP 403. The literal repository-name mismatch is a current open decision tracked by R12.

## R01 — Ambiguous lending and reservation policies

Likelihood **4** · Impact **4** · Score **16** · High · Monitoring role: Analyst

- Trigger: Conflicting or unanswered policy questions at SRS review.
- Mitigation: Maintain a policy-question log; prioritize librarian confirmation before baselining.
- Contingency: Record explicitly proposed rules, isolate affected requirements and re-review after clarification.

## R02 — Effort estimates exceed one student's availability

Likelihood **3** · Impact **4** · Score **12** · Medium · Monitoring role: Lead

- Trigger: Actual hours exceed estimate by 20% or a planned day exceeds six hours.
- Mitigation: Allocate all role hours to Talal; check aggregate daily demand; review estimates at each gate.
- Contingency: Use the 15% effort reserve, re-sequence discretionary polish and propose revised dates to the instructor.

## R03 — Repository URL or effective write access fails

Likelihood **5** · Impact **5** · Score **25** · High · Monitoring role: Lead

- Trigger: Push, Git data write or Issue creation returns an access error; currently triggered by HTTP 403.
- Mitigation: Use the verified trailing-dot URL; verify effective Contents and Issues write access rather than repository role alone; retain the local Git bundle.
- Contingency: Owner restores app access or publishes from an authorized CLI account; retain local commits and package without creating a replacement remote.

## R04 — Student unavailable during a critical work package

Likelihood **3** · Impact **4** · Score **12** · Medium · Monitoring role: Lead

- Trigger: Two planned work sessions missed or a milestone is forecast late.
- Mitigation: Keep tasks small and editable; confirm calendar availability; preserve handover notes.
- Contingency: Replan around remaining capacity; request a deadline adjustment if needed; do not invent another contributor.

## R05 — Official deadlines differ from proposed dates

Likelihood **4** · Impact **4** · Score **16** · High · Monitoring role: Lead

- Trigger: Instructor supplies dates earlier than current proposed gates.
- Mitigation: Keep every proposed date labeled; request actual submission dates before baselining.
- Contingency: Recalculate the dependency network and effort/capacity; obtain revised scope or timing agreement.

## R06 — Stakeholders or two classmates unavailable

Likelihood **3** · Impact **4** · Score **12** · Medium · Monitoring role: Analyst

- Trigger: No consultation or testing slot confirmed before the relevant phase.
- Mitigation: Request availability early and prepare focused questions and a short test script in the appropriate phase.
- Contingency: Reschedule with actual eligible participants; disclose missing evidence and seek instructor guidance.

## R07 — Git conflicts or accidental loss of existing work

Likelihood **2** · Impact **4** · Score **8** · Medium · Monitoring role: Lead

- Trigger: Remote head changes, conflict appears, or an export is overwritten.
- Mitigation: Inspect before editing; fetch before pushing; keep editable sources; use normal pushes and reviews.
- Contingency: Resolve on a branch, recover from Git and verify against the last reviewed baseline; never force-push.

## R08 — Figma access or prototype interactions delayed

Likelihood **3** · Impact **4** · Score **12** · Medium · Monitoring role: Designer

- Trigger: Figma creation, sharing or interaction checks fail at UI kickoff.
- Mitigation: Confirm account/tool access before design; retain source assets and a workflow checklist.
- Contingency: Prepare a local aid and precise Figma completion steps; mark the Figma requirement incomplete until the actual file works.

## R09 — SRS, UML and UI use inconsistent rules or terms

Likelihood **3** · Impact **4** · Score **12** · Medium · Monitoring role: Analyst

- Trigger: Review finds a workflow or term that cannot be traced to the baseline.
- Mitigation: Use a glossary, requirement IDs and cross-artifact review at M2–M4.
- Contingency: Pause dependent approvals, fix the source requirement and update all impacted diagrams/screens.

## R10 — Testing or screenshots are missing or unreadable

Likelihood **3** · Impact **4** · Score **12** · Medium · Monitoring role: Designer

- Trigger: Evidence index contains a missing file, illegible image or unsupported claim.
- Mitigation: Capture real pages/artifacts, record URLs/times, open exports and audit every evidence link.
- Contingency: Recapture actual state; mark unavailable evidence Pending or Blocked rather than recreating it.

## R11 — Scope expands into production implementation

Likelihood **3** · Impact **3** · Score **9** · Medium · Monitoring role: Lead

- Trigger: Tasks add backend, deployment, real data migration or live notifications.
- Mitigation: Keep the PDF's analysis/design boundary in the charter and review every scope change.
- Contingency: Defer implementation requests and restore effort to mandatory assessment artifacts.

## R12 — Repository trailing period conflicts with required literal name

Likelihood **3** · Impact **3** · Score **9** · Medium · Monitoring role: Lead

- Trigger: Instructor requires the exact repository spelling from the PDF.
- Mitigation: Disclose the name difference and ask the owner/instructor to confirm acceptability.
- Contingency: Owner renames the existing repository; update origin, document links, Issue map and screenshots; preserve history.

Editable [CSV](risk-register.csv) / [workbook](assignment-1-planning.xlsx). No risk is asserted to have been accepted by the instructor.
