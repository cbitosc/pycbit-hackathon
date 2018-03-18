def gcd(a,b):
    rem=0;
    while(b>0):
       rem=a%b;
       a=b;
       b=rem;
    return a;
x=gcd(1,2);
y=(1*2)//x;
z=y;
for i in range(1,19):
   k=i+2;
   z=(z*k)//gcd(z,k);
print(z);
