import sys

N,M=map(int,input().split())
l=[]
K=[]
if N<3:
  print(0)
else:
  for i in range(1,N+1):
    l.append(i)
  for i in range(M):
    a=[]
    for j in range(len(l)):
      a.append(l[j])
    A,B=map(int,sys.stdin.readline().split())
    a.remove(A)
    a.remove(B)
    if a not in K:
      K.append(a)
  print(len(K))

  