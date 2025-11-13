"""
Setup script for Tree and Roof Detection Pipelines
Checks that all required Python packages are installed,
and installs any missing dependencies automatically.
"""

import importlib
import subprocess
import sys

# --- Required dependencies ---
required_packages = [
    "numpy",
    "matplotlib",
    "open3d",
    "laspy",
    "scipy"
]

def install_if_missing(package: str):
    """Check if a package is installed; install it if missing."""
    module_name = package.replace("-", "_")
    try:
        importlib.import_module(module_name)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"⬇Installing {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    print("\n Setting up Python environment for Tree and Roof Detection Pipelines\n")
    for pkg in required_packages:
        install_if_missing(pkg)

    print("\nAll required dependencies are installed and ready.")

if __name__ == "__main__":
    main()
