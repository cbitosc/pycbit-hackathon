def pri(num=99999):
	for i in range(2,num+1):
	    count = 0
	    for j in range(2,i):
        	if i%j != 0:
        	    count += 1
	    if count == i-2:
        	print (i)
pri(100)
