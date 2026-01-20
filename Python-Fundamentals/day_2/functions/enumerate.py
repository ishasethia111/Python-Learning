"""
Enumerate:
    - enumerate() adds a counter (index number) to items in an iterable (like a list, tuple, or string).
    -Syntax:
        - enumerate(iterable, start=0)

"""
#without enumerate:
fruits = ["apple", "banana", "cherry"]

index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1


#with enumerate
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


"""
Best Practices
    - Always use enumerate() instead of manually tracking index
    - Improves readability and avoids errors
    - You can choose where indexing starts
"""

"""
Why use enumerate() and zip() together?
    - To loop over multiple sequences at the same time
    - Also get the index number of each pair of items
"""

names = ["Isha", "Riya", "Aman"]
scores = [85, 92, 78]

#Without enumerate + zip 
for i in range(len(names)):
    print(i, names[i], scores[i])
"""
Problem:
    - if list of different size it will cause IndexError
    - improves readability 
    - Prone to index bugs
"""

#With enumerate + zip:
for i, (name, score) in enumerate(zip(names, scores)):
    print(i, name, score)
