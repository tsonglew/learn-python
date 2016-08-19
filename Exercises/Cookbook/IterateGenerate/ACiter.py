# -*- coding: utf-8 -*-

items = ['a', 'b', 'c']
###
### PERMUTATIONS
from itertools import permutations
for p in permutations(items):
    print(p)

# With optional length
for p in permutations(items, 2):
    print(p)

### COMBINATIONS
from itertools import combinations
for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

### COMBINATIONS WITH REPLACEMENT
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
