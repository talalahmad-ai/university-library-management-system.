6. AI-assisted requirements review
ChatGPT reviewed the draft for unclear wording, missing cases, conflicting rules and
requirements that could not be tested. The table records the suggested changes and proposed
decisions; accepted changes are included in the final requirements.
Review / issue Finding Decision and reason Affected items
R-01
Ambiguity
“Members can borrow
books” does not define
eligibility or due dates.
Accept — define member-type
periods and limits, active status and
overdue checks; mark policy values
as proposed.
FR-06, FR-07;
A-01
R-02
Omission /
conflict
A returned book could
appear free even though
someone is waiting.
Accept — define FIFO holds,
expiry, cancellation and held-copy
status.
FR-08, FR-10;
A-02
R-03
Testability
“Search should be fast”
cannot be checked
consistently.
Accept — give a 2-second
threshold, workload and pass count.NFR-01
R-04
Omission
A second issue request
could create two loans
for one copy.
Accept — require exactly one
successful simultaneous issue and a
consistent copy state.
NFR-04;
AC-05c
R-05
Security
Sign-in alone does not
prevent members from
seeing another person’s
records.
Accept — enforce role and
ownership checks for each
protected operation.
NFR-02;
AC-09b
R-06
Scope conflict
Send automatic SMS/
email reminders and
collect overdue fines
online.
Reject — Assignment 1 excludes
live messaging and payment
processing; keep notices inside the
proposed LMS.
FR-12; C-01
R-07
Ambiguity
“Overdue” could be
applied on the due date
itself.
Accept — define it as an open loan
after the due date and test both
dates.
FR-11; AC-08a
Source: University Library Management System, Assignment 1, 12 November 2026, pp. 3–4
(scope and WBS), pp. 9–10 (policy and scope risks). Assignment 2 instructions supply the
required deliverables.
