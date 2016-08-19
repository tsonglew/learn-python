# -*- coding: utf-8 -*-

# Read
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# Write
import gzip
# compress level default=9
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
