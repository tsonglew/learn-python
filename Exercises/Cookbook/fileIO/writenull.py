# -*- coding: utf-8 -*-


with open('file2.txt', 'xt') as f:
    f.write('Hello\t')

## EQUAL
import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File Exists!')
