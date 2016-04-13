#!/usr/bin/env python
# coding: utf-8


# the vowel list
vowel = ['a', 'e', 'i', 'o', 'u']


# define the functions
# if the word start with 'qu'
def x(i):
    if i[:2] == 'qu':
        i = i[2:] + 'quay'
        print i,
    else:
        pass


# if the word does not start with a vowel
def y(i):
    if i[0] not in vowel:
        if i[0] == 'y':
            i = i[1:] + 'y'
        else:
	        n = 0
	        for m in i:
                if m in vowel.append('y'):
		            break
		        else:
		            n += 1
		    i = i[n:] + i[:n] + 'ay'
		    print i,
    else:
    	pass


# if the word  start with a vowel
def z(i):
    if i[0] in vowel:	
        i = i + 'hay'
        print i,

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

# get the string entered and seperate each word
a = raw_input('>').lower().split()


# check the words in sequence and tansform them in propriate ways
for i in a:
    x(i)
    y(i)
    z(i)
