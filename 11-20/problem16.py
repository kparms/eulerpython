#2^15 = 32768
# the sum of the digits is 26
#what is the sum of the digits of 2^1000?

#number = 2**15
number = 2**1000
numstring = str(number)

digitSum = 0
for x in range(0, len(numstring)):
    digitSum += int(numstring[x])
    #print (numstring[x])

print (digitSum)


    
