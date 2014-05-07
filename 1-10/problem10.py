#The sum of the primes below 10 is 2+3+5+7 = 17
#Find the sum of all the primes below two million.
import math

def sumPrimes(number):
	sum = 0
	for x in range(2,number):		
		if (isPrime(x)):
			sum += x	
			print (sum)
	print(sum)

def isPrime(number):
	for y in range(2, number):
		if (number%y == 0):
			return False
	return True
		
		
#sumPrimes(2000000)


# def primes(n):
	# sieve = [True] * n
	# for i in range(3,int(n**0.5)+1,2):
		# if sieve[i]:
			# sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
	# return [2] + [i for i in range(3,n,2) if sieve[i]]

# print (primes(10))
########################
#### This one works - I can pythons
##########################
sieve = [True] * 2000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in range(x+x, len(sieve), x):
        sieve[i] = False

for x in range(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

print (sum(i for i in range(2, len(sieve)) if sieve[i]) )



		
def prime_sieve(limit):
	limitn = limit+1
	primes=list(range(2,limitn))
		
	for x in primes:
		#print(x)
		factors = list(range(x, limitn, x))
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
	


#saved = prime_sieve2(50)
#print(saved)
#print (len(saved))
#print saved[10001]
#print saved[10000]
#print saved[10002]

#print saved[10001]
