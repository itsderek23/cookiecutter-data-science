#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import getopt

LONG_OPTIONS = ["nbenv="]

def parse_arguments(full_cmd_arguments):
    # Keep all but the first
    argument_list = full_cmd_arguments[1:]

    try:
        arguments, values = getopt.getopt(argument_list, "", LONG_OPTIONS)
    except getopt.error as err:
        # Output error, and return with an error code
        print (str(err))
        sys.exit(2)

    return arguments, values

def set_nbenv(arguments):
    nbenv = 'venv'
    for current_argument, current_value in arguments:
        if current_argument in ("--nbenv"):
            nbenv = current_value
    return nbenv

def exec(desc,cmd):
    """
    Executes the `cmd`, and prints `desc` prior to execution.
    If the exit code is nonzero, raises a `SystemExit` execption.
    """
    print(desc+"...", end="", flush=True)
    exit_code = os.system(cmd)
    if exit_code == 0:
        print("✓")
    else:
        print("⚠️  (exit code= {})".format(exit_code))
        raise SystemExit("💣 Aborting install. An error occurred running the install script.")

def exec_setup(nbenv):
    exec("Setting up venv","python3 -m venv {}/venv".format(os.getcwd()))
    exec("Installing Python dependencies via pip","venv/bin/pip install -r requirements.txt > /dev/null")
    if os.system('git rev-parse > /dev/null 2>&1') != 0:
        exec("Initializing the Git repo", "git init")
    if os.system("venv/bin/dvc status > /dev/null 2>&1") != 0:
        exec("Initializing DVC","venv/bin/dvc init > /dev/null")
    if not os.path.isfile(".git/hooks/post-checkout"):
        exec("Installing Git hooks into the DVC repository","venv/bin/dvc install > /dev/null")
    exec("Setting up venv for Jupyter Notebooks","venv/bin/python -m ipykernel install --user --name={}".format(nbenv))


if __name__ == "__main__":
    arguments, values = parse_arguments(sys.argv)
    nbenv = set_nbenv(arguments)
    exec_setup(nbenv)
    print("Install completed ✓.")
