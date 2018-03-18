def reverse(s):
    return s[::-1]
 
def Polindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False
 
 
s = raw_input("enter the string\n")
ans = Polindrome(s)
 
if ans == 1:
    print("Yes")
else:
    print("No")
