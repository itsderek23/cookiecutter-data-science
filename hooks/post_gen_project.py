import os
import sys

setup = {{ cookiecutter.setup }}

if setup:
    print("Running setup...")
    exit_code = os.system("scripts/install.py")
    if exit_code > 0:
        sys.exit(exit_code)
else:
    print("Skipping project setup. You can do this later by running `scripts/install.py`.")
