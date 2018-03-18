str=input("enter")
l=len(str)
k=l
n=0
for i in range(0,int(l/2)):
	if str[i]==str[k-1]:
		n=n+1
	k=int(k)-1
		
if n==int(l/2):
	print("given string "+str+" is palindrome")
else:
	print("given string "+str+" is not a palindrome")
