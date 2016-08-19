# -*- coding: utf-8 -*-

import os.path

def read_into_buffer(filename):
    # allocate memory for array
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        # fill data
        f.readinto(buf)
    return buf


# Same Size
record_size = 32

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
