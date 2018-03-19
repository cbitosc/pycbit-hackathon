mylist=["Ron",
"Hermione",
"Harry",
"Professor",
"Dobby",
"List Items 2",
"The House Elf",
"Potter",
"Granger",
"Lockhart",
"Weasley"
]
mylist.sort()
for x in sorted(mylist):
	print(x)
mylist.extend(["Potter",
"Fred",
"Greg",
"George",
"Voldemort",
"Sirius",
"Dumbledore"])
mylist.sort()
for x in sorted(mylist):
	print(x)
