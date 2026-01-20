"""
Higher Order Functions:
    - A higher-order function is any function that does at least one of the following:
        - Takes another function as an argument, or
        - Returns a function as its result.
    - Why we use higher-order functions
        - Higher-order functions allow you to:
            - Abstract repetitive behavior.
            - Build more expressive and concise logic.
            - Write cleaner transformations over data collections.
            - Implement callback-based, decorator-based, or pipeline-based designs.
Advanced use of higher-order functions
"""

#Common built-in higher-order functions in Python
result = list(map(lambda x: x * 2, [1, 2, 3]))
# [2, 4, 6]

result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
# [2, 4]

from functools import reduce
result = reduce(lambda a, b: a + b, [1, 2, 3, 4])
# 10


a = "I am global"

def outer():
    b = "I am enclosing"
    
    def inner():
        global a
        nonlocal b
        a = "Modified global"
        b = "Modified enclosing"
    
    inner()
    print("Inside outer:", b)
    
outer()
print("Outside outer:", a)#Inside outer: Modified enclosing #Outside outer: Modified global
