# -*- coding: utf-8 -*-


try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO


class SimpleObject(object):
    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return


data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))


# 模拟文件
out_s = StringIO()

for o in data:
    print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
    pickle.dump(o, out_s)
    # 清除内部缓存区
    out_s.flush()

in_s = StringIO(out_s.getvalue())

while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'READ: %s (%s)' % (o.name, o.name_backwards)
