import sys
input=sys.stdin.readline

N=int(input())
a=[0]*10000001
b=[0]*10000001
x=list(map(int, input().split()))
for i in range(N):
  if x[i] >= 0 :
    a[x[i]]=1
  else:
    b[x[i]]=1

M=int(input())
y=list(map(int, input().split()))
for j in range(M):
  if y[j] >= 0:
    y[j]=a[y[j]]
  else:
    y[j]=b[y[j]]
  
print(*y)