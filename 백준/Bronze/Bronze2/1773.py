N,C=map(int,input().split())
l=[0]*(C+1)
sum=0
for i in range(N):
  cnt=int(input())
  for j in range(cnt, C+1, cnt):
    if l[j]==0:
      l[j]=1
      sum+=1
print(sum)


