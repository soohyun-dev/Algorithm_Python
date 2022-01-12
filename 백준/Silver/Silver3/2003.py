N,M=map(int,input().split())
l=list(map(int,input().split()))
cnt=0
sum=0
a=0
while a!=N:
  for i in range(a,N):
    sum+=l[i]
    if sum==M:
      cnt+=1
      break
    elif sum>M:
      break
  a+=1
  sum=0
print(cnt)


