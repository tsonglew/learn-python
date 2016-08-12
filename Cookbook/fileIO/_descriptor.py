# -*- coding: utf-8 -*-
# 5.18

import os
# Open descriptor
fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

f = open(fd, 'wt')
f.write('hello world\n')
f.close()
