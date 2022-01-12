M=int(input())
N=int(input())
a=1
double=a*a
l=[]
while double <= N:
  if double>=M:
    l.append(double)
  a+=1
  double=a*a
  
if len(l)==0:
  print(-1)
else:
  print(sum(l))
  print(l[0])


