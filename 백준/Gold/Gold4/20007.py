from cmath import inf
import heapq
import sys
input=sys.stdin.readline

def dijkstra(start):
    q=[(0,start)]
    dist=[inf]*(N+1)
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
    return dist
        
N,M,X,Y=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

result=dijkstra(Y)

for i in range(N):
    if result[i]*2>X:
        print(-1)
        exit(0)
        
result.sort()
day=1
tmp=0
for i in range(1,N):
    tmp+=result[i]
    if tmp*2>X:
        day+=1
        tmp=result[i]
print(day)
