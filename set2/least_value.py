def gcd(a,b):
	
	# Everything divides 0 
	if (a == 0 or b == 0):
			False
	# base case
	if (a == b):
		return a

	# a is greater
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)


def lcm(n):
    ans = 1   
    for i in range(1, n + 1):
        ans = (ans * i)/gcd(ans, i)        
    return ans
 # main
n = 20
print(lcm(n));