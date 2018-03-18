def printArea(increasePercent, length = 6, breadth = 8, height=10):
	'''
	prints the area of the room when the dimesions are increased by a certain amount
	'''
	increase = increasePercent/100
	newLength = length + (length*increase)
	newBreadth = breadth + (breadth*increase)
	area = newBreadth*newLength
	print("The area of the room after the increase in dimensions is " + str(area))

printArea(15)

