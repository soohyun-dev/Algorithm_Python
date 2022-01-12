N=list(map(int,input().split()))
sum=0
for i in range(len(N)):
  if N[i]>0:
    sum+=1
print(sum)