
#area if c is height
area_c=0
#area if b is height
area_b=0
#area if a is height
area_a=0


def fu(a=6,b=8,c=10):
	global area_c,area_b,area_a
	area_a=(b*1.15)*(c*1.15)
	area_b=(c*1.15)*(a*1.15)
	area_c=(b*1.15)*(a*1.15)
try:
    fu(float(input("enter a")),float(input("enter b")),float(input("enter c")))
    print("if a is height ",area_c,"\nif b is height ",area_b,"\nif c is height",area_a)

except:
    print("enter real numbers")
