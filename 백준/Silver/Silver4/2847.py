import sys
input = sys.stdin.readline

N=int(input())
l=[]

for i in range(N):
  l.append(int(input()))

total=0

for i in range(N-1, 0, -1):
  if l[i] <= l[i-1]:
    total+= (l[i-1]-l[i]+1)
    l[i-1]=l[i]-1
print(total)

