##PS01: Counting bobs

# s_is defined by grader
s = 'azcbobobegghaklbob'

num_bobs = 0
bob_to_check = 'bob'
input_to_lower = s.lower()
idx = 0

while idx >= 0:
    found_at_idx = s.find(bob_to_check, idx)
    
    if found_at_idx >= 0:
        num_bobs += 1
        idx = found_at_idx + 1
    else:
        break;   

print 'Number of times bob occurs is: ' + str(num_bobs)