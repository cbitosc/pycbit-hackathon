#!/usr/bin/python3
'''calculates the area as well as the volume of the room'''
length=6
breadth=8
height=10

inc_ln=length+((15*length)/100.0)
inc_br=breadth+((15*breadth)/100.0)
inc_hgt=height+((15*height)/100.0)

area=inc_ln*inc_br
volume=inc_ln*inc_br*inc_hgt
print("area is : ",area,"\nvolume is : ",volume)
