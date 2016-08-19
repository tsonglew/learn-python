from collections import OrderedDict
import json

def order_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])

if __name__ == '__main__':
    order_dict()

# NOTICE
# a OrderedDict is twice the size of a normal dict, because of a linked 
# list served in it.
