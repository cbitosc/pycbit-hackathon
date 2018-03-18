def gcd(a,b):
	while b:
		a,b=b,a%b
	return a
def lcm(a,b):
	return (a*b)//gcd(a,b)
x=1
for i in range(2,21):
	x=lcm(x,i)
print(x)
