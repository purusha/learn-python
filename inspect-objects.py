#importo la print di python3 (anche se uso python2)
from __future__ import print_function
import inspect
from types import FunctionType

#for attr in inspect.getmembers(object):
#    print(attr)

class Foo:
    def bar(self): pass
    def baz(self): pass

def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]

def methods_on_instance(obj):
    return [method for method in dir(obj) if callable(getattr(obj, method))]

print("#" * 10, "give a class", "#" * 10)
print(methods(Foo))
print(methods_on_instance(Foo))

print("#" * 10, "give an instance", "#" * 10)
f = Foo()
print(methods(f))
print(methods_on_instance(f))
