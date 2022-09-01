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
        if dist[X]<Z:
            continue
        for cost,next in graph[X]:
            cost+=Z
            if cost < dist[next]:
                dist[next]=cost
                heapq.heappush(q,[cost,next])
    return dist[end]

for i in range(int(input())):
    N,M,T=map(int,input().split())
    S,G,H=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for j in range(M):
        a,b,c=map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
    target=[ [int(input()),inf] for _ in range(T)]
    for n in range(T):
        finish=target[n][0]
        target[n][1]=dijkstra(S,finish)
    
    target_G=dijkstra(S,G)
    target_H=dijkstra(S,H)
    target_GH=dijkstra(G,H)
    target_HG=dijkstra(H,G)
    answer=[]
    for k in range(T):
        if target[k][1]==inf:
            continue
        finish=target[k][0]
        HG=dijkstra(G,finish)
        GH=dijkstra(H,finish)
        check=False
        if target_G+target_GH+GH==target[k][1]:
            check=True
        if target_H+target_HG+HG==target[k][1]:
            check=True
        if check==True:
            answer.append(target[k][0])
    
    answer.sort()
    print(*answer)