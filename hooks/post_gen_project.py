import os
import sys

setup = {{ cookiecutter.setup }}
if setup:
    os.system("make setup")
