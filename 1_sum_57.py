def show_sum():
	sum = 0
	for x in range(0,500):
		if ((x % 5 == 0) and (x % 7 != 0)):
			sum += x
	print("Sum of numbers less than 500 which are divisble by 5 and not by 7 = %s" %(sum))

show_sum()
