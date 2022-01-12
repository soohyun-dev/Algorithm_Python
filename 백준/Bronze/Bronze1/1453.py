N=int(input())
l=list(map(int,input().split()))
sit=[]
sum=0
for i in range(N):
  if l[i] in sit:
    sum+=1
  else:
    sit.append(l[i])
print(sum)

