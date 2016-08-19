from random import randint
num = randint(1,20)


print "Guess what do I think?"
bingo = False


while bingo == False:
    answer = input()
    
    
    if answer > num:
        print "Too big."

    if answer < num:
        print "Too small."

    if answer == num:
        print "BINGO!"
        bingo = True


print " Bye bye!~"
