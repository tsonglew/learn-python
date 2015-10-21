# coding: utf-8
# kick the ball,the game.py

from random import choice  # make a random choice from the list of the direction below   
 

direction = ['左边','右边','中间']  # make a list of dirctions
print "轮到你点球了，准备射向哪边？从下面几个中选择一个吧！"
print "左边,中间,右边"


your_choice = raw_input(">")  # assign what you choose to your_choice
print "你射向了 %s."%your_choice


com = choice(direction)  # computer makes the random choice
print "守门员扑向了 %s."%com


if your_choice != com:
    print "进了!"
else:
    print "可惜."  # print the consequense
