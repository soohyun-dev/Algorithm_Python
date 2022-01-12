N,M=map(int,input().split())
l=[]
sum=0
for a in range(N):
  l.append(input().split())
K=int(input())
for b in range(K):
  i,j,x,y=map(int,input().split())
  if i==x and j==y:
    print(l[i-1][j-1])
  else:
    for c in range(i-1,x):
      for d in range(j-1,y):
        sum+=int(l[c][d])
    print(sum)
  sum=0
  