N=int(input())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
l.sort()
for i in range(len(l)):
  print(l[i], end=' ')



  