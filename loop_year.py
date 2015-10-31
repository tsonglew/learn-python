#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  A function used to check whether a year is a leap year by Kasheem Lew
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# To define a function at first
def leap_year (n):
    m = n % 4
    p = n % 100
    k = n % 400
    #if ( m == 0 and p == 0) or ( m == 0 and p != 0):
    if (m == 0) or (p == 0 and k == 0):
        # 判断闰年:能被4整除，或者能被100整除且能被400整除
        print " It is a leap year."
    else:
        print " It is not a leap year."


# Make a choice whether to invoke the function or exit
print "============================================"
print "||Find out whether it is a leap year?(y/n)||"
print "============================================"
mode = raw_input('>')


# Choice to invoke the function is made
if mode == 'y':
    while True:
        try:
            year = int(raw_input('Please input the year you want to check:'))
            leap_year (year)
            break
        except:
            print "Input a year!"  # If the value is not invalid


# Choice to exit is made
elif mode == 'n':
    print "Bye Bye!"


# When you enter something which is neither y nor n.
else:
    print "ERROR!"
