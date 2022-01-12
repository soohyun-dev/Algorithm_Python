l=[]
N=int(input())
for i in range(N):
  x, y, z = map(int, input().split())
  if x==y==z:
    l.append(10000 + (x * 1000))
  elif x==y or x==z:
    l.append(1000 + (x * 100))
  elif y==z:
    l.append(1000 + (y * 100))
  elif x!=y!=z:
    l.append(max(x, y, z) * 100)
print(max(l))

