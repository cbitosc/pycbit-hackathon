def Multiples(n):
	res = 0
	for i in range(5, n, 5):
		if(i%7 !=0):
			res+=i
	print("\n",res )
Multiples(500)