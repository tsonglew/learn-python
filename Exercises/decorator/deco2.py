def decorator_func_args(func):
    # handle with the arguments
    def handle_args(*args, **kwargs):
        print 'begin'
        # invoke the func
        func(*args,**kwargs)
        print 'end'
    return handle_args


@decorator_func_args
def foo(a, b = 2):
    print a, b


foo(1)
