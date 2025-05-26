#!/bin/bash
# Quick setup script for Windmill OpenRouter test

echo "🚀 Setting up Windmill OpenRouter Test Project"
echo "=============================================="

# Check if wmill is installed
if ! command -v wmill &> /dev/null; then
    echo "❌ Windmill CLI not found. Installing..."
    deno install --unstable -A https://deno.land/x/wmill/main.ts
else
    echo "✅ Windmill CLI found"
fi

# Add workspace if not already added
echo ""
echo "🔗 Setting up workspace connection..."
wmill workspace add philip-galebach philip-galebach https://app.windmill.dev 2>/dev/null || echo "Workspace already exists"

# Initialize sync
echo ""
echo "🔄 Initializing Windmill sync..."
wmill sync init

echo ""
# Set up Python virtual environment
echo ""
echo "🐍 Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "📋 Next steps:"
echo "1. Get your OpenRouter API key from https://openrouter.ai"
echo ""
echo "2. Set up local testing (choose one):"
echo "   Option A - Create .env file:"
echo "     cp .env.example .env"
echo "     # Edit .env and add your actual API key"
echo ""
echo "   Option B - Export environment variable:"
echo "     export OPENROUTER_API_KEY='your-key-here'"
echo ""
echo "3. Test locally:"
echo "   source venv/bin/activate"
echo "   ./test_local.py"
echo ""
echo "4. Add API key to Windmill Cloud:"
echo "   - Go to https://app.windmill.dev"
echo "   - Select workspace 'philip-galebach'"
echo "   - Variables → New variable"
echo "   - Path: u/philipgalebach/openrouter_api_key"  
echo "   - Value: your-api-key"
echo ""
echo "5. Deploy to Windmill:"
echo "   wmill sync push"
echo ""
echo "6. Test in Windmill:"
echo "   wmill script run movie_mood_generator --data '{\"movie_title\": \"Inception\"}'"
echo ""
echo "🎉 Setup complete! Check README.md for detailed instructions."
