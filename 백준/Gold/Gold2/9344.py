import heapq
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N,M,x,y=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    
    for i in range(M):
        u,v,w=map(int,input().split())
        graph[u].append((w,v,u))
        graph[v].append((w,u,v))
    
    q=graph[1]
    heapq.heapify(q)
    result=0
    visited=[True,True]+[False]*(N-1)
    check=False
    while q:
        Z,X,Y=heapq.heappop(q)
        if not visited[X]:
            visited[X]=True
            result+=Z
            if (X==x and Y==y) or (X==y and Y==x):
                check=True
            for i in graph[X]:
                if not visited[i[1]]:
                    heapq.heappush(q,i)
    
    if check==True:
        print('YES')
    else:
        print('NO')