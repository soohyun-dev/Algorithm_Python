from collections import deque
N=int(input())
l=[]
for i in range(1,N+1):
  l.append(i)
dq=deque(l)
while len(dq)!=1:
  dq.popleft()
  a=dq.popleft()
  dq.append(a)
print(dq[0])


