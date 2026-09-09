# Quick Start Guide - Running the Automation Script

This guide walks you through running the automation script to add labels and triage comments to all your issues in seconds.

## 🚀 Quick Start (5 minutes)

### Step 1: Generate GitHub Personal Access Token

1. Go to: https://github.com/settings/tokens/new
2. Name it: `IT414 Lab Script`
3. Select these scopes:
   - ✅ `repo` (for private/public repo access)
4. Scroll down and click **Generate token**
5. **Copy the token immediately** (you won't see it again!)

Example token format: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 2: Run the Script

Open your terminal in your repository directory and run:

#### Option A: Node.js (Recommended if you have Node.js installed)

```bash
export GITHUB_TOKEN=ghp_your_token_here
node scripts/add-labels-and-comments.js
```

#### Option B: Python (Recommended if you have Python 3 installed)

First, install the requests library (one-time):
```bash
pip install requests
```

Then run:
```bash
export GITHUB_TOKEN=ghp_your_token_here
python3 scripts/add-labels-and-comments.py
```

#### Option C: One-liner (no need to export)

**Node.js:**
```bash
GITHUB_TOKEN=ghp_your_token_here node scripts/add-labels-and-comments.js
```

**Python:**
```bash
GITHUB_TOKEN=ghp_your_token_here python3 scripts/add-labels-and-comments.py
```

### Step 3: Verify Results

The script will output:
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

Then visit: https://github.com/kjmasarap/IT414-Defect-Triage-Group04/issues

All your issues should now have:
- ✅ Appropriate severity/priority labels
- ✅ Professional QA triage comments

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| `GITHUB_TOKEN environment variable not set` | Make sure you export the token first: `export GITHUB_TOKEN=ghp_...` |
| `401 Unauthorized` | Token is invalid/expired. Generate a new one at https://github.com/settings/tokens |
| `command not found: node` | Install Node.js from https://nodejs.org or use Python instead |
| `ModuleNotFoundError: No module named 'requests'` | Install requests: `pip install requests` |
| `404 Not Found` | Check that repo name is correct: `kjmasarap/IT414-Defect-Triage-Group04` |

## 📋 What Gets Added

The script automatically adds:

**Labels per Issue:**
- SC-01 (Issue #2): `severity-critical` `priority-high` `status-new`
- SC-02 (Issue #3): `severity-high` `priority-high` `status-new`
- SC-03 (Issue #4): `not-a-defect` `status-new`
- SC-04 (Issue #5): `severity-high` `priority-high` `status-new`
- SC-05 (Issue #6): `severity-low` `priority-high` `status-new`
- SC-06 (Issue #7): `severity-medium` `priority-high` `status-new`
- SC-07 (Issue #8): `duplicate` `status-new`
- SC-08 (Issue #9): `severity-critical` `priority-high` `status-new`

**Triage Comments:**
Each issue gets a professional QA Lead triage comment with:
- Classification (Confirmed Defect / Not a Defect / Duplicate)
- Severity Justification
- Priority Justification
- Root Cause Assessment
- Recommended Assignment
- Estimated Effort
- Next Steps

## ✨ After Running the Script

Your lab will be **75% complete**! You still need to:

1. **Complete the Lifecycle Simulation (Part E)** - Update issues to show lifecycle:
   - SC-01: Close as resolved ✓
   - SC-02: Reopen with comment about insufficient fix
   - SC-03: Close as not-a-defect ✓
   - SC-05: Close as resolved ✓
   - SC-06: Add investigation comment

2. **Optional: Create a Project Board** - For visual workflow (Part G)

3. **Take a screenshot** of your final issues list for submission

## 🎯 Next Steps After Automation

Once the script completes successfully:

```bash
# View your issues in the browser
open https://github.com/kjmasarap/IT414-Defect-Triage-Group04/issues

# Or manually update lifecycle status by clicking each issue and:
# 1. Changing status labels (status-for-retest, etc.)
# 2. Adding developer/QA comments
# 3. Closing issues that are resolved/duplicate/not-a-defect
```

---

**Estimated time to complete:** 5 minutes to run script + 15 minutes to finish lifecycle simulation = **20 minutes total!**

Need help? Check `scripts/README.md` for detailed documentation.
