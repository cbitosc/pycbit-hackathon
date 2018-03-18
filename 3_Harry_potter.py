def hogwarts():

    list1=["Ron","Hermoine","Harry","Professor","Dobby"]
    list2=[" The House Elf"," Potter"," Granger"," Lockhart"," Weasley"]
    list3=[]
    list1.sort()
    for i in range(0,5):
        list3.append(list1[i]+list2[i])
    print(list3)

hogwarts()
