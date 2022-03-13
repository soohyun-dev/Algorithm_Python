import sys
input=sys.stdin.readline

n=int(input())
dp=[0 for i in range(n+1)]
wine=[0]
for i in range(n):
    wine.append(int(input()))
dp[1]=wine[1]
if n>1:
    dp[2]=sum(wine[:3])
    for i in range(3,n+1):
        dp[i]=max(dp[i-1],dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i])
print(dp[-1])

        
        