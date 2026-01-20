"""
Functions:
    - Python Functions are a block of statements that does a specific task.
    - We can define a function in Python, using the def keyword. A function might take input in the form of parameters.
    - Python treats functions as first-class citizens, which means you can store them in variables, pass them around, or return them exactly like objects.
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


#Pass statement: The pass statement in Python is a placeholder that does nothing when executed.
#Used: It is used to keep code blocks valid where a statement is required but no logic is needed yet.
x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")

#Global and Local Variable and Modify Global variables using  global
a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)


"""
Pass by Reference and Pass by Value
    - Python uses "pass-by-object-reference".
    - Mutable objects behave like pass by reference, while immutable objects behave like pass by value
    - Variables hold references to objects, not the objects themselves.
    - When you pass a variable into a function, Python passes the reference to that object, not a copy.
    ## Python’s actual behavior (simple version):
        - Python passes the reference to the object, but whether changes affect the original depends on the object type.
        - Mutable objects (list, dict, set):
            - Function can change the original.
        - Immutable objects (int, str, tuple):
            - Function cannot change the original because a new object is created on assignment.
"""

def changeMutable(x):
    x.append(10)

lst = [1, 2]
changeMutable(lst)
print(lst)   # [1, 2, 10]  (changed, because list is mutable)

def changeImmutable(n):
    n = n + 1

a = 5
changeImmutable(a)
print(a)   # 5 (not changed, because int is immutable)

"""
self:
    - self represents instance of the class itself, allowing you to access and modify its attributes and methods.
    - Self is the reference to the current object instance.
    - Python does not have implicit receivers like Java and C++
        - class Person {
            String name;
            void greet() {
                System.out.println("Hello " + name);  // 'this' is implied
            }
        }
    - Explicit is better than implicit. You always see which variables belong to the object.
    - Each instance manages its own state.
- When a method runs, self tells Python: "Use this specific folder."
- self is not reserved, you can accidentally or intentionally reuse the identifier self inside the method
    - Example:
    class Test:
    def show(self):
        self = "shadowed"
        print(self) #shadowed
"""

class Person:
    def greet(self):
        print("Hello")

p = Person()
p.greet()   # Python internally calls: Person.greet(p)

"""
How self works under the hood
    - Whenever you call an instance method:
        - Python binds the object to the method before execution.
        - The object is passed automatically as the first argument.
    - Mechanism
    p.greet()
    # Step 1: Python looks up 'greet' on p’s class
    # Step 2: Python binds p to greet as self
    # Step 3: Python executes greet(self=p)
    - Method binding works like this:
        - When you call obj.method(), Python does Class.method(obj) internally.
        - Whatever the first parameter is called, it receives the instance.
"""

"""#Important behaviors"""
#1. self allows access to instance attributes
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt#Without self, Python has no idea which object’s balance to update.

#2.Methods without self become static or class methods
class Demo:
    def f():         # No self
        print("Not bound to instance")

Demo.f()  # Works
#Demo().f()  # Error: missing 1 required positional argument

#3. Class methods use cls instead of self. they recieve class not instance
@classmethod
def create_default(cls):
    return cls("Default")

"""#Passing function as an argument in Python"""
def process(func, text):  # applies a function to text  
    return func(text)  

def uppercase(text):  # converts text to uppercase  
    return text.upper()  

print(process(uppercase, "hello")) #HELLO

""" Returning Functions from Other Functions"""
def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func()) #Message: Hello, World!

""" Storing Functions in Data Structures"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       #8
print(d["subtract"](5, 3)) #2








