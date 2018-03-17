def listofprime(start,end):
    countno=0
    list=[]
    for i in range(start,end+1):
        count=0
        for j in range(1,(i//2)+1):#checks only half of the values
            if(i%j==0):
                count+=1
        if(count==1):
            list.append(i)
            countno+=1
    print ("The number prime no.s between the given range is "+str(countno)+"LIST:"+str(list))
start=int(input("Enter starting no."))
end=int(input("Enter ending no."))
listofprime(start,end)#calls the listofprimes function

    
        
