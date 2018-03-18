def prime(start,end):#gives us the list of prime no.
    countno=0
    list=[]
    for i in range(start,end+1):
        count=0
        for j in range(1,(i//2)+1):#checks with only half of the values
            if(i%j==0):
                count+=1
        if(count==1):#if count is 1 it is stored in list since we are not iterating till the number
            list.append(i)
    return list
    
def power(a,n):#used to get the power of the prime number in the smallest number 
    pow=0
    b=a
    while(a<=n):
        a*=b
        pow+=1
    return pow

end=int(input("Enter ending no."))
res=prime(1,end)
value=1
for i in res:
    value*=i**power(i,end)
print(value)
  
  
    
        
