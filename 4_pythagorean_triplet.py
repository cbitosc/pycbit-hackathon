def pythagorean():
	sum = 1000
	for x in range(1, int(sum/3)+1):
		for y in range(x+1, int(sum/2)+1):
			z = sum - x - y
			if((x<y) and (y<z)) and (x+y+z == sum) and (x**2 + y**2 == z**2):
				print("Pythagorean triplets are:")
				print("a = %s" %(x))
				print("b = %s" %(y))
				print("c = %s" %(z))
				return
				
pythagorean()