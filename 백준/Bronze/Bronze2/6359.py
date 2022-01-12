T=int(input())
for i in range(T):
  n=int(input())
  l=[0]*(n+1)
  sum=0
  a=1
  for j in range(1,n+1):
    while j*a<=n:
      l[j*a]+=1
      a+=1
    a=1
  for t in range(1,n+1):   # 0번 방은 없으므로 1번방 부터 시작
      sum+=1
  print(sum)

