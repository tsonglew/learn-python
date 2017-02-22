class Descriptor(object):
    def __init__(self, name="default", value="default"):
        self.name = name
        self.value = value

    def __get__(self, obj, objtype):
        print "get from descriptor {}".format(self.name)
        return self.value

    def __set__(self, obj, val):
        print "set to descriptor {}".format(self.name)
        self.value = val


class MyClass(object):
    descriptor = Descriptor()

    def __repr__(self):
        return "<MyClass>"
