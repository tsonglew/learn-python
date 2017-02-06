#-*- coding: utf-8 -*-
# 元类（metaclass）可以控制类的创建过程，它拦截类的创建, 修改类的定义, 返回修改后的类

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Python2
class MyClass(object):
    __metaclass__ = Singleton

# Python3
class MyClass(metaclass=Singleton):
    pass
