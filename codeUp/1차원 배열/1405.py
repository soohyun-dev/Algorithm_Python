N=int(input())
nums=list(map(int,input().split()))
for i in range(N):
    print(*nums)
    tmp=nums[0]
    del(nums[0])
    nums.append(tmp)