for a in range(0,1000):
	for b in range(0,1000):
		for c in range(0,1000):
			if a**2 + b**2==c**2 and a+b+c==1000:
				if a<b<c:
					print a*b*c
					exit()
			
				