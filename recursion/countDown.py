

def countDown(num):
    # Unintentional Case - Constraint
    assert num >= 0 and num == int(num), "Enter posative integer!"
    
    # Base Case
    if num == 0:
        print("Done!")
    
    # Recursive Case
    else:
        print(num)
        countDown(num-1)

countDown(10)
