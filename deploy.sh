#!/bin/bash

# Portfolio Deployment Script for Linux Server
# Usage: ./deploy.sh [production|development]

MODE=${1:-development}
PORT=${2:-5005}

echo "🚀 Deploying Michael Xie Portfolio..."
echo "Mode: $MODE"
echo "Port: $PORT"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ app.py not found. Please run this script from the project root."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Set environment variables for production
if [ "$MODE" = "production" ]; then
    export SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
    export FLASK_ENV=production
    export FLASK_DEBUG=False
    
    echo "🛡️ Production mode: Security key generated"
    
    # Run with Gunicorn (production WSGI server)
    echo "🚀 Starting production server on port $PORT..."
    echo "💻 Visit: http://$(hostname -I | awk '{print $1}'):$PORT"
    echo "⚡ Press Ctrl+C to stop the server"
    
    gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 app:app
else
    # Development mode
    export FLASK_ENV=development
    export FLASK_DEBUG=True
    
    echo "🔧 Development mode: Debug enabled"
    echo "🚀 Starting development server on port $PORT..."
    echo "💻 Visit: http://localhost:$PORT or http://10.0.0.221:$PORT"
    echo "⚡ Press Ctrl+C to stop the server"
    
    python3 app.py
fi 