#!/bin/env python3
""" Installs this program and related dependences """

import sys
import os
import shutil

print("THIS WILL ONLY WORK ON *NIX-BASED OPERATING SYSTEMS")
print("IF ON WINDOWS, READ README\n\n")
print("SUDO IS REQUIRED TO INSTALL!")
NULL = input("CTRL+C TO CANCEL\nPRESS 'ENTER' TO CONTINUE!")

print("\n\nINSTALLING\n\n")
os.chmod("./aldl.py", 0o755)

print("\n\nMoving to /usr/bin/\n\n")
shutil.copy("./aldl.py", "/usr/bin/aldl")



