#!/usr/bin/env python
# coding: utf-8
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 A script to manage your employees' information including numbers and names.
                                                                by Kasheem Lew
                                                                     2015.11.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~Define The Function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# define the function
def hr():


    print '==============================================================================='
    print '||I will help you with the problem the messy information about your employees||'
    print '==============================================================================='


# create and initialize a dict
    data = {}


# make a choice whether to start (continue) the system
    while True:
        print 'Do you have any information about the staff to update?(y/n)'
        choice = raw_input('>').lower()
        # raw_input 默认输入的就是字符串,所以不用加str
        # 同样,输入数字的时候 input 就行了


# to get the information that the user entered
        if choice == 'y':
            key = raw_input('Enter your name:')


            while True:
                value = input('Enter your number:')
                # choose another number if the number already exists
                if value in data.values():
                    print 'The number already exists! Try another one!'
                else:
                    break


            item = {key:value}
            data.update(item)


# with no eager to start or have already got enough information
        elif choice == 'n':
            print 'No more information.'
            break


# when received a choice which is not mentioned
        else:
            print 'Please choose from y and n!'


# print the items that is already sorted(according to the employees' name)
    for key,value in sorted(data.items()):
        print 'Name:',key,'No.',value


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Choice to Invoke~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# make a choice whether to invoke the infomation managemant system
while True:
    print 'Do you want to start the information management system?(y/n)'
    print 'Your choice is:'
    want = raw_input('>').lower()


# start the information manage system and quit after that
    if want == 'y':
        hr()
        break


# quit and go to the terminal
    elif want == 'n':
        print 'You must be tricking me by running this!BYE BYE!'
        break


# return to the front after receiving an answer which is neither y nor n
    else:
        print 'ERROR:why not choose from y and n?'


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
