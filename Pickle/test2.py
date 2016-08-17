# -*- coding: utf-8 -*-


try:
    import cPickle as pickle
except:
    import pickle
import pprint


data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'BEFORE:',
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print 'AFTER:',
pprint.pprint(data2)


# 新构造的对象和原对象相同，但并非同一对象
print 'SAME?:', (data1 is data2)
print 'EQUAL?:', (data1 == data2)
