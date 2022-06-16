

def factorial(n):
    # Unintentional Case - The Constraint
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"
    # Base Case
    if n in [0,1]:
        return 1
    else:
    # Recursive Case
        fact = n * factorial(n-1)
        return fact

print(factorial(4))

# 4! = 4*3*2*1 = 24
# n! = n*(n-1)*(n-2)*...*2*1
