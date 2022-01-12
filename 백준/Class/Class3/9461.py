for _ in range(int(input())):
  N=int(input())
  l=[0,1,1,1,2,2]
  p=l
  if N>5:
    for i in range(1,N-4):
      l.append(p[i]+l[4+i])
  print(l[N])


  