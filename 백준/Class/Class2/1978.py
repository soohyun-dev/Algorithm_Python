N=int(input())
l=list(map(int, input().split()))
sum=0
for i in range(N):
  cnt=0
  for j in range(1,l[i]+1):
    if l[i]%j==0:
      cnt+=1
  if cnt==2:
    sum+=1
print(sum)



