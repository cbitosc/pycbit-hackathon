#take input
inp = input('Enter sequence: ')

# eliminate upper and lower case clashes
inp = inp.casefold()

# reverse the string
rinp = reversed(inp)

#converting inp & rinp to list for comparison
c=list(inp)
d=list(rinp)

# compare inp to rinp
if c == d:
   print("It is a palindrome")
else:
   print("It is not a palindrome")
