#!/bin/bash
echo "🔧 Post-create script running..."

python -m venv /workspace/.venv 
. /workspace/.venv/bin/activate
pip install --upgrade pip

echo "✅ Setup complete!"
