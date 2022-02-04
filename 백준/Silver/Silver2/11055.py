import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
dp=[0 for i in range(N)]
dp[0]=A[0]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i]=max(dp[i],A[i]+dp[j])
        else:
            dp[i]=max(dp[i],A[i])

print(max(dp))




