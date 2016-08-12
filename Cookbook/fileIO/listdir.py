# -*- coding: utf-8 -*-


import os
names = os.listdir('somedir')

# Get files
names = [name for name in os.listdir('somedir')
        if os.path.isfile(os.path.join('somedir', name))]

# Get dirs
dirnames = [name for name in os.listdir('somedir')
        if os.path.isdir(os.path.join('somedir', name))]

pyfiles = [name for name in os.listdir('somedir')
        if name.endwith('.py')]

# Match
import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
        if fnmatch(name, '*.py')]
