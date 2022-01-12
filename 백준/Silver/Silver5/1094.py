X=int(input())
l=[64]
while sum(l) != X:
  a=l[0]
  if sum(l)>X:
    del(l[0])
  l.append(a//2)
  l.append(a//2)
  l.sort()
  if sum(l)>X:
    del(l[0])
print(len(l))

 

