N,M=map(int,input().split())
l=[]
def check():
  if len(l)==M:
    print(' '.join(map(str, l)))
    return
  for i in range(1,N+1):
    if i not in l:
      l.append(i)
      check()
      l.pop()
check()
  



