#!/bin/bash

# Portfolio Website Stop Script
# Usage: ./stop_portfolio.sh

echo "🛑 Stopping Portfolio Website..."

# Check if screen session exists
if screen -list | grep -q "portfolio"; then
    echo "📱 Found portfolio session, stopping..."
    screen -S portfolio -X quit
    sleep 2
    
    # Verify it stopped
    if ! screen -list | grep -q "portfolio"; then
        echo "✅ Portfolio website stopped successfully!"
    else
        echo "❌ Failed to stop portfolio session"
        exit 1
    fi
else
    echo "💡 No portfolio session found running"
fi

echo "📊 Current screen sessions:"
screen -list 