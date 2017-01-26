import os

with open('ex.txt') as f:
    stat = os.stat(f.fileno())
    os.chmod(f.fileno(), 0o640)
