def sumOfNum():
    sum=0
    a=5
    for a in range(0,501):
        if a%5==0 and a%7!=0 :
            sum=sum+a
    
    print(sum)

sumOfNum()

