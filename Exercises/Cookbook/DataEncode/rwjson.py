# -*- coding: utf-8 -*-


import json

data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
        }
json_str = json.dumps(data)
data = json.loads(json_str)


# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read data
with open('data.json', 'r') as f:
    data = json.load(f)

## Python to JSON
## True      true
## False     false
## None      null

from urllib.request import urlopen
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
from pprint import pprint
pprint(resp)


s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)

print(json.dumps(data))
print(josn.dumps(data, indent=4))
