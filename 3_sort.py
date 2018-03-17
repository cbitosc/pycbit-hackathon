list1='Ron Hermione Harry Professor Dobby'
list2=['The House Elf','Potter','Granger','Lockhart','Weasley']

list1=list1.split()
list1.sort()
print("The sorted list is ")
for word in list1:
	
	print(word)
list2=list2+list1

print(list2)