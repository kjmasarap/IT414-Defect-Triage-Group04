# IT414 Defect Triage Lab - Issue Templates

This document contains ready-to-use issue templates. Copy each section to create a new GitHub Issue.

---

## Issue 1: SC-01 - Duplicate Payment Transaction on Double Submit

**Title:** Duplicate Payment Transaction on Double Submit

**Labels:** `severity-critical`, `priority-high`, `status-new`

**Description:**

### Module / Feature
Online Payment Processing

### Environment
Production - Payment Module

### Preconditions
- User account with sufficient balance
- Payment form loaded and ready for submission

### Steps to Reproduce
1. Navigate to the payment submission page
2. Enter valid payment amount and required details
3. Click the Submit button twice in rapid succession (within 1-2 seconds)
4. Observe the system response and check payment records

### Expected Result
- System should create only one valid payment transaction
- Account balance should be reduced once by the payment amount
- User should receive one confirmation with a single reference number

### Actual Result
- Two payment records are created with identical amounts and reference numbers
- Account balance is reduced twice (double deduction)
- User receives confirmation but system state is corrupted

### Evidence
- Payment transaction logs showing two identical entries with same timestamp and reference
- Account balance audit trail showing two separate deductions
- Payment confirmation email(s) received

### Triage Notes
This is a confirmed defect affecting financial transactions. The system lacks proper idempotency protection at both UI and server layers, allowing duplicate processing on rapid submission. This directly violates transaction integrity requirements and requires immediate remediation.

---

## Issue 2: SC-02 - Double Booking of Exclusive Time Slots

**Title:** Double Booking of Exclusive Time Slots in Adviser Appointments

**Labels:** `severity-high`, `priority-high`, `status-new`

**Description:**

### Module / Feature
Appointment / Booking System

### Environment
Staging - Booking Module

### Preconditions
- Adviser availability configured with exclusive time slots (e.g., 10:00 AM - 10:30 AM)
- Two independent user sessions (simulating concurrent requests)

### Steps to Reproduce
1. User A opens the booking page and selects adviser "John Smith" for 10:00 AM
2. User B simultaneously (within seconds) opens the same booking page and selects the same adviser and time slot
3. Both users complete their reservation flow independently
4. Both receive confirmation messages
5. Verify the booking records in the system

### Expected Result
- System should recognize the time slot is exclusively reserved
- Only the first user's reservation should be confirmed
- Second user should receive a "Slot unavailable" error message
- Single booking record should exist for that time slot

### Actual Result
- Both users receive "Confirmed" status messages
- Two independent booking records exist for the same adviser and identical time slot
- No conflict detection occurred

### Evidence
- Booking database records showing duplicate entries for identical time/adviser
- Confirmation messages from both user sessions
- System logs showing concurrent reservation requests

### Triage Notes
This is a race condition defect in the booking system's reservation logic. The system lacks proper locking or conflict detection for concurrent requests on exclusive resources. While the UI may visually disable occupied slots, backend validation is insufficient, allowing direct API requests to bypass constraints.

---

## Issue 3: SC-03 - Admin Dashboard Access Control Test Case Error

**Title:** Access Control Test Case Contains Incorrect Test Data

**Labels:** `not-a-defect`, `status-new`

**Description:**

### Module / Feature
Access Control / Admin Dashboard

### Environment
Test Execution - Access Control Module

### Preconditions
- Admin Dashboard feature exists in system
- Test case documentation specifies expected access conditions

### Steps to Reproduce
1. Execute test case for Admin Dashboard access
2. Use a Student account to attempt accessing the Admin Dashboard
3. Observe the system response

### Expected Result
- Admin Dashboard should open (per test case requirement)

### Actual Result
- System displays "Access Denied" error message
- Student account cannot access Admin Dashboard

### Evidence
- Test case documentation
- Execution log showing Student account used
- Access Denied error response

### Triage Notes
**This is not a software defect.** The test case contains incorrect test data. The Admin Dashboard access control is functioning correctly—it properly denies access to Student accounts as designed. The system requirement states the Admin Dashboard should be accessible only to Administrator accounts. When executed with the correct Admin account, the feature works as specified. This is a test case maintenance issue, not a product defect. The test case should be updated to use an Admin account for execution.

---

## Issue 4: SC-04 - Negative Inventory After Sales Transaction

**Title:** System Allows Negative Inventory Stock Values

**Labels:** `severity-high`, `priority-high`, `status-new`

**Description:**

### Module / Feature
Inventory Management / Sales Processing

### Environment
Production - Inventory Module

### Preconditions
- Item in stock with quantity of 1 unit
- Sales transaction workflow configured
- No business rule explicitly allowing negative inventory

### Steps to Reproduce
1. Verify current stock level for the item (quantity = 1)
2. Initiate a sales transaction for 3 units of the same item
3. Complete the transaction submission
4. Verify final inventory quantity in system

### Expected Result
- System should prevent the transaction if it exceeds available stock
- Alternative: If business rules allow backorders, system should clearly indicate the negative quantity as a backorder status (not regular inventory)
- Inventory should never show negative values in normal stock view

### Actual Result
- Transaction is completed successfully despite insufficient stock
- Inventory quantity becomes -2
- System records this as a normal completed sale with no backorder notation

### Evidence
- Inventory ledger showing item quantity changing from 1 to -2
- Sales transaction record marked as completed
- No backorder or override flag in transaction record

### Triage Notes
This is a confirmed defect in inventory validation. The system violates fundamental inventory management principles by allowing negative stock without proper business rule handling. Sales should be rejected if insufficient stock exists, or the system should have explicit business logic and UI indicators for backorders. This creates potential discrepancies in financial reporting and fulfillment.

---

## Issue 5: SC-05 - Spelling Error in Official University Name

**Title:** Spelling Error in University Name on Landing Page

**Labels:** `severity-low`, `priority-high`, `status-new`

**Description:**

### Module / Feature
Official Content / UI - Landing Page

### Environment
Production - Web Interface

### Preconditions
- System deployed and accessible
- Landing page visible to external users
- Official evaluators scheduled to review system tomorrow

### Steps to Reproduce
1. Navigate to system landing page
2. Locate the university name displayed on the page
3. Verify the spelling against official institutional records

### Expected Result
- University name should be spelled correctly and match official institutional naming standards
- Display should match official university branding guidelines

### Actual Result
- University name contains a spelling error
- Example: "Universty" instead of "University" (or similar)
- Error is visible to all external users

### Evidence
- Screenshot of landing page with spelling error highlighted
- Official university name from institutional records
- Visitor session logs showing external evaluators will access this page

### Triage Notes
This is a confirmed defect affecting system credibility. While the feature remains functionally usable and no transaction is impacted, official institutional information must be displayed correctly. This error will be directly observed during the external evaluation tomorrow and undermines organizational credibility. Despite low functional severity, this warrants immediate correction due to visibility and reputational impact.

---

## Issue 6: SC-06 - Date Range Filter Includes Out-of-Range Transactions

**Title:** Report Date Filter Includes Transactions Outside Selected Range

**Labels:** `severity-medium`, `priority-high`, `status-new`

**Description:**

### Module / Feature
Reports / Filtering

### Environment
Production - Reporting Module

### Preconditions
- Report module with date range filter capability
- Transactions existing for multiple dates including September 5 and 6
- Report filtered for September 1-5 date range

### Steps to Reproduce
1. Navigate to Reports section
2. Apply date filter: September 1 - September 5
3. Generate the filtered report
4. Review included transactions and total amount
5. Cross-reference with actual transactions for the filtered period

### Expected Result
- Report should contain only transactions dated September 1 through September 5
- September 6 transactions should be excluded
- Total amount should match the sum of only transactions within the selected range

### Actual Result
- Report includes transactions from September 6 despite filter range ending on September 5
- Total amount is inflated and does not match the selected period
- September 6 transactions appear in filtered results

### Evidence
- Report output showing September 6 transactions
- Transaction detail lines with dates outside selected range
- Discrepancy between reported total and manually calculated total for Sept 1-5

### Triage Notes
This is a confirmed defect in the date range filtering logic. The filter boundary conditions are incorrect—likely using an inclusive end date comparison (>= instead of <). This causes data accuracy issues in financial reports. **Note:** During retest, determine whether the CSV export behavior is part of the same root cause or a separate issue requiring independent investigation. Document the decision separately.

---

## Issue 7: SC-07 - Duplicate Defect Report

**Title:** Duplicate Report - Same Defect Submitted Multiple Times

**Labels:** `duplicate`, `status-new`

**Description:**

### Module / Feature
Issue Tracking / Defect Management

### Environment
QA Process - Issue Management

### Preconditions
- Two issues exist in the tracking system
- Both issues describe identical steps to reproduce
- Both are submitted in the same environment
- Both report the same failure behavior
- First issue was logged earlier by a different tester

### Steps to Reproduce
1. Review newly submitted issue X describing a specific failure scenario
2. Review existing open issue Y from earlier submission
3. Compare: reproduction steps, environment, expected vs. actual results
4. Verify both issues reference the same root cause failure

### Expected Result
- Team should recognize these as duplicate reports of the same defect
- Only one defect tracking entry should remain open
- Duplicate issue should be closed with clear documentation of the relationship

### Actual Result
- Two independent unresolved issues are tracked separately
- Team may work on the same problem twice
- Duplicate effort and resource allocation

### Evidence
- Issue X description and steps
- Issue Y description and steps
- Environmental details from both issues
- Test results from both submissions

### Triage Notes
This is a duplicate issue report, not a software defect in the application under test. The original issue (submitted earlier) should remain open with active investigation. This duplicate should be closed and linked to the original issue. Acknowledges independent testing efforts and consolidates team work on a single defect tracking entry.

**Duplicate of:** [Link to original issue]

---

## Issue 8: SC-08 - Misleading Success Message on API 500 Error

**Title:** App Shows Success Message Despite HTTP 500 API Error

**Labels:** `severity-critical`, `priority-high`, `status-new`

**Description:**

### Module / Feature
Mobile App / API - Record Creation

### Environment
Production - Mobile Application

### Preconditions
- Mobile app connected to backend API
- User initiates creation of a new record
- API backend experiences internal error

### Steps to Reproduce
1. Open mobile app and navigate to record creation feature
2. Complete form with valid data and submit
3. Observe success message in app UI
4. Close and reopen the app (or refresh the view)
5. Verify whether the newly created record exists
6. Check Network log/API inspector for HTTP response codes

### Expected Result
- Success message should only appear after the server confirms successful record creation
- HTTP response should be 200 or 201 (success codes)
- Record should persist and be visible after app refresh
- User should receive an error message if the API call fails

### Actual Result
- Mobile app displays "Saved successfully" message
- HTTP response code is 500 (Internal Server Error)
- After app refresh, the newly created record is missing
- Record was never persisted in backend database

### Evidence
- Network log showing HTTP 500 response
- Mobile app screenshot showing "Saved successfully" message
- Verification showing record missing after refresh
- Backend error logs for the failed API request

### Triage Notes
This is a confirmed defect in the mobile app's error handling and API response validation. The app is displaying success messages without proper validation of the actual HTTP response code. Users believe data has been saved when the backend API has returned an error. This creates data loss and severely undermines user trust. The fix must ensure the app validates successful HTTP status codes before displaying success messages to the user.

---

## Capstone Connection - SC-09 (Template)

**Title:** [Your Capstone Scenario Title]

**Labels:** `severity-[low|medium|high|critical]`, `priority-[low|medium|high]`, `status-new`

**Description:**

### Module / Feature
[Your module/feature]

### Environment
[Environment details]

### Preconditions
[List preconditions]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Expected Result
[What should happen]

### Actual Result
[What actually happens]

### Evidence
[What evidence would confirm this]

### Triage Notes
[Reasoning for severity/priority]

**Note:** [If simulated, add] This is a training scenario based on [capstone project description].

---

## Instructions for Creating Issues

1. Go to https://github.com/kjmasarap/IT414-Defect-Triage-Group01/issues
2. Click "New Issue" button
3. Copy the title from the template above
4. Copy the description (everything after "**Description:**")
5. Add the labels listed in the template
6. Submit the issue

All issues should be in `status-new` initially for triage discussion.
