import math
def pythagoreanTriplet():

    for b in range(1,1000):
        # a^2+b^2=(1000-(a+b))^2
        a=(500000-1000*b)/(1000-b)

        if math.floor(a)==a :
            c=math.sqrt(a*a+b*b)
            break

    print(a,b,c)

pythagoreanTriplet()
