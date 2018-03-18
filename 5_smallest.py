import fractions
 
# Returns the lcm of 1 to n 
def lcm(n=10):
    ans = 1   
    for i in range(1, n + 1):
        ans = (ans * i)/fractions.gcd(ans, i)        
    return ans
 
print lcm(20)
