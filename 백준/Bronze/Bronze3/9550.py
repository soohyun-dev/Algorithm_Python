for i in range(int(input())):
  sum=0
  N,K=map(int,input().split())
  l=list(map(int,input().split()))
  for i in range(N):
    sum+=l[i]//K
  print(sum)

  