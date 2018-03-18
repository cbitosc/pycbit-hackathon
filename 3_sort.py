list1=["Ron","Hermione","Harry","Professor","Dobby"]
list2=["The House Elf","Potter","Granger","Lockhart","Weasely"]
def concat(list1,list2):
	return(sorted(list1)+sorted(list2))
list3=concat(list1,list2)
print(list3)
