for i in range(1,1000):
	z=0
	for j in range(1,i):
		for k in range(1,i):
			if(i**2==j**2+k**2 and i+j+k==1000):
				z=1
				print(i)
				print(k)
				print(j)
				print("the product of required number is "+str(int(i*j*k)))
				break
		if z==1:
			break
	if z==1:
		break
