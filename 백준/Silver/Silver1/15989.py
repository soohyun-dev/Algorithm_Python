import sys
input=sys.stdin.readline

dp=[1]*10001  # 1만 가지고 합 만든 경우

cnt=0
for i in range(2,10001):
    if i%2==0:
        cnt+=1
    dp[i]+=cnt

cnt=1
for j in range(3,10001):
    dp[j]+=dp[j-3]

T=int(input())

for k in range(T):
    print(dp[int(input())])


