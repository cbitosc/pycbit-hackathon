def isPrime(x):
	'''helper function to check if a number is a prime
	'''
	for i in range(2, int(x**0.5)+1):
		if(x%i == 0):
			return(False)
	return(True)

def printPrimes(n):
	'''iterates over the given range, 
	checks if number is prime and prints it to the console
	'''
	print("The primes from 1 to " + str(n) + " are " )
	for i in range(2, n+1):
		if(isPrime(i)):
			print(i)

printPrimes(99999)



