l=8
b=8
h=10
def tsr1(l,b,h):
     area=2*((l*b)+(l*h)+(h*b))
     print("The area before increase in 15% of room's dimensions is : ",area)

def tsr2(l,b,h):
        l=8+0.15
        b=8+0.15
        h=10+0.15
        area=2*((l*b)+(l*h)+(h*b))
        print("The area after increase in 15% of room's dimensions is : ",area)

tsr1(l,b,h)
tsr2(l,b,h)