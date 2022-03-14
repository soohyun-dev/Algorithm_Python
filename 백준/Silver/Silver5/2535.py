import sys
input=sys.stdin.readline

l=[]
n=int(input())
for i in range(n):
  l.append(list(map(int, input().split())))
  l.sort(key=lambda x:-x[2])

print(*l[0][:2])
print(*l[1][:2])

if l[0][0]==l[1][0]:
  for i in range(2,n):
      if l[i][0]!=l[1][0]:
          print(*l[i][:2])
          break
else:
  print(*l[2][:2])