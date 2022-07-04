n,g=map(int,input().split())
nums=list(map(int,input().split()))
result=[]
for i in range(0,n,g):
    result.append(min(nums[i:i+g]))

print(*result, end=' ')