# Project charter and scope

**Project:** University Library Management System (LMS)  
**Version:** 1.0 · 12 November 2026 · Phase 1 planning baseline proposed for review  
**Student / repository owner:** Talal Ahmad (`talalahmad-ai`)  
**University / department:** Not supplied  
**Repository:** <https://github.com/talalahmad-ai/university-library-management-system.>

## 1. Background and problem

The instructor's scenario describes manual records or an outdated system for book borrowing, returns, student membership and overdue books. Such record keeping can make status checks slow and leave catalog, borrower and return information inconsistent. These are scenario-based analysis concerns; no site visit, interview or measured operational baseline has been supplied.

The proposed LMS will make catalog/copy information, membership, circulation and overdue status easier to understand and manage. The academic project produces a coherent analysis and design package, not a production system.

## 2. Objectives and measurable success criteria

| Objective | Acceptance measure / planned gate |
|---|---|
| Establish controlled planning and GitHub work | A1: README, four tracked folders, dated Gantt/schedule, WBS, named RACI, reconciled effort and scored risks; at least three meaningful new remote commits; one assigned Issue per major task; readable evidence |
| Specify the scenario accurately | A2 planned: at least four stakeholder types, 10 FR, four NFR, five assumptions/constraints, eight user stories and measurable criteria, five AI-review decisions and a structured SRS with traceability |
| Model consistent library workflows | A3 planned: editable use-case/class/borrowing sequence/return-overdue activity diagrams, exports and explanations matching the SRS |
| Demonstrate usable interactions | A4 planned: at least five connected prototype screens, two workflows, testing by two actual classmates and at least two changes based on their feedback |
| Keep evidence honest and reviewable | Every completion claim links to an actual artifact, live repository state or genuine screenshot; missing facts remain explicit |

Dates are proposed in the [schedule](project-schedule.md). Official submission deadlines remain unknown; none of the proposed dates is presented as an instructor commitment.

## 3. Scope boundaries

| Capability | Analysis/design work in scope | Boundary / clarification needed |
|---|---|---|
| Book catalog and copies | Catalog attributes, search and copy availability/status concepts | No real library import or production catalog |
| Membership | Student/faculty membership and librarian/administrator roles | Eligibility, authentication and privileges need confirmation |
| Borrowing | Member validation, available copy, loan record, due-date concept | Quotas and loan periods are unconfirmed |
| Returns | Identify active loan, record return and update copy status | Damaged/lost items and financial processing are not confirmed |
| Reservations | Search/detail/reserve workflow and availability/queue concepts | Queue precedence, expiry and pickup rules need confirmation |
| Overdue notifications | Identify overdue loans and show notification information in requirements/design | Delivery channel, frequency, grace period and penalties are unconfirmed |

The project also includes planning, requirements documentation, UML, a clickable UI prototype, quality reviews, GitHub management and submission evidence. Phase 1 executes only the planning/GitHub work. Later deliverables are planned in the WBS and schedule.

**Excluded:** complete backend/frontend implementation; live notification service; payment/fine collection; campus SSO integration; production hosting; migration of personal/student records; fabricated interviews or usability data. Optional ideas require an explicit scope decision before adding work.

## 4. Assumptions, constraints and dependencies

| ID | Type | Statement and consequence |
|---|---|---|
| A01 | Assumption | Talal is the only named student; he holds Lead, Analyst and Designer roles. The plan uses a one-person capacity check. |
| A02 | Assumption | Provisional window is 13 November–14 December 2026, including weekends. Replace it when official deadlines and availability are confirmed. |
| A03 | Assumption | Six hours per calendar day is an estimated coursework capacity, not a statement of Talal's actual availability. |
| A04 | Assumption | Library policy questions remain open until confirmed during requirements work. No unsupported quotas, fines or notification channels are approved. |
| C01 | Constraint | The assignment permits groups of 1–3; no additional members are invented or assigned. |
| C02 | Constraint | Full LMS implementation is unnecessary; effort is limited to the specified academic artifacts. |
| C03 | Constraint | Existing remote history and legitimate work must be preserved; no forced push or impersonated authorship. |
| C04 | Constraint | Use synthetic examples only; no credentials, private records or invented participation in evidence. |
| D01 | Dependency | Repository metadata reports Write permission and assignee eligibility passed. Effective Git push, Git data API writes and Issue creation return HTTP 403; Contents and Issues write access must be resolved. |
| D02 | Dependency | Official dates and the repository-name exception need owner/instructor resolution before submission approval. |
| D03 | Dependency | SRS review precedes dependent UML and UI work; UML review and screen designs precede prototype linking. |
| D04 | Dependency | Later prototype testing depends on actual classmates and a shareable clickable file; Phase 1 does not claim those exist. |

## 5. Governance and responsibilities

Talal Ahmad is the planned Responsible and Accountable student for every work package. Functional roles organize the type of effort, not additional people. The authenticated helper is `Hamza-Khaalid`; preparation commits are transparently attributed to Codex. This does not claim that Talal performed the preparation or approved every estimate. No library stakeholder, instructor or classmate has been represented as having participated.

Review the plan at each milestone. Record a requested change, its reason, affected WBS IDs, dependency/capacity impact and approval status. Regenerate the CSV, workbook, charts and PDF from the same planning source after approved changes. Keep official dates distinct from proposed targets.

## 6. Effort, risks and acceptance

The [effort table](responsibility-matrix.md) allocates 112 base person-hours to Talal across 16 leaf work packages. A 15% estimate reserve is 16.8 hours, for a planning envelope of 128.8 hours. The reserve is unallocated effort, not additional work already scheduled or a claim of calendar float. A delay still requires dependency/capacity review.

Review the [risk register](risk-register.md) at kickoff and at each phase gate. Effective GitHub write access failure is the highest-priority realized issue (25), followed by ambiguous policies and unknown official deadlines (16 each). The user's trailing-dot correction resolved the URL problem, but Git push, Git data writes and Issue creation remain blocked by HTTP 403.

Assignment 1 is ready for academic review when all official deliverables and genuine remote evidence pass the [compliance matrix](compliance-matrix.md), with any permitted exceptions disclosed. The owner must confirm deadlines/availability and resolve the literal repository-name difference. Preparation completion is distinct from student review or instructor acceptance.

## 7. Revision history

| Version | Date | Change | Attribution |
|---|---|---|---|
| 1.0 | 12 November 2026 | Phase 1 plan, named one-student allocation, corrected remote URL and verification approach | Codex-assisted preparation; Talal confirmed by user |
