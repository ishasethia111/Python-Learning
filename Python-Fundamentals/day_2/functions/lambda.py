"""
Anonymous Function:
    - functions without a name
    - lambda keyword used to create it.
    - Syntax
        - lambda arguments : expression

    -For short operations
    - When a function is needed only once
    - Used with map(), filter(), sorted(), reduce()

"""
#Basic Examples: of finding cube of a number
def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))


print("---------------------------------")

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
