#printing the present dimensions
length=10
width=6
height=8
print('The present dimensions of the room are: ')
print('Length: ',length)
print('Width: ',width)
print('Height: ',height)

print('*****************************')

#converting the dimensions
l=length + ((length*15)/100)
w=width + ((width*15)/100)
h=height + ((height*15)/100)
print('Increasing the dimensions by 15%, the new dimensions are: ')
print('Length: ',l)
print('Width: ',w)
print('Height: ',h)

print('*****************************')

print('Using the new dimensions:')

#calculating the area
area=l*w
print('AREA = ',area)

#calculating the volume
volume=l*w*h
print('VOLUME = ',volume)


