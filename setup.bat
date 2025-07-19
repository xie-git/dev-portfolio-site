@echo off
echo 🚀 Setting up Portfolio Website...
echo.

echo 📦 Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ Failed to create virtual environment. Make sure Python is installed.
    pause
    exit /b 1
)

echo 🔧 Activating virtual environment...
call venv\Scripts\activate

echo 📥 Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies.
    pause
    exit /b 1
)

echo ✅ Setup complete!
echo.
echo 🌐 Starting the website...
echo 💻 Open your browser and go to: http://localhost:5000
echo 🔧 Admin panel available at: http://localhost:5000/admin
echo.
echo ⚡ Press Ctrl+C to stop the server
echo.

python run.py 