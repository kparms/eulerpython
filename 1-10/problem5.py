#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#The smallest number that is divisible by two numbers is the LCM of those numbers.

def gcd(a,b):
	#print(str(a) + ', ' + str(b))
	if (b==0):
		return a
	else:
		return gcd(b,a%b)


def lcm(a,b):
	return (a*b)/(gcd(a,b))
		
#LCM(x0,x1,x2) = LCM(x0,LCM(x1,x2))
print(lcm(2,lcm(3,lcm(4,lcm(5,lcm(6,lcm(7,lcm(8,lcm(9,lcm(10,lcm(11,lcm(12,lcm(13,lcm(14,lcm(15,lcm(16,lcm(17,lcm(18,lcm(19,20)))))))))))))))))))


		
#too slow!
def divisible(num):
	for x in range(1,11):
		if (num%x != 0):			
			return 0	
	return 1

# pos = 11
# while 1==1:
	# print(pos)
	# if(divisible(pos) == 1):
		# break
	# else:
		# pos += 1
	
# print(divisible(2520))
		
	