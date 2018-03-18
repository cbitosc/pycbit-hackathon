def gcd(a, b):
	if a == 0:
		return b

	else:
		return gcd(b%a, a)

def calculate_num():
	flag = 1
	try:
		n = int(input("Enter the value of n to find smallest number divisible by all numbers upto n: "))
		for i in range(1, n+1):
			flag = (flag * i)/gcd(flag, i)
		print("The smallest number divisible by all numbers between 1 and %s: %s" %(n, flag))
	except:
		print("Invalid input. Please enter a whole number.")

calculate_num()