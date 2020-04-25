import os
import sys

setup = {{ cookiecutter.setup }}
if not setup:
    os.system("make setup")
