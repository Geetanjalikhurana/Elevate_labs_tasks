"""
run_app.py
Convenience script to launch the Streamlit app or test parsing logic.
"""

import sys
import subprocess

def main():
    print("Starting Smart Resume Parser Streamlit Application...")
    cmd = ["streamlit", "run", "app.py"]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
