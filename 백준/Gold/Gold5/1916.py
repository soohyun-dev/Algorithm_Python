from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    
start,end=map(int,input().split())
q=[(0,start)]
dist=[inf]*(N+1)

while q:
    Z,X=heapq.heappop(q)
    if dist[X]<Z:
        continue
    for cost,next in graph[X]:
        cost=cost+Z
        if dist[next]>cost:
            dist[next]=cost
            heapq.heappush(q,[cost,next])
print(dist[end])