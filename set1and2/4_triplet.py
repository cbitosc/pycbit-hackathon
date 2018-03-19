#function to find triplets
def triplet(a, b, c):
    return (a**2) + (b**2) == (c**2)

SUM = 1000
#finding products of triplets whose sum is 1000
for i in range(1, SUM):
    for j in range(i+1, SUM):
        c = SUM - (i + j)
        if(triplet(i, j, c)):
            if i + j + c == SUM:
                print (i * j * c)
                break
