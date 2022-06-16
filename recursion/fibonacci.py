

def fibonacci(n):
    assert n >= 0 and n == int(n), "Fibonacci number cannot be negative or non integer!"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10...
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
# f(n) = f(n-1) + f(n-2)
