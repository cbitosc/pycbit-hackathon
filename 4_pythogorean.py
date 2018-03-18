def check_triplet(a,b,c):
	return (a**2)+(b**2)==(c**2)

Sum=1000

for i in range(1,Sum):
	for j in range(i+1,Sum):
		c=Sum-(i+j)
		if(check_triplet(i,j,c)):
			if i+j+c==1000:
				print(i,j,c)
				print(i*j*c)
				break