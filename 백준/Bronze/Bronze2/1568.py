N=int(input())
sum=0
a=1
b=N
while True:
  if N-a>=0:
    N-=a
    sum+=1
    a+=1
    if N==0:
      print(sum)
      break
  elif N-a<0:
    a=1

