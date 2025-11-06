#!/usr/bin/env python3
"""
Simple script to start the Flask weather app server
"""
import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 50)
print("Starting Weather App Server...")
print("=" * 50)
print("\nServer will be available at: http://localhost:5000")
print("\nPress Ctrl+C to stop the server\n")
print("=" * 50)
print()

try:
    from app import app
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
except KeyboardInterrupt:
    print("\n\nServer stopped by user.")
except Exception as e:
    print(f"\nError starting server: {e}")
    import traceback
    traceback.print_exc()
    input("\nPress Enter to exit...")

