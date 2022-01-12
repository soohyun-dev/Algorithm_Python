cnt=int(input())
sum=0
for i in range(cnt):
  A=int(input())
  if A==1:
    sum+=1
  else:
    sum-=1
if(sum>0):
  print("Junhee is cute!")
elif(sum<0):
  print("Junhee is not cute!")


