import math
def prime(num):
	k=0
	for i in range(2,num):
		c=0
		for j in range(2,int(math.sqrt(i)+1)):
			if i%j==0:
				c=1
		if c==0:
			print(i)
prime(99999);
		
		
