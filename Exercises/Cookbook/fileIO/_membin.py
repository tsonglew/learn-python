# -*- coding: utf-8 -*-
# 5.10


import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 1000000
with open('data', 'wb') as f:
    # seek(off, whence=0), pointer & starting index
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
len(m)
