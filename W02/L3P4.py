##L3 P4

print "======================="
print "No 1"
print "===="

num = 10
for num in range(5):
    print num
print num 

print "======================="
print "No 2"
print "===="

divisor = 2
for num in range(0, 10, 2):
    print num/divisor

print "======================="
print "No 3"
print "===="

for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!'

print "======================="
print "No 4"
print "===="

for letter in 'hola':
    print letter 

print "======================="
print "No 5"
print "===="

count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count 
