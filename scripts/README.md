# GitHub Automation Scripts

This directory contains scripts to automate GitHub API operations for the IT414 Defect Triage Lab.

## Prerequisites

- Node.js (v12 or higher)
- GitHub Personal Access Token with `repo` and `issues` scopes

## Setup

### 1. Create a GitHub Personal Access Token

1. Go to https://github.com/settings/tokens/new
2. Give it a name like "IT414 Lab Script"
3. Select scopes:
   - ✅ `repo` (full control of private repositories)
   - ✅ `public_repo` (access to public repositories)
4. Click **Generate token**
5. Copy the token (you won't see it again!)

### 2. Set Environment Variable

```bash
export GITHUB_TOKEN=your_token_here
```

Or set it inline when running the script:

```bash
GITHUB_TOKEN=your_token_here node scripts/add-labels-and-comments.js
```

## Scripts

### `add-labels-and-comments.js`

Automatically adds labels and QA Lead triage comments to all 8 defect scenario issues (SC-01 through SC-08).

**What it does:**
- Adds appropriate severity, priority, and status labels to each issue
- Adds professional QA Lead triage comments with classification, justification, and next steps
- Handles rate limiting and errors gracefully

**Labels applied per issue:**
- **SC-01** (Issue #2): severity-critical, priority-high, status-new
- **SC-02** (Issue #3): severity-high, priority-high, status-new
- **SC-03** (Issue #4): not-a-defect, status-new
- **SC-04** (Issue #5): severity-high, priority-high, status-new
- **SC-05** (Issue #6): severity-low, priority-high, status-new
- **SC-06** (Issue #7): severity-medium, priority-high, status-new
- **SC-07** (Issue #8): duplicate, status-new
- **SC-08** (Issue #9): severity-critical, priority-high, status-new

**Usage:**

```bash
GITHUB_TOKEN=your_token node scripts/add-labels-and-comments.js
```

**Expected output:**

```
🚀 Starting GitHub Issue Automation Script
📦 Repository: kjmasarap/IT414-Defect-Triage-Group04
📋 Processing 8 issues

📌 SC-01: Duplicate Payment Transaction
   Issue #2
  ✅ Added labels: severity-critical, priority-high, status-new
  ✅ Added triage comment

[... more issues ...]

============================================================
📊 SUMMARY
============================================================
✅ Successfully processed: 8/8 issues
✨ Script completed!
🔗 View results: https://github.com/kjmasarap/IT414-Defect-Triage-Group04/issues
```

## Troubleshooting

### "GITHUB_TOKEN environment variable not set"
Make sure you've exported the token before running the script:
```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxx
node scripts/add-labels-and-comments.js
```

### "401 Unauthorized"
Your token may be invalid or expired. Generate a new one at https://github.com/settings/tokens

### "404 Not Found"
Verify the repository name and owner are correct in the script.

### Rate limiting
If you get rate limit errors, the script includes a 500ms delay between requests. This should be sufficient for 8 issues.

## Manual Alternative

If you prefer not to use the script, you can manually add labels and comments through the GitHub web interface:

1. Go to https://github.com/kjmasarap/IT414-Defect-Triage-Group04/issues
2. Click each issue
3. Click **Labels** on the right sidebar → select labels
4. Scroll to comments and paste the triage comment from the script file

## API Rate Limits

GitHub's API allows:
- 5,000 requests per hour (for authenticated requests)
- This script makes approximately 16 requests (2 per issue)

No rate limiting issues should occur with this script.
