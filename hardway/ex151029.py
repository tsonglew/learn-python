#!/usr/bin/python


# define a function to get the greatest common divisor and the lowest common multiple
# the common divisor
def common_divisor (a, b):
    for i in range (1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            m  = i
    print "The greatest common divisor is %s ." % m


# the common multiple
def common_multiple (c, d):
    maxmum = max(c, d)
    while True:
        if  maxmum % c == 0 and maxmum % d == 0:
            n = maxmum
            break
        else:
            maxmum += 1
    print "The lowest common multiple is %s ." % n


# start
print "=================TEST======================"
print "|||Please enter 1 to invoke the function|||"
print "==========================================="
i = raw_input('>')


# invoking function
if i == '1':
       num1 = int(raw_input('Enter the first num:\n'))
       num2 = int(raw_input('Enter the second num:\n'))
       common_divisor (num1, num2)
       common_multiple (num1, num2)
