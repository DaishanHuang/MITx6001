##L3 P1

print "======================="
print "No 1"
print "===="

num = 0
while num <= 5:
    print num
    num += 1

print "Outside of loop"
print num 

print "======================="
print "No 2"
print "===="

print "infinite loop"
#numberOfLoops = 0
#numberOfApples = 2
#while numberOfLoops < 10:
#    numberOfApples *= 2
#    numberOfApples += numberOfLoops
#    numberOfLoops -= 1
#print "Number of apples: " + str(numberOfApples)

print "======================="
print "No 3"
print "===="

num = 10
while num > 3:
    num -= 1
    print num

print "======================="
print "No 4"
print "===="

num = 10
while True:
    if num < 7:
        print 'Breaking out of loop'
        break
    print num
    num -= 1
print 'Outside of loop'

print "======================="
print "No 5"
print "===="

print "infinite loop"
#num = 100
#while not False:
#    if num < 0:
#        break
#print 'num is: ' + str(num)