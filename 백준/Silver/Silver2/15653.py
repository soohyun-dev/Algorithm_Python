N,M=map(int,input().split())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
l.sort()

def check():
  if len(l)==M:
      print(' '.join(map(str, l)))
  for i in range(1, N+1):
    if i not in l:
      l.append(i)
      check()
      l.pop()

check()

    