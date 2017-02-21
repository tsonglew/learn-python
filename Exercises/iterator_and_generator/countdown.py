class countdown(object):
    """class iterator countdown"""
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def next(self):
        if self.count <= 0:
            raise StopIteration
        t = self.count
        self.count -= 1
        return t


def countdown2(n):
    while n > 0:
        yield n
        n -= 1


def countdown3(n):
    print "Executing countdown ..."
    while n > 0:
        yield n
        n -= 1
