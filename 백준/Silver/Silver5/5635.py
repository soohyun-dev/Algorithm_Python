N=int(input())
l=[]
for i in range(N):
  l.append(list(input().split()))
l.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))

print(l[N-1][0])
print(l[0][0])
