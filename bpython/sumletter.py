# -*- coding: utf-8 -*-
#!usr/bin/env python
'''Calculate a series of letters given in a series of strings, \
        sum up the nums and return the result'''


# All the imports
import time


# User enter the string to calculate
sep = '.'
string = ''
for i in iter(raw_input, sep):
    string += i + '\n'


# Time to start
start = time.time()


# Ensure the letters in lowercase
lowercase_string = string.lower()


# Split the letters and store them in a list
aList = lowercase_string.split('\n')
del aList[-1]


for i in aList:
    aDict = {}
    sums = 0
    for eachletter in i:
        if ord(eachletter) in range(97, 123):
            aDict[(ord(eachletter)-96)] = eachletter
        else:
            aDict[0] = eachletter
    bList = list(aDict)
    sums = sum(bList)
    print sums


# Time to end
end = time.time()
print 'The program costs ', (end-start) * 1000, 'ms.'
