my_str=input('Enter the String\n')
my_str=my_str.lower()

my_str2=reversed(my_str)

if list(my_str2)==list(my_str) :
	print("The string is a palindrome")
else:
	print("The string is not a palindrome")
