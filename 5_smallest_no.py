import fractions
def smallestNo(n):
    i=1
    while i>0:
        k=0
        for j in range(1,n+1):
            if i%j==0:
                k+=1
            
        if k==n:
            return i;
        i+=1      #O(m*n)

def smallNo(n):
    no = 1   
    for i in range(1, n + 1):
        no = (no * i)/fractions.gcd(no, i)        
    return no

num=smallestNo(10)
num1=smallNo(20)
print(num,num1)



