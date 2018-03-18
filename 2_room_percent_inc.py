#!/usr/bin/python
ln=6
wd=8
ht=10
area=int(ln)*int(wd)
volume=int(ln)*int(ht)*int(wd)
print("initial area is "+str(area))
print("initial volume is "+str(volume))
area1=float(int(ln)+float(15/100*ln))*float(int(wd)+float(15/100*wd))
print("increased area is "+str(area1))
volume2=float(int(ln)+float(15/100*ln))*float(int(wd)+float(15/100*wd))*float(int(ht)+float(15/100*ht))
print("increased volume is "+str(volume2))
