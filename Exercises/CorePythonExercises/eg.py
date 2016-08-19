#!/usr/bin/env python


class Parent(object):


    def altered(self):
        print 'Parent altered():'


    def override():
        print 'Parent override()'


class Child(Parent):


    def altered(self):
        super(Child, self).altered()


    def override():
        pass


dad = Parent()
son = Child()


dad.altered()
son.altered()


dad.override()
son.override()
