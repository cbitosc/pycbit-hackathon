def func1(increase):
    length=6
    breadth=8
    height=10
    len1=length+(increase/100)
    breadth1=breadth+(increase/100)
    height1=height+(increase/100)
    newarea=len1*breadth1*height1
    print("new area is "+str(newarea))
func1(15)

