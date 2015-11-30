#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
decorator to accept any amount of arguments
'''


def decorator(func):
    def inner(*args, **kwargs):
        print 'Arguments are', args, kwargs
        return func(*args, **kwargs)
    return inner
