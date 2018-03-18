sum=0
#initializing step value to 5 so that numbers which are not multiples of 5 are not counted
for i in range(5,500,5):
	if(i%5==0) and (i%7!=0):
		sum=sum+i

print("sum of numbers less than 500 which are divisible by 5 and not divisible by 7 is "+str(sum))
 
