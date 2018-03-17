#!/usr/bin/python3
'''calculates the least number which is divisible by all the numbers in the range 1 to 20'''
import fractions
def calc(n):
	if(n==2):
		return lcm(2,1)
	else:
		return lcm(n,calc(n-1))
def lcm(a,b):
	return (a*b)/fractions.gcd(a,b)
print(calc(20))
