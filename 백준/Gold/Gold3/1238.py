from cmath import inf
import heapq
from multiprocessing import heap
import sys
input=sys.stdin.readline

def dijkstra(start,end):
    q=[(0,start)]
    dist=[inf]*(N+1)
    dist[start]=0
    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
           continue
        for cost,next in graph[X]:
            cost=cost+Z
            if dist[next]>cost:
                dist[next]=cost
                heapq.heappush(q,[cost,next]) 
        
    return dist[end]

N,M,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    
result=[]
for i in range(1,N+1):
    A=dijkstra(X,i)
    B=dijkstra(i,X)
    result.append(A+B)

print(max(result))