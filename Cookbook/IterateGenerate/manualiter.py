#-*- coding: utf-8 -*-

def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

def manual_ter2():
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')  # end default: '\n'


items = [1, 2, 3]
# Get the iterator
it = iter(items)
next(it)
next(it)
next(it)
