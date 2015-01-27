## Lecture 6, Problem 7A

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# Your Code Here
def absList(a):
    return abs(a)

applyToEach(testList, absList)

print testList

#####################
# Problem 7B

testList = [1, -4, 8, -9]

#>>> print testList
#   [2, -3, 9, -8]

# Your Code Here
def plusOneList(a):
    return a + 1

applyToEach(testList, plusOneList)

print testList

#####################
# Problem 7C

testList = [1, -4, 8, -9]

#>>> print testList
#    [1, 16, 64, 81]

# Your Code Here
def multSelf(a):
    return a * a

applyToEach(testList, multSelf)

print testList