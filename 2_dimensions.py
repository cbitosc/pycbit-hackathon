# Consider a room with dimension 6X8X10, Write a program to compute the volume of the room if the dimensions are increased by 15 percent.

x = float(6)
y = float(8)
z = float(10)

print ('Original Volume:' ,  x*y*z)
print ('Original Area:' ,  x*y)

print ('New Volume:' , (x+x*0.15)*(y+y*0.15)*(z+z*0.15))
print ('New Area:' , (x+x*0.15)*(y+y*0.15))


