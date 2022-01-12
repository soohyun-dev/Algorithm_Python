N=int(input())
l=list(map(int,input().split()))
a=1
sum=0
for i in range(N):
  if l[i]==1:
    sum+=a
    a+=1
  else:
    a=1
print(sum)