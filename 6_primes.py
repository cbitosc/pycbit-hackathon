def prime(n):
	for i in range(2,n):
		if(n%i==0):
			return -1
	return 1
n=int(input("enter number of primes less than a number"))
x=0
for i in range(1,n):
	x=prime(i)
	if(x==1):
		print(i)
