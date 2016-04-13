def decorator_with_params_and_func_args(arg_of_decorator):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            print 'begin'
            func(*args, **kwargs)
            print 'end'
            print arg_of_decorator, func, args, kwargs
        return handle_args
    return handle_func


@decorator_with_params_and_func_args("123")
def foo(a, b = 2):
    print "Content"


foo(1, b = 3)
