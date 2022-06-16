
def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)

# FILO
# Stack memory for recursive calls
# First in Last out
"""
n is less than 1     base case    
1                    forth
2                    third
3                    second
4                    first in last out
"""
