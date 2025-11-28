"""
Variables are containers for storing data values.
Variable names are case-sensitive.
Variable Name:
    - Camel Case
        - myVariableName
    - Pascal Case
        - MyVariableName
    - Snake Case
        - my_variable_name
Global Keyword: 
    - Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
"""

x = 5 # x is is numeroc
y = "John"
print(x)
x = "JDOE" # x is now string
print(x)
print(y)

#If you want to specify the data type of a variable, this can be done with casting. 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

#Get data type of varaiable
print(type(x))
print(type(y))
print(type(z))

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)