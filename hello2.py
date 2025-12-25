#!/usr/bin/env python3
import sys
arg = sys.argv[1]          # first argument after the script name
if "=" in arg:
    key, value = arg.split("=", 1)
    name = value
else:
    name = arg

print("My name is ", name)
