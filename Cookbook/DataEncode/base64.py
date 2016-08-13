# -*- coding: utf-8 -*-

s = b'Hello'
import base64

# Encode as base64
a = base64.b64encode(s)
print(a)

# Decode from base64
s = base64.b64decode(a)
print(s)
