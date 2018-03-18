# Print the sum of numbers less than 500 which are divisible by 5 and not divisible by 7

var = 0
for x in range(0, 500):
    if (x % 7 != 0) and (x % 5 == 0): var += x
print(var)
