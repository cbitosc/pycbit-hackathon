max=int(input("enter max. no. upto which you want find prime numbers : " ))
for i in range(2,max+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
    if prime:
        print(i)
        
        
        
        
#python program for 4_pythogorean_triplet
for a in range(1,1000):
	for b in range(a+1,1000):
		c=1000-(a+b)
		if(a**2)+(b**2)==(c**2):
			if a+b+c==1000:
				print(a*b*c)
				break


