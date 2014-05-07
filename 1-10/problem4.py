#A palindromic number reads the same both ways.  The largest palindrome made from the product of two 2-digit numbers is:
# 9009 = 91 x 99
# Find the largest palindrome made form the product of two 3-digit numbers
import sys

def palintest(number):	
	number = str(number)	
	for x in range(0, round(len(number)/2)):
		#print(number[x])
		#print(number[len(number)-(x+1)])
		if (number[x] != number[len(number)-(x+1)]):
			#print('exit')
			return 0
	return 1


products = []
for x in reversed(range(1,1000)):
	for y in reversed(range(1,1000)):
		if (palintest(x*y) == 1):
			products.append(x*y)
			break
		
		
print(max(products))

	
#result = palintest(99915544551999)
#print(result)