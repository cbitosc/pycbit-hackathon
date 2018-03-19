#Special Pythagorean Triplet
#Find a,b,c and hence the product abc
print('Program to find the special pythagorean triplets and their product, where a+b+c=1000 and a<b<c')
print('')

def spt():
    for a in range(1,333):  #start a between 1 and 333 since we can deduce from a<b<c that a<s/3
        for b in range(a,500):  #start b between a and 500 since we can deduce from a<b<c that b<s/2
            c = 1000 - a - b   #get c
            if a * a + b * b == c * c: #check with given condition 
                print('a is found to be: ',a)
                print('b is found to be: ',b)
                print('c is found to be: ',c)
                print('hence, the product a*b*c is equal to',a*b*c)  #print values
                break 
spt()
