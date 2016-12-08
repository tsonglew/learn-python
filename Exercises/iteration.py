# -*- coding: utf-8 -*-

def get_a_index(string):
    for index, word in enumerate(string):
        if word == 'a':
            yield index

string = "this is a string"
indexs = get_a_index(string)

for i in indexs:
    print i

# indexs has iterated for one turn, next(indexs) this would trigger a
# StopIteration Error
# define a iterable object could solve this problem

class LoopIter(object):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for index, word in enumerate(self.data):
            if word == 'a':
                yield index

indexs = LoopIter(string)

for i in indexs:
    print i
for i in indexs:
    print i
