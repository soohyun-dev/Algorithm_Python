import sys
input=sys.stdin.readline

n,k=map(int,input().split())
nums=[]
for i in range(n):
    nums.append(int(input()))

dp=[0 for i in range(k+1)]
dp[0]=1

for num in nums:
    for k in range(num, k+1):
        dp[k]+=dp[k-num]
print(dp[k])
