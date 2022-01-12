import sys
N=int(input())
Q=[]
for i in range(N):
  order=sys.stdin.readline().split()
  if order[0]=='push':
    Q.append(order[1])
  elif order[0]=='pop':
    if len(Q)==0:
      print(-1)
    else:
      a=Q[0]
      del(Q[0])
      print(a)
  elif order[0]=='size':
    print(len(Q))
  elif order[0]=='empty':
    if len(Q)==0:
      print(1)
    else:
      print(0)
  elif order[0]=='front':
    if len(Q)==0:
      print(-1)
    else:
      print(Q[0])
  elif order[0]=='back':
    if len(Q)==0:
      print(-1)
    else:
      print(Q[-1])


