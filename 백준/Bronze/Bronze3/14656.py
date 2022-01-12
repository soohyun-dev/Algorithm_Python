N=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(N):
  if i+1==l[i]:
    continue
  else:
    sum+=1
print(sum)

