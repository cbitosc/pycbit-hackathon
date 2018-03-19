list_items_2=['Potter',
'Fred',
'Greg',
'George',
'Voldemort',
'Sirius',
'Dumbledore']

#SORTING WORDS PRESENT IN SET1

# IF LIST ITEM 2 IS IN LIST 1
list_items_1=['Ron',
'Hermione',
'Harry',
'Professor',
'Dobby',
'The House Elf',
'Potter',
'Granger',
'Lockhart',
'Weasley']

#since list_items_2 is in list_items_1 in the QUESTION

list_items_1.extend(list_items_2)
print("sorting the list_items_1")
list_items_1.sort()
#IF SORTING OF LIST 2 IS REQ REMOVE THE COMMENT IN LINE BELOW
#list_items_2.sort()

print(list_items_1)
print(list_items_2)


list_items_1=[a + b for a, b in zip(list_items_1,list_items_2)]
print(list_items_1)
