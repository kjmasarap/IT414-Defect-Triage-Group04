# IT414 Defect Triage Lab - GitHub Issues Setup

**Repository:** [kjmasarap/IT414-Defect-Triage-Group01]
https://github.com/kjmasarap/IT414-Defect-Triage-Group04
## Overview

This repository contains the IT414 System Quality Assurance - GitHub Issues Defect Triage Lab. The lab demonstrates professional defect identification, triage, and lifecycle management using GitHub Issues.

## Part A: Repository Setup ✓

- [x] Repository created: `IT414-Defect-Triage-Group04`
- [x] Issues feature enabled
- [x] Labels configured in `.github/labels.json`

### Labels Created

**Severity Labels:**
- `severity-critical` (Red - #FF0000)
- `severity-high` (Orange - #FF6600)
- `severity-medium` (Yellow - #FFCC00)
- `severity-low` (Green - #00CC00)

**Priority Labels:**
- `priority-high` (Dark Red - #CC0000)
- `priority-medium` (Gold - #CCAA00)
- `priority-low` (Green - #00AA00)

**Workflow Status Labels:**
- `status-new` (Blue - #0075CA)
- `status-in-progress` (Green - #1F883D)
- `status-for-retest` (Purple - #A371F7)

**Triage Result Labels:**
- `duplicate` (Gray - #CCCCCC)
- `deferred` (Dark Gray - #696969)
- `not-a-defect` (Gold - #D4AF37)

## Part B: Defect Scenarios

### Required Scenarios (SC-01 to SC-08)

| Scenario | Title | Severity | Priority | Status |
|----------|-------|----------|----------|--------|
| SC-01 | Duplicate Payment Transaction on Double Submit | Critical | High | New |
| SC-02 | Double Booking of Exclusive Time Slots | High | High | New |
| SC-03 | Access Control Test Case Contains Incorrect Test Data | N/A | N/A | Not-a-Defect |
| SC-04 | System Allows Negative Inventory Stock Values | High | High | New |
| SC-05 | Spelling Error in University Name on Landing Page | Low | High | New |
| SC-06 | Report Date Filter Includes Transactions Outside Range | Medium | High | New |
| SC-07 | Duplicate Report - Same Defect Submitted Multiple Times | N/A | N/A | Duplicate |
| SC-08 | App Shows Success Message Despite HTTP 500 API Error | Critical | High | New |

### Additional Scenarios (SC-09 to SC-11)

| Scenario | Title | Severity | Priority |
|----------|-------|----------|----------|
| SC-09 | Users Logged Out Without Warning After Session Timeout | High | High |
| SC-10 | System Allows Registration with Duplicate Email Addresses | High | High |
| SC-11 | PDF Export Corrupts Special Characters and Text Formatting | Medium | Medium |

## Part C: Creating GitHub Issues

### Quick Start

1. Navigate to the Issues tab: https://github.com/kjmasarap/IT414-Defect-Triage-Group01/issues
2. Click **"New Issue"** button
3. Use the templates provided in `ISSUE_TEMPLATES.md` and `ADDITIONAL_SCENARIOS.md`

### Issue Template Structure

Each issue includes:
- **Title:** Clear, concise summary
- **Module/Feature:** Area affected
- **Environment:** Testing context
- **Preconditions:** Setup requirements
- **Steps to Reproduce:** Numbered reproduction steps
- **Expected Result:** What should happen
- **Actual Result:** What actually happens
- **Evidence:** Supporting documentation
- **Triage Notes:** Initial classification reasoning

### Labels to Apply (per issue type)

**For Confirmed Defects:**
```
severity-[critical|high|medium|low]
priority-[high|medium|low]
status-new
```

**For Non-Defects:**
```
not-a-defect
status-new
```

**For Duplicates:**
```
duplicate
status-new
```

## Part D: Triage Comments

For each issue, add at least one QA Lead comment explaining:
- [ ] Why this is/is not a confirmed defect
- [ ] Rationale for severity classification
- [ ] Rationale for priority classification
- [ ] Next steps or assignment

### Example Comment Format

```markdown
## QA Lead - Triage Decision

**Classification:** Confirmed Defect

**Severity Justification:** Critical - This defect directly impacts financial 
transactions and violates transaction integrity requirements.

**Priority Justification:** High - Affects production payment processing with 
potential financial liability.

**Root Cause Assessment:** System lacks idempotency protection at both UI and 
server layers, allowing duplicate processing on rapid form submission.

**Recommended Assignment:** Dev Lead - Backend Payment Team
**Estimated Effort:** Medium
**Next Steps:** Code review of submit button handler and server transaction logic
```

## Part E: Lifecycle Simulation

Apply the following updates to demonstrate the complete defect lifecycle:

### SC-01: Fixed and Verified ✓
- **Developer Update:** Duplicate prevention implemented at UI and server
- **Status Change:** `status-new` → `status-for-retest`
- **Retest Result:** PASS - Only one payment record created
- **Final Status:** Close as `RESOLVED`

### SC-02: Partially Fixed, Further Testing Needed
- **Developer Update:** UI disables occupied slots visually
- **Status Change:** `status-new` → `status-for-retest`
- **Retest Finding:** Direct API request still allows double booking
- **Decision:** Keep OPEN, escalate as backend issue
- **Comment:** Document that UI fix is insufficient; backend locking required

### SC-03: Test Case Error, No Product Fix ✓
- **QA Review:** Test data was incorrect (Student account used instead of Admin)
- **Status Change:** `status-new` → Close as `NOT-A-DEFECT`
- **Comment:** Document the test case error and correction needed

### SC-05: Fixed and Verified ✓
- **Developer Update:** Spelling corrected
- **Status Change:** `status-new` → `status-for-retest`
- **Retest Result:** PASS - University name displayed correctly
- **Final Status:** Close as `RESOLVED`

### SC-06: Requires Investigation
- **Developer Update:** Date filter corrected for on-screen report
- **Status Change:** `status-new` → `status-for-retest`
- **Retest Finding:** CSV export still includes Sept 6 transactions
- **Decision:** Document whether this is same root cause or separate issue
- **Comment:** Add analysis of whether CSV behavior should be separate issue

## Part F: Capstone Connection

Create one additional GitHub Issue (SC-09 minimum) based on capstone project:

- [ ] Use professional issue format
- [ ] Assign appropriate severity and priority
- [ ] Include evidence requirements
- [ ] Write sustainable fix considerations
- [ ] Mark as "Training Scenario" if simulated

**Templates:**
- `ADDITIONAL_SCENARIOS.md` includes SC-09, SC-10, SC-11 examples
- Adapt to your specific capstone project

## Files in This Repository

```
IT414-Defect-Triage-Group01/
├── README.md                    (This file)
├── DEFECT_SCENARIOS.md          (SC-01 to SC-08 detailed descriptions)
├── ISSUE_TEMPLATES.md           (Ready-to-copy GitHub issue formats)
├── ADDITIONAL_SCENARIOS.md      (SC-09, SC-10, SC-11 examples)
└── .github/
    └── labels.json              (Label configuration)
```

## Submission Checklist

- [ ] Repository created and public
- [ ] At least 6 GitHub Issues created (5 required + 1 capstone)
- [ ] All issues use professional defect report format
- [ ] Severity labels applied consistently
- [ ] Priority labels applied consistently
- [ ] Workflow status labels applied
- [ ] Triage result labels applied (where applicable)
- [ ] At least one QA Lead comment per issue
- [ ] Lifecycle changes documented:
  - [ ] At least 2 issues closed (resolved)
  - [ ] At least 1 issue remains open or reopened
  - [ ] At least 1 issue closed as not-a-defect or duplicate
- [ ] SC-06 CSV behavior decision documented
- [ ] Screenshot of final Issues list or Project board

## GitHub Project Board (Optional)

Create a project named "Defect Triage Board" with columns:
- New
- In Progress
- For Retest
- Done

Move issues through the board as they progress through the lifecycle.

## Resources

- [GitHub Issues Documentation](https://docs.github.com/en/issues)
- [GitHub Labels Best Practices](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)
- [Professional Defect Reporting](https://www.softwaretestinghelp.com/how-to-write-good-bug-reports/)

## Repository Links

- **Issues:** https://github.com/kjmasarap/IT414-Defect-Triage-Group01/issues
- **Labels:** https://github.com/kjmasarap/IT414-Defect-Triage-Group01/labels
- **Repository:** https://github.com/kjmasarap/IT414-Defect-Triage-Group01

---

**Last Updated:** September 9, 2026  
**Course:** IT414 - System Quality Assurance  
**Lab:** GitHub Issues Defect Triage
