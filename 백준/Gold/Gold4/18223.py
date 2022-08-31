from cmath import inf
import heapq
import sys

input=sys.stdin.readline

def dijkstra(start,end):
    q=[(0,start)]
    dist=[inf]*(N+1)
    dist[start]=0
    while q:
        Z,X=heapq.heappop(q)
        for cost,next in graph[X]:
            cost+=Z
            if cost<=dist[next]:
                dist[next]=cost
                heapq.heappush(q,[cost,next])
    return dist[end]

N,M,P=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
MIN=dijkstra(1,N)
A=dijkstra(1,P)  # 시작지점부터 건우까지의 최단거리
B=dijkstra(P,N)  # 건우부터 끝까지의 최단거리
if MIN==A+B:
    print('SAVE HIM')
else:
    print('GOOD BYE')