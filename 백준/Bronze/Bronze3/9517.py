K=int(input())
N=int(input())
Time=210
for i in range(N):
  t,z=input().split()
  Time-=int(t)
  if(Time<=0):
    print(K)
    break
  if(z=='T'):
    K+=1
    if(K>8):
      K=1
  elif(z=='N'or z=='P'):
    continue
 
