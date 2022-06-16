

def sumOfDigits(n):
    assert int(n) == n and n >= 0, "The number has to be positive integer!"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n//10))

print(sumOfDigits(11111))

# 10/10  = 1  remainder  = 0
# 54/10  = 5  remainder  = 4

# 112/10 = 11 remainder  = 2
# 11/10  = 1  remainder  = 1

# f(n) = n%10 + f(n/10)
