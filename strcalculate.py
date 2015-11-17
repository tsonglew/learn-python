#!/usr/bin/env python
# coding: utf-8


import time, sys


def calculate(iinput):


# Split into parts at lines
    iinput = iinput.lower().split()


# Transform into numercail values
    for str in iinput:
        m = 0
        for cha in str:
            if ord(cha) in range(97, 123):
                m += ord(cha) - 96
            else:
                pass
        print m

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Enter at lines
print "Enter the words and enter '.' to quit "
iinput = ''
for str in iter(raw_input, '.'):
    iinput += str + '\n'


# Start timing
t1 = time.time()


# Invoke the function
calculate(iinput)


# Stop timing
t2 = time.time()
print 'time:', (t2 - t1) * 1000, 'ms'


# Get the size of the function
print 'size:', sys.getsizeof(calculate), 'bytes'
