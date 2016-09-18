#-*- coding: utf-8 -*-


def common(*args, **kwargs):
    a = args
    def _common(func):
        def _deco(*args, **kwargs):
            print 'args:', args, a
            return func(*args, **kwargs)
        return _deco
    return _common

@common('c')
def test(p):
    print p

test(10)
