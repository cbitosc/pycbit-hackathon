max=int(input("enter max. no. upto which you want find prime numbers : " ))
for i in range(2,max+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
    if prime:
        print(i)


