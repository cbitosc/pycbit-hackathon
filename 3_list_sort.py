# Sort the given words alphabetically and concat them with the second set
# List Items 1
#     Ron
#     Hermione
#     Harry
#     Professor
#     Dobby
# List Items 2
#     The House Elf
#     Potter
#     Granger
#     Lockhart
#     Weasley

potter=["Ron","Hermione","Harry","Professor","Dobby"]

potter.sort()
print(potter)

head=["The House Elf", "Potter", "Granger", "Lockhart", "Weasley"]

for x in range (0,4): print(potter[x], head[x])
