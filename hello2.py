import os
print("Environment vars:", os.environ)
myname = os.environ.get('myname', 'Default Name')
print('My Name is ', myname)
