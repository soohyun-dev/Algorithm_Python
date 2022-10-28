N=int(input())
nums=list(map(int,input().split()))

result=0
SUM=sum(nums)

for i in range(0,N-1):
    v=nums[i]
    SUM-=v
    result+=v*SUM
print(result)