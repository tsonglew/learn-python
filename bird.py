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


Bird.name
Bird.age
b.eat()
b.sing()

class Lark(Bird):


    def eat(self):
        print 'eat2'


l = Lark()


Lark.name
Lark.age
l.eat()
l.sing()
