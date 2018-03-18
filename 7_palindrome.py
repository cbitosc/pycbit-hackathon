'''Program to check for a palindrome string'''

def isPalindrome(str):
        rev=str[::-1]
        print("String : ",str)
        print("reverse : ",rev)
        if(str==rev):
            return True
        else:
            return False
x=input("enter a string : ")
if isPalindrome(x):
    print("It is a Palindrome string")
else:
    print("It is not a palindrome string")
