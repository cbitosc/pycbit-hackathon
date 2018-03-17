lst = [] #declaring list
num = int(input('What is the max range? '))
print('')
print('CONDITIONS:')
print('Numbers in the range must be divisible by 5 but not by 7.')
print('')
for i in range(num): #giving range to check each number in range
    if i%5==0 and i%7!=0: #condition: divisible by 5, not divisible by 7
        lst.append(i) #if satisfied, add number to the list at the end.
print("The numbers in the given range satisfying the conditions are:\n"+str(lst))
print('')
print('The sum of all these numbers is: '+str(sum(lst)))
print('')
