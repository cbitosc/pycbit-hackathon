a = "Ron,Hermione,Harry,Professor,Dobby,List Items 2,The House Elf,Potter,Lockhart,Weasley"
list1 = a.split(",")
b = "Potter,Fred,Greg,George,Voldemort,Sirius,Dumbledore"
list2 = b.split(",")

def sort_concat(list1, list2):
	'''
	takes two lists, sorts and concatenates them to return a new list
	'''
	return(sorted(list1) + sorted(list2))

new_list = sort_concat(list1, list2)
print(new_list)

