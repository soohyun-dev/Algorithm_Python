n=int(input())
m=int(input())
L=m
for i in range(n):
  d,e=map(int,input().split())
  m+=d-e
  if(L<=m):
    L=m
  elif(m<0):
    print(0)
    break
if(m>0):
  print(L)
  
  