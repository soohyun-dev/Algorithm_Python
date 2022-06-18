import sys
input=sys.stdin.readline

N,X,K=map(int,input().split())
nums=[False]*(N+1)
nums[X]=True

for j in range(K):
    A,B=map(int,input().split())
    tmp=nums[A]
    nums[A]=nums[B]
    nums[B]=tmp

for j in range(1, N+1):
    if nums[j]==True:
        print(j)
        break
    