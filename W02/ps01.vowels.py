##PS01: Counting Vowels

# s_is defined by grader
s = 'azcbobobegghakl'

num_vowels = 0
vowels = ['a', 'e', 'i', 'o', 'u']
input_to_lower = s.lower()

for vowel in vowels:
    num_vowels += input_to_lower.count(vowel)

print 'Number of vowels: ' + str(num_vowels)