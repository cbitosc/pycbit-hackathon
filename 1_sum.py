def divisible(num,div):
	if(num%div==0):
		return 1
	else:
		return 0
		
sum=0;
for i in range(1,500):
	if divisible(i,5) and not divisible(i,7):
		sum+=i

print("sum of numbers less than 500 which are divisible by 5 and not divisible by 7 is: {}".format(sum))
