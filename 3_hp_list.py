list1 = ["Ron", "Hermione", "Harry", "Professor", "Dobby"]

list2 = ["The House Elf", "Potter", "Granger", "Lockhart", "Weasley"]

print("List 1: " + str(list1))
list1.sort()
print("Sorted List 1: " + str(list1) + "\n")

print("List 2: " + str(list2))
list2.sort()
print("Sorted List 2: " + str(list2) + "\n")

list3 = list1 + list2
print("Concatenated list: " + str(list3))
list3.sort()
print("Sorted Concatenated list: " + str(list3))