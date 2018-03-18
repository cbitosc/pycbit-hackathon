list1 = ['Ron', 'Hermoine', 'Harry', 'Professor','Potter','Dobby','Granger','Lockhart','Weasly']
list2=['Potter','Gred','Greg','George','Voldemort','Sirius','Dumbledore']
list1.sort();
list2.sort();
print("The sorted list1 is : ",list1)
print("The sorted list2 is : ",list2)

concatlist=list(set(list1+list2))
print("List after concatenation : ",concatlist)
concatlist.sort();
print("list after sorting the concatenated list : ",concatlist)