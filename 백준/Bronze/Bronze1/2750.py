cnt=int(input())
l=[]
for i in range(cnt):
  N=int(input())
  l.append(N)
l.sort()
for i in range(cnt):
  print(l[i])

