"""
Inner Functions:
    - A function defined inside another function is called an inner function (or nested function). 
    - An inner function can use variables from the outer function. 
    - We use inner functions to hide small helper logic inside a main function so the code stays clean and organized.
    - An inner function cannot be called from outside the outer function.
"""

def outer():
    message = "Hello from outer!"

    def inner():
        print(message)  # inner function can access 'message'

    inner()
outer()

print("---------------------------------")
"""
Inner functions can modify outer variables using `nonlocal` keyword
"""
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # 20
outer()

print("---------------------------------")
"""
Inner Function also used by:
    - Closures: They are memory-equipped functions. 
        - A closure is an inner function that remembers and uses variables from its outer function, even after the outer function has finished running.
    - How Closures Work Internally?
        - It stores outer function’s variables in a special attribute called __closure__.
        - The inner function keeps a reference, not a copy, to these variables.
"""
# Example: where inner function retains outer function’s variable even after outer function has finished executing
def outer_function(x):
    # Outer function: takes 'x' and defines inner_function
    def inner_function(y):
        return x + y  # 'x' is remembered from outer_function
    return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
closure = outer_function(10)

# Call the closure with different values of 'y'
print(closure(5)) 
print(closure(20))
print(closure.__closure__[0].cell_contents)

"""
Useful in:
1. Encapsulation
2. Function Factory
3. Maintaining state without using classes
4. Decorators
"""
