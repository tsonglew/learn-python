# -*- coding: utf-8 -*-

# Read binary
with open('file.bin', 'rb') as f:
    data = f.read()

# Write binary
with open('file.bin', 'wb') as f:
    f.write(b'Hello World')

with open('file.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    # Read into memory
    f.readinto(a)
