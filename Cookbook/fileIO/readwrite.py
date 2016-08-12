# -*- coding: utf-8 -*-


# Read the file as single string
with open('file.txt', 'rt') as f:
    data = f.read()

# Iterate over the lines of the file
with open('file.txt', 'rt', encoding='latin-1') as f:
    for line in f:
        print(line)

# Write chunks of text data
with open('file.txt', 'wt') as f:
    f.write('write line 1')
    f.write('write line 2')

# Redirected print statement
with open('file.txt', 'wt') as f:
    print('statement 1', file=f)
    print('statement 2', file=f)
