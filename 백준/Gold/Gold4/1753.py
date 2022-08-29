from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
K=int(input())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))

q=[(0,K)]
dist=[inf]*(N+1)
dist[K]=0
while q:
    Z,X=heapq.heappop(q)
    if dist[X]<Z:
        continue
    for cost,next in graph[X]:
        cost=cost+Z
        if cost<dist[next]:
            dist[next]=cost
            heapq.heappush(q,[cost,next])

for i in range(1,N+1):
    if dist[i]==inf:
        print('INF')
    else:
        print(dist[i])