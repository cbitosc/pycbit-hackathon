def prime(n):
	for i in range(2,n//2+1):
		if n%i==0:
			return -1
	return 1
x=0
print("prime numbers between 1 and 99999:")
for i in range(1,99999):
	x=prime(i)
	if(x==1):
		print(i)
