#!/bin/bash
# ============================================================
# Script to initialize and push to GitHub
# Usage: bash scripts/github_push.sh <github-username> <repo-name>
# ============================================================

GITHUB_USERNAME=${1:-"your-username"}
REPO_NAME=${2:-"patient-case-similarity"}

echo "Initializing git repository..."
git init
git add .
git commit -m "Initial commit: AI-Powered Patient Case Similarity System

- React frontend with symptom input and disease prediction UI
- Flask backend with Random Forest ML model for disease classification
- OpenAI GPT-3.5 integration for AI dietary recommendations
- Treatment lookup with medication, cure methods, and hospital info
- Dataset with patient case records and treatment mappings
- Professional project structure with docs and setup scripts"

echo ""
echo "Next steps to push to GitHub:"
echo ""
echo "  1. Create a new repository on GitHub named: $REPO_NAME"
echo "     (Do NOT initialize with README — we already have one)"
echo ""
echo "  2. Run these commands:"
echo "     git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
echo "     git branch -M main"
echo "     git push -u origin main"
echo ""
echo "Done! Your repo will be live at:"
echo "  https://github.com/$GITHUB_USERNAME/$REPO_NAME"
