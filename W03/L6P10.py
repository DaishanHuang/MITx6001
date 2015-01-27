## Lecture 6, Problem 10 + 11

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for value in aDict.values():
        result += len(value)
    return result

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict) == 0:
        return None
        
    maxLen = 0
    big = None
    
    for key, value in aDict.iteritems():
        if len(value) > maxLen:
            maxLen = len(value)
            big = key
        elif maxLen <= 0:
            big = key

    return big