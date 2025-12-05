"""
map():
    - map() applies a function to every item in an iterable.
    - syntax:
        - map(function, iterable)
"""

from functools import reduce


result = list(map(lambda x: x*2, [1, 2, 3, 4]))
print(result)   # [2, 4, 6, 8]


"""
filter:
    - filter() keeps only the items that satisfy a condition.
"""

nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)  # [2, 4]


"""
reduce():
    - reduce() repeatedly applies a function to reduce iterable to a single value.
"""

nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums)
"""
Internally:
Step 1: 1 + 2 = 3
Step 2: 3 + 3 = 6
Step 3: 6 + 4 = 10
Final result = 10
It keeps reducing until one value remains.
"""
print(result)  # 10
