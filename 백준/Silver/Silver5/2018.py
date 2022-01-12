N=int(input())
if N%2==0:
  M=N//2
else:
  M=(N//2)+1
sum=0
cnt=0
for i in range(1,M+1):
  for j in range(i,M+1):
    sum+=j
    if sum==N:
      cnt+=1
      sum=0
      break
    elif sum>N:
      sum=0
      break
print(cnt+1)
  

  

