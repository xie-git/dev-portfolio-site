#!/bin/bash

# Portfolio Website Startup Script
# Usage: ./start_portfolio.sh

echo "🚀 Starting Michael Xie's Portfolio Website..."

# Check if screen session already exists
if screen -list | grep -q "portfolio"; then
    echo "❌ Portfolio is already running in screen session 'portfolio'"
    echo "💡 To view: screen -r portfolio"
    echo "💡 To stop: screen -r portfolio, then Ctrl+C"
    exit 1
fi

# Start new screen session
echo "📱 Starting new screen session 'portfolio'..."
screen -dmS portfolio python run.py

# Wait a moment for startup
sleep 3

# Check if it started successfully
if screen -list | grep -q "portfolio"; then
    echo "✅ Portfolio website started successfully!"
    echo ""
    echo "🌐 Access your website at: http://10.0.0.221:5005"
    echo "⚙️  Admin panel at: http://10.0.0.221:5005/admin"
    echo ""
    echo "📱 Screen commands:"
    echo "   - View session: screen -r portfolio"
    echo "   - Detach session: Ctrl+A, then D"
    echo "   - Stop portfolio: screen -r portfolio, then Ctrl+C"
    echo ""
    echo "📊 Check status: screen -list"
else
    echo "❌ Failed to start portfolio. Check for errors."
    exit 1
fi 