# Quiz, Problem 4

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    result = 0
    
    while b**result <= x:
        result += 1
        
    return result - 1
    