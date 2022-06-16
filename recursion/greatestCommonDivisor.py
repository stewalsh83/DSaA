

def gcd(a, b):

    # Constraints
    assert int(a) == a and int(b) == b, "The numbers must be integer only!"
    if a < 0:
        a = a*(-1)
    if b < 0:
        b = b*(-1)
    
    # Base Case
    if b == 0:
        return a
    
    # Recursive Case
    else:
        return gcd(b, a%b)

print(gcd(48, -18))


# Euclidean algorithm
# 48/18 = 2 r12
# 18/12 = 1 r6
# 12/6  = 2 r0

