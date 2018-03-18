import fractions
def Sum(n):
    ans = 1   
    for i in range(1, n + 1):
        value = (value * i)/fractions.gcd(ans, i)        
    return value

print(Sum(20))