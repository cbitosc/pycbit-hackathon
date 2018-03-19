def pytha(a, b, c):
    return (a**2) + (b**2) == (c**2)

sum = 1000

for i in range(1, sum):
    for j in range(i+1, sum):
        c = sum - (i + j)
        if(pytha(i, j, c)):
            if i + j + c == sum:
                print i * j * c
                break

				
