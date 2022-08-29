from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
dist=[inf]*(N+1)
graph=[[] for _ in range(N+1)]

for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
q=[(0,1)]

while q:
    Z,X=heapq.heappop(q)
    if Z>dist[X]:
        continue
    for cost,next in graph[X]:
        cost=cost+Z
        if cost<dist[next]:
            dist[next]=cost
            heapq.heappush(q,[cost,next])
print(dist)
print(dist[N])