import heapq
import sys
input=sys.stdin.readline

while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    graph=[[] for _ in range(N)]
    total=0
    for i in range(M):
        a,b,c=map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
        total+=c
        
    visited=[True]+[False]*(N)
    q=graph[0]
    heapq.heapify(q)
    result=0

    while q:
        Z,X=heapq.heappop(q)
        if not visited[X]:
            visited[X]=True
            result+=Z
            for i in graph[X]:
                if not visited[i[1]]:
                    heapq.heappush(q,i)

    print(total-result)
    