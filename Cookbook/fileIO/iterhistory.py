# -*- coding: utf-8 -*-


from functools import partial

RECORD_SIZE = 32

with open('somefile.data', 'rb') as f:
    # partial read certain nums of bytes from a file
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(i)
