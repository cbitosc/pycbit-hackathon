def isprime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")

for n in range(1,99999):
    isprime(n)