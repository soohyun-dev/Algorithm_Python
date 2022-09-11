N=int(input())
dp=[1]*117
for i in range(4,N+1):
    dp[i]=dp[i-1]+dp[i-3]
print(dp[N])