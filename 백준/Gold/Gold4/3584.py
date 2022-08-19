from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    check=[False for _ in range(N+1)]
    l=[[] for _ in range(N+1)]
    for i in range(N-1):
        a,b=map(int,input().split())
        l[b].append(a)
    x,y=map(int,input().split())
    check[x],check[y]=True,True
    dq=deque()
    dq.append(x)
    dq.append(y)
    while dq:
        K=dq.popleft()
        if len(l[K])==1:
            if check[l[K][0]]==True:
                print(l[K][0])
                break
            else:
                check[l[K][0]]=True        
                dq.appendleft(l[K][0])