#-*- coding: utf-8 -*-
# 定义了一个装饰器 singleton，它返回了一个内部函数 getinstance，该函数会判断某
# 个类是否在字典 instances 中，如果不存在，则会将 cls 作为 key，cls(*args, **kw)
# 作为 value 存到 instances 中，否则，直接返回 instances[cls]。

from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1
