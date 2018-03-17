'''Iterate for 'a' from 1 to 1000, iterate for 'b' from current 'a' value to 1000-a, get corrsponding 'c' value and check for pythogorean condition
'''

for a in range(1, 1000):
	for b in range(a, 1000-a):
		c = 1000-a-b
		if(a**2 + b**2 == c**2):
			print( "The triplets are " +  " ".join(map(str, [a, b, c])))
			print("And their product is " + str(a*b*c))