# -*- coding: utf-8 -*-


def myfun():
    return 1, 2, 3

a, b, c = myfun()
print('{a}{b}{c}'.format(a=a,b=b,c=c))
