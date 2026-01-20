"""
Recursion:
    - when function calls itself directly or indirectly
"""

#Example: Factorial
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5)) #outPut: 120

"""Type of Recursion:
    - Tail: The function calls itself last, with no work afterward. It can be optimized like a loop.
    - Non-Tail: The function calls itself but has work after the call. It cannot be optimized into a loop.
"""

def tail_fact(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Tail recursive call with an accumulator
    else:
        return tail_fact(n-1, acc * n)

def nontail_fact(n):
    # Base case
    if n == 1:
        return 1
    # Non-tail recursive call because the multiplication happens after the call
    else:
        return n * nontail_fact(n-1)

# Example usage
print(tail_fact(5))  #120
print(nontail_fact(5))#120