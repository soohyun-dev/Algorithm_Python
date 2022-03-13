import sys
input=sys.stdin.readline

n=int(input())
dp=[0 for i in range(n+1)]
stair=[0]
for i in range(n):
    stair.append(int(input()))
dp[1]=stair[1]
if n>1:
    dp[2]=sum(stair[:3])
    for i in range(3,n+1):
        dp[i]=max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
print(dp[-1])