N,M=map(int,input().split())
l=list(map(int,input().split()))
min=100000
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if i==j or j==k or i==k:
        continue
      result=M-(l[i]+l[j]+l[k]) 
      if result < min and result>=0:
        min=result
        card=l[i]+l[j]+l[k]
print(card)
        

