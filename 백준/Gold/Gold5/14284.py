from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
dist=[inf]*(N+1)
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
start,end=map(int,input().split())
q=[(0,start)]
while q:
    Z,X=heapq.heappop(q)
    if dist[X]<Z:
        continue
    for cost, next in graph[X]:
        cost+=Z
        if cost<dist[next]:
            dist[next]=cost
            heapq.heappush(q,[cost,next])
            
print(dist[end])