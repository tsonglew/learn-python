#!/usr/bin/env python
# coding: utf-8


class Bird(object):
    
    
    def __init__(self, nm, a):
        self.name = nm
        self.age = a


    def eat(self):
        print 'eat'


    def sing(self):
        print 'sing'


b = Bird('bird', 423)


print b.name
print b.age
b.eat()
b.sing()

class Lark(Bird):


    def eat(self):
        print 'eat2'


l = Lark('lark', 5423)


print l.name
print l.age
l.eat()
l.sing()
