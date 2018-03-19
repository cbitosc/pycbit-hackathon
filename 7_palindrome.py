strng=str(input('Enter the string\n'))
strng_rev=str(strng[::-1])

if(strng == strng_rev):
	print("palindrome")
else:
	print("not a palindrome")
