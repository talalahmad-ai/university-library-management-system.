3. Non-functional requirements
ID Requirement Priority
NFR-01
Performance
At least 95 of 100 catalog searches shall return within 2 seconds in a
future test with 1,000 book records and 20 concurrent users.
Should
NFR-02
Access control
Every protected operation shall enforce role and record ownership on
the server; all unauthorized attempts in the role test shall be denied
without changing data.
Must
NFR-03
Ease of use
At least 4 of 5 first-time test users shall find a known book and its
availability in 60 seconds without assistance.
Should
NFR-04
Data consistency
For two simultaneous issue attempts on the same available copy,
exactly one shall succeed; no copy shall have more than one open loan
or an open loan and an active hold at the same time.
Must
NFR-05
Password protection
The system shall store passwords only as salted, adaptive password
hashes and shall not display or log plaintext passwords.
Must
