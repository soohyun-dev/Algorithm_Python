N,M=map(int,input().split())
l=[]
result=[]
for i in range(2):
  l.append(list(map(int, input().split())))
  for j in range(len(l[i])):
    result.append(l[i][j])
result.sort()

for k in range(len(result)):
  print(result[k], end=' ')

  