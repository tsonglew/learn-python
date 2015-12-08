#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Bird(object):

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry == True:
            print 'Aaaah..'
            self.hungry = False
        else:
            print 'No, thanks.'


class SongBird(Bird):

    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print self.sound

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

b = Bird()
print 'Hello, Bird b, want something to eat?'
b.eat()
print 'Anymore?'
b.eat()

print ' '

s = SongBird()
print 'Hello, SongBird s, want something to eat?'
s.eat()
print 'Anymore?'
s.eat()
print 'You have eaten so much, sing a song!'
s.sing()
