#importo la print di python3 (anche se uso python2)
from __future__ import print_function

list = [["a",["b",["c","x"]]]]
print(list)

tuple = ("tuples", "are", "immutable")
print(tuple)

str = "Python under Linux is great"
print(str[::3])

abc = ["a","b","c","d","e"]
print("a" in abc)
print("a" not in abc)

food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
print(food)

for key in food:
    print("%s => %s" % (key, food[key]))

print(food.keys())
print(food.values())
