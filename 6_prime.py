def isPrime(x):
	for i in range(2,int(x**0.5)+1):
		if(x%i==0):
			return False
	return True		

def printPrimes(n):
	print("primes are")
	for i in range(2,n+1):
		if(isPrime(i)):
			print(i)
printPrimes(9999)
