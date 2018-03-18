l=6
b=8
h=10
def calc(l,b,h):
    area=2*((l*b)+(b*h)+(h*l))
    print(area)
calc(6,8,10)
def inc(l,b,h):
    l=l*1.15
    b=b*1.15
    h=h*1.15
    area = 2 * ((l * b) + (b * h) + (h * l))
    print(area)
inc(6,8,10)