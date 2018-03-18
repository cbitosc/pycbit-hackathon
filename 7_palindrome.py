i=0
flag=0
s1=input("enter string")
n=len(s1)
for i in range(1,n):
	if(s1[i]!=s1[n-i-1]):
		flag=1
		break
if(flag==1):
	print("string is not palindrome")
else:
	print("string is palindrome")
	
