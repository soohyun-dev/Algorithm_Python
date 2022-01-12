N,M=map(int,input().split())
cnt=N
N=[0]*(N+1)
for l in range(M):
  i,j,k = map(int,input().split())
  for m in range(i,j+1):
    N[m]=k
for a in range(1,cnt+1):
  print(N[a], end=' ')

  