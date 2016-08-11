# -*- coding: utf-8 -*-

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# Standard slice would cast a TypeError
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)
