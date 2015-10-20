def isEqual(num1,num2):
    if num1<num2:
        print 'too small'
        return False
    if num1>num2:
        print 'too big'
        return False
    if num1==num2:
        print 'BINGO'
        return True

from random import randint
num = randint(1,100)
print 'Guess what I think?'
bingo = False
while bingo == False:
    answer = input()
    bingo = isEqual(answer,num)

