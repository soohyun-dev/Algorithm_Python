import sys

N,M = map(int,input().split())
l =[]
d =[]
sum=0

for listen in range(N):
  l.append(sys.stdin.readline().rstrip())

for look in range(M):
  d.append(sys.stdin.readline().rstrip())
  
man = sorted(list(set(l) & set(d)))

print(len(man))

for i in range(len(man)):
  print(man[i])


