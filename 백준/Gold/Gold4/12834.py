from cmath import inf
import heapq
import sys
input=sys.stdin.readline

def dijkstra(start,end):
    q=[(0,start)]
    dist=[inf]*(V+1)
    dist[start]=0
    while q:
        Z,X=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next in graph[X]:
            cost+=Z
            if cost<dist[next]:
                dist[next]=cost
                heapq.heappush(q,[cost,next])
    return dist[end]

N,V,E=map(int,input().split())
A,B=map(int,input().split())
team=list(map(int,input().split()))
graph=[[] for _ in range(V+1)]
result=0

for i in range(E):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
for j in range(N):
    A_cnt=dijkstra(A,team[j])
    B_cnt=dijkstra(B,team[j])
    if A_cnt==inf:
        A_cnt=-1
    if B_cnt==inf:
        B_cnt=-1
    result+=(A_cnt+B_cnt)
    
print(result)
    