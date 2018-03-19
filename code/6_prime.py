flag=0
for i in range(2,99999):
	for j in range(2,((i/2)+1)):
		if i%j==0:
			flag=1
			break
	if flag==0:
		print(i)
	else:
		flag=0
	
