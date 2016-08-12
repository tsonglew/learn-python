# -*- coding: utf-8 -*-


import os
path = '/Users/kasheemlew/Data/data.csv'

os.path.basename(path)
os.path.dirname(path)

os.path.join('tmp', 'data', os.path.basename(path))


# Expand
path = '~/Data/data.csv'
os.path.expanduser(path)

# Split extension
os.path.splitext(path)
