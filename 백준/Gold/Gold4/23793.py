from cmath import inf
import heapq
import sys
input=sys.stdin.readline

def dijkstra(start,end,center):
    q=[(0,start)]
    dist=[inf]*(N+1)
    dist[start]=0

    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next in graph[X]:
            cost+=Z
            if next!=center:
                if cost<dist[next]:
                    dist[next]=cost
                    heapq.heappush(q,[cost,next])
    print(dist)
    return dist[end]

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    
start,center,end=map(int,input().split())
A=dijkstra(start,center,0)
B=dijkstra(center,end,0)
XZ=dijkstra(start,end,center)
XYZ=A+B
if XYZ==inf:
    XYZ=-1
if XZ==inf:
    XZ=-1
print(XYZ,XZ)