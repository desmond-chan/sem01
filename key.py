#!/usr/bin/env python3
import sys
import os

# Get the first argument after the script name
arg = sys.argv[1]

# Parse the argument
if "=" in arg:
    key, value = arg.split("=", 1)
    name = value
else:
    name = arg

# Print the name (same functionality as hello2.py)
print("My name is ", name)

# Check if key name from environment is 'ipf'
# Semaphore stores Key Store variables as environment variables
key_name = os.environ.get('SEMAPHORE_KEY_NAME', '')
key_login = os.environ.get('SEMAPHORE_KEY_LOGIN', '')

if key_name == 'ipf':
    print(f"Key Name: {key_name}")
    print(f"Login: {key_login}")
