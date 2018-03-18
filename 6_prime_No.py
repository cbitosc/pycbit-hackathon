def primeNo():

    for i in range(1,99999):
        f=0
        j=2
        while j<=i/2:
            if i%j==0 :
                f=1
                break
            j+=1
        if f==0 :
            print(i)
        i+=1

primeNo()
