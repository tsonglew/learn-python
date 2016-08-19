# -*- coding: utf-8 -*-

from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.sartwith('#'), f):
        print(line, end='')


# Known the specific index
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
