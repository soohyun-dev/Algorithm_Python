import copy
import heapq
import sys
input=sys.stdin.readline

def Dijk(graph,node):
    dist = [0 for _ in range(N)]
    dist[node]=0
    t=[]
    heapq.heappush(t, [0,node])
    
    while t:
        Z,X=heapq.heappop(t)
        if dist[X]>=Z:
            for i in graph[X]:
                if dist[i[1]]<Z+i[0]:
                    dist[i[1]]=Z+i[0]
                    heapq.heappush(t,[Z+i[0],i[1]])
    print(dist)
    return dist

def MST(graph):
    visited=[True]+[False]*(N-1)
    q=graph[0]
    heapq.heapify(q)
    SUM=0
    g=[[] for _ in range(N)]
    
    while q:
        Z,X,Y=heapq.heappop(q)
        if not visited[X]:
            visited[X]=True
            SUM+=Z
            g[X].append((Z,Y))
            g[Y].append((Z,X))
            for i in graph[X]:
                if not visited[i[1]]:
                    heapq.heappush(q,i)
    return [SUM,g]

N,M=map(int,input().split())
graph=[[] for _ in range(N)]

for i in range(M):
    u,v,w=map(int,input().split())
    graph[u].append((w,v,u))
    graph[v].append((w,u,v))
    
result=MST(graph)

MAX=0
for i in range(N):
    tmp=Dijk(result[1],i)
    MAX=max(MAX,max(tmp))
print(MAX)