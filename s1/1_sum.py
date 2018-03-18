def sumof500():
    sum=0 #stores the sum of the numbers satisfying the below condition
    for i in range(1,500):
        if(i%5==0 and i%7!=0):
            sum+=i
    print ("sum is "+str(sum))
sumof500()#function call 
            
