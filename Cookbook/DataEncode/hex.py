# -*- coding: utf-8 -*-

# Initial byte string
s = b'Hello'
# Encode as hex
import binascii
h = binascii.b2a_hex(s)
print(h)

# Decode to bytes
s = binascii.a2b_hex(h)
print(s)

import base64
h = base64.b16encode(s)
print(h)
s = base64.b16decode(h)
print(s)

