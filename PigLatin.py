#!/usr/bin/env python


# the vowel list
vowel = ['a', 'e', 'i', 'o', 'u']


# define the functions
def x(i):
    i = i[2:] + 'quay'
    print i,


def y(i):
    if i[0] == 'y':
        i = i[1:] + 'y'
    else:
        pass


    n = 0
    for m in i:
        if m in vowel :
            break
        else:
            n += 1
    i = i[n:] + i[:n] + 'ay'
    print i,

def z(i):
    i = i + 'hay'
    print i,

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

# get the string entered and seperate each word
a = raw_input('>').lower().split()


# check the words in sequence and tansform them in propriate ways
for i in a:


# if the word start with 'qu'
    if i[:1] == 'qu':
        x(i)


# if the word start with a vowel
    elif i[0] not in vowel:
        y(i)


# if the word does not start with a vowel
    elif i[0] in vowel:
        z(i)
