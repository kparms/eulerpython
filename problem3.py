#The prime factors of 13195 are 5,7,13 and 29
#What is the largest prime factor of the number 600851475143 ?

#Prime factorization function
def primes(num):
	factors = []
	myfactor=2
	while myfactor*myfactor <= num:
		#The number is a prime factor if the mod is zero, add it to the primefac array and 
		#divide the number num, keep going
		while (num % myfactor) == 0:
			factors.append(myfactor)
			num /= myfactor
		#This is inefficient? We're checking every number instead of just primes, is there a faster way?
		myfactor += 1
	if num > 1:
		factors.append(num)
	return factors
	
print(primes(600851475143))

#These problems are really fun

#My initial attempt, I was listing all primes for a given number
#Then mod division of that number against the prime, the largest prime
#that gave a mod of zero was the largest prime factor

# a=list(range(2,114))
# for x in a:
	# comp=[]
	# for y in range(a.index(x),len(a)):
		# q=x*a[y]
		# if q<=max(a):
			# comp.append(q)
		# else:
			# break
	# for z in comp:
		# a.remove(z)

	

# for p in a:
	# print(str(p) + ' mod: ' + str(13195%p))