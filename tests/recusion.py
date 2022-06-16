import sys

# Stack Limit
sys.setrecursionlimit(100)

def factorial(n):
    print(n)
    # Recursive Case
    return n * factorial(n-1)

# RecursionError:
factorial(3)

 # --------------------------------

