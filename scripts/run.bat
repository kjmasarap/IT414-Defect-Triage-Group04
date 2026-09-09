@echo off
REM GitHub API Automation Script Wrapper for Windows
REM Simple batch script to run the automation with proper error checking

setlocal enabledelayedexpansion

REM Colors aren't as easy in batch, so we use simple formatting
echo.
echo ========================================================================
echo   IT314 GitHub Issues Automation Script
echo   Adds labels and triage comments to all defect issues
echo ========================================================================
echo.

REM Check if GITHUB_TOKEN is set
if "%GITHUB_TOKEN%"=="" (
    echo [ERROR] GITHUB_TOKEN environment variable not set
    echo.
    echo To fix this, run one of the following:
    echo.
    echo Option 1: Set token in Command Prompt
    echo   set GITHUB_TOKEN=ghp_your_token_here
    echo   %0
    echo.
    echo Option 2: Set token inline (no space after equals sign)
    echo   GITHUB_TOKEN=ghp_your_token_here %0
    echo.
    echo Option 3: Create a GitHub Personal Access Token
    echo   1. Go to https://github.com/settings/tokens/new
    echo   2. Name it 'IT414 Lab Script'
    echo   3. Select 'repo' scope
    echo   4. Click 'Generate token'
    echo   5. Copy the token and run: set GITHUB_TOKEN=your_token
    echo.
    exit /b 1
)

REM Detect which script engine to use
where node >nul 2>nul
if !errorlevel! equ 0 (
    echo [INFO] Found Node.js, using Node.js version...
    echo.
    call node scripts\add-labels-and-comments.js
    exit /b !errorlevel!
)

where python >nul 2>nul
if !errorlevel! equ 0 (
    echo [INFO] Node.js not found, checking for Python...
    echo.
    
    REM Check if requests library is installed
    python -c "import requests" >nul 2>&1
    if !errorlevel! equ 0 (
        echo [INFO] Found Python with requests library, using Python version...
        echo.
        call python scripts\add-labels-and-comments.py
        exit /b !errorlevel!
    ) else (
        echo [WARNING] Python found but 'requests' library not installed
        echo.
        echo Installing requests library...
        pip install requests
        echo.
        echo [INFO] Running Python script...
        echo.
        call python scripts\add-labels-and-comments.py
        exit /b !errorlevel!
    )
)

echo [ERROR] Neither Node.js nor Python found
echo.
echo Please install one of the following:
echo   - Node.js: https://nodejs.org/
echo   - Python: https://www.python.org/downloads/
echo.
exit /b 1
