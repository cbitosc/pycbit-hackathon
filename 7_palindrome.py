#!/usr/bin/python3
'''checks if the entered string is a plaindrome or not'''
word=str(input('Enter the string'))
word_rev=str(word[::-1])

if(word == word_rev):
	print("palindrome")
else:
	print("not a palindrome")
