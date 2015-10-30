#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  A function used to check whether a year is a loop year by Kasheem Lew
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# To define a function at first
def loop_year (n):
    m = n % 4
    p = n % 100
    if ( m == 0 and p == 0) or ( m == 0 and p != 0):
        print " It is a loop year."
    else:
        print " It is not a loop year."


# Make a choice whether to invoke the function or exit
print "============================================"
print "||Find out whether it is a loop year?(y/n)||"
print "============================================"
mode = raw_input('>')


# Choice to invoke the function is made
if mode == 'y':
    while True:
        try:
            year = int(raw_input('Please input the year you want to check:'))
            loop_year (year)
            break
        except:
            print "Input a year!"  # If the value is not invalid


# Choice to exit is made
elif mode == 'n':
    print "Bye Bye!"


# When you enter something which is neither y nor n.
else:
    print "ERROR!"
