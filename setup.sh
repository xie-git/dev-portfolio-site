#!/bin/bash

echo "🚀 Setting up Portfolio Website..."
echo

echo "📦 Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment. Make sure Python 3.8+ is installed."
    exit 1
fi

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📥 Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies."
    exit 1
fi

echo "✅ Setup complete!"
echo
echo "🌐 Starting the website..."
echo "💻 Open your browser and go to: http://localhost:5000"
echo "🔧 Admin panel available at: http://localhost:5000/admin"
echo
echo "⚡ Press Ctrl+C to stop the server"
echo

python run.py 