n,T=map(int,input().split())
l=list(map(int,input().split()))
sum=0
cnt=0
for i in range(n):
  sum+=l[i]
  if(T<sum):
    break
  cnt+=1
print(cnt)
