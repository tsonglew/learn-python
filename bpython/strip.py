#!/usr/bin/env python
# coding: utf-8


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Strip a string without string.strip()
                                                                by Kasheem Lew
                                                                     2015.11.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# Enter the string that is to be dealt with.
print '\n==================================='
print '|To Delete The Blanks in A String.|'
print '===================================\n'
original = raw_input('Enter the string please:\n>')
length = len(original)


# Check whether there are blanks in the string from the head
for i in range( 0,length + 1 ):
    if original[i] != ' ':
        lstrip = original[i:]
        length = len(lstrip)
        break
    else:
        pass


# Check whether there are blanks in the string form the tail
for i in range( 1,length + 1 ):
    if original[-1] != ' ':
        strip = lstrip
        break
    elif lstrip[-i] != ' ':
        strip = lstrip[:-i+1]
        break
    else:
        pass


# Print the final result and make it easy to compare
print 'Before:"',original,'"'
print 'After:"',strip,'"'
