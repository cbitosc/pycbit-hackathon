

def palindrome(user_input):
    if(user_input[::-1]==user_input):
	       print("palindroime")
    else:
        print("not a palindrome")


palindrome(user_input=input("enter a string"))
