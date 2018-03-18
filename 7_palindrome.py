s1=input("Enter a string: ")
s2=s1[::-1]
if s1==s2:
	print("{} is palindrome".format(s1))
else:
	print("{} is not a palindrome".format(s1))
