N=input()
sum=0
for i in range(len(N)-1):
  if N[i]!=N[i+1]:
    sum+=1
print((sum+1)//2)


