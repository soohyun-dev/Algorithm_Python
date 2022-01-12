N,K=map(int,input().split())
l=[]
Josephus=[]
plus=K
cnt=0
for i in range(1,N+1):
  l.append(i)
while len(l)!=0:
  a=l[K-1]
  l.remove(a)
  Josephus.append(str(a))
  if len(l)<1:
    break
  K+=plus-1
  while K>len(l):
    K-=len(l)
  cnt+=1
print("<"+", ".join(Josephus)+">")





