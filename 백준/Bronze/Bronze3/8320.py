n=int(input())
sum=0
for i in range(1, n+1):
  if(n%2==0):
    sum+=1
    if((n//2)>2 and (n//2)%2!=0):
      sum+=1
  elif(n==1):
    continue
  else:
    sum+=1
print(sum)
