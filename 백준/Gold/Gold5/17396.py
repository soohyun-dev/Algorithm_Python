from cmath import inf
import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=list(map(int,input().split()))
graph=[[] for _ in range(N)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

q=[(0,0)]
dist=[inf]*N
dist[0]=0
while q:
    Z,X=heapq.heappop(q)
    if dist[X]<Z:
        continue
    for cost,next in graph[X]:
        cost+=Z
        if arr[next]!=1 or (arr[next]==1 and next==N-1):
            if cost<dist[next]:
                dist[next]=cost
                heapq.heappush(q,[cost,next])
if dist[N-1]==inf:
    print(-1)
else:
    print(dist[N-1])