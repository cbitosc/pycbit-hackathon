#Print the sum of numbers less than 500 which are divisible by 5 and not divisible by 7
sum=0
num=0
for num in range(1,501):
 	if num % 5==0 and num%7!=0:
 		sum=sum+num
 
print sum