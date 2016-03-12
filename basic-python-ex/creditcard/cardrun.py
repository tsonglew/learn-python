#!/usr/bin/env python
# coding: utf-8


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Credit Card Management.
                                                                by Kasheem Lew
                                                                     2015.11.8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


'''
~~~~~~~~~~~~~~~~~~~~~~Define--The--Function~~~~~~~~~~~~~~~~~~~~~~~
'''


# change the input value into float and return a waring when it goes wrong
def safe_float(obj):
    try:
      retval = float(obj)
    except (ValueError, TypeError), diag:
      retval = str(diag)
    return retval


'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


# add the content in carddata.txt into cardlog.txt
def main():
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError, e:
        log.write('no txns this month\n')
        log.close()
        return


    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')


    for eachTxn in txns:
        result = safe_float(eachTxn)


# the result's type is float,and it will be written in
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')


# the result's type is not float,then it will be ignored
        else:
            log.write('ignored: %s' % result)
    print '$%.2f (new balance)' % (total)
    log.close()


'''
~~~~~~~~~~~~~~~~~~~~Invoke--The--Function~~~~~~~~~~~~~~~~~~~~~
'''


main()
