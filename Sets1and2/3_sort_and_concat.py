a = "Ron,Hermione,Harry,Professor,Dobby,List Items 2,The House Elf,Potter,Lockhart,Weasley"
list1 = a.split(",")
b = "Potter,Fred,Greg,George,Voldemort,Sirius,Dumbledore"
list2 = b.split(",")

def sort_concat(list1, list2):
	'''
	assuming the question is to
	take two lists, sort the first list and concatenate these values index wise to the values from second list
	'''
	list1.sort()
	for i in range(len(list2)):
		#print(list1[i])
		list1[i] = list1[i] + " " +  list2[i]
		
	


sort_concat(list1, list2)
print(list1)

def sort1_concat(list1, list2):
	'''
	if the question is to sort the lists and simply concatenate them
	'''
	return(sorted(list1) + sorted(list2))


