"""
zip():
    - zip() pairs elements from multiple iterables.
    - The zip() function in Python is used to combine two or more iterables (like lists, tuples, strings, dictionaries, etc.) into a single iterator of tuples.
    - When the iterables passed to zip() have unequal lengths, Python stops pairing as soon as the shortest iterable runs out of elements. 
"""

names = ["Asha", "Isha", "Mina"]
scores = [90, 85, 88]

result = list(zip(names, scores))
print(result)
# [('Asha', 90), ('Isha', 85), ('Mina', 88)]

print("---------------------------------")
"""
Best Practices

Use zip when you need to iterate over two lists in parallel

Use zip(*iterable) to unzip a list of tuples
"""


"""
Unzipping:
    - Unzipping is the reverse of zipping. If you already have a list of pairs, you can split them back into separate sequences using the * operator.
    - * operator unpacks the list of tuples, allowing zip() to regroup the first elements together and the second elements together.
"""
a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]
fruits, quantities = zip(*a)

print("Fruits:", fruits)
print("Quantities:", quantities)

print("---------------------------------")
"""
zip() can also be used to pair dictionary keys and values.
"""
d = {'name': 'Felix', 'age': 27, 'grade': 'A'}
keys = d.keys()
values = d.values()

res = zip(keys, values)
print(list(res))

##the zip() function is designed to stop pairing elements as soon as the shortest input iterable is exhausted, effectively ignoring any extra elements in the longer iterables.

names = ["Asha", "Isha", "Mina", "Ravi"]
scores = [90, 85, 88]

result = list(zip(names, scores))
print(result)