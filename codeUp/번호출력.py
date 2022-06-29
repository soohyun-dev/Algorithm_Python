import random

N=int(input())
nums=[]
for i in range(1,N+1):
    nums.append(i)
random.shuffle(nums)
del(nums[8])
for i in range(N-1):
    print(nums[i])