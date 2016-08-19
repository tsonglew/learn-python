def decorator_with_params(arg_of_decorator): # with arguments in decorator
    print arg_of_decorator

    # return the function
    def newDecorator(func):
        print func
        return func
    return newDecorator


@decorator_with_params("deco_args")
def foo():
    pass


foo()
