#importo la print di python3 (anche se uso python2)
from __future__ import print_function

def single(n):
    print("n is %d" % n)

def single_with_default(n, m=42):
    print("n is %d, m is %d" % (n, m))

def values(*m):
    print("multiple values are %s" % m)

def values_and_named(*m, **named):
    print("multiple values are %s and named are %s" % (m, named))

single(1)

single_with_default(2)
single_with_default(2, 3)

values(range(2, 6))
values_and_named(range(2, 6), a=1, b=2)
