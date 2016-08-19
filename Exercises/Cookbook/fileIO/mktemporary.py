# -*- coding: utf-8 -*-


from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Testing\n')

    # seek back to beginning
    f.seek(0)
    data = f.read()

# with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f

# Named temporary file
from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
        print('filename is:', f.name)
