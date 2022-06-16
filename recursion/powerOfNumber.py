

def power(num, exp):
    assert exp >= 0 and int(exp) == exp, "The exponent must be a positive integer only!"
    if exp == 0:
        return 1
    if exp == 1:
        return num
    else:
        return int(num) * power(num, exp-1)

print(power(2,4))

# x = x*x*x..(n times)..*x
# 2^4 = 2*2*2*2
# x^n = x * x^n-1
