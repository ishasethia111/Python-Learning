#Arithmetic
x = 15
y = 4

print(x + y)#Addition
print(x - y)#Subtraction
print(x * y)#Multiplication
print(x / y)#Division
print(x % y)#Modulus
print(x ** y)#Exponentiation
print(x // y)#Floor division


#Assignment 
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison 
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical 
x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

#Identity 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Membership 
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


#Bitwise......
