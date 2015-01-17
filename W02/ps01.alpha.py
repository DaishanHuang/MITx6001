##PS01: Alphabetical Substrings

# s_is defined by grader
s = 'azcbobobegghakl'

max_sub = ""
current_sub = ""
previous_char = ""

for current_char in s:
    if current_char >= previous_char:
        current_sub = current_sub + current_char
        if len(current_sub) > len(max_sub):
            max_sub = current_sub
    else: 
        current_sub = current_char
        
    previous_char = current_char

print "Longest substring in alphabetical order is: " + max_sub