# -*- coding: utf-8 -*-
##L3 P9
# Guess the number

print 'Please think of a number between 0 and 100!'

low = 0
high = 100
ans = (high + low)/2
correct_ans_given = False

while not correct_ans_given:
    print 'Is your secret number ' + str(ans) + '?'
    in1 = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        
    if in1 == 'l':
        low = ans
        ans = (high + low)/2
    elif in1 == 'h':
        high = ans
        ans = (high + low)/2
    elif in1 == 'c':
        break
    else:
        print 'Sorry, I did not understand your input.'

print 'Game over. Your secret number was: ' + str(ans)
