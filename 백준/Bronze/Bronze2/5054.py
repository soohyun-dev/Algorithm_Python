t=int(input())
for i in range(t):
  n=int(input())
  l=list(map(int,input().split()))
  l.sort()
  sum=(l[n-1]-l[0])*2
  print(sum)


