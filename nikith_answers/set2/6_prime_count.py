def eratosthenes(x):
    """
    Generate the primes less than or equal to n using the sieve of
    Eratosthenes.
    """
    multiples = []
    for i in range(2, x+1):
        if i not in multiples:
            print (i)
            for j in range(i*i, x+1, i):
                multiples.append(j)
    
def view():
    x=int(input("Enter max number: "))
    y=eratosthenes(x)
    
view()
