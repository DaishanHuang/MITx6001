## Lecture 6, Problem 2

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    result_out = ()
    x = 0
    
    for nm in aTup:
        if x % 2 == 0:
            result_out += (nm,)
        x += 1
        
    return result_out