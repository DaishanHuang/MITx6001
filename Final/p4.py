# PROBLEM 4
def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0: # change 1
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == 0: # change 2
            break
            
        if sign == -1:
            guess *= 2
        else:
            guess -= 1
    return guess
    
def isMyNumberImplementation(theNumber):
    secret_number = 100
    
    if theNumber == secret_number:
        return 0  
    elif theNumber < secret_number:
        return -1
    elif theNumber > secret_number:
        return 1

print "Guess was: " + str(jumpAndBackpedal(isMyNumberImplementation))