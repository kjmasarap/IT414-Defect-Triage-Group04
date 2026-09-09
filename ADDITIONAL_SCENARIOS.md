# IT414 Defect Triage Lab - Additional Scenario

## SC-09: Session Timeout Logout Occurs Without User Notification

**Title:** Users Logged Out Without Warning After Session Timeout

**Labels:** `severity-high`, `priority-high`, `status-new`

**Description:**

### Module / Feature
Authentication / Session Management

### Environment
Production - Web Application

### Preconditions
- User is logged in to the system
- System has session timeout policy configured (e.g., 30 minutes of inactivity)
- User is actively working on a form or document

### Steps to Reproduce
1. Log in to the system with valid credentials
2. Navigate to a form with unsaved data (e.g., a student registration form or payment details)
3. Spend 30+ minutes without submitting or interacting with the form
4. Attempt to submit the form or perform an action
5. Observe the system response

### Expected Result
- System should display a warning message before session expires (e.g., "Your session will expire in 5 minutes")
- User should have the option to extend their session before timeout
- If timeout occurs, user should be notified they were logged out before being redirected to login
- Previously entered form data should be preserved (either in session or cached locally)
- User should be able to resume work if session data is recoverable

### Actual Result
- No warning message is displayed before session timeout
- User is abruptly logged out without notification
- Form data is lost completely
- User is redirected to login page without explanation
- No indication of why they lost their session

### Evidence
- Browser console logs showing session termination
- Timestamps of user activity and logout event
- Screenshot of abrupt redirect to login page
- User session audit logs showing logout without explicit user action
- Lost form data before submission

### Triage Notes
This is a confirmed defect in session management and user experience. While automatic logout after inactivity is a security best practice, the implementation lacks proper user notification and data preservation mechanisms. This causes frustration and data loss when users are working on time-consuming forms or transactions. The system should provide:
1. Pre-logout warning dialog (5 minutes before timeout)
2. Option to extend session or save work
3. Clear message explaining the logout
4. Mechanism to recover unsaved form data if possible

---

## SC-10: Duplicate Email Addresses Allowed During User Registration

**Title:** System Allows Registration with Duplicate Email Addresses

**Labels:** `severity-high`, `priority-high`, `status-new`

**Description:**

### Module / Feature
User Registration / Account Management

### Environment
Staging - Registration Module

### Preconditions
- Valid email address already registered in system (e.g., john@university.edu)
- Registration form is accessible
- Email validation is not enforced during registration

### Steps to Reproduce
1. Complete initial user registration with email: john@university.edu
2. Verify successful registration and account creation
3. Attempt to register a second account with the same email: john@university.edu
4. Submit the registration form
5. Check system response and database records

### Expected Result
- System should validate that email is unique
- Second registration attempt should be rejected with error message: "This email is already registered"
- User should be prompted to use a different email or recover the existing account
- Only one account record should exist per email address

### Actual Result
- Second registration is accepted without error
- Two accounts are created with identical email addresses
- Both accounts are marked as active and verified
- System allows duplicate email records in database
- Login system may authenticate the wrong account (unpredictable behavior)

### Evidence
- User database showing multiple records with same email address
- Two separate registration confirmation emails sent
- Successful completion messages for both registrations
- Test logs showing both email values in separate account records

### Triage Notes
This is a confirmed defect in data validation and database constraints. Email should be enforced as a unique constraint at both application and database levels. This creates several problems:
1. Account recovery and password reset functionality fails (unclear which account to recover)
2. Email-based authentication becomes unreliable
3. Compliance issues with many regulatory frameworks that require unique identifiers
4. Potential security vulnerability (account takeover by registering with victim's email)

The fix should include both application-level validation and database-level unique constraints to prevent duplicate emails.

---

## SC-11: PDF Report Export Removes Special Characters and Formatting

**Title:** PDF Export Corrupts Special Characters and Text Formatting

**Labels:** `severity-medium`, `priority-medium`, `status-new`

**Description:**

### Module / Feature
Reports / Export Functionality

### Environment:** Production - Reporting Module

### Preconditions
- Report contains international characters (e.g., accented letters: é, ñ, ü)
- Report contains special symbols (e.g., currency: €, ¥, mathematical: ±, ∞)
- Report has structured formatting (tables, indentation, headers)
- PDF export feature is being used

### Steps to Reproduce
1. Generate a report with data containing special characters and formatting
   - Example: "Université de Côte d'Ivoire" with "Price: €150.50"
   - Example: Table with centered headers and indented subtotals
2. Click "Export to PDF" button
3. Download and open the generated PDF file
4. Review the exported content for accuracy

### Expected Result
- Special characters should be preserved exactly as displayed in the report
- Text formatting (indentation, alignment, bold, font sizes) should be maintained
- Currency symbols and international text should render correctly
- PDF should be visually identical to the on-screen report

### Actual Result
- Special characters are replaced with placeholder symbols or removed entirely
  - "Université de Côte d'Ivoire" appears as "Universit de Cte d'Ivoire"
  - "€150.50" appears as "?150.50" or missing currency symbol
- Text formatting is lost in PDF export
  - Table alignment is broken
  - Indentation and spacing is incorrect
  - Header styling is not applied
- PDF quality is significantly degraded

### Evidence
- Original on-screen report screenshot showing correct characters and formatting
- Exported PDF file showing corrupted content
- Character encoding comparison between HTML source and PDF output
- User complaint from international markets reporting rendering issues

### Triage Notes
This is a confirmed defect in the PDF export library or character encoding configuration. The system is not properly handling UTF-8 or Unicode characters during PDF generation. This affects:
1. International users and multilingual reports
2. Financial reports with currency symbols
3. Professional report quality and credibility
4. Regulatory compliance for international institutions

The fix should ensure the PDF export process preserves character encoding and applies formatting templates correctly. Investigation should verify if the PDF library supports the required character sets or if configuration changes are needed.

