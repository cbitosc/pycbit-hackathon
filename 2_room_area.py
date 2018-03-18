class room:
	def __init__(self, length, width, height):
		self.length = length
		self.width = width
		self.height = height
		print("Room of dimensions %s X %s X %s is created.\n" %(self.length, self.width, self.height))

	def new_dimensions(self, increase_percentage):
		self.length *= (1+(increase_percentage/100))
		self.width *= (1+(increase_percentage/100))
		self.height *= (1+(increase_percentage/100))
		print("Room dimensions increased by %s percent.\n" %(increase_percentage))

	def calculate_area(self):
		area = 2 * (self.length * self.width + self.width * self.height + self.height * self.length)
		print("Suface Area of room of new dimensions is = %s" %(area))
		volume = self.length * self.width * self.height
		print("Volume of room of new dimensions is = %s" %(volume))

try:
	dim = input("Enter dimensions(aXbXc): ")
	dim = dim.split('X')
	x = room(int(dim[0]), int(dim[1]), int(dim[2]))
	percent = int(input("Enter increase percent: "))
	x.new_dimensions(percent)
	x.calculate_area()
except:
	print("Unexpected error! Please re-enter values.")