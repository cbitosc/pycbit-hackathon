list1=["Ron","Hermione","Harry","Professor","Dobby","List Items 2","The House Elf","Potter","Granger","Lockhart","Weasley"]
list2=["Potter","Fred","Greg","George","Voldemort","Sirius","Dumbledore"]
temp=""
l=len(list1)
for i in range(0,l-1):
	for j in range(0,l-i-1):
		if list1[j]>list1[j+1]:
			list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1+list2)
