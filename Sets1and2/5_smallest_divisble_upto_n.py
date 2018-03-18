def smallestDivisor(n):
	'''
	prints the smallest number divisible by all numbers from 1-n
	Time complexity = O(n*n)
	'''
	s = {} # to keep track of completed numbers. Using a dictionary will bring down search operation to O(1)
	t = {} # tp keep track of completed numbers that are not directly part of the product.
	res = 2
	if(n==1):
		print(1)
		return
	for i in range(2, n+1): 
		'''
		iterate from 2 to n. 
		at each iteration 
			check if the current number is divisible by the previously completed value. 
			If divisible find out the smallest number that has to multiplied to the product.
			update the product
		'''
		if(len(s) == 0):
			s[i] = True		
		cur_min = i

		for j in s.keys():

			if(i%j==0):
				temp = i/j
				if(temp in s and temp!=j and temp not in t):
					cur_min = 1
					break
				if(temp < cur_min):
					cur_min = temp
		res = res*cur_min
		if(cur_min != i):
			t[i] = True
		#print(cur_min)
		s[i] = True
	print(res)

smallestDivisor(20)





