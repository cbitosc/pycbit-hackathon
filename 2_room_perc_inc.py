def PercInc(l,b,h):
    
    print("Area:",l*b)
    l=l+(l*0.15)
    b=b+(b*0.15)
    h=h+(h*0.15)

    area=l*b

    print("Updated Area:",area)

PercInc(6,8,10)
