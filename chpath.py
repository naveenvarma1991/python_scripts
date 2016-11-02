#!/usr/bin/env python3

#!/usr/bin/python3

import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

import subprocess # just to call an arbitrary command e.g. 'ls'

# enter the directory like this:
with cd("/home/naveen"):
   # we are in ~/Library
   subprocess.call("ls")
