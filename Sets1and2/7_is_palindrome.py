def isPalindrome(string):
	l = len(string)
	for i in range(int(l/2)):
		if(string[i] != string[-(i+1)]):
			return(False)
	return(True)

print(isPalindrome(input("Enter a word to check if it is a palindrome: ")))


