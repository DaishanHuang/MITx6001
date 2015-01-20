## Lecture 5, Problem 4 & 5

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smallest_nbr = min(a, b)
    cnt_smallest_nbr = smallest_nbr
    reached_result = False
    
    while not reached_result:
        if (a % cnt_smallest_nbr == 0 and b % cnt_smallest_nbr == 0) \
            or (cnt_smallest_nbr == 0):
            smallest_nbr = cnt_smallest_nbr
            break
            
        if cnt_smallest_nbr == 0:
            break
        
        cnt_smallest_nbr -= 1

    return smallest_nbr
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
        
    return gcdRecur(b, a % b)