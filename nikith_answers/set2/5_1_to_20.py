print('Program to find smallest number divisible between 1-20:')
def gcd(x,y):
    return y and gcd(y, x % y) or x  
def lcm(x,y):
    return x * y / gcd(x,y)  
  
n = 1  
for i in range(1, 21):  
     n = lcm(n, i)  
print('The smallest divisible number is',n)  
