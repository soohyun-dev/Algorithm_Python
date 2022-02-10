import sys
input=sys.stdin.readline

dp=[0]*1000001
dp[0],dp[1],dp[2]=1,1,2
for i in range(3,1000001):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i]%=1000000009

for j in range(int(input())):
    print(dp[int(input())])
