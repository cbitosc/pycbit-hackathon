import sys

t=[]
#u can find all the number divisible by 1to 20 if u remove the if found condition
for i in range(2520,int(sys.maxsize)):
    found=False
    if (i%2==0 and i%3 and i%5==0 and i%7==0 and i%11==0 and i%13==0 and i&17==0 and i%19==0):
        t.append(i)
        found=True
    if found:
        print(i)
        break
#print(t)    
