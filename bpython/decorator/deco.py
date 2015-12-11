def decorator(func):
    print 'hello'
    return func


@decorator
def foo():
    pass


foo()
