nums = []
for i in range(1,500):
    if i%5==0 and i%7!=0:
        nums.append(i)
    else:
        a = 1
print(nums)
sum=0
for n in range(0,len(nums)):
    ins=nums[n]
    sum=sum +ins
print(sum)