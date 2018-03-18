n=500
flag=0
sum=0
for i in range(1,n):
	if((i%5==0)and(i%7!=0)):
		flag=1
		sum=sum+i
if(flag==1):
	print(int(sum))

