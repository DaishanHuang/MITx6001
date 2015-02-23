# Quiz, Problem 8

#########################
# 8-1
# Fix bug in this code
#def fixedPoint(f, epsilon):
#    """
#    f: a function of one argument that returns a float
#    epsilon: a small float
#  
#    returns the best guess when that guess is less than epsilon 
#    away from f(guess) or after 100 trials, whichever comes first.
#    """
#    guess = 1.0
#    for i in range(100):
#        if f(guess) - guess < epsilon:
#            return guess
#        else:
#            guess = f(guess)
#    return guess

# Fixed code:
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

#########################
# 8-2
# Fix bug in code
#def sqrt(a):
#    def tryit(x):
#        return 0.5 * (a/x + x)
#    return fixedPoint(tryit(a), 0.0001)

# Fixed code:
#def sqrt(a):
#    def tryit(x):
#        return 0.5 * (a/x + x)
#    return fixedPoint(tryit, 0.0001)

#########################
# 8-3
# Fix bug in code
#def babylon(a):
#    def test(x):
#        return 0.5 * ((a / x) + x)
#    return test
#
#def sqrt(a):
#    return fixedPoint(babylon, 0.0001)

# Fixed code:
def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)
