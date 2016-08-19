# -*- coding: utf-8 -*-

import sys
sys.getfilesystemencoding()

with open('jalapae\xf1o.txt', 'w') as f:
    f.write('Spicy!')

import os
# Raw listing
os.listdir('.')

os.listdir(b'.')
