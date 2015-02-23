# Quiz, Problem 5

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    idx = 0
    result = ""
    
    while idx < len(s1) and idx < len(s2):
        result += s1[idx] + s2[idx]
        idx += 1
        
    result += s1[idx:]
    result += s2[idx:]
    
    return result