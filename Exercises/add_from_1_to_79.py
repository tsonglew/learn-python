# coding: utf-8
# 记得加上上面这句哦

bingo = False
a=1
i=2

while bingo == False:
    a = a+i;
    i = i+1;

    if i >= 80:
        print "The answer is %d." % a
        bingo = True

   
