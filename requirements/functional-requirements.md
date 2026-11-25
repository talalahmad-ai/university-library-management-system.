2. Functional requirements
These requirements describe the intended system. Must means essential; Should
means important but may be deferred if coursework time is limited.
ID Requirement Priority
FR-01
Sign in
The system shall authenticate users with their registered ID and
password, reject invalid or inactive accounts, and open the
dashboard for the assigned role.
Must
FR-02
Search catalog
The system shall allow signed-in users to search by title, author
or ISBN and display matching book records or a no-results
message.
Must
FR-03
View book details
The system shall show title, author, ISBN, total active copies and
the number of copies available for immediate borrowing.
Must
FR-04
Manage catalog
The system shall allow librarians to add or edit book and copy
records and retire copies only if they are not on loan or held.
Each copy shall have a unique copy ID.
Must
FR-05
Manage membership
The system shall allow librarians to register student or faculty
members with a unique university ID, view their records and
activate or deactivate membership.
Must
FR-06
Issue a book
The system shall allow a librarian to issue an available copy, or a
copy held for that member, to an active member below the loan
limit who has no overdue loans. Otherwise it shall reject the issue
and show the reason.
Must
FR-07
Calculate due date
On issue, the system shall record the member ID, copy ID, issue
date and due date using the member type and current loan policy.
Must
FR-08
Return a book
The system shall allow a librarian to close an open loan once,
record the return date and make the copy available or hold it for
the next eligible reservation.
Must
FR-09
Place reservation
The system shall allow an active member to join the queue for a
title with no immediately available copy, provided the member
has no existing open reservation for that title.
Must
FR-10
Manage reservations
The system shall allocate returned or released copies to the
earliest eligible waiting member, show the hold expiry, and allow
members to cancel their own open reservations. Expired or
cancelled holds shall release the copy to the next eligible member
or to availability. Issuing a held copy shall fulfil its reservation.
Must
FR-11
Identify overdue loans
The system shall mark an open loan overdue when the current
calendar date is later than its due date, and list overdue loans for
librarians.
Must
FR-12
Overdue notice
The system shall create one in-system overdue notice per
overdue loan during the daily overdue check, containing the title
and due date, visible only to the borrowing member and
librarians.
Should
FR-13
Member dashboard
The system shall show a member only their own open loans, due
dates, reservation status and overdue notices.
Must
FR-14
Library administration
The system shall allow an administrator to assign librarian
accounts and update loan periods, loan limits and reservation
hold duration using positive whole numbers. Policy changes shall
apply to new loans and holds only.
Must
