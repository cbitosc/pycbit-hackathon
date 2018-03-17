list1 = ['Ron','Hermione','Harry','Professor','Dobby','List Items 2','The House Elf','Potter','Granger','Lockhart','Weasley']
list2 = ['Potter','Fred','Greg','George','Voldemort','Sirius','Dumbledore']

print('')
print("The first list is:\n",list1)
print("The second list is:\n",list2)
print('')

#sorting the lists
l1 = sorted(list1)
l2 = sorted(list2)

print('After sorting:')
print("List 1 =\n",l1)
print("List 2 =\n",l2)
print('')

#concatenating both the lists
l3 = l1 + l2

print('After concatenation:')
print("Combined List =\n",l3)
print('')

#sorting the new list
l4=sorted(l3)

print('Sorting the new list:')
print("Sorted and concatenated list =\n",l4)
