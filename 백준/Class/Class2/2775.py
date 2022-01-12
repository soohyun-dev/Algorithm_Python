for i in range(int(input())):
  k=int(input())
  n=int(input())
  if n==1:
    print(1)
  else:
    l=[]
    T=[]
    for i in range(1,n+1):
      l.append(int(i))
      T.append(int(i))
    for i in range(1,k+1):
      for j in range(n):
       l[j]=sum(T[:j+1])
      for k in range(n):
        T[k]=l[k]
    print(l[n-1])



