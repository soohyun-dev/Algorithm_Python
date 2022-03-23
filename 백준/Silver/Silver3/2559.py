import sys
input=sys.stdin.readline

N,K=map(int, input().split())
nums=list(map(int,input().split()))
tmp=sum(nums[0:K])
M=tmp

for i in range(1,N-(K-1)):
    tmp=tmp-nums[i-1]+nums[K-1+i]
    M=max(tmp,M)

print(M)





