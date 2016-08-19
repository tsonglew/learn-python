# -*- coding: utf-8 -*-
# Coming across `surrogates not allowed

import sys

def bad_filename(filename):
    return repr(filename)[1:-1]

def bad_filename2(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
