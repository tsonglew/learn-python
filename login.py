#!/usr/bin/env python
# coding: utf-8
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 A script to log in or register.
                                                                by Kasheem Lew
                                                                     2015.11.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~Define The Function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# the database of users' information
data = {'kasheem':'123'}


# the login function
def login():


# provide the user with 3 opportunities to log in
    count = 3
    while True:
        name = raw_input('Enter your name please:')
        if name not in data.keys():
            print 'Please register before logging in!'
            break


# start to log in
        while count > 0:
            pwd = raw_input('Enter your pwd please:')


# the password matches the name in the database
            if pwd == data[name]:
                print '\n',' '*20,'=================='
                print ' '*20,'||Welcome Back!!||'
                print ' '*20,'==================\n'
                break

# after a failed attempt to log in and you have to try again
            else:
                print 'WRONG PASSWORD!'
                count -= 1
                continue
        else:
            print 'You have used up all 3 opportunities!'
            break
        break


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# the register function
def hr():

    while True:
        print 'Register?(y/n)'
        choice = raw_input('>').lower()


# to get the information that the user entered
        if choice == 'y':
            value = raw_input('Choose a name:' )


            while True:
                key = raw_input('Enter your password:')

                # choose another number if the number already exists
                if key in data.keys():
                    print 'The name already exists! Try another one!'
                else:
                    break


            item = {key:value}
            data.update(item)

            break


# with no eager to start or have already got enough information
        elif choice == 'n':
           break 


# when received a choice which is not mentioned
        else:
            print 'Please choose from y and n!'


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Choice to Invoke~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


# make a choice whether to invoke the infomation managemant system
while True:
    print '''
           ---------------------
           ---------------------
           || Choose the MODE:||
           ||1.(L)ogin        ||
           ||2.(R)egister     ||
           ||3.(Q)uit         ||
           ---------------------
           ---------------------
          '''


    print 'Your choice is:'
    want = raw_input('>').lower()


# start the information manage system and quit after that
    if want == 'r':
        hr()
        print '\n',' '*20,'***********************'
        print ' '*20,'======================='
        print ' '*20,'||YOU CAN LOG IN NOW!||'
        print ' '*20,'======================='
        print ' '*20,'***********************\n'


# start the register system
    elif want == 'l':
        login()
        break


# quit and go to the terminal
    elif want == 'q':
        print ' '*20,'BYE BYE BYE BYE!!!!'
        break


# return to the front after receiving an answer which is neither y nor n
    else:
        
        print '\n',' '*20,'======================================'
        print ' '*20,'ERROR:CHOOSE FROM THE MODES MENTIONED!'
        print ' '*20,'======================================\n'

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
