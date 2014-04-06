def prime_sieve(limit):
	limitn = limit+1
	primes=range(2,limitn)
		
	for x in primes:
		print x
		factors = range(x, limitn, x)
		for f in factors[1:]:
			if f in primes:				
				primes.remove(f)
	return primes
	
#I found that resizing the array with remove is expensive

def prime_sieve2(limit):
	a = [True] * limit
	a[0] = a[1] = False
		
	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):
				a[n] = False
	
	
saved = prime_sieve(120000)
print len(saved)
print saved[10001]
print saved[10000]
print saved[10002]

#print saved[10001]

	
