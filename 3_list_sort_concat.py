list1=["Ron","Hermione","Harry","Professor","Dobby"]
list2=["The House Elf","Potter","Granger","Lockhart","Weasley"]
list1.sort()
list2.sort()
def concat(*s):  
    x = []
    for i in s:
        x += i
    return x
list3=[]
list3= concat(list1,list2)
print(list3)
