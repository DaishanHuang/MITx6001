# -*- coding: utf-8 -*-
##L4 P3, P4, P5, P6, P8, P9, P10, P11

def square(x):
    '''
    x: int or float.
    '''
    return x * x

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b * x + c

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    
    return min(max(x,lo),hi)

def fourthPower(x):
    '''
    x: int or float.
    '''
    #square(square(x))
    return square(x)*square(x)
    
def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    #(x % 2 == 1)
    return bool(x % 2)
    
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    low_char = char.lower()
    return  low_char == ('a') or low_char == ('e') or \
    low_char == ('i') or low_char == ('o') or low_char == ('u') 

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    low_char = char.lower()
    return low_char in vowels

print "P3 square: 3*3=" + str(square(3))
print "P4 quadratic:⋅a*x**2+b*x+c=" + str(evalQuadratic(3,4,5,6))
print "P5 clip: 5,10,15=" + str(clip(5,10,15))
print "P5 clip: 10,5,15=" + str(clip(10,5,15))
print "P5 clip: 5,15,10=" + str(clip(5,15,10))
print "P8 fourthPower: -3.64**4=175.5519 is:" + str(fourthPower(-3.64))
print "P9 odd: 13=True is:" + str(odd(13))
print "P9 odd: 48=False is:" + str(odd(48))
print "P10 isVowel: a=True is:" + str(isVowel('a'))
print "P10 isVowel: b=False is:" + str(isVowel('b'))
print "P10 isVowel: c=False is:" + str(isVowel('c'))
print "P10 isVowel: u=True is:" + str(isVowel('u'))
print "P11 isVowel2: a=True is:" + str(isVowel2('a'))
print "P11 isVowel2: b=False is:" + str(isVowel2('b'))
print "P11 isVowel2: c=False is:" + str(isVowel2('c'))
print "P11 isVowel2: u=True is:" + str(isVowel2('u'))