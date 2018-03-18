a=0
b=0
c=0
def test(a,b):
	for b1 in range(1,b-1):
		test1(a,b1,1000-a-b1)
def test1(a,b,c):
	if a+b+c==1000:
		if a*a+b*b==c*c:
			print(a,b,c)
		
for a in range(1,998):
	test(a,1000-a)

