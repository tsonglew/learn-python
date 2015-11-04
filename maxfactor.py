#!/usr/bin/env python
# coding: utf-8
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 A script to show the num's max factor in the range user provides
                                                                by Kasheem Lew
                                                                    2015.11.04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# set a range to find the max factor for
print 'Enter the range you want!'
a = input('Start from:')
b = input('End at:') + 1


# start to check at sequence
for num in range( a , b , 1 ):
    half = num / 2


    while half > 1:


# aquire the max factor
        if num % half == 0:
            print 'The max factor of', num , 'is',half,'.'
            break
        else:
            half -= 1

# no more factors
    else:
        print num,'is prime.'
