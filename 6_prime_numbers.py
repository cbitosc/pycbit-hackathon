def print_primes():
	n = int(input("Enter the last number upto which prime numbers should be found: "))
	count = 0
	prime = [True for x in range(n+1)]
	p = 2

	while (p * p <= n):
		if prime[p]:
			for i in range(p ** 2, n+1, p):
				prime[i] = False
		p += 1
	for i in range(2, n):
		if prime[i]:
			count += 1
			print(i)
	print("Total number of prime numbers: %s" %(count))


print_primes()