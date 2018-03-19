def gcd(n1,n2):
	while n1!=n2:
		if n1>n2:
			n1=n1-n2
		elif n1<n2:
			n2=n2-n1
	return n1
def lcm1(num1,num2):
    lcm=int(int(num1*num2)/int(gcd(num1,num2)))
    return lcm
     
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 
num1=l[0]
num2=l[1]
lcm=lcm1(num1,num2)
 
for i in range(2,len(l)):
    lcm=lcm1(lcm,l[i])
     
print(lcm)
