"""
Cross-platform setup script for face_blur project.
Creates a virtual environment named 'face_blur' and installs dependencies.
"""

import subprocess
import sys
import os
import venv

VENV_NAME = "face_blur"

def create_venv():
    print(f"Creating virtual environment '{VENV_NAME}'...")
    venv.create(VENV_NAME, with_pip=True)
    print("Virtual environment created.")

def get_pip_path():
    if sys.platform == "win32":
        return os.path.join(VENV_NAME, "Scripts", "pip")
    return os.path.join(VENV_NAME, "bin", "pip")

def install_requirements():
    pip = get_pip_path()
    print("Installing dependencies from requirements.txt...")
    subprocess.check_call([pip, "install", "-r", "requirements.txt"])
    print("Dependencies installed successfully.")

def get_activate_hint():
    if sys.platform == "win32":
        return f"{VENV_NAME}\\Scripts\\activate"
    return f"source {VENV_NAME}/bin/activate"

if __name__ == "__main__":
    create_venv()
    install_requirements()
    print(f"\nSetup complete. Activate the environment with:\n  {get_activate_hint()}")
