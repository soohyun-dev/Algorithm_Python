l=[]
for i in range(int(input())):
  l.append(list(map(int, input().split())))
  l.sort(key=lambda x:-x[2])

print(*l[0][:2])
print(*l[1][:2])

if l[0][0]==l[1][0]:
  print(*l[3][:2])
else:
  print(*l[2][:2])