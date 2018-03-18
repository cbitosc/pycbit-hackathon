def room(length=6,height=10,width=8,increase=15): 
    # Calculate increase %
    length=length+((increase*length)/100.0)
    height=height+((increase*height)/100.0)
    width=width+((increase*width)/100.0)
    #print the SURFACE AREA
    print('SURFACE AREA :',2 * (length * width + length * height + width * height))
    # Print the Volume
    print("VOLUME",length * width * height)
     
room()

