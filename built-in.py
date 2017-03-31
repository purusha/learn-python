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
