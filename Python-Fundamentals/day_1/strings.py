"""
Strings:
    - strings in Python are arrays of unicode characters.
    - rsplit() method splits a string into a list, starting from the right.

"""

#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String: check if a certain phrase or character is present in a string
txt = "The best things in life are free!"
print("free" in txt)

#Check if not
txt = "The best things in life are free!"
print("expensive" not in txt)

#Slicing in String: You can return a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5])

#Slice To the End
b = "Hello, World!"
print(b[2:])

#Negative Indexing
"""
 H   e   l   l   o
 0   1   2   3   4
-------------------
 H   e   l   l   o
-5  -4  -3  -2  -1
"""
b = "Hello, World!"
print(b[-5:-2])

"""
String Method
"""
#upper()
a = "Hello, World!"
print(a.upper())

#lower()
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Convert String to Lsit
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)