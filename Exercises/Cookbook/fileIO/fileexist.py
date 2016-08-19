# -*- coding: utf-8 -*-


import os

os.path.exists('/etc/passwd')
os.path.exists('/tmp/spam')


# Whether a file
os.path.isfile('/etc/passwd')
# Whether a dir
os.path.isdir('/etc/passwd')
# Whether link
os.path.islink('/usr/local/bin/python3')
# Get link to
os.path.realpath('/usr/local/bin/python3')


# file size
os.path.getsize('/etc/passwd')

os.path.getmtime('/etc/passwd')

import time
time.ctime(os.path.getmtime('/etc/passwd'))
