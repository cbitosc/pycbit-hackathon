numbers = [];
count = int(input ("HOW MANY NUMBERS YOU WANT TO CALCULATE GCD?\n"))
for i in range(0, count):
  number = int(input("ENTER THE NUMBER : \n"))
  numbers.append(number)
numbers_sorted = sorted(numbers)
print ('NUMBERS SORTED IN INCREASING ORDER\n',numbers_sorted)
gcd = numbers_sorted[0]
for i in range(1, count):
  divisor = gcd
  dividend = numbers_sorted[i]
  remainder = dividend % divisor
  if remainder == 0 :
    gcd = divisor
  else :
    while not remainder == 0 :
      dividend_one = divisor
      divisor_one = remainder
      remainder = dividend_one % divisor_one
      gcd = divisor_one
product=1
for j in range(0,len(numbers)):
  product=product*numbers[j]
print(product/gcd)  
