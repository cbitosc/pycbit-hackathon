def primenum(upperbound):
    for num in range(1,upperbound+1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               print(num)

try:
    primenum(int(input("enter the upper bound ")))
except Exception as e:
    print("enter a postive number")
