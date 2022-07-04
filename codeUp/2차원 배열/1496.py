N=int(input())
nums=list(map(int,input().split()))
result=[]
for i in range(0,N,2):
    result.append(min(nums[i],nums[i+1]))

print(*result, end=' ')