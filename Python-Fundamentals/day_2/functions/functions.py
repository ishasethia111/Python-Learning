"""
Functions:
    - Python Functions are a block of statements that does a specific task.
    - We can define a function in Python, using the def keyword. A function might take input in the form of parameters.
"""


def fun():
    print("Welcome to My World")
    
fun() # Driver code to call a function

"""
Types of Argument in function in Python:
"""

#1. Default Arguments: A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#2. Keyword Arguments: In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.

def student(fname, lname):
    print(fname, lname)

student(fname='John', lname='Doe')
student(lname='Doe', fname='John')

#3. Positional Arguments: In positional arguments, values are assigned to parameters based on their order in the function call.

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("John", 27)

print("\nCase-2:")
nameAge(27, "John")

#4  Arbitrary Arguments
"""
Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)
"""
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Lets', 'Learn', first='about', mid='args', last='kwargs')




