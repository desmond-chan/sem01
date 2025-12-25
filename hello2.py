#!/usr/bin/env python3
import os

# Semaphore turns every survey variable into an env-var.
name = os.environ["name"]          # raises KeyError if not set
print("My name is", name)
