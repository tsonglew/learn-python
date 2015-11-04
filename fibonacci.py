#!/usr/bin/env python
# coding: utf-8
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Enter a num and a relevant num in Fibonacci Sequence will be returned
                                                                by Kasheem Lew
                                                                    2015.11.04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


a = 2
n1 = 1
n2 = 1


# which one do you want
count = input('>')


# print until the one you want is got
while a < count:
    n3 = n2
    n2 += n1
    n1 = n3
    a += 1
    continue
else:
    print n2
