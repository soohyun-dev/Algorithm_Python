N=int(input())
sum=0
cnt=9
num=1
if N < 10:
  print(N)
else:
  while True:
    sum+=(cnt*num)
    N-=cnt
    cnt*=10
    num+=1
    if cnt>N:
      sum+=(num*N)
      break
  print(sum)
