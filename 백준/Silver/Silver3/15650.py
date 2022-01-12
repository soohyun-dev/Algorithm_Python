N,M=map(int,input().split())
l=[]

def check():
  a=0
  if len(l)==M:
    for i in range(len(l)-1):
      if l[i]>=l[i+1]:
        a=1
    if a==0:
      print(' '.join(map(str, l)))
    a=0
    return
  for i in range(1,N+1):
    if i not in l:
      l.append(i)
      check()
      l.pop()
check()
  

