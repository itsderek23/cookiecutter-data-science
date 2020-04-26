#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def exec(desc,cmd):
    print(desc+"...", end="", flush=True)
    exit_code = os.system(cmd)
    if exit_code == 0:
        print("✓")
    else:
        print("⚠️  (exit code= {})".format(exit_code))
        raise SystemExit("💣 Aborting install. An error occurred running the install script.")

exec("Setting up venv","python3 -m venv venv")
exec("Installing Python dependencies via pip","source venv/bin/activate ; pip install -r requirements.txt > /dev/null")
exec("Initializing the Git repo", "git init")
exec("Initializing DVC","source venv/bin/activate ; dvc init > /dev/null")
exec("Installing Git hooks into the DVC repository","source venv/bin/activate ; dvc install > /dev/null")
print("👍 Install completed.")
