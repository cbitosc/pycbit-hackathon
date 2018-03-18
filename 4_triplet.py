#!/usr/bin/python3
'''checks for a specific pythagoras triplet whose sum of numbers is 1000 and prints the product of those numbers'''
flag=0
for i in range(1,500):
	for j in range(1,500):
		c=1000-i-j
		if((i**2)+(j**2)==(c**2)):
			print(i*j*c)
			flag=1
			break
	if(flag==1):
		break
