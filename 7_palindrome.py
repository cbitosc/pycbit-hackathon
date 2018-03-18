def palindrome(s):
    rs=list(s)
    st=list(s)
    ind=len(s)
    i=ind-1
    j=0
    while i>=0 and j<=ind-1:
        rs[j]=st[i]
        j+=1
        i-=1
    if st==rs :
        return "Given string is a Palindrome";
    else :
        return "Given string is not a palindrome";

s=input("Enter the string:");
print(palindrome(s))
