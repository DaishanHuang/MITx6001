## Lecture 5, Problem 6, 7, 8

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    cnt_nbr = 0
    
    for c in aStr:
        cnt_nbr += 1

    return cnt_nbr
    
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[0:-1])
        
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here   
    if(aStr == ''):
        return False
    elif(aStr == char):
        return True
    else:
        # Bisection
        middleIdx = len(aStr) / 2
        fromIdx = 0
        toIdx = -1

        if(aStr[middleIdx] == char):
            return True
        if(aStr[middleIdx] > char):
            fromIdx = 0
            toIdx = middleIdx
        if(aStr[middleIdx] < char):
            fromIdx = middleIdx + 1
            toIdx = len(aStr)
        return isIn(char, aStr[fromIdx : toIdx])