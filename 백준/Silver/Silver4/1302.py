N=int(input())
l=[]
for i in range(N):
  l.append(input())
l.sort()
print(max(l, key=l.count))

