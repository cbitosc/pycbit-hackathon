def prime(q):
    for a in range(2,q):
        k=0
        for i in range(2,a//2+1):
            if(a%i==0):
                k=k+1
        if(k<=0):
            print(a)
prime(99999)
