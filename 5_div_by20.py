n=1
for i in range(1,20):
	n=int(n)*i
i=1
while (i<n):
	k=0
	for j in range(1,20):
		if i%j==0:
			k=int(k)+1
		
	if k>=19:
		print(i)
		break
	i=int(i)+1

	
	
		
		
	
