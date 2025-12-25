import os

myname = os.environ.get('myname', 'Default Name')  # Use 'myname' as the key (from the survey Name field)
print('My Name is ', myname)
