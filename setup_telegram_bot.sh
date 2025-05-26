#!/bin/bash

# Telegram Movie Bot Setup Script
# This script helps you deploy and configure the Telegram Movie Bot integration

echo "🤖 Telegram Movie Bot - Setup & Deployment"
echo "=========================================="

# Check if in correct directory
if [ ! -f "telegram_movie_bot.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo ""
echo "📋 Pre-deployment checklist:"
echo "✅ telegram_movie_bot.py - Main bot handler"
echo "✅ telegram_webhook.py - Webhook endpoint"
echo "✅ movie_mood_generator.py - Mood generation logic"

# Deploy to Windmill
echo ""
echo "🚀 Deploying to Windmill..."
if command -v wmill &> /dev/null; then
    wmill sync push
    echo "✅ Scripts deployed to Windmill!"
else
    echo "⚠️  wmill CLI not found. Please deploy manually or install wmill CLI."
fi

echo ""
echo "🔗 Next Steps:"
echo ""
echo "1. WEBHOOK SETUP:"
echo "   • Go to your Windmill instance"
echo "   • Find the 'telegram_webhook' script"  
echo "   • Copy the webhook URL (should end with '/telegram_webhook')"
echo "   • Set this URL as your Telegram bot webhook:"
echo ""
echo "   curl -X POST \"https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook\" \\"
echo "        -H \"Content-Type: application/json\" \\"
echo "        -d '{\"url\": \"<YOUR_WINDMILL_WEBHOOK_URL>\"}'"
echo ""
echo "2. RESOURCE VERIFICATION:"
echo "   • Verify your Telegram resource 'u/philipgalebach/windmill_telegram_test2_bot' is configured"
echo "   • Verify your OpenRouter resource 'u/philipgalebach/thinner_openrouter' has the API key"
echo ""
echo "3. TESTING:"
echo "   • Send '/start' to your bot in Telegram"
echo "   • Send a movie title like 'Inception' or 'The Matrix'"
echo "   • Bot should respond with mood words!"
echo ""
echo "4. MONITORING:"
echo "   • Check Windmill logs if issues occur"
echo "   • Both scripts will log processing details"
echo ""
echo "🎬 Your Movie Mood Bot is ready! Send movie titles to get mood words! ✨"
