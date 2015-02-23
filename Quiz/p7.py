# Quiz, Problem 7

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    # 6a+9b+20c=n

    # Recursive
    #if n == 0:
    #    return True
    #    
    #if n < 0:
    #    return False
    #    
    #return McNuggets(n-6) or McNuggets(n-9) or McNuggets(n-20)

    # Guess-and-check
    noOf6  = n/6
    noOf9  = n/9
    noOf20 = n/20
    
    guessNum = 0    
    result = False
    
    for a in range(0, noOf6+1):
        for b in range(0, noOf9+1):
            for c in range(0, noOf20+1):
                guessNum = 6*a + 9*b + 20*c
                if (guessNum == n):
                    result = True
                    break
               
    return result
