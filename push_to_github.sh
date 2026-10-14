#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

# ============================================================
# GitHub Notebook Library Sync & Publisher
# Pushes all Colab notebooks to user's GitHub repository
# ============================================================

REPO_OWNER="kylejaco916"
REPO_NAME="${2:-"colab_redteam_notebooks.ipynb"}"
BRANCH="main"
LIB_DIR="/data/data/com.termux/files/home/colab_notebook_library"

TOKEN="${1:-"${GITHUB_TOKEN:-}"}"

echo "============================================================"
echo " 🐙 GitHub Notebook Publisher (Account: $REPO_OWNER)"
echo "============================================================"

if [ -z "$TOKEN" ]; then
  # Check if gh CLI is already authenticated
  if gh auth status >/dev/null 2>&1; then
    echo "✅ Authenticated via GitHub CLI (gh)."
    TOKEN=$(gh auth token 2>/dev/null || true)
  fi
fi

if [ -z "$TOKEN" ]; then
  if [ -t 0 ]; then
    echo "GitHub authentication token required to push to remote repository."
    echo "You can generate a token in 10 seconds at:"
    echo "👉 https://github.com/settings/tokens (classic -> scope: 'repo')"
    echo ""
    read -r -p "Enter your GitHub Personal Access Token (or paste): " input_token
    TOKEN="${input_token:-}"
  else
    echo "❌ Error: GitHub token required. Usage: upload-notebooks-github <PERSONAL_ACCESS_TOKEN>"
    exit 1
  fi
fi

if [ -z "$TOKEN" ]; then
  echo "❌ Error: No token provided. Push cancelled."
  exit 1
fi

echo "🚀 Configuring Git remote with authenticated token..."
cd "$LIB_DIR"

if [ ! -d ".git" ]; then
  git init -b "$BRANCH"
fi

# Configure authenticated remote URL
git remote remove origin 2>/dev/null || true
git remote add origin "https://${REPO_OWNER}:${TOKEN}@github.com/${REPO_OWNER}/${REPO_NAME}.git"

# Configure user
git config user.name "$REPO_OWNER"
git config user.email "71399545+${REPO_OWNER}@users.noreply.github.com"

# Fetch remote if existing to sync history
echo "🔄 Checking remote branch state..."
git fetch origin "$BRANCH" 2>/dev/null || true

# Add all files (ignoring items in .gitignore)
git add -A

if git diff-index --quiet HEAD -- 2>/dev/null; then
  echo "ℹ️ No uncommitted local changes."
else
  git commit -m "Upload all project Colab notebooks (Red Team suite, AI Stack, ComfyUI, Cloud Bridge)"
fi

echo "📤 Pushing to https://github.com/${REPO_OWNER}/${REPO_NAME} ($BRANCH)..."
if git push -u origin "$BRANCH"; then
  echo ""
  echo "============================================================"
  echo "🎉 SUCCESS! All notebooks are now live on GitHub:"
  echo "👉 https://github.com/${REPO_OWNER}/${REPO_NAME}"
  echo "============================================================"
  echo ""
  echo "To open in Google Colab directly from browser:"
  echo "1. Go to https://colab.research.google.com"
  echo "2. Click 'GitHub' tab"
  echo "3. Type '$REPO_OWNER' -> select '$REPO_NAME'"
  echo "============================================================"
else
  echo "⚠️ Direct push rejected, syncing with remote branch..."
  git pull origin "$BRANCH" --rebase || true
  git push -u origin "$BRANCH"
fi
