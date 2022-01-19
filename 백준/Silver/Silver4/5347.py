for i in range(int(input())):
  A,B=map(int,input().split())
  m=max(A,B)
  a=1
  t=m
  if A==m:
    while (t*a)%B!=0:
      a+=1
      m=t*a
  elif B==m:
    while (t*a)%A!=0:
      a+=1
      m=t*a
  print(m)


  