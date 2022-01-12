import sys
N=int(input())
l=list(map(int,sys.stdin.readline().split()))
l.sort()
for i in range(1,N):
  l[i]=l[i]+l[i-1]
print(sum(l))

