5. User stories and acceptance criteria (continued)
US-06
As a librarian, I want to record book returns, so that copies can be borrowed again.
AC-06a: Return an open loan with no waiting reservation: the loan closes, the return date is
recorded and availability increases by one. A repeat return is rejected without another
increase.
AC-06b: Return a copy for a title with an eligible waiting member: the loan closes and the
copy is held for that member, not counted as available.
US-07
As a faculty member, I want to reserve an unavailable book, so that I can borrow it when a
copy becomes free.
AC-07a: For a title with zero free copies, an active faculty member can create one waiting
reservation; a repeat reservation, an inactive member or a title with a free copy is rejected.
AC-07b: Given two eligible waiting members, the earlier request gets the first released
copy and the hold expires 48 hours after allocation; a waiting member who has become
ineligible is skipped.
AC-07c: Cancel a waiting reservation and confirm removal from the queue. Cancel or
expire a held reservation and confirm the next eligible member gets the copy; if none is
eligible, it becomes available. Issuing a held copy to its holder marks the reservation
fulfilled.
US-08
As a librarian, I want to see overdue loans, so that I can follow up on late returns.
AC-08a: A loan due 25 November is not overdue on that date; on 26 November it appears
in the overdue list if still open. A returned loan is not listed.
AC-08b: Run the overdue check twice for the same loan; exactly one notice with the
correct title and due date exists and is visible to the borrower and librarians only.
US-09
As a student, I want to see my borrowing and reservation details, so that I can keep track of
due dates and notices.
AC-09a: Sign in with a test member who has two open loans, one reservation and one
overdue notice; the dashboard shows all four records, correct due dates and reservation
status.
AC-09b: Try to open another member’s record and perform librarian/admin actions as a
student or faculty member; every attempt is denied and no data changes. A librarian is also
denied access to admin-only settings. Repeat the role and ownership checks for every
protected operation.
US-10
As a library administrator, I want to manage librarian access and lending rules, so that the
library can apply its policies.
AC-10a: Assign an account the librarian role; it can access librarian functions after sign-in
but not administrator settings.
AC-10b: Change the student loan period from 14 to 21 days, the limit from 3 to 4 and hold
duration from 48 to 72 hours. A new student loan uses 21 days, a fourth loan is allowed if
otherwise eligible, and a new hold expires after 72 hours. Existing due dates and hold
expiries stay unchanged; zero and negative values are rejected.
