#!/bin/bash

# GitHub API Automation Script Wrapper
# Simple shell script to run the automation with proper error checking

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║   IT414 GitHub Issues Automation Script                    ║"
echo "║   Adds labels and triage comments to all defect issues     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check if GITHUB_TOKEN is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${RED}❌ Error: GITHUB_TOKEN environment variable not set${NC}"
    echo ""
    echo -e "${YELLOW}To fix this, run one of the following:${NC}"
    echo ""
    echo "Option 1: Export token globally"
    echo "  export GITHUB_TOKEN=ghp_your_token_here"
    echo "  $0"
    echo ""
    echo "Option 2: Set token inline"
    echo "  GITHUB_TOKEN=ghp_your_token_here $0"
    echo ""
    echo "Option 3: Create a GitHub Personal Access Token"
    echo "  1. Go to https://github.com/settings/tokens/new"
    echo "  2. Name it 'IT414 Lab Script'"
    echo "  3. Select 'repo' scope"
    echo "  4. Click 'Generate token'"
    echo "  5. Copy the token and run: export GITHUB_TOKEN=your_token"
    echo ""
    exit 1
fi

# Detect which script engine to use
if command -v node &> /dev/null; then
    echo -e "${BLUE}📦 Found Node.js, using Node.js version...${NC}"
    node scripts/add-labels-and-comments.js
    exit $?
elif command -v python3 &> /dev/null; then
    echo -e "${BLUE}📦 Node.js not found, checking for Python 3...${NC}"
    
    # Check if requests library is installed
    if python3 -c "import requests" 2>/dev/null; then
        echo -e "${BLUE}📦 Found Python 3 with requests library, using Python version...${NC}"
        python3 scripts/add-labels-and-comments.py
        exit $?
    else
        echo -e "${YELLOW}⚠️  Python 3 found but 'requests' library not installed${NC}"
        echo ""
        echo "Installing requests library..."
        pip install requests
        echo ""
        echo -e "${BLUE}Running Python script...${NC}"
        python3 scripts/add-labels-and-comments.py
        exit $?
    fi
else
    echo -e "${RED}❌ Error: Neither Node.js nor Python 3 found${NC}"
    echo ""
    echo "Please install one of the following:"
    echo "  - Node.js: https://nodejs.org/"
    echo "  - Python 3: https://www.python.org/downloads/"
    echo ""
    exit 1
fi
