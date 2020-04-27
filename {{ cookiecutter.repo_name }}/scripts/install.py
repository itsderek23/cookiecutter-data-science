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
print("python---")
print(os.system("which python"))
print("pwd---")
print(os.system("pwd"))
print("cwd---")
print(os.getcwd())
print("ls -lath---")
print(os.system("ls -lath"))
exec("Setting up venv","python -m venv {}/venv".format(os.getcwd()))
os.system("touch blah.txt")
print("AFTER venv: ls -lath---")
print(os.system("ls -lath"))
print("venv ls ---")
print(os.system("ls venv/bin/ -lath"))
exec("Installing Python dependencies via pip","venv/bin/pip install -r requirements.txt > /dev/null")
if os.system('git rev-parse > /dev/null 2>&1') != 0:
    exec("Initializing the Git repo", "git init")
if os.system("venv/bin/dvc status > /dev/null 2>&1") != 0:
    exec("Initializing DVC","venv/bin/dvc init > /dev/null")
if not os.path.isfile(".git/hooks/post-checkout"):
    exec("Installing Git hooks into the DVC repository","venv/bin/dvc install > /dev/null")
print("👍 Install completed.")
