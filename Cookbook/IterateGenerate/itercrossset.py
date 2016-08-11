# -*- coding: utf-8 -*-

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

# for x in a+b
for x in chain(a, b):
    print(x)
