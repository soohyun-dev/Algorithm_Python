N,X=map(int,input().split())
l=list(map(int,input().split()))
for i in range(N):
  if(X>l[i]):
    print(l[i], end=' ')


