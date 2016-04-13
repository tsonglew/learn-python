#!/usr/bin/env python
# coding: utf-8
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 A script to read or write a file
                                                                by Kasheem Lew
                                                                    2015.11.05
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

'''
~~~~~~~~~~~~~~~~~~~~~~Read a file~~~~~~~~~~~~~~~~~~~~~~
'''


# enter the name of the file you want to read and open the file
filename = raw_input("Enter the name:")
f = open(filename,'r')


# print the file
for eachline in f:
    print eachline,
f.close


'''
~~~~~~~~~~~~~~~~~~~~~~Write a file~~~~~~~~~~~~~~~~~~~~~
'''


# name the new file
filename2 = raw_input('Enter file name:')
fobj = open(filename2, 'w')


# write or quit writing
while True:
    aLine = raw_input("Enter a line('.' to quit)")
    if aLine != '.':
        fobj.write('%s%s' % ( aLine, os.linesep))
    else:
        break
fobj.close
