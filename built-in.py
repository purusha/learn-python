#importo la print di python3 (anche se uso python2)
from __future__ import print_function

print("abs is {0}".format(abs(3)))
print("abs is {0}".format(abs(3.3)))
print("abs is {0}".format(abs(0x33)))
print("#" * 42)

print("all is {0}".format(all(range(1, 42))))
print("all is {0}".format(all([True, False, True])))
print("all is {0}".format(all([])))
print("#" * 42)

print(isinstance("ciccio", basestring))
print(isinstance(42, basestring))
print(basestring)
print("#" * 42)

print(bin(0))
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print("#" * 42)

print(bool())
print(bool(1))
print("#" * 42)

class MyClass:
    def __call__():
        pass

print(callable(MyClass))
print(callable(MyClass()))
print("#" * 42)

class MyAttr:
    def __init__(self):
        self.name = "Alan"
        self.age = 34

instance1 = MyAttr()
instance2 = MyAttr()

print("attributes of object {0}: {1}".format(id(instance1), instance1.__dict__))
print("attributes of object {0}: {1}".format(id(instance2), instance2.__dict__))
delattr(instance1, "age")

print("attributes of object {0}: {1}".format(id(instance1), instance1.__dict__))
print("attributes of object {0}: {1}".format(id(instance2), instance2.__dict__))
print("#" * 42)

print(isinstance(instance1, MyAttr))
print("#" * 42)

print(iter([1, 2, 3]))
print(iter([1, 2, 3], MyClass()))
print("#" * 42)
