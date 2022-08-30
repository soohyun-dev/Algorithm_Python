from cmath import inf
import heapq
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N,M,C=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for i in range(M):
        a,b,c=map(int,input().split())
        graph[b].append((c,a))
        
    dist=[inf]*(N+1)
    dist[C]=0
    q=[(0,C)]
    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next in graph[X]:
            cost=cost+Z
            if cost<dist[next]:
                dist[next]=cost
                heapq.heappush(q,[cost,next])
    cnt=0
    MAX=0
    for i in range(1,N+1):
        if dist[i]!=inf:
            cnt+=1
            if dist[i]>MAX:
                MAX=dist[i]
    print(cnt,MAX)
        
        