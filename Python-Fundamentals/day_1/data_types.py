"""
Data Type:
    - Text Type: str
    - Numeric Types: int, float, complex
    - Sequence Types: list, tuple, range
    - Mapping Type: dict
    - Set Types: set, frozenset
    - Boolean Type: bool
    - Binary Types: bytes, bytearray, memoryview
    - None Type: NoneType
- You cannot convert complex numbers into another number type.
"""

# str
x = "Hello World"
print(x)
#int
x = 20
print(x)
#float
x = 20.5
print(x)
#complex
x = 1j
print(x)
#list
x = ["apple", "banana", "cherry"]
print(x)
#tuple
x = ("apple", "banana", "cherry")
print(x)
#range
x = range(6)
print(x)
print(list(x))
#dict
x = {"name" : "John", "age" : 36}
print(x)
#set
x = {"apple", "banana", "cherry", "cherry"}
print(x)
#frozenset
x = frozenset({"apple", "banana", "cherry", "cherry"})
print(x)
#bool
x = True
print(x)
#bytes
x = b"Hello"
print(x)
#bytearray
x = bytearray(5)
print(x)
#memoryview
x = memoryview(bytes(5))
print(x)
#NoneType
x = None
print(x)

#Random Numer
"""
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers
"""
import random

print(random.randrange(1, 10))