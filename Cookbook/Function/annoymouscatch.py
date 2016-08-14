# -*- coding: utf-8 -*-

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))
print(b(10))
print('Both return 30')
# x is a free parameter and will be bound when executed
