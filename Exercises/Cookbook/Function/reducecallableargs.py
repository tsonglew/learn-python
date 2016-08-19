# -*- coding: utf-8 -*-

def spam(a, b, c, d):
    print(a, b, c, d)


from functools import partial
s1 = partial(spam, 1)
print(s1(2, 3, 4))
print(s1(4, 5, 6))

s2 = partial(spam, d=42)
print(s2(1, 2, 3))
print(s2(4, 5, 5))
