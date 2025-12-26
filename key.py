# Print all Key Store environment variables from Semaphore
print("=== Semaphore Key Store Information ===\n")

# Get all environment variables
env_vars = os.environ

# Look for key-related environment variables
# Semaphore typically uses patterns like:
# - SEMAPHORE_KEY_NAME
# - SEMAPHORE_KEY_LOGIN
# - Or with key ID/name suffix for multiple keys

key_info = {}
for key, value in env_vars.items():
    if 'KEY' in key.upper() and 'SEMAPHORE' in key.upper():
        key_info[key] = value

if key_info:
    print("Found Key Store variables:")
    for key, value in sorted(key_info.items()):
        print(f"{key}: {value}")
else:
    print("No Key Store variables found in environment.")
    print("\nNote: Key Store variables are only available during task execution")
    print("when keys are associated with the task in Semaphore UI.")

print("\n=== All Environment Variables (for debugging) ===")
for key in sorted(env_vars.keys()):
    if 'SEMAPHORE' in key or 'KEY' in key:
        print(f"{key}={env_vars[key]}")
