import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'SOWPODS.txt')

with open(filename, 'r') as f:
    SOWPODS = f.read().splitlines()