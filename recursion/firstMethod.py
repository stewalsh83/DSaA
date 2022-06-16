# Stack memory
# First in Last out

def firstMethod():
    secondMethod()
    print("I am the First Method")

def secondMethod():
    thirdMethod()
    print("I am the Second Method")

def thirdMethod():
    forthMethod()
    print("I am the Third Method")

def forthMethod():
    print("I am the Forth Method")

firstMethod()
# secondMethod()
# thirdMethod()
# forthMethod()
