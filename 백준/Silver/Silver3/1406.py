import sys
input=sys.stdin.readline
from collections import deque

left=list(input().rstrip())
right=deque([])
for i in range(int(input())):
    order=list(input().split())
    if order[0]=='P':
        left.append(order[1])
    elif order[0]=='L':
        if len(left)>0:
            tmp=left.pop()
            right.appendleft(tmp)
    elif order[0]=='D':
        if len(right)>0:
            tmp=right.popleft()
            left.append(tmp)
    elif order[0]=='B':
        if len(left)>0:
            left.pop()

print(''.join(left+list(right)))

