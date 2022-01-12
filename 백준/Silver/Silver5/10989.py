import sys
N=int(input())
l=[0]*10001
for i in range(N):
  l[int(sys.stdin.readline())]+=1

for i in range(10001):
  if l[i]!=0:
    for j in range(l[i]):
      print(i)


      