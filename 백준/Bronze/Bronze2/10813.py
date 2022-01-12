N,M=map(int,input().split())
l=[]
for i in range(0,N+1):
  l.append(i)
for j in range(M):
  A,B=map(int,input().split())
  l[A],l[B]=l[B],l[A]
print(*l[1:])


