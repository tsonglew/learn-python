# -*- coding: utf-8 -*-
import attr
import pprint

@attr.s
class A(object):
    x = attr.ib()
    y = attr.ib()

insOfA = A(1, 2)

# to JSON
attr.asdict(A(1, 2))
pprint.pprint(attr.fields(A))




from attr.validators import instance_of
@attr.s
class B(object):
    x = attr.ib(validator=instance_of(float))
    y = attr.ib(validator=instance_of(float))
    z = attr.ib(validator=instance_of(float))



@attr.s
class Bag:
    _contents = attr.ib(default=attr.Factory(list))
    def add(self, something):
        self._contents.append(something)
    def get(self):



------------------------------------------------------------------------------
@attr.s
class SmartClass(object):
    a = attr.ib()
    b = attr.ib()



class ArtisanalClass(object):
     def __init__(self, a, b):
         self.a = a
         self.b = b

     def __repr__(self):
         return "ArtisanalClass(a={}, b={})".format(self.a, self.b)

     def __eq__(self, other):
         if other.__class__ is self.__class__:
             return (self.a, self.b) == (other.a, other.b)
         else:
             return NotImplemented

     def __ne__(self, other):
         result = self.__eq__(other)
         if result is NotImplemented:
             return NotImplemented
         else:
             return not result

     def __lt__(self, other):
         if other.__class__ is self.__class__:
             return (self.a, self.b) < (other.a, other.b)
         else:
             return NotImplemented

     def __le__(self, other):
         if other.__class__ is self.__class__:
             return (self.a, self.b) <= (other.a, other.b)
         else:
             return NotImplemented

     def __gt__(self, other):
         if other.__class__ is self.__class__:
             return (self.a, self.b) > (other.a, other.b)
         else:
             return NotImplemented

     def __ge__(self, other):
         if other.__class__ is self.__class__:
             return (self.a, self.b) >= (other.a, other.b)
         else:
             return NotImplemented

     def __hash__(self):
         return hash((self.a, self.b))       return self._contents[:]
