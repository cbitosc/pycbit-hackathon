'''program in python to print the sum of numbers 
that are divisible by 5 and not divisible by 7'''
sum = 0
for i in range(1, 500):   #specify max-range of 500
     if (i % 5 == 0 and i % 7 != 0): #initial condition
         sum = sum + i
print sum