import os
path = './test/test.py'
directory = os.path.dirname(path)

if not os.path.exists(directory):
    os.makedirs(directory)

with open(path, 'w') as f:
    f.write('print(\'hello\')')
