#!/usr/bin/env python
#-*- coding: utf-8 -*-


class MoneyFmt(object):

    # constructor
    def __init__(self, value = 0.0):
        self.value = float(value)
        self.__str__()

    # allow updates
    def update(self, value = None):
        if value is not None:
            try:
                self.value = float(value)
            except:
                pass

    # display as a float
    def __repr__(self):
        return repr(self.value)

    # formatted display
    def __str__(self):
        val = self.dollarize(self.value)
        return val

    # boolen
    def __nonzero__(self):
        return self.value

    def dollarize(self, value):
        val = str(round(abs(value), 2)).split('.')

        # whether minus sign
        if value < 0:
            sym = 1
        else:
            sym = 0

        n_value = self.insertSym(val[0])
        return '-'*sym + '$' + n_value + '.' + val[1]

    def insertSym(self, value):
        num = len(value) % 3
        List = list(value)

        if num > 0:
            List.insert(num, ',')

        for i in range(1, len(value) / 3):
            List.insert(i * 3 + i + num, ',')

        return  '.'.join(List)

    def __getattr__(self, attr):
        return getattr(self.value, attr)  # print self.value or not find
