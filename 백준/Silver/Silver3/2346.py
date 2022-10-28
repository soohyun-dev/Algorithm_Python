from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
dq=deque(enumerate(arr))
result=[]

while dq:
    print(dq)
    i,next=dq.popleft()
    result.append(i+1)
    
    if next>0:
        dq.rotate(-(next-1))
    elif next<0:
        dq.rotate(-next)
        
print(' '.join(map(str,result)))