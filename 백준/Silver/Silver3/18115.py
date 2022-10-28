from collections import deque
import sys
input=sys.stdin.readline

T=int(input())
order=list(map(int,input().split()))
order.reverse()
dq=deque()

for i in range(T):
    if order[i]==1:
        dq.appendleft(i+1)
    elif order[i]==2:
        dq.insert(1,i+1)
    elif order[i]==3:
        dq.append(i+1)

print(*dq)