#!/usr/bin/env python3
"""
Simple test to verify the setup works
"""

import os
import sys
import subprocess
from pathlib import Path

def test_setup():
    """Test if we can set up and activate the virtual environment."""
    project_root = Path(__file__).parent
    venv_path = project_root / "venv"
    
    print("🧪 Testing virtual environment setup...")
    
    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    
    if not in_venv:
        print("📦 Not in virtual environment, setting up...")
        
        # Create virtual environment if it doesn't exist
        if not venv_path.exists():
            print("Creating virtual environment...")
            subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        
        # Determine the correct python executable
        if os.name == 'nt':  # Windows
            python_exe = venv_path / "Scripts" / "python.exe"
            pip_exe = venv_path / "Scripts" / "pip.exe"
        else:  # Unix/Linux/macOS
            python_exe = venv_path / "bin" / "python"
            pip_exe = venv_path / "bin" / "pip"
        
        print(f"Installing Flask...")
        subprocess.run([str(pip_exe), "install", "Flask==3.0.0"], check=True)
        
        print(f"Testing Flask import...")
        result = subprocess.run([str(python_exe), "-c", "import flask; print('Flask imported successfully!')"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Setup successful!")
            print(result.stdout.strip())
            return True
        else:
            print("❌ Setup failed!")
            print(result.stderr)
            return False
    else:
        print("✅ Already in virtual environment!")
        try:
            import flask
            print(f"✅ Flask {flask.__version__} is available!")
            return True
        except ImportError:
            print("❌ Flask not available in current environment!")
            return False

if __name__ == '__main__':
    success = test_setup()
    sys.exit(0 if success else 1) 