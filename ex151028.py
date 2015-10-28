#!/usr/bin/env python

#  print and get mod
print "============Test==========="
print "Enter 1 to add 5 nums."
print "Enter 2 to get the average value of 5 nums."
print "Enter X to exit."


while True:
    (a, b, i) = (0, 0, 1)
    x = raw_input('Choose a mod above:')


# mod 1 , add the nums you enter
    if x == '1':
        while i < 6:
            try:
                a += float(raw_input('Please enter the NO.%d num:' % i))
                i += 1
            except:
                print "Please enter a num." # handle with incorrect entering


        print "The result is %s." % a


# mod 2 , get the average value of the nums you enter
    elif x == '2':
        while i < 6:
            try:
                b += float(raw_input('Please enter the NO.%d num:' % i))
                i += 1
            except:
                print "Please enter a num." # handle with incorrect entering


        print "The result is %s." % (b/ 5)


# mod 3 , exit
    elif x == 'X':
        break


# require for a correct entering
    else:
        print "Please choose a mod given above."
