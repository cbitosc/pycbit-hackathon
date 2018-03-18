#!/usr/bin/python3
'''sorts the lists in ascending order and concatentes them'''
list_a=['Ron','Hermione','Harry','Professor','Dobby','List Items 2','The House Elf','Potter','Granger','Lockhart','Weasley']
list_b=['Potter','Fred','Greg','George','Voldemort','Sirius','Dumbledore']

res_list=sorted(list_a)+sorted(list_b)
print('...'.join(res_list))
