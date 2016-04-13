def add(x):
    def do_add(value):
        return x + value
    return do_add

add_5 = add(5)
print add_5(1)
print add_5(2)
