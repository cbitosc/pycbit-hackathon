#check given string is palindrome or not

text=input("enter the string");
text2=[];
length=len(text);

for i in range(length):
	text2.append(text[length-1]);
	length=length-1;

text1="".join(str(i) for i in text2);

if(text==text1):
	print("palindrome");
else:
    print("not a plaindrome"); 	




