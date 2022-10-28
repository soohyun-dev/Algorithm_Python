import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
Nums=sorted(list(map(int,input().split())))
for i in range(1,N):
  Nums[i]=Nums[i]+Nums[i-1]

for i in range(Q):
  a,b=map(int,input().split())
  if a==1:
    print(Nums[b-1])
  else:
    print(Nums[b-1]-Nums[a-2])