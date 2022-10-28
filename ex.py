from collections import deque

N,K,M=map(int,input().split())
q=deque(range(1,N+1))
idx=0

while q:
    if idx//M%2==0:
        for _ in range(K-1):
            q.append(q.popleft())
    else :
        for _ in range(K):
            q.appendleft(q.pop())
    idx+=1
    print(q.popleft())
    
    