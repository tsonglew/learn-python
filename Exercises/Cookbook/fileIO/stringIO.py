# -*- coding: utf-8 -*-

import io

# BytesIO() for binary
s = io.StringIO()
s.write('Hello World\n')

print('This is a test', file=s)
# Get written data
s.getvalue()

# Wrap interface
s = io.StringIO('Hello\nWorld\n')
s.read(4)
s.read()
