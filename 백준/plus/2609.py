A,B=map(int,input().split())
a=(min(A,B))

while True:
  if A%a==0 and B%a==0:
    break
  a-=1
print(a) 
print((A//a)*(B//a)*a)