list1=["Ron","Hermione","Harry","Professor","Dobby","List Items 2","The House Elf","Potter","Granger","Lockhart","Weasley"]
list2=["Potter","Fred","Greg","George","Voldemort","Sirius","Dumbledore","Potter","Fred","Greg","George"]
list1.sort()
for i in range(0,11):
	for j in range(0,11):
		str=list1[i]+list2[i]
		print str
		break		