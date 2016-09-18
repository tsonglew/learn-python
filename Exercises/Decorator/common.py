#-*- coding: utf-8 -*-

def common(func):
    def _deco(*args, **kwargs):
        print 'args:', args
        return func(*args, **kwargs)
    return _deco

@common
def test(p):
    print(p)

test(1)
