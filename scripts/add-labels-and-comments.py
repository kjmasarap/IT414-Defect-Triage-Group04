#!/usr/bin/env python3

"""
GitHub API Script - Add Labels and Triage Comments to Issues
Python alternative to the Node.js version

Usage: GITHUB_TOKEN=your_token python3 scripts/add-labels-and-comments.py

This script automates adding labels and QA Lead triage comments to all defect scenario issues.
"""

import os
import sys
import json
import time
import requests
from typing import List, Dict, Tuple

# Configuration
OWNER = 'kjmasarap'
REPO = 'IT414-Defect-Triage-Group04'
TOKEN = os.environ.get('GITHUB_TOKEN')
BASE_URL = 'https://api.github.com'

if not TOKEN:
    print('❌ Error: GITHUB_TOKEN environment variable not set')
    print('Usage: GITHUB_TOKEN=your_token python3 scripts/add-labels-and-comments.py')
    sys.exit(1)

# Headers for GitHub API
HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
}

# Issue data with labels and triage comments
ISSUES_DATA = [
    {
        'issue_number': 2,
        'title': 'SC-01: Duplicate Payment Transaction',
        'labels': ['severity-critical', 'priority-high', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Confirmed Defect

**Severity Justification:** Critical - This defect directly impacts financial transactions and violates transaction integrity requirements. Multiple charges on a single payment creates immediate financial liability and customer trust issues.

**Priority Justification:** High - Affects production payment processing with potential financial liability. This must be addressed before any further payment operations.

**Root Cause Assessment:** System lacks idempotency protection at both UI and server layers, allowing duplicate processing on rapid form submission. The submit button is not disabled after initial click, and server-side transaction processing lacks duplicate detection.

**Recommended Assignment:** Dev Lead - Backend Payment Team  
**Estimated Effort:** Medium  
**Next Steps:** 
1. Code review of submit button handler and transaction processing logic
2. Implement UI-level submit button disabling after first click
3. Implement server-side idempotency token or request deduplication
4. Add integration tests for concurrent payment submissions'''
    },
    {
        'issue_number': 3,
        'title': 'SC-02: Double Booking of Exclusive Time Slots',
        'labels': ['severity-high', 'priority-high', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Confirmed Defect

**Severity Justification:** High - Major feature impairment. Double booking creates scheduling conflicts and impacts customer experience and business operations.

**Priority Justification:** High - Directly affects appointment scheduling, a core business function. Multiple overbookings will degrade service quality.

**Root Cause Assessment:** Race condition in concurrent request handling. UI-level slot disabling provides false sense of security, but backend lacks proper database-level locking or conflict detection. Direct API requests bypass UI constraints entirely.

**Recommended Assignment:** Dev Lead - Backend Booking Team  
**Estimated Effort:** Medium-High  
**Next Steps:**
1. Implement database-level unique constraint or row-level locking on availability slots
2. Add pessimistic or optimistic locking in reservation transaction logic
3. Implement backend validation independent of UI state
4. Add load testing to verify concurrent request handling'''
    },
    {
        'issue_number': 4,
        'title': 'SC-03: Admin Dashboard Access Control Test Case Error',
        'labels': ['not-a-defect', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Not a Defect

**Root Cause Assessment:** Test data error, not a product defect. The test case incorrectly uses a Student account to access the Admin Dashboard. System requirement explicitly states only Administrator accounts should have access. When tested with the correct Admin account, the feature functions as designed.

**QA Recommendation:** Update the test case to use an Administrator account for execution. The access control mechanism is working correctly and denies unauthorized access as intended.

**Next Steps:**
1. Close this issue as "not-a-defect"
2. Update test case documentation to use Admin account
3. Add note to QA process checklist: verify correct account types are used in access control tests'''
    },
    {
        'issue_number': 5,
        'title': 'SC-04: Negative Inventory After Sales Transaction',
        'labels': ['severity-high', 'priority-high', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Confirmed Defect

**Severity Justification:** High - Violates fundamental inventory management principles. Negative inventory creates data integrity issues and breaks fulfillment logic.

**Priority Justification:** High - Impacts financial reporting accuracy and order fulfillment process. Cannot reliably determine stock availability.

**Root Cause Assessment:** Missing input validation in sales transaction workflow. No business logic to prevent overselling or handle backorder scenarios explicitly. Inventory field lacks constraint validation.

**Recommended Assignment:** Dev Lead - Inventory Management Team  
**Estimated Effort:** Medium  
**Next Steps:**
1. Add validation to prevent transactions exceeding available stock
2. Clarify business requirements: Should system prevent overselling or support backorders?
3. If backorders supported: Implement explicit backorder status and UI indicators
4. Add unit tests for inventory boundary conditions'''
    },
    {
        'issue_number': 6,
        'title': 'SC-05: Spelling Error in Official University Name',
        'labels': ['severity-low', 'priority-high', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Confirmed Defect

**Severity Justification:** Low - Cosmetic issue with no functional impact. Feature remains usable and no data/transactions are affected.

**Priority Justification:** High - Despite low functional severity, this is high priority due to reputational impact. Official institutional information must be displayed correctly, especially with external evaluation scheduled tomorrow.

**Root Cause Assessment:** Simple typo in landing page content. String value contains spelling error in university name.

**Recommended Assignment:** Dev Lead - Frontend/Content Team  
**Estimated Effort:** Low (trivial fix)  
**Next Steps:**
1. Correct spelling in source content/configuration
2. Verify spelling against official university branding guidelines
3. Deploy immediately before external evaluation'''
    },
    {
        'issue_number': 7,
        'title': 'SC-06: Date Range Filter Includes Out-of-Range Transactions',
        'labels': ['severity-medium', 'priority-high', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Confirmed Defect

**Severity Justification:** Medium - Incorrect data inclusion affects reporting accuracy but doesn't completely break functionality (workaround: manual adjustment possible).

**Priority Justification:** High - Financial reporting accuracy is critical for compliance and decision-making.

**Root Cause Assessment:** Date range filter boundary condition error. Likely using >= comparison for end date instead of <, causing September 6 transactions to be included in September 1-5 range.

**Recommended Assignment:** Dev Lead - Reporting Module Team  
**Estimated Effort:** Low-Medium  
**Next Steps:**
1. Fix date comparison logic (use < for end boundary)
2. During retest: Determine if CSV export has same issue or separate root cause
3. If CSV behavior differs: File as separate issue with investigation notes
4. Add unit tests for date boundary conditions
5. Test with edge cases (month boundaries, year boundaries)'''
    },
    {
        'issue_number': 8,
        'title': 'SC-07: Duplicate Defect Report',
        'labels': ['duplicate', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Duplicate Issue

**Assessment:** This is a duplicate report of the same defect submitted independently by a different tester. Both issues describe identical reproduction steps, same environment, and same failure behavior.

**Consolidation Decision:** Close this duplicate issue and link to the original issue (SC-01 or the earlier submission). This consolidates team effort and prevents duplicate work.

**Recommendation:** Link this issue to the original issue and close as duplicate with clear documentation of the relationship.

**Next Steps:**
1. Link to original issue
2. Close with "duplicate" status
3. Add note acknowledging independent testing contribution'''
    },
    {
        'issue_number': 9,
        'title': 'SC-08: Misleading Success Message on API 500 Error',
        'labels': ['severity-critical', 'priority-high', 'status-new'],
        'comment': '''## QA Lead - Triage Decision

**Classification:** Confirmed Defect

**Severity Justification:** Critical - Severe impact on user experience and data integrity. Users believe data was saved when it actually failed. Causes data loss and severely undermines user trust.

**Priority Justification:** High - Mobile users are immediately affected when API errors occur. Must be addressed before production release.

**Root Cause Assessment:** Client-side error handling and API response validation is insufficient. Mobile app displays success message without properly validating HTTP response code. App ignores HTTP 500 (Internal Server Error) response and treats it as success.

**Recommended Assignment:** Dev Lead - Mobile App Team  
**Estimated Effort:** Medium  
**Next Steps:**
1. Audit all API response handling in mobile app
2. Implement proper HTTP status code validation before showing success messages
3. Differentiate between HTTP 2xx (success), 4xx (client error), and 5xx (server error) responses
4. Implement retry logic with exponential backoff for server errors
5. Add user-facing error messages for failed API calls
6. Add integration tests for error response handling'''
    }
]


def add_labels_to_issue(issue_number: int, labels: List[str]) -> Tuple[bool, str]:
    """Add labels to an issue"""
    try:
        url = f'{BASE_URL}/repos/{OWNER}/{REPO}/issues/{issue_number}/labels'
        response = requests.post(url, headers=HEADERS, json={'labels': labels})
        
        if response.status_code in (200, 201):
            return True, f'Added labels: {", ".join(labels)}'
        else:
            return False, f'HTTP {response.status_code}: {response.text}'
    except Exception as e:
        return False, str(e)


def add_comment_to_issue(issue_number: int, comment: str) -> Tuple[bool, str]:
    """Add comment to an issue"""
    try:
        url = f'{BASE_URL}/repos/{OWNER}/{REPO}/issues/{issue_number}/comments'
        response = requests.post(url, headers=HEADERS, json={'body': comment})
        
        if response.status_code in (200, 201):
            return True, 'Added triage comment'
        else:
            return False, f'HTTP {response.status_code}: {response.text}'
    except Exception as e:
        return False, str(e)


def process_all_issues() -> None:
    """Process all issues"""
    print('\n🚀 Starting GitHub Issue Automation Script')
    print(f'📦 Repository: {OWNER}/{REPO}')
    print(f'📋 Processing {len(ISSUES_DATA)} issues\n')

    success_count = 0
    failure_count = 0

    for issue in ISSUES_DATA:
        print(f'\n📌 {issue["title"]}')
        print(f'   Issue #{issue["issue_number"]}')

        # Add labels
        labels_success, labels_msg = add_labels_to_issue(
            issue['issue_number'],
            issue['labels']
        )
        print(f'  {"✅" if labels_success else "❌"} {labels_msg}')

        # Add comment
        comment_success, comment_msg = add_comment_to_issue(
            issue['issue_number'],
            issue['comment']
        )
        print(f'  {"✅" if comment_success else "❌"} {comment_msg}')

        if labels_success and comment_success:
            success_count += 1
        else:
            failure_count += 1

        # Rate limiting - be respectful to the API
        time.sleep(0.5)

    # Summary
    print('\n' + '=' * 60)
    print('📊 SUMMARY')
    print('=' * 60)
    print(f'✅ Successfully processed: {success_count}/{len(ISSUES_DATA)} issues')
    if failure_count > 0:
        print(f'❌ Failed: {failure_count}/{len(ISSUES_DATA)} issues')
    print('\n✨ Script completed!')
    print(f'🔗 View results: https://github.com/{OWNER}/{REPO}/issues')


if __name__ == '__main__':
    try:
        process_all_issues()
    except KeyboardInterrupt:
        print('\n\n⚠️  Script interrupted by user')
        sys.exit(1)
    except Exception as e:
        print(f'\n❌ Fatal error: {e}')
        sys.exit(1)
