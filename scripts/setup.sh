#!/bin/bash
# ============================================================
# Setup Script for AI-Powered Patient Case Similarity System
# ============================================================

set -e

echo "========================================"
echo "  Patient Case Similarity System Setup"
echo "========================================"

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $PYTHON_VERSION"

# Check Node version
NODE_VERSION=$(node --version 2>&1)
echo "✓ Node version: $NODE_VERSION"

# ---- Backend Setup ----
echo ""
echo ">>> Setting up Backend..."

cd "$(dirname "$0")/../backend"

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate and install dependencies
source venv/bin/activate
pip install --quiet -r ../requirements.txt
echo "✓ Python dependencies installed"

# Check for OpenAI key
if [ -z "$OPENAI_API_KEY" ]; then
    echo ""
    echo "⚠️  WARNING: OPENAI_API_KEY environment variable is not set."
    echo "   The AI chat feature will not work without it."
    echo "   Set it with: export OPENAI_API_KEY='your_key_here'"
fi

deactivate

# ---- Frontend Setup ----
echo ""
echo ">>> Setting up Frontend..."

cd "../frontend"
npm install --silent
echo "✓ Node.js dependencies installed"

echo ""
echo "========================================"
echo "  Setup complete!"
echo "========================================"
echo ""
echo "To start the application:"
echo ""
echo "  1. Start the backend:"
echo "     cd backend && source venv/bin/activate && python app.py"
echo ""
echo "  2. Start the frontend (new terminal):"
echo "     cd frontend && npm start"
echo ""
echo "  Frontend: http://localhost:3000"
echo "  Backend:  http://localhost:5000"
