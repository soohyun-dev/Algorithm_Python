N=int(input())
l=[]
for i in range(N):
  x,y=list(map(int,input().split()))
  l.append([y,x])
l.sort()
for i in range(len(l)):
  for j in range(1,-1,-1):
    print(l[i][j], end=' ')
  print()


