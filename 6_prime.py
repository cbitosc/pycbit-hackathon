#!/usr/bin/python3
'''prints all the prime numbers less than 99999'''
def isPrime(n):
	for i in range(2,(n//2)+1):
		if(n%i==0):
			return False
	return True
for i in range(2,99999):
	if(isPrime(i)):
		print(i)
