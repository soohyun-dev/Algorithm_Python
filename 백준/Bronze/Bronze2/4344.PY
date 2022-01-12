C=int(input())
for i in range(C):
  N=list(map(int,input().split()))
  a=N[0]
  sum=0
  cnt=0
  for j in range(1,a+1):
    sum+=N[j]
  avg=sum/a
  for k in range(1,a+1):
    if N[k] > avg:
      cnt+=1
  print('%.3f' %((cnt/N[0])*100) +'%')
