#!/usr/bin/env python3
"""
Simple local runner for Windows
Just runs the portfolio directly without any setup complexity
"""
import os
import sys

# Set environment variables
os.environ['PORT'] = '5005'
os.environ['FLASK_DEBUG'] = 'True'

# Import and run the app
if __name__ == '__main__':
    from simple_app import run_simple_app
    run_simple_app() 