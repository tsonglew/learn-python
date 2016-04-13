#!/usr/bin/env python
# coding: utf-8
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 To display a text by showing 25 lines at a time
                                                                by Kasheem Lew
                                                                     2015.11.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# get the text to show and open it
filename = raw_input('Enter the name of the text:\n>')
f = open(filename)


# set a counter and start print
num = 0
for eachline in f:


# print until the counter get 25
    if num % 25 != 0:
        print eachline,
        num += 1


# when get the 25th line you have make a choice
    else:
        print 'Continue? \nPress C to continue , others to quit.'
        go = raw_input('>').lower().strip()    # lower the str and remove the useless blanks
        num += 1
        if go != 'c':    # entering other str will make you quit
            break
