#!/usr/bin/env python


import os
# the alphabet
alet = 'abcdefghijklmnopqrstuvwxyz'


# establish a dict
aDict = {}


# assign the characters in the alphabet
n = 1
for i in alet:
    aDict[i] = n
    n += 1


# input the str into a text
file = 'a.txt'
fobj = open(file, 'w')
while True:
    aLine = raw_input('Enter a line("." to quit): ').lower()
    if aLine != '.':
        fobj.write('%s%s' % (aLine, os.linesep))
    else:
        break
fobj.close()


# check the text by line and change the into numericial values
f = open(file, 'r')
for eachLine in f:
    m = 0
    for i in eachLine:
        if i in alet:
            m += aDict[i]
        else:
            pass
    print m
f.close()
