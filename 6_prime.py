n=1000000
i=1
j=1
for i in range(1,n):
	count=0
	for j in range(1,n):
		if i%j==0:
			count+=1	
	if count==2:
		print(i)
	

