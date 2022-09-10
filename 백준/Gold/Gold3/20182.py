from cmath import inf
import heapq
import sys
input=sys.stdin.readline

def dijkstra(S,E,C):
    q=[(0,S,0)]
    A=inf
    dist=[inf]*(N+1)
    dist[S]=0
    while q:
        Z,X,M=heapq.heappop(q)
        if dist[X]<Z:
            continue
        for cost,next in graph[X]:
            cost+=Z
            if cost < dist[next] and cost <=C:
                dist[next]=cost
                if M<cost-Z:
                    M=cost-Z
                if next==E:
                    if A>M :
                        A=M
                heapq.heappush(q,[cost,next,M])
    return A

N,M,S,E,C=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
result = dijkstra(S,E,C)

if result==sys.maxsize:
    print(-1)
else:
    print(result)