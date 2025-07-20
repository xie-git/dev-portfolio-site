#!/usr/bin/env python3
"""
Simple local runner for Windows
Just runs the portfolio directly without any setup complexity
"""
import os
from app import create_app

# Set environment variables for local debugging
os.environ['FLASK_DEBUG'] = 'True'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
