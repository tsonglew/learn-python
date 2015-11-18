#!usr/bin/env python
# coding: utf-8


# Import modules
from operator import add, sub
from random import randint, choice


# Set a dictionary to choose method from
ops = {'+': add, '-': sub}
# Two chances for trying
MAXTRIES = 2


def doprob():
    # Choose 'add' or 'sub'
    op = choice('+-')
    # Choose the nums to operate
    nums = [randint(1, 10) for i in range(2)]
    # Sort the nums from the biggest to the smallest(in case of answers tinier
    # than 0
    num.sort(reverse = True)
    # Computer calculate the answer
    ans = ops[op](*nums)


    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0


    while True:
            try:
                # Get the correct answer
                if int(raw_input(pr)) == ans:
                    print 'correct'
                    break
                # No more chances for trying
                if oops == MAXTRIES:
                    print 'answer\n %s %d' % (pr, ans)
                # Incorrect answer will add the chances you have tried
                else:
                    print 'incorrect...try again'
                    oops += 1


            except (KeyboardInterrupt, EOFError, ValueError):
                print 'invalid input... try again'


def main():
    while True:
        doprob()
        # Entering 'n' and invalid input will lead to a break
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
