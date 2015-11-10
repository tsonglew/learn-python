#!/usr/bin/env python
# coding: utf-8


class Bird(object):
    name = 'bird'
    age = 123


    def eat(self):
        print 'eat'


    def sing(self):
        print 'sing'


b = Bird()


print b.name
print b.age
b.eat()
b.sing()

class Lark(Bird):


    def eat(self):
        print 'eat2'


l = Lark()


print l.name
print l.age
l.eat()
l.sing()
