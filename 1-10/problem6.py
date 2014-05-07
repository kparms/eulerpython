# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#this one was a little too easy...

sum=0
for x in range(0,101):
	sum += x

print(sum*sum)

sumsq=0
for y in range(0,101):
	sumsq += (y*y)
	
print(sumsq)

total = (sum*sum) - sumsq
print(total)