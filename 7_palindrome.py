def check_palindrome():
	var = input("Enter a string to check whether its a palindrome or not: ")
	length = len(var)
	flag = 0
	low = 0
	high = length-1
	while(low < high):
		if var[low] != var[high]:
			print("%s is not a palindrome." %(var))
			return
		else:
			low += 1
			high -= 1
	print("%s is a palindrome." %(var))	

check_palindrome()