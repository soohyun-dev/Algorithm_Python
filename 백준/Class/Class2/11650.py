N=int(input())
l=[]
for i in range(N):
  x,y=list(map(int,input().split()))
  l.append([x,y])
l.sort()
for i in range(len(l)):
  for j in range(2):
    print(l[i][j], end=' ')
  print()


  