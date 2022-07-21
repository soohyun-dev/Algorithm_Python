import sys
input=sys.stdin.readline
from collections import deque
    
def bfs(graph):
    MIN=sys.maxsize
    for i in range(1,N+1):
        dq=deque()
        dq.append(i)
        check=[i]
        n=[0]*(N+1)
        while dq:
            x=dq.popleft()
            for j in graph[x]:
                if j not in check:
                    n[j]=n[x]+1
                    check.append(j)
                    dq.append(j)
        if sum(n) < MIN:
            MIN=sum(n)
            cnt=i
    return cnt

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph))

