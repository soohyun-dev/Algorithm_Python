N,m,M,T,R=map(int,input().split())
e=sum=0
n=m
if m+T>M:
  print(-1)
else:
  while e<N:
    if n+T<=M:
      n+=T
      e+=1
      sum+=1
    else:
      n=max(n-R,m)
      sum+=1
  print(sum)


