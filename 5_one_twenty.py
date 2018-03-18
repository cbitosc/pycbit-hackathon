primeNo = [2,3,5,7,11,13,17,19]
sno = 1

#def Primefac(n): returns the list of prime factors of 'n'
def Primefac(n):
        pfac = []
        for j in primeNo:
                if i % j == 0:
                        pfac.append(j)

        return pfac

#multiplies all the prime factors of all the numbers 
#from 1[1..20]
for i in range(1,20+1):
        primelst = Primefac(i)
        for i in primelst:
                sno *= i 
print ('smallest number divisible by [1..20] without remainder ',sno)
