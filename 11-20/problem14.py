#The following iterative sequence is defined for the set of positive integers:
 
#n n/2 (n is even)
#n 3n + 1 (n is odd)
 
#Using the rule above and starting with 13, we generate the following sequence:
 
#13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
 
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
 
#Which starting number, under one million, produces the longest chain?
 
#NOTE: Once the chain starts the terms are allowed to go above one million.


def even(num):
    return (int(num/2))

def odd(num):
    return ((num*3)+1)

max = 0
#chain = [0] * 20

for x in range(1, 1000000):
    num = x
    count = 0
    while x > 1:
        if (x%2 == 0):
            x = even(x)
            #print (x)
        else:
            x = odd(x)
            #print (x)
        count += 1
    if (count > max):
        max = count
        print (str(count) + ":" + str(num))

#print (chain[13])
#print (even(4))
#print (odd(13))
