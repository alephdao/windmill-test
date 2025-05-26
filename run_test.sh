#!/bin/bash
# Convenience script to activate venv and run local tests

echo "🔋 Activating virtual environment..."
source venv/bin/activate

echo "🧪 Running local tests..."
./test_local.py

echo ""
echo "💡 To manually test different movies:"
echo "python movie_mood_generator.py"
echo ""
echo "🚀 To deploy to Windmill:"
echo "wmill sync push"
