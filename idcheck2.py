#!/etc/bin/env python


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A script to check whether the characters and nums entered is legal.
                                                  by Kasheem Lew
                                                  2015.10.31
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


import string


# set a range to check
alphas = string.letters + '_'
alnums = alphas + string.digits
iden = raw_input('Identifier to check:')


# when something is entered
if len(iden) > 0:


    # the first element dosen't meet the requirement
    if iden[0] not in alphas:
        print "ERROR:first char must be alphabetic."


    # the first element is qualified
    else:
        if len(iden) > 1:
            # check the element left one by one
            for eachChar in iden[1:]:
                if eachChar not in alnums:
                    print "ERROR:others must be alnum."
                    break


        # with only one element to check
            else:
                import keyword
                if iden not in keyword.kwlist:
                    print "OK."
                else:
                    print "ERROR:keyword name!"


# nothing is entered
else:
    print "ERROR:no identifier entered!"
