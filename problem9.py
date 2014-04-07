
#Fibonacci's method of finding primitive triples, does not find a+b+c = 1000
def fibs(x):
	for x in range(3,100,2):
		oddsq = x*x
		n = (int(oddsq + 1) / 2)
		b = n-1
		print(str(oddsq) + ' + ' + str(int(b*b)) + ' = ' + str(int(n*n)))
		print (x+b+n)	
	
	
#just brute force it
for a in range(1,1000):
	#a < b, so a+1
	for b in range(a+1, 1000):
		#a + b + c = 1000
		c = 1000 - a - b
		#check if legit
		if (a*a + b*b == c*c):
			print(str(a) + ' ' + str(b) + ' ' + str(c))
			print(a*b*c)