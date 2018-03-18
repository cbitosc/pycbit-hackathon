#!/usr/bin/python3
'''adds the numbers which are divisible by 5 but not by 7 to the sum and prints it'''
sum=0
for i in range(1,500):
	if(i%5==0 and i%7!=0):
		sum+=i
print(sum)
