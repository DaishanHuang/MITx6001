## Lecture 5, Problem 1, 2, 3

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    
    while exp > 0:
        result *=base
        exp -= 1
        
    return result
    
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        if exp % 2 != 0:
            return base * recurPowerNew(base, exp-1)
        else:
            return recurPowerNew(base*base, exp/2)
